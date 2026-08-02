# Reviewer checklists - illustrated articles

Distilled from /home/user/earx-catalogue/LEARNINGS.md (entries numbered
through #221, 2026-05 to 2026-07; #1-#41 exist only as the summary at the
file head, and early numbers #46-#48, #56, #59 and #73 each label more than
one entry, so the file carries 187 numbered headers, not 221). Checklists are failure-class driven per the adversarial-review-battery
skill: every item below is a defect class that actually shipped or nearly shipped
in the catalogue, cited by LEARNING number. Items marked (adapted) generalize a
listing-specific mechanic; the article-shaped version is what the item states.
Unmarked items transfer directly. Run every item on every review; do not skim
for "the ones that apply".

## Pass 1 - Factual accuracy

1. Verify every existence, completion, or "already covered" claim against the
   actual files or draft, with the search location stated. Handover notes,
   session memory, and outlines are unverified claims until checked. (#158,
   #161, #201)
2. Trace every "only", "never", "all", "exclusively" to a source stating that
   exact direction. "X only fits Y" does not license "Y only takes X"; state the
   sourced direction and stay silent on the converse. (#168)
3. Check each verification chain for circularity: a claim confirmed against copy
   that inherited the claim is UNVERIFIED, not confirmed. Every confirmation
   names the independent source it was checked against. (#205)
4. Grep the author's own prior artifacts (earlier articles, research notes,
   corrections) for every load-bearing claim. Contradicting your own corpus is
   the same defect as contradicting canon; a document written hours ago is a
   source. (#194, #209)
5. Reject reasoning from absence. A fact missing from one channel, sample, or
   schema is evidence about that surface, not about the world - and only counts
   at all once the instrument is shown able to register a positive. An absence
   claim states where it looked. (#190, #203, #204, #220)
6. For any cited versioned source, record edition and publication date, not just
   the URL. A fact that post-dates its cited edition is arithmetic proof of a
   wrong citation; endpoints rotate editions silently. (#218)
7. Never assert a count or status from memory - derive it fresh, and never
   present one number read two ways as two corroborating readings. (#213, #217,
   CLAUDE.md census rule)
8. Separate speculation from fact in research inputs: "coming soon", forum
   guesses, and hedged synthesis read identically to confirmed fact once pasted.
   Verify product and compatibility claims against a primary source. (#92)
9. (adapted) Category membership does not imply attribute inheritance. In the
   catalogue this was platform vs form factor vs parts; in articles it is any
   "X is in family F, so X has F's property" move. Verify all three levels.
   (#94, #100)
10. Check the draft for internal contradictions: a new positive claim that falls
    inside an existing exclusion elsewhere in the piece means one of the two is
    wrong - treat the existing statement as a fact-check, not an obstacle. Also
    scan for opposite advice in different sections. (#94, #67 item 5)
11. (adapted) Do not assert a property of an artifact you have not opened or
    executed - an image "showing X", a linked page "saying Y". In instructions
    to other agents this bar is higher, not lower: an unverified premise inside
    an instruction becomes an executable defect. (#211)
12. Grade evidence tiers before treating identity claims as settled: marketing
    "same platform" language is SUSPECTED; only primary documentation asserting
    identity on both sides is CONFIRMED. (#186, #192)

## Pass 2 - Carryover (the clone-audit class)

Articles adapted from a sibling article, template, or research dossier inherit
their donor's defects byte-for-byte. This was the catalogue's single most
expensive class (117-file contamination, #162).

1. Before adapting, enumerate and classify EVERY subject-bearing token in the
   donor (brand, product, number, audience) as swap / invert / keep - the
   classification pass doubles as a donor audit and catches donor defects before
   they multiply. (#183)
2. Audit the donor itself, not just the adaptation: donor defects propagate
   silently, including invisible ones like uncommented template-instruction
   text. (#162, #165)
3. Scan variant-bearing strings, not a known-defect list. A donor contaminates
   every token position, not just the ones already noticed; pass 2 of the same
   sweep found as many wrong strings as pass 1. (#172, #173)
4. Check the donor's own testimony about the target subject: if the donor
   explicitly says the target differs, adaptation is refused and the piece goes
   to research instead. (#186)
5. When a defect is found, census the defect CLASS across every artifact
   carrying that element - not just the files the fix touched. Sibling wordings
   of the same defect hide behind a clean residue check scoped to one needle.
   (#173, #219, and the sec.47 rule via #162)
6. When one false claim is found, grep the whole piece (and siblings) for the
   entity - the same claim is often repeated for emphasis elsewhere. (#67)
7. (adapted) If the donor carries a flagged-but-unresolved disputed claim, the
   adaptation names the inherited dispute rather than silently copying or
   silently "fixing" it - silence reads as endorsement, and a fork doubles the
   eventual correction. (#187)
8. A flagged-but-unfixed defect in a donor is a defect factory: every open flag
   becomes a fix or an owned queue item before the donor is reused. (#172, #99
   via #172)

## Pass 3 - Terminology

1. Mechanism confusion is the number-one defect class in the source domain:
   near-identical product mechanisms (CeruShield vs CeruStop, ProWax vs NoWax,
   SnapFit 1.0 vs 2.0) swapped mid-copy. Verify every mechanism name against the
   product it is attached to, per mention. (CLAUDE.md guardrails; #130, #67)
2. Verify every brand+product pairing exists - "Unitron Infinio" shipped in 117
   live files and was a nonexistent product. Composed names are inventions until
   checked. (#183)
3. Use current product names and mark older generations as such; renames
   (Audeo Infinio to Audeo Infinio Ultra) silently stale a piece. (#152, #153)
4. No web/UI vocabulary in reader-facing copy: "callout", "card", "section
   below" describe structure, not content. Navigation references are positional
   ("see below"), and the copy must read aloud cleanly to someone who has never
   seen a web page. (#49)
5. Terminology normalization is per-context, never blanket regex: the same word
   is correct in one product context and wrong in the next. Audit each instance.
   (#121, #124, #125, #126)
6. Attribute trademarks and brand ownership to the correct entity; group-shared
   platforms are not owned by the sub-brand using them. (#67 item 4, #194)

## Pass 4 - Structure

1. Review the RENDERED article, not the source diff. Structural validity is not
   structural correctness: well-formed markup can hide invisible sections,
   leaked placeholder text, and nonsense a buyer-eye read catches instantly.
   Render review repeatedly caught what every mechanical audit passed. (#83,
   #165, #173, #193)
2. Semantic heading-vs-body check: every section's body is about what its
   heading names. A cloned section kept its title and someone else's body for
   weeks. (#162)
3. One message, one surface within a reading flow: the intro's thesis is not
   restated as a section opener, adjacent blocks do not duplicate each other,
   and each visible layer has exactly one role. Four costumes of this defect
   shipped before the pattern was named. (#169, #176, #178, #185)
4. Diff fresh-authored pieces against 2-3 shipped siblings AND against written
   canon - component usage and section roles both. Nearest-sibling conformance
   propagates dialects; the canon must be written, not inferred from whichever
   donor was handy. (#188, #189, #195)
5. Cross-references live where their subject lives: a note about product B does
   not sit inside product A's section. (#100)
6. (adapted) Check generated headings and captions for leaked markup or
   variable-shadowing artifacts - a heading containing "<" is a hard fail.
   (#193)
7. (adapted) Review the version that ships, not the working copy: draft on
   disk, committed draft, and published render are different surfaces, and a
   check on one certifies nothing about the others. Name the surface each check
   read. (#215, #216 scope note)

## Pass 5 - Style

1. Zero em-dashes in shipped output; space-hyphen-space instead. Run the check
   before every write - this regressed repeatedly whenever fresh copy was
   generated without the gate. (#86, #102, CONVENTIONS sec.11 via #86)
2. Check for mojibake and encoding damage by MECHANISM, not by example: derive
   the needle set from "every codepoint this damage class can produce", and give
   any detector a control that fails loudly when the detector itself is broken.
   An em-dash gate reported zero while 2,514 double-encoded ones shipped. (#216,
   #221)
3. Surgical edits only: when removing a wrong detail, do not strip the correct
   context around it; when an edit is disputed, check the piece's history first -
   one proposal had already been executed once and reversed by the operator.
   (#125, #72/#78 via #217)
4. Watch the second change: iterating a good fix into an overcorrection is its
   own failure mode. (#76, #117)

## Reviewer instrument discipline (checks on the checks)

1. A zero from a bounded pattern is not a zero - verify absence with a second,
   independently derived method, and never reproduce the author's number with
   the author's own method and call it corroboration. (#203, #207)
2. State what a count counts (instances vs definitions, exact vs substring
   match) before trusting it; a set-valued accumulator hides multiplicity by
   construction. (#198, #213)
3. When your finding contradicts a working, operator-reviewed artifact, the
   assertion is on trial first: re-verify your own selectors before writing the
   finding. (#198)
4. A correction pass is a pass and inherits every failure mode of the pass it
   corrects; relationships between two sets need the computed intersection,
   never inference from cardinalities. (#212)
5. Differential checks (draft vs previous draft) cannot see defects that
   predate the wave; keep at least one absolute check in the battery. (#214)
6. Evidence must be fresh: checksum screenshots and illustrations against
   previously used assets before accepting "new capture" claims. (#200)

## Does not transfer (eBay/platform mechanics - noted so nobody stretches them)

- eBay description-wrapper viewport, CSP, and style-survival findings. (#204)
- eBay master CSV keying, CustomLabel grammar, status columns, variation rows.
  (#184, #191, #199)
- SKU gap-matcher tooling and brand-prefix census mechanics. (#158 tooling,
  #207 script, #213)
- Listing UI conventions: pickers, pills, hover states, accordion mechanics,
  brand palette hex derivation and live-site palette audits. (#46-#66,
  #109-#120, #177, #179-#182, #196, #197, #202)
- Multi-agent git sync, lock, and wave-commit mechanics (the orchestrator owns
  integration here). (#159, #160, #164, #206)
- B1-B10 blocker delegation and provisional-ruling machinery. (#170, #171)

## Growth rule

Any defect class caught twice in article review graduates into this file as a
named check, in the pass where it belongs, citing both catches - the same
ladder as the source system (LEARNINGS entry, then named checklist item, then
machine gate where a check can be mechanized; see adversarial-review-battery
SKILL.md growth rule and #195's registry graduation). A defect flagged but not
converted into a named check or an owned queue item is a defect factory (#172).
