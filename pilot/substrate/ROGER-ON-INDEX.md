# Roger On - factual substrate index (article 1)

Map of the catalogue's verified material for the Phonak Roger On article
(subject per pilot/anchor-spec/SUBJECTS.md). Grounding rule: every product
fact in the article traces to an entry below; this index is what makes that
rule executable. All paths are under /home/user/earx-catalogue/. Surveyed
read-only on 2026-08-02.

Identity note, load-bearing: the shipped SKU is Roger On 3 (third
generation). Earlier generations (Roger On, Roger On iN) exist only inside
dossiers as compatibility context, never as listings. An article titled
"Roger On" is describing a product whose catalogue-verified form is the
gen-3 unit; generation claims must respect the version boundary below.

## 1. Listings (evidence standing: verified listing copy)

Canonical files in catalogue-view/listings/; each has a brand-tree mirror
and FAMILY_SPEC under Phonak/ (example: "Phonak/Wireless
Microphones/phonak-roger-on-3-v1.html" and
"phonak-roger-on-3.FAMILY_SPEC.md" - note the literal space in the dir).

- phonak__phonak-roger-on-3-v1.html - the subject. Roger On 3 copy:
  use cases, RogerDirect (15 mentions), cross-links to Select/Clip-On.
  Carries NO numeric specs (no battery hours, range, weight) and does not
  name MultiBeam.
- Ecosystem, same directory (one line each): roger-select-3, roger-select-in,
  roger-clip-on-mic, roger-pass-around-mic, roger-table-mic-3,
  roger-table-mic-ii, roger-table-mic-ii-in, roger-touchscreen-mic,
  roger-touchscreen-mic-3 (mics); roger-x-02, roger-x-03, roger-neckloop-02,
  roger-design-integrated-receivers (receiver pathways).
- Adjacent AirStream family for CI/streaming context: phonak__phonak-tv-connector-v1.html,
  phonak__phonak-remotecontrol-v1.html, unitron__unitron-partnermic-v1.html.

Standing caveat: DL-030 (see section 5) found real defects on Roger pages
mid-2026-07 (one repeated factual error on 4 gen-3 mic pages, 4 cross-page
contradictions); correction waves W3i and others have shipped but the Gap-1
rework was still open at DL-034. Before quoting a Roger listing sentence as
verified, check DECISION_LEDGER DL-030 status; where listing copy and a
producer fact-sheet conflict, the fact-sheet plus primary source wins.

## 2. Research dossiers (evidence standing: evidence-tiered dossier)

Master index first - it enumerates and reconciles everything below:

- research/ROGER_DOSSIER_CHAIN_CONSOLIDATED_INDEX_2026_07_16.md - full
  cross-reference of every Roger artifact, 14-SKU census, inconsistency log.
- research/PHONAK_ROGER_DOSSIER.md - all 14 SKUs, per-claim citations,
  HIGH/MEDIUM/LOW-UNVERIFIED confidence tiers. Core factual spine.
- research/T14_PHONAK_ROGER_DOSSIER.md - currently-shipping lens, per-product
  use cases, receiver classes, MSRP research (USD/AUD, tier UNVERIFIED),
  FDA status; cites Roger On datasheet and Roger On 3 user guide by URL.
- research/T14_PHONAK_ROGER_FAMILY_DOSSIER.md - taxonomy, compatibility
  grid, lifecycle, D-ROG-1 picker.
- DL-030 gap fact-sheets (producer lane, byte-citable, DO-NOT-SAY lists):
  - DL_030_GAP1_ROGERDIRECT_UNLIMITED_RECEIVERS_2026_07_27.md - which
    gen-3 mics carry built-in unlimited RogerDirect receivers; version
    boundary: that capability is documented first in Rogerpedia V9 AU
    (Roger Unlimited launch 2024-08-29); never cite it to V7/V8. Rework
    was still open at DL-034 - check ledger before leaning on it.
  - DL_030_GAP2 - who Roger does NOT work for (not-suitable substrate).
  - DL_030_GAP3 - receiver install authority (who can install).
  - DL_030_GAP4 - receiver-connection limits per mic per generation.
  - DL_030_GAP5 - Select iN licence count. GAP6 - cross-generation network
    rules (iN + gen-3). GAP7 - EasyGain/Check/Option (02) vs (03),
    byte-verified to Rogerpedia. GAP8 - meaning of "02" in NeckLoop 02.
- research/T26_ROGER_X_02_03_AUTHORITATIVE_AMENDMENT_2026_07_28.md plus
  T32, T32b, T33 - Roger X option split and tier-label deltas, re-derived
  at primary source by the consumer lane (DL-034).
- research/OP7_ROGER_PAIRING_DOSSIER_2026_07_18.md - per-device pairing
  and setup sequences.
- research/M5_NHS_ROGER_DISPOSITION_2026_07_16.md - NHS/Roger channel
  disposition. research/audioservice_roger.md - Phase 2 family analysis.
- blockers_research/B8, B9, B10 dossiers and OP6 - SKU-level blocker
  resolutions and mic availability.
- research/AIRSTREAM_FIRMWARE_LOCK_SCOPE.md - AirStream firmware-lock
  scope (adjacent, for the compatibility story).
- research/operator_briefs/DL_030_ROGER_CONFUSION_AUDIT_2026_07_27.md -
  the audit that defined what confuses buyers; useful as a negative map of
  what the article must explain clearly.
- Context matrices: STREAMER_CROSS_COMPAT_MATRIX.md,
  WIRELESS_ACCESSORY_COMPATIBILITY_MATRIX_2026_07_16.md.

## 3. Primary sources in-repo (evidence standing: primary source PDF)

Magic-byte verified against research/SOURCE_ARTEFACT_VERIFICATION.md -
consult that register before citing any PDF; nine fake artefacts (saved
404 pages) were caught there in July.

- research/rogerpedia_source_pdfs/rogerpedia_028-1902-02_V7.00_2023-02.pdf (+.txt)
- research/rogerpedia_source_pdfs/rogerpedia_028-1902-02_V8.00_2023-06.pdf (+.txt)
- research/rogerpedia_source_pdfs/rogerpedia_028-1902-48_V9.00_2024-09_AU.pdf (+.txt)

Version boundary (LEARNING #218): V7/V8 predate the Roger 3 generation;
Roger Unlimited built-in receivers appear only in V9 AU. Option (02)/(03)
feature table is V8 p26; V9 drops the Option split. MultiBeam appears in
the Rogerpedia texts, not on the Roger On 3 listing.

## 4. Conventions (evidence standing: convention rule)

- CATALOGUE-CONVENTIONS.md section 5 "Phonak ecosystem cross-compatibility"
  (lines ~206-230): the AirStream ecosystem list (Unitron, KS9/KS10, AB
  Naida CI M90, Sky CI M90) and the required CI-audience treatment for
  Roger-family products (CI in lede, chips, FAQ, bimodal Naida Link M).
- CATALOGUE-CONVENTIONS.md platform de-emphasis pattern (lines ~55-75):
  current-platform-first framing, "without AirStream wireless cannot pair"
  generic phrasing - transfers directly to article compatibility prose.
- CLAUDE.md "Domain guardrails" AirStream bullet - pointer only; CONVENTIONS
  section 5 is the home.
- Transfer limit, stated honestly: most CONVENTIONS rules (pills, palettes,
  spec rows, cross-pointer placement) are listing-layout law and do NOT
  transfer to article form. What transfers is the CI-audience requirement,
  the de-emphasis framing, and mechanism accuracy discipline.

## 5. Decisions and learnings

- build/scope-docs/DECISION_LEDGER.md DL-030 - the Roger rebuild directive,
  audit results, and current gate state. DL-031 (not-suitable rider,
  provenance boundary), DL-034 (14-PR merge, citation-defect story,
  source-artefact standard). Read before trusting any Roger listing byte.
- LEARNINGS.md #218 - version-URL mismatch on Rogerpedia editions; the
  citation defect class an article writer will otherwise repeat.
- LEARNINGS.md #170/#171 - why Roger was deliberately deferred (Tier 3,
  B8/B9/B10 blockers); background, not product fact.

## GAPS - what the substrate does NOT hold (source externally, flag for verification)

1. UK GBP pricing. T14 holds USD/AUD retail spreads tagged UNVERIFIED and
   no official MSRP anywhere. Category: genuinely absent at source for UK;
   an article price claim needs fresh external sourcing.
2. Roger On generation timeline. Gen-3 launch 2024-08-29 is held (Sonova
   press release, cited in T14/GAP1). Launch dates for Roger On v1 and
   Roger On iN are not in the dossiers I searched (PHONAK_ROGER_DOSSIER,
   T14 pair, DL-030 gaps); external sourcing needed for a history section.
3. Numeric hardware specs: battery life hours, streaming range in metres,
   weight, charge time. Absent from the listing; the Roger On datasheet and
   user guide are cited by URL in T14 but NOT committed in-repo, so any
   spec quoted from them must be re-fetched and verified (the saved-404
   lesson applies).
4. Independent review and comparison material (vs competitor remote mics,
   user experience, real-world benefit studies). The substrate is
   manufacturer-fact substrate; article-voice evaluation needs external
   sources clearly separated from catalogue-verified fact.
5. Phonak marketing tech-name explanations (MultiBeam behaviour detail
   beyond Rogerpedia's text; Stereo Wide Pointing specifics). Partially
   held (GAP1, Rogerpedia V9 txt); verify depth before writing.
6. Roger On 3 compatibility beyond the Phonak/AB ecosystem (e.g. use with
   non-Sonova aids via Roger X/DAI is covered; cochlear-brand or Oticon
   direct claims are not) - do not extrapolate past the matrices.
