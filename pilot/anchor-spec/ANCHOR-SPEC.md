# ANCHOR-SPEC - illustrated articles for the directory property

STATUS: SIGNED by the operator (RainforestX), 2026-08-02, in session:
"sign the anchor spec. proceed with the first article". Generation is
authorized against this version. Section 3's skeleton remains PROPOSED in
origin - signed as the working structure, refined by what production
teaches. Amendments require a new signature.

Every rule cites its source (CATALOGUE-CONVENTIONS.md as CONV; CLAUDE.md
where a rule lives only there). CONV carries three colliding numbering
regimes (CONV header note, 2026-07-05); this spec is plain ASCII, so:
"CONV p.N" = the plain original sections 1-14; "CONV sec.N" = the
section-glyph regime; "CONV S-N" = the glyphless S-series. Titles are added
where numbers collide (CONV sec.64, evidence tiers, and CONV S-64, charset
markup, are different sections).

Voice and form: form-references.md in this directory is incorporated by
reference. Voice target: independent, audiologist-grade, consumer-readable.
Form references are mined for skeleton only; phrasing is never copied or
closely derived; factual claims come only from the catalogue substrate,
never from those pages.

Method per the subjective-quality-guidance doctrine: negative constraints
over positive direction, verification against the rendered artifact.

## 1. What transfers from the catalogue conventions

### 1.1 Factual discipline

- Mechanism accuracy is the number one defect class (CLAUDE.md, "Mechanism
  accuracy"): SnapFit 1.0 is not 2.0, CeruShield is not CeruStop, ProWax is
  not NoWax. Never blur adjacent mechanisms; identify wax guards/filters by
  SHAPE language, never colour - pack colour varies by region and batch
  (CONV sec.44).
- Wax filter type follows receiver generation, not hearing aid platform
  (CLAUDE.md, "Wax filters"). Never platform-cutoff framing for filters.
- Any numeric spec (mm, g, ml, hours) requires a primary or near-primary
  source; never inherited from a sibling product, a single forum claim, or
  convention defaults. Where the manufacturer publishes no consumer figure,
  flag with "approx." (CONV sec.41).
- Tool requirements and procedures are verified against manufacturer
  documentation before writing; retailer compatibility lists are
  descriptive, not prescriptive; similarly named tools are different
  products until proven identical; procedures vary by generation within one
  brand, so verify each (CONV sec.13, "Tool requirements and procedural
  copy"). Procedural claims quote the manufacturer with the source named.
- Evidence tiers govern confidence (CONV sec.64, "Evidence-grade tier
  definitions"): CONFIRMED and SUSPECTED-STRONG claims may appear in
  confident-but-hedged prose; SUSPECTED, [UNVERIFIED], and NONE never
  appear in confident form - they become explicit "verify with your hearing
  care professional" language or are omitted.
- Hedge preservation (CONV sec.66, layer 3): adapting a hedged claim must
  preserve the hedge's TARGET (what exactly is unresolved) and its EVIDENCE
  CONTEXT (why). Stripping a hedge, or keeping hedge-shaped wording while
  hiding why it exists, is a defect.
- Quotation fidelity: quoted text is never altered to satisfy a style rule;
  intentional edits sit outside the quotation marks with an "amended:"
  preface (CONV S-72; violation classes in CONV sec.54e).
- Brand-family attribution must be correct: Sonova (Phonak, Unitron,
  Hansaton, Advanced Bionics), Demant (Oticon, Bernafon, Sonic, Philips
  Hearing Solutions), independents (Widex, GN ReSound, Starkey, Signia).
  Cross-compatibility claims stay inside the verified family (CONV sec.38).
- Brand OWNER and hardware SUPPLIER are separate claims, stated separately;
  a rebadge supply relationship never implies ownership (CONV sec.62).
- Verification-first authorship: no brand, family, or product claim is
  inherited from memory or a prior artifact without checking the substrate
  first; contradicting an existing artifact requires a primary-source
  citation (CONV sec.55b). Unstated manufacturer facts are never invented
  (CONV sec.53, rule 4).

### 1.2 Terminology

- Manufacturer-authoritative naming at first mention: full official
  designations ("Phonak Receiver (SDS 6.0)", "Oticon Receiver (miniFit
  Detect)"); shorter forms only once context is established (CONV sec.14,
  "Manufacturer-authoritative naming").
- Buyer mental-model framing for rebadges: "high street retailer variants
  made by Sonova (Costco Kirkland Signature, Specsavers Advance Elite)",
  never "whitelabel" or "OEM rebrands"; name the specific model, not the
  whole range (CONV p.5).
- Where a retailer range is multi-OEM-sourced, prefer concrete verified
  model lists over blanket disclaimers; check-with-retailer framing only
  when the split is not cleanly identifiable (CONV sec.38).
- Brand-pure model lists: never Oticon model names in Bernafon context (or
  vice versa) without an explicit brand label (CONV p.4; p.14, "Copy-paste
  hygiene"). Never call current platforms "older" (CONV p.14).
- Reader-facing vs audiologist language: plain language on the surface,
  technical codes (SDS generations, receiver codes) introduced deeper in
  with explanation, so both audiences are served (CONV p.12).
- Prose never references page structure: no "see the section below", no
  "card", "accordion", "callout" - write "see above"/"see below" or name
  the topic (CONV sec.26, "Buyer copy never references HTML structure").

### 1.3 Typography and ASCII

- No em-dashes anywhere in article output; a hyphen with surrounding spaces
  instead (CONV p.11, "Typography conventions"; CLAUDE.md hard discipline).
  House style extends this to full plain ASCII: no en-dashes, smart quotes,
  or ellipsis characters.
- Single hyphens in compound modifiers, no surrounding spaces ("push-in
  stick format") (CONV p.11).

### 1.4 Accessibility and rendering

- Text contrast passes WCAG AA; light brand colours are decoration only,
  never text-on-white - a darker same-hue tone carries text (CONV p.2;
  sec.57). Applies to illustrations, diagrams, captions.
- Colour is never the sole information channel in an illustration, except
  the industry-standard receiver ear markers (red = right, blue = left),
  which are functional (CONV sec.16; sec.44 scope note).
- Wide content must not force horizontal scroll; layouts adapt at narrow
  widths (CONV p.9, "Mobile responsiveness" - the principle, not the CSS).
- Two-pass review before ship: a structural/visual pass on the rendered
  page, and a separate content pass reading the words as a reader would;
  the content pass cannot be replaced by structural checks (CONV sec.34,
  sec.35).

### 1.5 Audience framing

- Older-platform de-emphasis: lead with current-generation models; older
  platforms appear as supplementary support, tagged as earlier platforms,
  never featured; list ordering is actively-fitted first, legacy last
  (CONV p.1; p.9, "Receiver / platform list ordering"). Older-model
  questions phrased generically ("What about older Phonak models?"), not
  as name-list cutoffs (CONV p.1A). Never mislabel current aids as "older"
  because they use a classic receiver platform (CONV p.1B).
- Cochlear implant users are a required audience wherever AirStream-family
  products appear (TV Connector, Roger, PartnerMic, RemoteControl): name AB
  CI compatibility explicitly, cover bimodal use, name older AB processors
  that lack AirStream (CONV p.5, "Cochlear implant audience visibility";
  CLAUDE.md "AirStream listings").
- NHS Phonak is "AirStream-equipped", not tied to one platform name
  (CONV p.5, "NHS Phonak").
- Affirmative-vs-redirect division of labour: the passage saying who a
  product IS for never doubles as the redirect for who it is NOT for, and
  no model is named in both (CONV p.10, "Scope and warning callout").
- FAQ tone: lead with the answer (yes where defensible), then caveats;
  conditional language ("may need") over absolutes; warning-first framing
  only for genuine safety risks (CONV sec.15). Each FAQ answer adds at
  least one net-new fact, never a restatement (CONV sec.56b).
- Independence and attribution honesty: correct parent-company trademark
  attribution and a plain statement that the property is independent of the
  manufacturers (CONV p.6, adapted from listing fine-print to an
  article-foot disclosure).

## 2. Explicitly excluded - listing-specific, does not transfer

Listed so a reviewer can see the judgment, not just its result:

- Pill styling, picker tables, self-pills, browse pills, picker dynamics
  (CONV p.9, sec.36, sec.51, sec.52, S-71).
- Glance grid, chips bar, spec table mechanics, comparison-table CSS
  (CONV sec.18, sec.46, sec.49, sec.43; CLAUDE.md "Pills").
- CTA buttons, hover CSS, tint hierarchy, brand CSS variables, structural
  border rules (CONV sec.27 through sec.33, both colliding regimes).
- eBay constraints: numeric-entity encoding (CONV S-64), the presentation
  and mobile CSS blocks (CONV S-65, S-68, S-69), the S-74 notice element,
  eBay search-URL cross-links (CONV p.13), listing title grammar
  (CONV sec.61).
- Manufacturer part numbers stay non-reader-facing (CONV sec.11,
  "Manufacturer part / reference numbers"). The dispute-risk rationale is
  retail-specific, but the default carries over: readers identify by model
  and size; an article citing a PN needs a stated reason.
- Two-lane process machinery: flow gears, cron, bus, PR gates (CONV
  sec.53-sec.60, sec.63, sec.65-sec.69, S-66-S-73) - governance for the
  catalogue repo. What survives of it is already extracted above (evidence
  tiers, hedge preservation, quote fidelity, fresh authorship).
- Cross-sell tiering by attach-rate (CONV sec.19) - directory articles are
  not merchandising surfaces; commercial links are an operator decision
  outside this spec.

## 3. Article structure grammar - PROPOSED, not derived

The conventions define listings, not articles. This skeleton adapts what
listings do well (scope statements, compatibility precision, FAQ
discipline) to long form; section names are working labels.

1. Title and standfirst - manufacturer-authoritative product identity
   (CONV sec.14), then 2-3 sentences of what it is and who it serves. No
   decision-narrowing, no duplication of later sections (CONV sec.37, lede
   rules).
2. Scope statement - affirmative: what the article covers, which devices
   and audiences, current platforms leading (CONV p.10; p.1).
3. What it is and how it works - mechanism in plain language first,
   technical designations introduced with explanation (CONV p.12);
   shape-language identification where relevant (CONV sec.44).
4. Real-world use - the form-reference territory: usage patterns, practical
   strengths and limits, independent voice (form-references.md). Every
   factual claim tiered per CONV sec.64.
5. Compatibility in precise terms - current-first ordering, family-correct
   cross-brand claims, retailer variants named at model level, CI audience
   where AirStream applies (CONV p.1, p.5, sec.38).
6. Who this is not for - redirect framing with named alternatives, kept
   apart from the scope statement (CONV p.10, warning framing).
7. FAQ - lead-with-yes tone, generic older-model questions, net-new fact
   per answer (CONV sec.15, p.1A, sec.56b).
8. Sources and independence - what the claims rest on, plus the
   independent-property disclosure (CONV p.6, adapted).

Illustrations: each caption is itself a claim and is fact-checked like body
prose; the contrast and colour rules of 1.4 apply.

## 4. Negative constraints - the never list
1. Never an em-dash, en-dash, smart quote, or ellipsis character (CONV
   p.11; CLAUDE.md; house style).
2. Never identify a wax guard or filter by colour (CONV sec.44).
3. Never platform-cutoff framing for wax filters - receiver generation
   determines filter type (CLAUDE.md, "Wax filters").
4. Never confuse adjacent mechanisms - CeruShield/CeruStop, ProWax/NoWax,
   SnapFit 1.0/2.0 (CLAUDE.md, "Mechanism accuracy").
5. Never call a current platform "older"; never sister-brand model names
   without a brand label (CONV p.14; p.4).
6. Never a numeric spec without a primary or near-primary source
   (CONV sec.41).
7. Never a tool requirement or procedure unverified against manufacturer
   documentation (CONV sec.13).
8. Never infer brand ownership from hardware supply, or vice versa
   (CONV sec.62).
9. Never an unverified cross-brand compatibility claim outside the
   verified corporate family (CONV sec.38).
10. Never SUSPECTED, [UNVERIFIED], or NONE-tier claims in confident prose
    (CONV sec.64, "Evidence-grade tier definitions").
11. Never strip a hedge or detach it from its evidence context
    (CONV sec.66, layer 3).
12. Never alter quoted text to satisfy a style rule (CONV S-72).
13. Never "whitelabel" or "OEM rebrand" in reader-facing prose (CONV p.5).
14. Never reference the page's own structure in prose - no "section
    below", "card", "accordion" (CONV sec.26).
15. Never lead an FAQ answer with warnings where a service-offer answer is
    defensible (CONV sec.15).
16. Never omit the CI audience from AirStream-family coverage (CONV p.5).
17. Never copy or closely derive phrasing from form references, and never
    take a factual claim from them or from manufacturer marketing or
    retailer pages (form-references.md standing discipline; CONV sec.13
    source-authority order).
18. Never invent an unstated manufacturer fact; absent facts are absent or
    flagged (CONV sec.53, rule 4).
19. Never declare an article done without reviewing the rendered page,
    every illustration included, at desktop and phone widths - the
    acceptance test is the artifact, judged by the operator, not the
    author (CONV sec.34, sec.35; subjective-quality-guidance mechanism 5).

## 5. Verification and sign-off
An article draft ships to review with: the rendered page at all target
widths; the negative constraints checked BY NAME (an unnamed check did not
happen); and a claims table mapping each factual claim to its substrate
source and evidence tier (CONV sec.64). The operator holds aesthetic and
factual authority; disagreement resolves in the operator's favour, and
taste rulings are recorded here (subjective-quality-guidance, "Reviewing
subjective work").

Signature status lives in the STATUS line at the head of this file.

## Amendment A1 - product imagery (SIGNED)

Basis: the operator stated in session, 2026-08-04: "we have full
permissions for from the manufacturer", and on 2026-08-04 (late session)
directed integration: "what about the official supplier photography and
diagrams as discussed?" - recorded here as the activating signature.
Execution note, same date: the Drive archive's Roger On packshot set
(asset 056-3010, created 2021-02) is GEN-1 imagery, and no Roger On 3 or
Select 3 packshots exist in the archive; since gen 1 and gen 3 are
externally near-identical, generation evidence must come from asset
provenance (which portal folder or asset number it came from), not from
looking at the picture. Integration therefore waits on gen-3 assets
landing in Drive (or operator photography of held stock) - tracked in
pilot/ACQUISITIONS.md.

1. Sources, in order of preference: (a) the operator's own photography of
   held stock - no licence question, reinforces the independence
   disclosure, unique to the property; (b) official manufacturer imagery
   under the stated permission, taken from the operator's Drive archive
   (the archive holds official packshots and product renders); (c) nothing
   - absence over an unverified image.
2. Every image is a claim. An IMAGES section in the article's CLAIMS.md
   records: filename, source (Drive file id or shoot date), licence basis
   (operator permission / own photograph), and generation-verified-by -
   the visual check that the pictured unit is the generation the article
   covers. A filename's generation claim is never trusted (the misfiled
   user guide precedent, RESEARCH.md sec 6 of the Roger On 3 article).
3. Captions are body prose: fact-checked, tiered, and listed in the
   claims table like any sentence.
4. Attribution: official imagery is captioned "Image: Phonak" (or the
   owning brand); own photography needs no attribution line.
5. Presentation: images are compressed files in the article directory,
   relative src, explicit width and height, alt text written as a factual
   description (the alt is also a claim); the AA-contrast rule applies to
   any text overlaid or adjacent; no image may be the sole carrier of a
   fact the prose does not state.
6. Diagrams are not replaced: photographs show what a thing looks like;
   the drawn figures carry mechanism. Both justify their place
   independently.
