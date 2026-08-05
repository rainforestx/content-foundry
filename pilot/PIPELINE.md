# PIPELINE - how an article gets made

The production process as it actually runs, so a fresh session follows
this rather than re-deriving it. Governing documents in order of
authority: ANCHOR-SPEC.md (signed law), AUDIENCE.md (signed, binds
briefs), VOICE.md (taste rulings), BRAND-TOKENS.md (design system, gate-
enforced once signed), reviewer/CHECKLISTS.md (the battery), the machine
gates (gates/README.md).

## Stages

1. SUBJECT. Chosen on documented reader demand (the audience dossier,
   the shipped FAQ corpus, forum evidence) and substrate strength. The
   brief names a primary segment, a secondary, and required audiences.
2. GROUNDING (workflow, two parallel agents): a substrate index mined
   from the catalogue (read-only, tree verified untouched) and a
   RESEARCH.md - Drive route first, imprint over filename, snippets
   secondary-tier, claim-then-counter-claim searches for uncertain
   facts, ABSENT section with locations searched.
3. PRODUCE (one agent): writes index.html + CLAIMS.md against the
   signed docs and the grounding. Lane discipline (operator directive,
   2026-08-05): the producer stays on the article's lane; everything in
   the grounding is research INPUT to choose from, not obligations to
   discharge. When genuinely unsure, a targeted web search or a
   consensus of independent verifier agents settles it - unsettled
   facts become stated absences, never guesses. The producer runs the
   machine gates itself before finishing.
4. REVIEW (one adversarial agent, writes nothing): the full battery by
   name, tier-wall enforcement, audience-register pass, sibling
   consistency with shingle census, claims verification to source
   bytes, fresh renders, gates re-run independently.
5. FIX LOOP (conditional): one fixer takes all CRITICAL/MAJOR findings
   verbatim; scoped re-review confirms each ADDRESSED. Findings outside
   the fixer's write grant route back to the orchestrator (the
   cross-article census pattern).
6. INTEGRATE (orchestrator): apply out-of-grant corrections, add
   reciprocal cross-links, run gates, commit with explicit paths,
   render at 1280 and 375, deliver to the operator. Acceptance is the
   operator's, on the rendered artifact.

## Standing rules the stages inherit

- earx-catalogue is read-only; every agent that touches it reports
  git status --porcelain verbatim (must be empty).
- A claim that cannot go on the claims table does not ship; absences
  are stated to the reader, never padded.
- Twice-caught defects graduate to named checks; mechanizable checks
  graduate to gates (see CHECKLISTS.md growth rule).
- Operator decisions are recorded verbatim where they land (signatures
  in STATUS lines, taste in VOICE.md, accepted gate findings in the
  allowlist with justification).
