# Phonak TV Connector - factual substrate index (article 3)

Map of the catalogue's verified material for the Phonak TV Connector
article (the dedicated TV streamer for AirStream-capable hearing devices).
Grounding rule: every product fact traces to an entry below. All paths are
under /home/user/earx-catalogue/. Surveyed read-only on 2026-08-05.

Identity note, load-bearing: the shipped listing is the TV Connector V2
(the FAQ names it TV Connector "D"). Phonak's master-row title says plain
"TV Connector", and the FAMILY_SPEC flags the V2 label for producer
confirmation - never present the version label as settled beyond "the
listing identifies the shipped unit as V2". A second identity tension:
T19 lifecycle tags the product LEGACY (named in the Rappel section of
Phonak's 2025-07 FR phase-out PDF) while phonak.com still showed it as a
current accessory the same pass - the article must not call it either
"current flagship" or "discontinued" without fresh external verification.

## 1. Listings (evidence standing: verified listing copy)

- catalogue-view/listings/phonak__phonak-tv-connector-v1.html - the
  subject, 1,014 lines, CustomLabel PHO-TV-CONNECT. Brand-tree mirror
  "Phonak/TV Streamers/phonak-tv-connector-v1.html" verified byte-identical
  by diff this survey; FAMILY_SPEC.md and -v1.md siblings alongside.
  Cloned structurally from the Bernafon TV-A donor (header comment), all
  copy rewritten. Carries: range "Up to 15 metres (50 ft)", optical
  TOSLINK + 3.5 mm jack inputs, Dolby Digital compatible, unlimited
  simultaneous listeners, V1-vs-V2 delta FAQ, PCM/Stereo TV-settings tip,
  Sky Glass incompatibility note, TVLink S / ComPilot named as the legacy
  pre-AirStream path, 1-year accessory warranty FAQ, and the full CI
  treatment (see section 3).
- catalogue-view/listings/unitron__unitron-tv-connector-v1.html - the
  sister listing, 1,023 lines, UNI-TV-CONNECT; mirror "Unitron/TV
  Streamers/" also verified identical. Same V2 copy adapted per the
  LEARNING on donor cross-brand claims (substitution proceeded because the
  Phonak donor FAQ itself asserts hardware equivalence). Carries no part
  number; T57 supplies 076-5049-06 (see section 4) as a proposal only.
- Adjacent AirStream family in the same directory (grep airstream):
  phonak__phonak-remotecontrol-v1.html (Phonak-specific, NOT shared with
  Unitron - T15 sec 6.2), unitron__unitron-partnermic-v1.html, and the
  Roger family (indexed by the two sibling articles).

Quote-check state: DECISION_LEDGER greps ZERO rows for "TV Connector" or
AirStream - no ledger dispute on the subject. The live dispute lives in
the FAMILY_SPEC instead: SPEC-DIV-1 (category 1-buyer-facing, status
waiting-on-operator). The shipped listing claims USB-C power in 4 places
(incl. box contents "USB-A to USB-C cable (1.3 m)"), but the
operator-supplied phonakpro.com TV Connector datasheet says micro-USB
(5 VDC >500 mA) "for both legacy and current models" (recorded in
research/brand_palettes.md notes). No HTML edit until the operator rules.
THE ARTICLE MUST NOT ASSERT EITHER CONNECTOR TYPE - this is the exact
divergence, unresolved, and the datasheet is not committed in-repo.

## 2. AirStream doctrine - CONVENTIONS section 5 is LAW here

CATALOGUE-CONVENTIONS.md section 5 "Phonak ecosystem cross-compatibility"
(lines 206-230):

- Ecosystem list: Phonak (primary), Unitron (Sonova consumer brand, uses
  AirStream), Costco Kirkland Signature KS9/KS10 (made by Sonova), Vitus+
  (Phonak's value brand, Marvel-based), Advanced Bionics Naida CI M90
  (current adult CI sound processor, SWORD chip - same Sonova radio
  platform as Marvel/Paradise/Lumity), AB Sky CI M90 (paediatric).
- Required CI treatment, six placements, and the TV Connector is named
  first in the rule's own product list: CI named in lede; scope "Also
  supports" clause; a CI-aware chip; FEATURED compat bullets (never a
  footnote); a dedicated AB FAQ covering bimodal use - the rule's words:
  "Cover bimodal use (Phonak Naida Link M + AB CI streaming together)";
  and older AB processors (Naida CI Q-series, Harmony, Neptune, Chorus)
  in not-suitable. The shipped FAQ (listing line 977) renders the bimodal
  fact precisely: "If you wear a Phonak Naida Link M hearing aid alongside
  your CI as a bimodal solution, both devices stream from a single TV
  Connector simultaneously." Cite it in that shape - one TV Connector,
  both devices, simultaneous.
- NHS rule: NHS Phonak (sometimes branded Nathos Nova) is described as
  "AirStream-equipped", never tied to a platform name; the listing adds
  the honest caveat that NHS provision varies and some fittings lack
  AirStream.
- The de-emphasis pattern (CONV lines ~55-80) names "the Phonak TV
  Connector pattern" as its own worked example - current platforms in the
  lede, older tagged grey, warning framed "Older Phonak hearing aids
  without AirStream wireless cannot pair", generic older-model FAQ.
- Trademark line (CONV section 6): "Phonak, AirStream, and TV Connector
  are trademarks of Sonova AG."

## 3. Dossiers and research (evidence standing: evidence-tiered dossier)

- research/AIRSTREAM_FIRMWARE_LOCK_SCOPE.md - the P0 settlement of Issue
  #11: "firmware-locked against cross-brand use" means locked against
  NON-SONOVA brands, not between Phonak and Unitron. Primary anchors: the
  Sonova SWORD chip press release (chip spans Phonak, Unitron, Hansaton,
  AB; names AirStream explicitly) and the Rogerpedia brochure. Hansaton is
  SUSPECTED-STRONG at platform level only - no Hansaton-branded TVC SKU
  found; never assert one. Also flags the Phonak Roger receivers page
  drift (CORRECTIONS_LEDGER Correction #20, citation refresh, unapplied).
- research/STREAMER_CROSS_COMPAT_MATRIX.md - Phonak-Unitron TV Connector
  hardware CONFIRMED shared (the strongest cluster in the whole matrix; a
  reversal of the charger finding for the same pair). Sec 7.1 terminology
  law: Phonak/Unitron copy says "TV Connector", never "TV streamer" or
  "TV adapter". Sec 6: V2 span Infinio/Lumity/Paradise/Marvel/B-Direct
  plus AB CI processors - materially broader than Oticon's TV Adapter 3.0
  LE Audio boundary (a usable comparison, already tiered).
- research/TV_STREAMER_CATALOGUE_v1.md - 17-SKU cross-brand enumeration.
  Phonak row: 2.4 GHz AirStream, 15 m range, unlimited users, GBP 160 inc
  VAT via HAB Hearing (RETAILER citation - near-primary at best). Unitron
  row: GBP 144.00-172.80 via Crystal Hearing. Not manufacturer MSRP.
- research/WIRELESS_ACCESSORY_COMPATIBILITY_MATRIX_2026_07_16.md sec 2.7 -
  Unitron TVC existence CONFIRMED, full platform-ladder detail SUSPECTED.
- research/T15_PHONAK_FAMILY_TAXONOMY.md sec 6.1 - flags the listing's
  compat claims SUSPECTED-STRONG pending re-verification against a live
  Phonak spec page (never fetched); sec 6.2 RemoteControl is
  Phonak-specific; sec 7.3 AB is a distinct business, NOT a rebadge -
  state accessory compatibility, never corporate identity (CONV sec.62).
- research/T19_PHONAK_LIFECYCLE_2026_07_17.md - the legacy-vs-active
  lifecycle tension (see identity note).
- research/T57_..._TV_CONNECTOR_CODE_2026_07_29.md - Unitron part number
  076-5049-06 byte-verified in BOTH banked AU order forms; a proposal,
  not shipped, and PNs stay non-reader-facing (CONV sec.11) anyway.
- Rogerpedia V9 AU pdf/txt (registered genuine in
  research/SOURCE_ARTEFACT_VERIFICATION.md; no TVC-specific PDFs are
  banked there): "Watch TV and more" lines 275-279; RogerDirect device
  list lines 562-576 is the CI primary source (AB Naida CI M and Sky CI M).
- operator_uploads/research_notes/Unitron_TV_Connector.md - pre-discipline
  Perplexity note (claims "Relate" compatibility, auto-pairing at 1 m
  radius). Historical colour only; NOT evidence.
- DO-NOT-SAY lists: the DL-030 gap fact-sheets are Roger-scoped; no TV
  Connector-specific DO-NOT-SAY sheet exists (looked in research/,
  research/operator_briefs/, blockers_research/).

## 4. AirStream device boundary (what is catalogue-verified)

Verified span: Phonak Infinio (incl. Audeo Infinio Ultra and Sphere),
Lumity, Paradise; Marvel and Audeo B-Direct as earlier platforms; NOT
Quest, Venture, or standard Belong. Unitron wireless platforms (matrix
names Tempus/Discover/Blu/Vivante/Smile/Moxi - dossier tier, ladder
detail SUSPECTED). KS9/KS10; Vitus+ with the listing's own "message us"
caveat (the Vitus+ range spans manufacturers). AB Naida CI M90 / Sky CI
M90; older AB processors lack AirStream. Boundary of knowledge: Hansaton
platform-level only; Specsavers "Sonova Advance" exists only inside a
quoted forum post, never in shipped copy; all non-Sonova brands excluded.

## GAPS - what the substrate does NOT hold (source externally, flag)

1. Power connector: micro-USB vs USB-C is a LIVE unresolved buyer-facing
   divergence (SPEC-DIV-1); the deciding datasheet is uncommitted.
2. Numeric specs beyond 15 m range: latency (listing says "low-latency"
   qualitatively, no ms), dimensions, weight, supported audio formats
   detail (Dolby Digital named, but no committed first-party doc backs
   it, nor the "unlimited listeners" figure). Looked: listing,
   FAMILY_SPEC, research/, SOURCE_ARTEFACT_VERIFICATION register.
3. Version history: V1-vs-V2 delta exists only as listing FAQ copy with
   no cited source; launch dates for V1 and V2 held nowhere; TVLink S /
   ComPilot predecessors named only in the FAQ.
4. UK pricing: retailer spreads only (GBP 160 / 144-172.80); no MSRP.
5. Lifecycle status: legacy-vs-current tension needs a fresh external
   check; the phase-out PDF is FR-market and 2025-07 vintage.
6. Independent reviews: HearingTracker threads are cited for hardware
   sharing, not evaluation; article-voice review material is absent.
