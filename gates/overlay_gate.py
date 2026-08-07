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
REPO = os.path.dirname(HERE)
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
            findings.append((name, "name is not a plausible skill name; an "
                                   "overlay binds by filename, so this one "
                                   "binds to nothing"))
            malformed.add(name)
            continue
        with open(path) as fh:
            body = fh.read()
        stripped = body.strip()
        low = stripped.lower()
        if any(m in low for m in STUB_MARKERS) and len(stripped) < MIN_BYTES * 3:
            findings.append((name, "looks like a stub (contains a TBD/TODO "
                                   "marker and is short)"))
            continue
        if len(stripped) < MIN_BYTES:
            findings.append((name, "only %d bytes of content; an overlay that "
                                   "says nothing still reads as coverage"
                             % len(stripped)))
            continue
        if not referenced_by(root, name):
            findings.append((name, "nothing in the repository points at it. "
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
            findings.append((m, "on disk but absent from the README table"))
        for p in phantom:
            findings.append((p, "listed in the README table but not on disk"))

    return findings, real


def main(argv):
    root = REPO
    if len(argv) > 1:
        if argv[1] == "--selftest":
            return selftest()
        if argv[1] == "--root" and len(argv) > 2:
            root = argv[2]
        else:
            sys.stderr.write("usage: overlay_gate.py [--root DIR | --selftest]\n")
            return 2

    findings, real = check(root)
    findings += [(n, w) for n, w in check_proposals(root)]
    for name, why in findings:
        sys.stderr.write("%s/%s: %s\n" % (OVERLAY_DIR, name, why))
    if findings:
        sys.stderr.write("overlay_gate: FAIL - %d finding(s) over %d overlay(s)\n"
                         % (len(findings), len(real)))
        return 1
    print("overlay_gate: clean (%d overlay(s) live, %d proposal file(s); "
          "user-level parents NOT checkable from here)"
          % (len(real), len(proposals(root))))
    return 0


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

    failed = [c for c in cases if not c[1]]
    for name, ok, detail in cases:
        print("%s %s - %s" % ("PASS" if ok else "FAIL", name, detail))
    print("%d/%d selftest cases pass" % (len(cases) - len(failed), len(cases)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
