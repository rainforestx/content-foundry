#!/usr/bin/env python3
"""Every skill overlay is pointed at, non-empty, and named for a real skill.

The convention (see .claude/overlays/README.md): a skill named X reads
.claude/overlays/X.md when it runs here. The filename is the binding.

What this gate can check, and what it cannot, is the whole point of reading
this docstring. The parent skills that consume overlays may live at USER level,
outside this repository, where nothing here can see them. So an overlay can be
perfectly formed, correctly named, and read by nothing at all, and no gate can
tell you. That silence is the same failure class as LEARNING #236, where an
imported skill named six tools that did not exist and failed loudly for nobody.

So this checks the half that is checkable:

1. Every overlay is referenced by something in the repository. An overlay that
   nothing points at is either dead or its parent forgot to look, and both are
   worth surfacing. README.md is exempt - it documents the directory.
2. No overlay is empty or a stub. A file that exists and says nothing is worse
   than an absent one, because its presence reads as coverage.
3. Every overlay has a plausible parent name: lowercase, hyphens, .md. A
   mis-named overlay silently binds to no skill.
4. The README's overlay table lists what is actually on disk. A register that
   disagrees with the tree is how a directory stops being trustworthy.
5. Proposals in .claude/overlays/_proposed/ stay unread, dated, free of
   verdict language, and do not outlive PROPOSAL_MAX_AGE_DAYS. That directory
   is the staging area an agent may write to unattended, and every one of
   those properties is what makes writing to it safe.

The decay check makes this gate DATE-DEPENDENT: an unchanged tree can pass
today and fail in three months. That is intended - an expired proposal needs
action - but it means a red build here is not always caused by the commit in
front of you.

It deliberately does NOT try to verify the user-level side. A gate that
appeared to check something it cannot is worse than one that states the limit.

Exit 0 clean, 1 on a violation, 2 on a usage error.
"""

import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _repo_root(start):
    """Walk up to the enclosing git repository.

    Every copy of this file is byte-identical, so it cannot hardcode how deep
    it sits. Byte-identity is what lets SOURCE_SHA detect drift between
    installations rather than merely detecting a different install path.
    """
    d = start
    while True:
        if os.path.isdir(os.path.join(d, ".git")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return start
        d = parent


REPO = _repo_root(HERE)
# Stamped by --stamp from the canonical copy, and checked by --verify-source.
# Computed over this file with the stamp line itself excluded, so stamping does
# not invalidate the value it writes.
SOURCE_SHA = "72d8a0a8c5f0f14ab5bdeca283b4113affea0db5485441544278f5354147cc5f"
OVERLAY_DIR = os.path.join(".claude", "overlays")
PROPOSED_DIR = os.path.join(OVERLAY_DIR, "_proposed")
# An observation carries a date so it can age and be re-tested. A rule stated
# without one is a verdict by construction: nothing can expire what it cannot
# date. ISO first, then the two shapes people actually type.
DATE_RE = re.compile(r"\b(20\d{2}-\d{2}-\d{2}|\d{1,2} \w{3,9} 20\d{2})\b")
# Phrases that assert a standing property of the world rather than reporting a
# measurement. Every one of these was written into this repo by an agent in a
# single day (LEARNING #238) before the rule existed.
VERDICT_PHRASES = (
    "is blocked", "is open", "is unreachable", "cannot be reached",
    "always fails", "never works", "the proxy blocks", "is not available",
)
PROPOSAL_MAX_AGE_DAYS = 90
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")
MIN_BYTES = 400
STUB_MARKERS = ("tbd", "todo", "coming soon", "placeholder")


def overlays(root):
    d = os.path.join(root, OVERLAY_DIR)
    if not os.path.isdir(d):
        return []
    return sorted(f for f in os.listdir(d) if f.endswith(".md"))


def referenced_by(root, name):
    """Which tracked files mention this overlay by path."""
    needle = "overlays/%s" % name
    try:
        out = subprocess.run(
            ["git", "-C", root, "grep", "-l", "--fixed-strings", needle],
            capture_output=True, text=True)
    except OSError:
        return []
    hits = [l for l in out.stdout.splitlines() if l.strip()]
    # The overlay itself and the directory README do not count as pointers.
    return [h for h in hits
            if not h.endswith(os.path.join(OVERLAY_DIR, name))
            and not h.endswith(os.path.join(OVERLAY_DIR, "README.md"))]


def proposals(root):
    d = os.path.join(root, PROPOSED_DIR)
    if not os.path.isdir(d):
        return []
    return sorted(f for f in os.listdir(d)
                  if f.endswith(".md") and f != "README.md")


def _entries(body):
    """Split a proposal into entries. A heading starts one."""
    parts = re.split(r"^#{2,}\s+", body, flags=re.M)
    return [p for p in parts[1:] if p.strip()]


def check_proposals(root, today=None):
    """Hygiene on the proposal staging area.

    Nothing here may be read as behaviour. These checks exist so that the
    autonomous stages of the pathway cannot quietly become the ratified one.
    """
    import datetime
    today = today or datetime.date.today()
    findings = []

    # P1. No skill and no live overlay may point at a proposal. Being unread
    # is the entire safety property of this directory; a pointer removes it.
    scan = []
    sk = os.path.join(root, ".claude", "skills")
    for base, _, fns in os.walk(sk):
        scan += [os.path.join(base, f) for f in fns if f.endswith(".md")]
    od = os.path.join(root, OVERLAY_DIR)
    if os.path.isdir(od):
        scan += [os.path.join(od, f) for f in os.listdir(od)
                 if f.endswith(".md") and f != "README.md"]
    for f in scan:
        try:
            body = open(f, errors="ignore").read()
        except OSError:
            continue
        if "_proposed" in body:
            findings.append((os.path.relpath(f, root),
                             "points at the proposal staging area. Proposals "
                             "must be unread; a pointer promotes one without "
                             "review."))

    for name in proposals(root):
        rel = os.path.join(PROPOSED_DIR, name)
        body = open(os.path.join(root, PROPOSED_DIR, name),
                    errors="ignore").read()
        ents = _entries(body)
        if not ents:
            findings.append((rel, "no dated entries; an empty proposal file "
                                  "reads as coverage"))
            continue
        for i, e in enumerate(ents, 1):
            head = e.splitlines()[0].strip()[:60]
            dates = DATE_RE.findall(e)
            # P2. Undated entries cannot expire and cannot be re-tested.
            if not dates:
                findings.append((rel, "entry %d (%s) carries no date. An "
                                      "observation without one is a verdict."
                                 % (i, head)))
                continue
            # P3. Verdict language, which is the failure this bridge exists
            # to prevent being automated.
            low = e.lower()
            hit = [v for v in VERDICT_PHRASES if v in low]
            if hit:
                findings.append((rel, "entry %d (%s) states a verdict (%r). "
                                      "Record the command and its output, not "
                                      "a standing property of the world."
                                 % (i, head, hit[0])))
            # P4. Decay. NOTE: this makes the gate date-dependent - the same
            # tree can pass today and fail later. That is intended for a decay
            # rule and is declared in the module docstring.
            try:
                iso = [d for d in dates if re.match(r"^20\d{2}-", d)]
                if iso:
                    seen = datetime.date.fromisoformat(sorted(iso)[-1])
                    age = (today - seen).days
                    if age > PROPOSAL_MAX_AGE_DAYS:
                        findings.append((rel, "entry %d (%s) is %d days old. "
                                              "Promote it or delete it; a "
                                              "proposal nobody acted on is "
                                              "lore accumulating."
                                         % (i, head, age)))
            except ValueError:
                pass

        # P5. A promoted proposal that was never cleaned up leaves two homes
        # for one fact, which is what DL-023 exists to stop.
        live = os.path.join(root, OVERLAY_DIR, name)
        if os.path.exists(live):
            lb = open(live, errors="ignore").read()
            for e in ents:
                chunk = " ".join(e.split())[:120]
                if len(chunk) > 60 and chunk in " ".join(lb.split()):
                    findings.append((rel, "an entry is already verbatim in the "
                                          "live overlay. Promotion is a move, "
                                          "not a copy - delete the proposal."))
                    break
    return findings


def readme_table(root):
    p = os.path.join(root, OVERLAY_DIR, "README.md")
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        text = fh.read()
    return set(re.findall(r"`([a-z0-9-]+\.md)`", text))


def check(root=REPO):
    findings = []
    found = overlays(root)
    real = [f for f in found if f != "README.md"]
    malformed = set()

    for name in real:
        path = os.path.join(root, OVERLAY_DIR, name)
        if not NAME_RE.match(name):
            findings.append((os.path.join(OVERLAY_DIR, name), "name is not a plausible skill name; an "
                                   "overlay binds by filename, so this one "
                                   "binds to nothing"))
            malformed.add(name)
            continue
        with open(path) as fh:
            body = fh.read()
        stripped = body.strip()
        low = stripped.lower()
        if any(m in low for m in STUB_MARKERS) and len(stripped) < MIN_BYTES * 3:
            findings.append((os.path.join(OVERLAY_DIR, name), "looks like a stub (contains a TBD/TODO "
                                   "marker and is short)"))
            continue
        if len(stripped) < MIN_BYTES:
            findings.append((os.path.join(OVERLAY_DIR, name), "only %d bytes of content; an overlay that "
                                   "says nothing still reads as coverage"
                             % len(stripped)))
            continue
        if not referenced_by(root, name):
            findings.append((os.path.join(OVERLAY_DIR, name), "nothing in the repository points at it. "
                                   "Either its parent skill does not look for "
                                   "it, or it is dead. Both are findings."))

    listed = readme_table(root)
    if listed is None:
        if real:
            findings.append((OVERLAY_DIR, "overlays exist but there is no "
                                          "README documenting the convention"))
    else:
        missing = sorted(set(real) - listed - malformed)
        phantom = sorted(listed - set(real) - {"README.md"})
        for m in missing:
            findings.append((os.path.join(OVERLAY_DIR, m), "on disk but absent from the README table"))
        for p in phantom:
            findings.append((os.path.join(OVERLAY_DIR, p), "listed in the README table but not on disk"))

    return findings, real


def main(argv):
    root = REPO
    if len(argv) > 1:
        if argv[1] == "--selftest":
            return selftest()
        if argv[1] == "--verify-source":
            stamped, actual = verify_source()
            if stamped in (None, "unstamped"):
                print("overlay_gate: unstamped copy (sha %s). Run --stamp on "
                      "the canonical copy." % actual[:12])
                return 0
            if stamped != actual:
                sys.stderr.write(
                    "overlay_gate: SOURCE DRIFT. stamped %s, actual %s. This "
                    "copy has been edited since installation, so the "
                    "installations no longer enforce the same rules. Re-stamp "
                    "at the canonical source and re-run --init, or port the "
                    "edit deliberately.\n" % (stamped[:12], actual[:12]))
                return 1
            print("overlay_gate: source matches its stamp (%s)" % actual[:12])
            return 0
        if argv[1] == "--stamp":
            path = os.path.abspath(__file__)
            new = body_hash(path)
            with open(path) as fh:
                src = fh.read()
            with open(path, "w") as fh:
                fh.write(STAMP_RE.sub('SOURCE_SHA = "%s"' % new, src))
            print("overlay_gate: stamped %s" % new[:12])
            return 0
        if argv[1] == "--init" and len(argv) > 2:
            dry = "--dry-run" in argv[3:]
            try:
                created, skipped, gd, stamp = init(argv[2], dry_run=dry)
            except IOError as exc:
                sys.stderr.write("overlay_gate: %s\n" % exc)
                return 2
            for c in created:
                print("%s %s" % ("would create" if dry else "created", c))
            for s in skipped:
                print("exists, left alone: %s" % s)
            print("overlay_gate: %s into %s (gate at %s/, stamp %s)"
                  % ("dry run" if dry else "installed", argv[2], gd,
                     stamp[:12]))
            if not dry:
                print("Next: add a pointer to the overlay from a skill or a "
                      "doc in that repo, or the gate will fail - an overlay "
                      "nothing references is either dead or unread.")
            return 0
        if argv[1] == "--root" and len(argv) > 2:
            root = argv[2]
        else:
            sys.stderr.write(
                "usage: overlay_gate.py [--root DIR | --selftest | "
                "--verify-source | --stamp | --init TARGET [--dry-run]]\n")
            return 2

    findings, real = check(root)
    findings += [(n, w) for n, w in check_proposals(root)]
    for name, why in findings:
        sys.stderr.write("%s: %s\n" % (name, why))
    if findings:
        sys.stderr.write("overlay_gate: FAIL - %d finding(s) over %d overlay(s)\n"
                         % (len(findings), len(real)))
        return 1
    print("overlay_gate: clean (%d overlay(s) live, %d proposal file(s); "
          "user-level parents NOT checkable from here)"
          % (len(real), len(proposals(root))))
    return 0


# --- provenance and installation --------------------------------------------

STAMP_RE = re.compile(r'^SOURCE_SHA = ".*"$', re.M)


def body_hash(path):
    """sha256 of this file with the stamp line normalised out.

    Excluding the stamp is what makes the value stable: a hash that covered
    the line holding it could never be written down.
    """
    import hashlib
    with open(path, "rb") as fh:
        raw = fh.read().decode("utf-8", "replace")
    normalised = STAMP_RE.sub('SOURCE_SHA = ""', raw)
    return hashlib.sha256(normalised.encode("utf-8")).hexdigest()


def verify_source(path=None):
    """Has this copy been edited since it was stamped?

    Detects local edits, and by extension divergence between installations:
    all copies are byte-identical and carry the same stamp, so a copy whose
    computed hash differs from its stamp has drifted from the canonical.
    It CANNOT tell you the canonical itself is current - for that, re-stamp
    at the source and re-run --init.
    """
    path = path or os.path.abspath(__file__)
    actual = body_hash(path)
    with open(path) as fh:
        m = STAMP_RE.search(fh.read())
    stamped = m.group(0).split('"')[1] if m else None
    return stamped, actual


README_OVERLAYS = """# Skill overlays

A skill named `X` reads `.claude/overlays/X.md` when it runs here and applies
it over its own defaults. The filename is the binding, so there is nothing to
register and nothing to keep in sync.

**The doctrine is not restated here.** It lives in
`skills/instruction-overlays/SKILL.md` in rainforestx/agentic-app-architecture.
Read it before adding an overlay. What follows is only what is local.

## The short version

- An overlay is a **specialisation**, never an entry point. Plain markdown, no
  frontmatter, no description, no triggers, so it cannot collide with the skill
  it modifies.
- It may **narrow, never weaken** the parent skill's evidence discipline.
- New local knowledge goes to `_proposed/` as a dated observation, not straight
  into an overlay. See `_proposed/README.md`.
- `overlay_gate.py` enforces the checkable half and states in its own output
  that it cannot verify whether the parent skill actually looks.

## Current overlays

| Overlay | Parent skill | Covers |
|---|---|---|

<!-- Add a row when you add an overlay. The gate fails if this table and the
     directory disagree. -->
"""

README_PROPOSED = """# Proposals - staging, not behaviour

**Nothing reads this directory.** That is its safety property. An agent may
write here unattended, mid-task, without asking, precisely because writing here
changes nothing. The gate fails if any skill or live overlay points at this
path.

Write an **observation**, not a rule: what you ran, what came back, when, and
what you were doing. Every entry carries a date, because an observation that
cannot age cannot be re-tested, and one that cannot be re-tested is a verdict
wearing a timestamp.

Never write standing claims about the world. The gate rejects those phrasings
by name, because a conclusion outlives the condition that produced it.

Something leaves here when a second occurrence in a different task appends
alongside the first, a different actor generalises it, it **moves** into
`../<skill>.md`, and the owner signs it off. Entries older than 90 days fail
the gate: promote or delete.
"""


def init(target, self_path=None, dry_run=False):
    """Install the convention into another repository.

    Creates the overlay directory, the staging area, both READMEs, and a copy
    of this gate stamped with the canonical source hash. Never overwrites: an
    existing file is reported and left alone, because a scaffolder that
    clobbers a repository's own writing is worse than one that does nothing.
    """
    self_path = self_path or os.path.abspath(__file__)
    target = os.path.abspath(target)
    if not os.path.isdir(target):
        raise IOError("target is not a directory: %s" % target)

    gate_dir = "gates" if os.path.isdir(os.path.join(target, "gates")) else None
    if gate_dir is None:
        gate_dir = ("build/automation"
                    if os.path.isdir(os.path.join(target, "build", "automation"))
                    else "gates")

    planned = [
        (os.path.join(OVERLAY_DIR, "README.md"), README_OVERLAYS),
        (os.path.join(PROPOSED_DIR, "README.md"), README_PROPOSED),
        (os.path.join(gate_dir, "overlay_gate.py"), None),
    ]
    created, skipped = [], []
    stamp = body_hash(self_path)
    with open(self_path) as fh:
        gate_src = STAMP_RE.sub('SOURCE_SHA = "%s"' % stamp, fh.read())

    for rel, content in planned:
        full = os.path.join(target, rel)
        if os.path.exists(full):
            skipped.append(rel)
            continue
        if dry_run:
            created.append(rel)
            continue
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w") as fh:
            fh.write(gate_src if content is None else content)
        if content is None:
            os.chmod(full, 0o755)
        created.append(rel)
    return created, skipped, gate_dir, stamp


# --- selftest ---------------------------------------------------------------

BODY = ("# x overlay\n\n" + ("Real content that says something specific about "
                             "this repository and its rules. " * 12))


def selftest():
    import shutil
    import tempfile

    cases = []

    def build(tmp, files, pointer=True, readme=True):
        od = os.path.join(tmp, OVERLAY_DIR)
        os.makedirs(od, exist_ok=True)
        for name, body in files.items():
            open(os.path.join(od, name), "w").write(body)
        if readme:
            rows = "\n".join("| `%s` | p | c |" % n for n in files)
            open(os.path.join(od, "README.md"), "w").write(
                "# Skill overlays\n\n| Overlay | Parent | Covers |\n|---|---|---|\n"
                + rows + "\n")
        if pointer:
            os.makedirs(os.path.join(tmp, ".claude", "skills"), exist_ok=True)
            open(os.path.join(tmp, ".claude", "skills", "p.md"), "w").write(
                "\n".join("see `.claude/overlays/%s`" % n for n in files))
        subprocess.run(["git", "-C", tmp, "init", "-q"], check=False)
        subprocess.run(["git", "-C", tmp, "add", "-A"], check=False,
                       capture_output=True)

    def case(name, files, expect, **kw):
        tmp = tempfile.mkdtemp()
        try:
            build(tmp, files, **kw)
            findings, _ = check(tmp)
            ok = len(findings) == expect
            cases.append((name, ok, "%d finding(s): %s"
                          % (len(findings), [f[1][:40] for f in findings])))
        finally:
            shutil.rmtree(tmp)

    # POSITIVE: a well-formed overlay passes.
    case("accepts a well-formed, pointed-at overlay", {"perplexity.md": BODY}, 0)

    # NEGATIVE: the defect the gate exists for.
    case("catches an overlay nothing points at",
         {"perplexity.md": BODY}, 1, pointer=False)

    # NEGATIVE: presence without content.
    case("catches an empty overlay", {"perplexity.md": "# x\n"}, 1)

    # NEGATIVE: presence without content, by size.
    case("catches a short empty-ish overlay",
         {"perplexity.md": "# x\n\nnot much here at all.\n"}, 1)

    # NEGATIVE: a stub long enough to pass the size check still reads as a
    # stub. This case exists because the marker branch was unreachable behind
    # the size check until the order was swapped.
    case("catches a long TBD stub that clears the size floor",
         {"perplexity.md": "# x\n\nTODO: write this up later.\n"
                           + ("Filler that pads the file past the size floor "
                              "without saying anything. " * 8)}, 1)

    # NEGATIVE: a name that binds to no skill.
    case("catches an implausible overlay name",
         {"Perplexity Notes.md": BODY}, 1)

    # NEGATIVE: register disagreeing with the tree.
    case("catches an overlay missing from the README table",
         {"perplexity.md": BODY}, 1, readme=False)

    # --- proposal staging ------------------------------------------------

    import datetime
    TODAY = datetime.date(2026, 8, 7)
    GOOD = ("## SDS receiver filter lookup\n\n"
            "2026-08-07, task: sourcing the SDS 4.0 filter spec. Ran "
            "`curl -sSL https://www.example.com/x` and got HTTP 000, 0 bytes. "
            "WebFetch on the same URL returned EGRESS_BLOCKED the same minute. "
            "Retried after the policy change: HTTP 200, 240666 bytes.\n")

    def pcase(name, files, expect, extra=None, today=TODAY):
        tmp = tempfile.mkdtemp()
        try:
            pd = os.path.join(tmp, PROPOSED_DIR)
            os.makedirs(pd, exist_ok=True)
            for fn, body in files.items():
                open(os.path.join(pd, fn), "w").write(body)
            for rel, body in (extra or {}).items():
                full = os.path.join(tmp, rel)
                os.makedirs(os.path.dirname(full), exist_ok=True)
                open(full, "w").write(body)
            f = check_proposals(tmp, today=today)
            ok = len(f) == expect
            cases.append((name, ok, "%d finding(s): %s"
                          % (len(f), [x[1][:44] for x in f])))
        finally:
            shutil.rmtree(tmp)

    # POSITIVE: a well-formed, dated observation passes.
    pcase("accepts a dated observation", {"perplexity.md": GOOD}, 0)

    # NEGATIVE: the defect the whole bridge exists to prevent.
    pcase("catches a verdict instead of an observation",
          {"perplexity.md": "## net\n\n2026-08-07: phonak.com is blocked.\n"}, 1)

    # NEGATIVE: undated entries cannot expire or be re-tested.
    pcase("catches an undated entry",
          {"perplexity.md": "## net\n\nRan curl, got 200, 240666 bytes.\n"}, 1)

    # NEGATIVE: a pointer removes the unread property that makes staging safe.
    pcase("catches a skill pointing at the staging area",
          {"perplexity.md": GOOD}, 1,
          extra={".claude/skills/p/SKILL.md":
                 "read `.claude/overlays/_proposed/perplexity.md`"})

    # NEGATIVE: decay. Same tree, later date.
    pcase("catches an expired proposal", {"perplexity.md": GOOD}, 1,
          today=datetime.date(2027, 8, 7))

    # NEGATIVE: promoted but never cleaned up leaves two homes for one fact.
    pcase("catches a proposal already verbatim in the live overlay",
          {"perplexity.md": GOOD}, 1,
          extra={os.path.join(OVERLAY_DIR, "perplexity.md"): GOOD})

    # An empty proposal file reads as coverage.
    pcase("catches an empty proposal file", {"perplexity.md": "\n"}, 1)

    # --- provenance and installation -------------------------------------

    def icase(name, fn):
        tmp = tempfile.mkdtemp()
        try:
            ok, detail = fn(tmp)
            cases.append((name, ok, detail))
        finally:
            shutil.rmtree(tmp)

    SELF = os.path.abspath(__file__)

    # POSITIVE: a fresh repo gets the full scaffold and the gate passes on it.
    def fresh(tmp):
        subprocess.run(["git", "-C", tmp, "init", "-q"], check=False)
        os.makedirs(os.path.join(tmp, "gates"), exist_ok=True)
        created, skipped, gd, stamp = init(tmp, self_path=SELF)
        want = {os.path.join(OVERLAY_DIR, "README.md"),
                os.path.join(PROPOSED_DIR, "README.md"),
                os.path.join("gates", "overlay_gate.py")}
        if set(created) != want:
            return False, "created %s" % sorted(created)
        subprocess.run(["git", "-C", tmp, "add", "-A"], check=False,
                       capture_output=True)
        findings, _ = check(tmp)
        findings += check_proposals(tmp)
        return (not findings and not skipped,
                "created %d, gate findings %d" % (len(created), len(findings)))
    icase("init scaffolds a fresh repo and the gate passes on it", fresh)

    # NEGATIVE: never clobber. A scaffolder that overwrites is worse than one
    # that does nothing.
    def noclobber(tmp):
        os.makedirs(os.path.join(tmp, OVERLAY_DIR), exist_ok=True)
        mine = os.path.join(tmp, OVERLAY_DIR, "README.md")
        open(mine, "w").write("MINE - do not overwrite\n")
        init(tmp, self_path=SELF)
        body = open(mine).read()
        return body.startswith("MINE"), "existing README preserved: %s" % (
            body.startswith("MINE"))
    icase("init never overwrites an existing file", noclobber)

    # The installed gate carries a stamp that matches its own body.
    def stamped(tmp):
        subprocess.run(["git", "-C", tmp, "init", "-q"], check=False)
        init(tmp, self_path=SELF)
        inst = os.path.join(tmp, "gates", "overlay_gate.py")
        st, act = verify_source(inst)
        return st == act, "stamped %s actual %s" % (
            (st or "")[:8], act[:8])
    icase("the installed copy verifies against its own stamp", stamped)

    # NEGATIVE: an edited copy fails verification. This is the drift check.
    def drift(tmp):
        subprocess.run(["git", "-C", tmp, "init", "-q"], check=False)
        init(tmp, self_path=SELF)
        inst = os.path.join(tmp, "gates", "overlay_gate.py")
        with open(inst, "a") as fh:
            fh.write("\n# a local edit nobody ported back\n")
        st, act = verify_source(inst)
        return st != act, "stamp %s != actual %s" % ((st or "")[:8], act[:8])
    icase("an edited copy fails source verification", drift)

    # The stamp is computed with its own line excluded, or stamping could
    # never converge.
    def stable(tmp):
        a = os.path.join(tmp, "g.py")
        shutil.copy(SELF, a)
        h1 = body_hash(a)
        src = open(a).read()
        open(a, "w").write(STAMP_RE.sub('SOURCE_SHA = "%s"' % h1, src))
        h2 = body_hash(a)
        return h1 == h2, "hash stable across stamping: %s" % (h1 == h2)
    icase("the stamp does not invalidate itself", stable)

    # Layout detection: a repo using build/automation/ gets the gate there.
    def layout(tmp):
        subprocess.run(["git", "-C", tmp, "init", "-q"], check=False)
        os.makedirs(os.path.join(tmp, "build", "automation"), exist_ok=True)
        _, _, gd, _ = init(tmp, self_path=SELF)
        return gd == "build/automation", "chose %s" % gd
    icase("init follows an existing build/automation layout", layout)

    # dry-run writes nothing.
    def dry(tmp):
        subprocess.run(["git", "-C", tmp, "init", "-q"], check=False)
        created, _, _, _ = init(tmp, self_path=SELF, dry_run=True)
        wrote = os.path.exists(os.path.join(tmp, OVERLAY_DIR, "README.md"))
        return (len(created) == 3 and not wrote,
                "planned %d, wrote anything: %s" % (len(created), wrote))
    icase("dry run plans without writing", dry)

    failed = [c for c in cases if not c[1]]
    for name, ok, detail in cases:
        print("%s %s - %s" % ("PASS" if ok else "FAIL", name, detail))
    print("%d/%d selftest cases pass" % (len(cases) - len(failed), len(cases)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
