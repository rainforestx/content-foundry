# BASELINE - adjacent-process figures for the article pipeline

Status: FROZEN on 2026-08-02. Corrections are new dated entries below the
freeze line, never edits over these numbers (pre-agent-baseline-capture
SKILL.md, section 5, "Freeze it, and version any revision").

## What this is, and what it is not - the three honesty layers

1. **Adjacent process, not the target process.** These figures measure eBay
   LISTING production in /home/user/earx-catalogue, not article production.
   Differences, named per the substitution rule (SKILL.md section 4:
   "usable knowingly, differences named, never presented as this work's
   unaided cost"): listings are structured template instances (earx-v6)
   propagated in families from one operator-locked pilot, so the marginal
   listing is closer to variant emission than authorship; articles are
   long-form, each needing its own research depth; the illustration
   workflow differs (listings inherit template visuals, articles will not).
   Per-unit throughput below therefore CANNOT be read as an article rate.
2. **The incumbent is already agent-assisted.** The catalogue was built by
   an agent+operator system (earx CLAUDE.md, "Multiple AI agents
   collaborate on this repo"; .sync/AGENTS.md). So this is a baseline of
   the operator's current best production process - the honest comparator
   for "does the article pipeline beat how we produce now" - and it can
   never answer "what would a human alone cost". That counterfactual was
   destroyed before this repo began.
3. **The true article counterfactual is still open.** Operator's own
   articles from other properties were invited; none supplied as of
   2026-08-02. Failing that, the green-field gate (SKILL.md section 4)
   requires one deliberately hand-made, timed article before the pipeline
   contributes. Until one of those lands, this file is the only baseline,
   and it is the weaker, adjacent kind.

## Method and window (applies to every figure below)

Method: read-only mining of git history at /home/user/earx-catalogue,
commit 47b2f2b64 (HEAD, 2026-08-02). `git log --reverse --name-status`
over all 1,786 commits; a "listing" is any .html under
catalogue-view/listings/ or the 12 top-level brand trees, normalised to
its SKU basename (catalogue-view names strip their "brand__" prefix) so
canonical files and mirrors count once. 1,575 unique SKUs result, matching
the census in earx CLAUDE.md. Script preserved at scratchpad mine.py for
the session; figures are from its output, not recollection.

Window: 2026-06-23 21:05 to 2026-08-02 16:47 UTC (5.7 weeks, 1,786
commits, 305 touching listings). The 522 listings in the seed commit
2a2e81f7d ("baseline: earx-v6 catalogue at 522 listings") were produced
BEFORE this history, from work seeded off a 2026-05-27 zip (earx
CLAUDE.md, Current state); their production timing is unrecoverable and
they are excluded from rate figures.

Precision: counts are exact (executed against the log); anything called an
estimate below is labelled as one.

## Figures

### Production rate (unit = one listing SKU, first git addition)

- Post-seed production: 1,053 new SKUs in the 5.7-week window.
- Naive average: ~185 SKUs/week. Do not use this number alone - see
  cadence. Method: first-add date per SKU basename, weekly ISO buckets.
- Weekly first-adds: W27: 19, W28: 990, W29: 36, W30: 8, W31: 0.
- Production mechanism: 22 family-propagation commits added 955 of the
  1,053 (each ships 31-105 listings from one piloted family, e.g.
  9faf78452 "ReSound receivers - 105 listings"); 26 small commits added
  the remaining 98. The countable unit of authored work is closer to the
  ~48 add-commits (families/pilots) than to 1,575 listings.

### Cadence shape

- Burst, not steady: 1,009 of 1,053 post-seed SKUs (96 percent) landed in
  the 8 days 2026-07-05 to 2026-07-12; peak day 2026-07-11 added 477.
  W28 alone holds 63 percent of all first-adds in the repo's life.
- Listing-touching commits occurred on 23 of the window's 41 days;
  median 10 per active day, max 36 (2026-07-17).
- The last ~3 weeks (W29-W31) are consolidation and hygiene waves with
  near-zero new production.

### Rework rate (edit-after-ship proxy)

- Small-commit rework (commits touching <=10 listing SKUs, after the
  SKU's creation commit): 119 of 1,575 SKUs (8 percent) ever touched;
  199 touch events; median 1 touch per reworked SKU, mean 1.7, max 5.
- Wave rework, counted separately as directed: 228 of the 305
  listing-touching commits are waves (>10 SKUs). Every SKU sits under a
  median of 36 waves (max 50); four waves touched all 1,575 files (e.g.
  971e2ac7e pill centering fix, e6cd9fbbd name-drop removal).
- Stated limits of this proxy: (a) commit granularity is not hours - a
  touch says an edit happened, not what it cost; (b) the 8 percent
  understates true rework, because many waves ARE defect repair applied
  catalogue-wide (pill fixes, charset-proofing, wording compliance) and
  are excluded from the per-listing figure by construction; (c) defects
  caught by the operator at rendered-pilot review, before the pilot
  commit, leave no git trace at all. Escaped-to-buyer defects are not
  observable from this repo.

### Measures that do NOT transfer, said plainly

Cost per unit in hours or money: not derivable - git timestamps bound
sessions, not effort, and no timesheets exist here. Turnaround per unit:
not derivable for the same reason. Defect rate split by who caught it:
only the shape transfers (operator catches errors on RENDERED output
before propagation - earx CLAUDE.md working agreement; LEARNINGS.md
documents 200+ numbered mistakes as the internal-catch record), not a
rate. Outcome value (sales per listing): lives outside this repo,
unmeasured here. Stretching any of these from commit data would
manufacture numbers; per SKILL.md section 2, absence is stated instead.

### Unrepresentative-window hazard, argued both ways

This window is odd, and the hazard runs both directions (SKILL.md
section 5). Flattering direction: it contains a deliberate build sprint -
an 8-day family-propagation burst clearing a planned brand backlog with
mature template, tooling and conventions already in place. Read as
steady-state, ~185/week makes any article pipeline look hopelessly slow;
the sprint rate is the ceiling of a rehearsed process, not its norm.
Unflattering direction: the final three weeks show near-zero new
production because effort went to consolidation, governance and hygiene;
read alone, they make the incumbent look unable to produce at all, and
would hand the article pipeline an unearned win. Additionally, the 522
seed listings carry no timing, so the process's slower early period
(learning the template, accumulating LEARNINGS #1-150) is invisible -
the measured window is biased toward the process at its most practised.
No second window exists to sample; this whole repo is one campaign.

### What the post-agent comparison of each figure looks like

Per SKILL.md section 3, each figure names how its future twin is produced:
article production rate = first-add dates of article files in
content-foundry git; cadence = same bucketing over article commits;
rework = same two-tier proxy (small-commit touches per article, waves
separate) over article files. Units differ (listing vs article) and that
difference is permanent - comparisons stay adjacent, layer 1 above.

## Attestation

Figures computed and recorded by Claude (subagent, baseline-mining task)
on 2026-08-02 from the git history cited above. Attestation by a person
with standing is OUTSTANDING: the operator (RainforestX) has not yet
countersigned these numbers, and per SKILL.md section 5 this gap is a
ledger-grade caveat until they do.

---- FREEZE LINE 2026-08-02 - corrections below, dated, never above ----

CORRECTION 2026-08-02 (adversarial verification, same day as freeze).
The wave rework bullet cites e6cd9fbbd (CRA name-drop removal) as one of
the four waves touching all 1,575 files. Independent recount: that commit
touched 2,995 HTML files normalising to 1,478 unique SKUs, so it does not
belong in that set. The load-bearing figure stands - exactly four commits
do cover all 1,575 (971e2ac7e, 92b7075b9, a646fd183, 41d487446) - and the
correct second example is 92b7075b9 (pill optical centering). Same pass:
the waves-per-SKU median is method-sensitive; an independent script gets
37 against the frozen 36 (max 50 matches exactly). Read it as 36-37.
