# NHS hearing aid names translated - factual substrate index (article 6, TRIAL CYCLE 2)

REFERENCE-type article (the corpus's third type); this index doubles as the
evidence bundle for the pending type amendment (sec 6). REGION-AS-SUBJECT
under signed Amendment A3 rule 5: the UK IS the topic and must be declared
in the scope box. The NHS overrule wall applies with FULL FORCE - the
INSTITUTIONAL-ENTITLEMENT WALL and REGION SCOPING checks (CHECKLISTS.md,
added 2026-08-06) run BY NAME at review: assert only what a named source
states about NHS provision, or route the reader to their audiology
department; every regional fact names institution AND region in the same
sentence.

Substrate surveyed read-only 2026-08-06 at /home/user/earx-catalogue,
HEAD 8c3b46d (tree clean; local branch tip matches origin). Absence claims
below are against this working tree: catalogue-view/listings/ (1,575
canonical files, grep census), research/ (filename sweep + targeted reads),
data/claim_sources.csv (full NHS-term filter), DECISION_LEDGER.md and
PLAN.md (grep). Open PR branches were NOT fetched (only main and one
architecture branch exist locally), so no absence here is an "anywhere"
claim. CONV = CATALOGUE-CONVENTIONS.md. Reach states: FULL / PARTIAL /
NOT-REACHED.

## 1. Reach map - what was mined and how far

- danalogic listings (159 canonical): FULL. Filename enumeration + model
  and NHS phrase census across all 159.
- phonak/unitron Nathos + NHS mentions: FULL for grep census (Nathos in
  159 phonak + 129 unitron files); PARTIAL for underlying dossiers (M5
  and SONOVA position docs read in part).
- Cross-brand NHS mentions, all 12 prefixes: FULL grep census. Files
  mentioning NHS: oticon 187, bernafon 185, resound 168, phonak 159,
  danalogic 159, unitron 130, starkey 5, signia 2, widex 1, rexton 0,
  audio service 0.
- research/ NHS dossiers: DANALOGIC_NHS_TIER_HUNT_v1.md FULL (read
  entire); XREF_TRANCHE4_DANALOGIC FULL; PROWAX_NHS_ENGAGE_SAGE findings
  FULL; PARTIAL: M5_NHS_ROGER_DISPOSITION (summary + method),
  SONOVA_NHS_PICKER_POSITION (secs 0-2), NHS_DEMANT_RECEIVER_COMPAT
  (header verdicts), NHS_LI_STRENGTHENING_SURVEY (census head),
  AMPLIFON_GN_NHS_CONTINUITY_UPDATE (secs 0-1), DL_028 RIE-61 platform
  doc (verdict), RETAILER_PRIVATE_LABEL_OEM_MAP (Nathos rows),
  resound_danalogic.md (inventory head). NOT-REACHED this pass:
  DANALOGIC_PLATFORM_CONSOLIDATION.md, FAMILY_MAP_GN.md S2.7-2.9,
  T19_DANALOGIC_FAMILY_TAXONOMY.md, GN_CLUSTER_FAMILY_SPEC.md (cited by
  the read docs as their groundwork; production should open them before
  printing lineage detail they own).
- data/claim_sources.csv: FULL. Exactly 3 rows touch the topic:
  danalogic-gn-manufacturer (FULL, five banked GN Hearing A/S guide
  declarations); danalogic-resound-interchangeable (NOT-REACHED - see
  gap 1); danalogic-surefit-size-ladder (FULL - thin tubes in 5 sizes
  -1/0/1/2/3, Danalogic-Models-Both.pdf read in full).

## 2. Census - which NHS ranges the substrate evidences

### 2.1 Danalogic = GN / ReSound (the deep family: 159 listings)

Listing split: 120 receivers (SureFit 2C x60, SureFit 3 x60; power
LP/MP/HP x length 0-4 x L/R/RL/var), 30 thin tubes (sizes -1,0,1,2,3 x
L/R/RL per platform), 9 wireless/charging accessories. No complete
hearing aid SKU (tier-hunt sec 6.1: 169 CSV rows, all parts/accessories).

Generations the listings name, with parts mapping as shipped:
- SureFit 2C tier: "Danalogic Ambio 67/77/88/98, Ambio Smart 67/77,
  Ambio Smart RIE 61/62" - receivers, tubes, SureFit wax guards shared
  with "ReSound Enya, LiNX2, LiNX 3D, LiNX Quattro, Key (RIE,
  pre-Aug-2020)".
- SureFit 3 tier: "Danalogic Actio, Ambio Smart RIE 61, Extend
  Standard/Power/CROS BTE" shared with "ReSound ONE, Omnia, Nexia,
  Vivia, Savi, Key (post-Aug-2020)". NOTE the RIE 61 appears on BOTH
  cards - live contradiction, gap 2.
- Accessory tiers: classic GN wireless (Multi Mic, Micro Mic, Phone
  Clip+, TV Streamer 2, Remote Control/2) for "Ambio and CS-series" plus
  Actio; Auracast generation (TV Streamer+, Multi Mic+) EXTEND ONLY, a
  manufacturer hardware/firmware gate with mandated warnings. Premium
  Charger names "Luvo miniRIE" (naming puzzle, gap 11). Chargers are
  model-specific; consumables interchange, chargers do not.
- Self-identification flow already shipped: "Your NHS fitting paperwork
  names your range (e.g. 'Danalogic Extend' or 'Danalogic Ambio
  Smart')". This is the article's routing pattern, pre-proven in buyer
  copy.
- Wax guards: NO Danalogic-branded SKU exists anywhere; routed through
  the ReSound SureFit Wax Guards listing (150 danalogic files reference
  SureFit; see wax article index sec 2).

Framework facts (DANALOGIC_NHS_TIER_HUNT_v1.md, all URL-tier July 2026,
nothing byte-banked - time-sensitivity in gap 4): NHS Supply Chain
framework 2022/S 000-010796, 27 Mar 2023 to 26 Mar 2027; Lot 1 suppliers
GN ReSound UK Ltd, Oticon Limited, Puretone Ltd, Sivantos Limited,
Phonak/Sonova UK, Starkey Laboratories Limited; shared allocation -
individual trusts/boards pick brands locally. Danalogic is a brand name
inside GN ReSound UK Ltd's contract, NHS-exclusive (no private Danalogic
market). No numbered tech-tier system on any Danalogic page: one feature
set per generation (SUSPECTED-STRONG, absence-based). Extend's feature
names ("All Access directionality", "Ultra Focus") are a CONFIRMED
terminology match to ReSound Nexia Level 7, not Vivia any tier; no DNN
co-processor. NHS patients buy accessories at manufacturer retail (GBP
100-240 per item, "not applicable for VAT exemption" on several) - NHS
provision does not bundle the accessory ecosystem. Amplifon-GN
acquisition (signed 2026-03-16, close expected end-2026) includes
Danalogic; NHS continuity SUSPECTED-STRONG through framework expiry,
no NHS statement located (AMPLIFON update, 2026-07-25).

### 2.2 Nathos = Phonak (Sonova)

Nathos appears in 159 phonak + 129 unitron files (receiver, dome, wax
listings; CeruStop/CeruShield twins). Two generations, CONFIRMED at
FLAG2-precedent strength (M5 dossier; RETAILER_PRIVATE_LABEL_OEM_MAP
secs 1.7/2.7): Nathos Auto M/SP/PR = Venture platform (older); Nathos
Nova M/PR = Marvel platform (current). Shipped canon: Nathos are BTE
models that typically use thin tubes, so SDS receivers do not fit;
Nathos Nova has NO DAI port - Roger reaches it via RogerDirect (Roger X
as one-time installer tool) or NeckLoop via telecoil; Nathos Auto uses
Roger X with the AS18 audio shoe. CONV p.5 rule binds prose: NHS Phonak
is "AirStream-equipped", never tied to one platform name; one unitron
listing adds "NHS provision varies by region - some NHS Phonak fittings
use models without AirStream". A stray "NHS Phonak Sync" mention exists
in the unitron CeruShield listing (unadjudicated name - verify before
tabling it).

### 2.3 Oticon NHS (Demant)

Current NHS names evidenced first-party (PROWAX follow-up, oticon.co.uk
products-nhs): Engage BTE / BTE PP / miniRITE; Sage miniRITE R,
miniRITE-T, miniBTE R. Legacy NHS names in shipped copy: Spirit Synergy,
Spirit 3, Spirit Zest (Corda miniFit slim-tube users). Key mechanism
facts: NHS Engage miniRITE has a receiver-mounted wax filter (CONFIRMED,
IFU 206004GB); Sage miniRITE takes miniFit receivers and ProWax miniFit
at SUSPECTED-STRONG (retailer-corroborated, first-party RIC anchor); NHS
BTE/miniBTE models use Corda miniFit thin tubes (0.9/1.3 mm), not
receivers. The shipped NHS li across 272 Oticon+Bernafon receiver
listings was strengthened via NHS_DEMANT_RECEIVER_COMPAT (Q1
SUSPECTED-STRONG on Speaker60 asset naming). One tubes listing also
names "Synergy Sense, Como, Geno" in a mixed Oticon-or-NHS list without
per-name labelling - do not reuse in a reference table unverified
(gap 12).

### 2.4 The rest of the map - thinner, honestly so

- Bernafon: listings claim "NHS-supplied Zerena / Viron / Alpha
  miniRITE" and "NHS-branded Bernafon BTE and miniBTE" - but Bernafon is
  NOT a named Lot 1 framework supplier (Oticon Limited is Demant's named
  entity). Tension, gap 3.
- Signia (Sivantos, a named supplier): NHS name Stretta. Substrate: 2
  listings only - "NHS-issue Signia Stretta Aya thin tubes also take
  NanoCare 3.0" (part-level confirmed); StreamLine Mic explicitly NOT
  verified against Stretta fittings. No Stretta range enumeration
  anywhere in-repo (gap 6).
- Starkey (named supplier): 5 listings say "Some NHS trusts fit Starkey
  aids" with pair-only-if-listed caveat; no NHS model names (gap 7).
- Widex: 1 listing states "Widex is not on the current NHS supply
  framework" - a shipped negative claim the article can reuse.
- Puretone: named Lot 1 supplier, ZERO substrate presence (no listings,
  no research doc) - looked for in listings grep and research filename
  sweep. First-class absence (gap 8).
- Rexton, Audio Service: zero NHS mentions (grep, all listings). Not
  NHS-evidenced brands.
- Custom ear moulds lot (DCL Hearing, Minerva, Normanby, Sonic Labs,
  Universal Aids etc.): named in tier-hunt sec 1.2, zero catalogue
  substrate. Absence.
- Paediatric NHS provision (Phonak Sky/Naida class, Oticon paediatric):
  NO NHS-labelled paediatric aid name anywhere in listings or the read
  research docs (looked: listings grep for NHS contexts, tier-hunt,
  M5). S5 projection has no substrate (gap 9).
- Devolved nations: tier-hunt sec 1.3 cites Swansea Bay UHB, Hywel Dda
  UHB, NHS Lothian, NHS Shetland dispensing Danalogic - evidence that
  GN supply spans the four nations, but the framework doc itself is NHS
  Supply Chain (England-facing). Scope-box decision needed (gap 5).

## 3. AUDIENCE PROJECTION (formalized per the operator-agreed plan)

Source dossier: pilot/anchor-spec/AUDIENCE.md (SIGNED 2026-08-05).
Binding input: the wax-cycle operator correction (wax-guards-explained
CLAIMS.md correction record) - the NHS device mix is BTE-dominant, and
NHS free-supply claims failed verification; both constrain every segment
baseline below.

Ranked for THIS topic:

1. S4 CHANNEL-IDENTIFIED WEARER - PRIMARY (the trial brief and TRIAL.md
   name it). This article is the direct answer to S4's defining need:
   "channel-to-ecosystem translation no manufacturer page provides".
   Topic-specific baseline, sourced: knows the aid as "Danalogic" or
   "the NHS one", genuinely cannot name GN/ReSound (AUDIENCE sec 1 S4,
   substrate lens); holds the range name on NHS fitting paperwork - the
   shipped Danalogic FAQ pattern proves the paperwork route works as
   self-identification (sec 2.1 above); assumes clinic supply covers
   parts (AUDIENCE S2 baseline extends to S4) - reality per the
   overrule and tier-hunt 5.1: batteries/repairs are trust-served,
   filter policy is trust-variable, and accessories are paid retail
   even on the manufacturer's own NHS-facing page. The article's
   register must be ask-your-department routing plus honest
   paid-accessory facts, never free-assertion.
2. S2 FITTED-AND-FORGOT WEARER - SECONDARY. Baseline: identifies parts
   by shape and red/right blue/left markers, knows no codes (AUDIENCE
   sec 1 S2). BTE-dominance (binding correction) means most S2 NHS
   readers hold a thin-tube BTE: the translation table must lead with
   tube-fitted BTE ranges and not imply receiver-wire dominance -
   despite the parts substrate skewing 120-receivers-to-30-tubes
   (sellable-parts skew, not wearer skew; state the difference).
3. S3 SELF-DIRECTED TECHNICAL OWNER - OPT-IN DEPTH. Baseline: speaks
   version numbers, comparison-shops clinic vs online, resents markup
   (AUDIENCE sec 1 S3). For this topic S3 wants exactly the equivalence
   the substrate carries: Nathos Nova = Marvel platform, Extend feature
   set = Nexia 7 language, SureFit 2C vs 3. Two-tier layering rule
   (AUDIENCE sec 4): this depth is opt-in, never the surface.
4. S5 PARENT OF A DEAF CHILD - NAMED BUT THIN. Baseline: "radio aid"
   vocabulary, entitlement-first approach via local authority (AUDIENCE
   sec 1 S5). No paediatric NHS name substrate exists (sec 2.4) - the
   article can serve S5 only with routing language, not a names table.
   Do not fabricate a paediatric section.
5. S6 COCHLEAR IMPLANT USER - LOW for this topic, with one live wire:
   NHS CI provision is a different pathway from hearing aid supply, and
   no substrate maps NHS CI names. CONV p.5 CI rules trigger only if
   the article covers AirStream-family accessories; a names-reference
   scope that stays on hearing aid ranges does not owe the CI FAQ
   furniture (that furniture is product-guide-shaped - a point for the
   type amendment, sec 6).
6. S1 PRE-AWARENESS - LOWEST. A reference article is a destination for
   people who already hold a name, not a symptom-search landing.

Section-5 tensions activating: TENSION 3 (funding-route prominence)
activates hardest - the entire article adjoins the commercial interest;
NHS-free-first ordering (AUDIENCE sec 4) plus the entitlement wall
govern. TENSION 1 (price) is resolved in principle by signed Amendment
A2 - the GBP accessory observations (sec 2.1) are usable only as dated
indicative figures, re-verified at production. TENSION 2 (named author)
remains BLOCKED on operator byline text (VOICE ruling 5); property
voice carries.

Amendment proposals to the dossier (flagged, not silently applied):
- AUDIENCE.md sec 1 S4 exemplifies NHS names as "(Nathos, Danalogic)"
  only. Substrate evidences a wider set (Oticon Engage/Sage/Spirit,
  Signia Stretta, claimed Bernafon models, trust-fitted Starkey).
  Propose enriching S4's example list; no contradiction, an extension.
- AUDIENCE.md S4's "some retailer ranges are multi-manufacturer" is
  retailer-scoped; the NHS analogue is different and worth stating in
  the brief: one trust = usually one brand ecosystem, but the brand
  varies BY trust (tier-hunt sec 1.3), so two NHS readers hold
  different manufacturers' aids under the same "NHS aid" identity.

No projection point above contradicts the signed dossier; the two items
are extensions requiring sign-off only if adopted into AUDIENCE.md.

## 4. Doctrine that binds this article specifically

- A3 rule 2 wall phrasing: institution AND region named in the same
  sentence ("NHS audiology departments in the UK"), no silent regional
  assumption; rule 5: region declared in the scope box.
- Entitlement wall: every provision claim needs a named source or
  becomes routing. The corrected wax-article NHS surfaces are the
  template register ("probably free" died; "ask your department"
  shipped).
- CONV sec.62 owner-vs-supplier separation and sec.38 family walls
  govern every equivalence row (Danalogic = GN's brand is ownership;
  receiver interchange is a hardware claim - separate tiers, separate
  sources; the shipped Danalogic copy already models this split:
  distributor-stated, "stated by UK distributors rather than in a
  manufacturer filing").
- Never-list 13: "NHS brand of ReSound" framing is the shipped pattern;
  "whitelabel"/"OEM rebrand" stay banned.
- CONV p.1 older-platform de-emphasis: lead current (Extend, Actio,
  Nathos Nova, Sage), tag earlier ranges as earlier, never delete them
  (replacement-parts buyers hold old aids).

## 5. What articles 1-5 already say about NHS names

Article 5 (wax guards) carries the corrected NHS routing surfaces and
names Danalogic as GN's NHS brand in its family map; articles 1-4
(Roger/TV Connector) carry the NHS Phonak "AirStream-equipped" line and
Nathos receiver-path facts. First full treatment of the names-map as a
subject; cross-link substrate exists both ways (this article is the
natural target of article 5's "Will these fit my Danalogic NHS aid?"
FAQ pattern).

## 6. TYPE-AMENDMENT EVIDENCE (measured; production carries the proposal)

Method identical to prior cycles' recorded measurements: index.html text
minus script/style/svg/figcaption and minus scope box, in-brief box and
page nav (BeautifulSoup, whitespace-split words), run fresh 2026-08-06
on current bytes.

| Article | Type | Words at ship (recorded) | Words now | h2 | FAQ dt | Figures | Claims rows |
|---|---|---|---|---|---|---|---|
| phonak-roger-on-3 | product guide | 2,730-2,997 band (batch note) | 2,759 | 6 | 6 | 3 | ~55 |
| phonak-roger-select-3 | product guide | (same batch note) | 2,940 | 6 | 8 | 3 | ~78 |
| phonak-tv-connector | product guide | (same batch note) | 3,012 | 6 | 7 | 3 | ~70 |
| roger-receivers | system explainer | 3,050 | 3,053 | 8 | 6 | 3 | ~67 |
| wax-guards-explained | system explainer | 3,213 | 3,321 | 9 | 7 | 3 | ~53 |

Notes on deltas: recorded figures come from the two CLAIMS.md production
notes (roger-receivers records 3,050 and cites "three shipped siblings
measure 2,730-2,997"); wax's growth to 3,321 is post-measurement
correction text (the four corrected NHS surfaces plus BTE/RIE nuance);
tv-connector's 3,012 vs the recorded sibling ceiling of 2,997 is
consistent with the region-scoping audit wave adding scoped wording.
Claims rows = markdown table-row count in each CLAIMS.md (includes a few
non-claim header/discipline rows; comparable across articles, not exact).

Structure signature by type:
- Product guides share one fixed 6-section skeleton, verbatim from
  ANCHOR-SPEC sec 3 (what-it-is / living-with-it / compatibility /
  not-for / FAQ / sources).
- System explainers break the skeleton's front half (8-9 subject-shaped
  h2 sections) while keeping the invariant tail (not-for / FAQ /
  sources) and all page furniture.
- Invariant across all five: 3 figures (inline SVG figboxes), FAQ as dl
  with 6-8 dt, scope box, in-brief box, pagenav, sources+independence
  foot.

Band evidence: the nominal 1,500-2,500 band is exceeded by every shipped
article; the two types cluster separately (guides 2,759-3,012; explainers
3,053-3,321 current bytes). VOICE ruling 4 accepted the explainer overage
as evidence "the type split is real and the band needs the type amendment
when article 5 confirms it" - article 5 confirmed it (overage accepted
again). The production step should therefore propose: per-type bands
(product guide circa 2,500-3,100; system explainer circa 2,900-3,400,
both measured by the recorded method), a distinct REFERENCE type whose
band is set by article 6's own measurement (reference articles are
table/entry-driven, so raw word count under-represents content - the
proposal should say how tables are counted), and a note that the
CI-FAQ/price-sentence furniture list (CHECKLISTS.md ratified furniture)
is product-guide-shaped and needs a per-type applicability column.

## 7. Gaps, sharpest first

1. THE CENTRAL CLAIM IS NOT-REACHED FIRST-PARTY. "Danalogic is the NHS
   supply brand of ReSound; receivers interchangeable" ships on 593/457
   files, but claim_sources.csv rates it NOT-REACHED: none of the five
   banked GN guides mentions ReSound; basis is operator trade knowledge
   (primary for their own supply) plus T11 taxonomy plus UK distributor
   statements. XREF tranche 4 names the bridge: Danalogic guides declare
   radio-equipment type codes CABR70/CABR80 (Extend) and BE60 (Ambio); a
   ReSound BTE guide declaring the same code would close it. The article
   must carry the claim with its shipped hedge target intact
   (distributor-stated, not manufacturer-filed) or the bridge must be
   fetched first.
2. Ambio Smart RIE 61 sits on BOTH SureFit platform cards in live buyer
   copy (SF2C "RIE 61/62" and SF3 "RIE 61 (post-2020)"); DL_028 could
   not resolve it - retailers split 2 (SF2C: Sound Hearing Shop,
   Connevans) vs 1 (SF3: Hearing Aid Accessories), first-party silent.
   The reference table cannot print a single platform for RIE 61 without
   resolving this; a dated post-Aug-2020 split may be the true shape.
3. Bernafon-NHS tension: shipped copy claims NHS-supplied Zerena / Viron
   / Alpha, but Bernafon is not a named Lot 1 supplier (tier-hunt sec
   1.2). Targeted search (claim then counter-claim) needed before the
   article lists Bernafon as an NHS ecosystem - possible routes:
   historic framework membership, supply via Oticon Limited, or
   trust-local contracts.
4. Time-sensitive layer: framework expires 2027-03-26 (extension option
   unknown); Amplifon close expected end-2026; every framework/supplier
   fact is URL-tier from July 2026 dossiers, nothing byte-banked; the
   GBP accessory prices are dated 2026-07-11 observations. All need A2
   dating and production-time re-verification.
5. Four-nations scoping: the framework evidence is NHS Supply Chain
   (England); the dispensing evidence spans Wales and Scotland boards.
   The scope box must choose "UK" or "England, with notes" - an A3/
   REGION check finding if left silent.
6. NHS Signia = Stretta rests on 2 listings; no range enumeration, and
   the only accessory claim is an explicit not-verified. Looked in:
   listings grep, research filename sweep (no Stretta dossier exists).
7. Starkey NHS models: "some NHS trusts fit Starkey" with no model list
   anywhere in-repo.
8. Puretone: named Lot 1 supplier, zero substrate. Either a one-line
   framework mention with no ecosystem mapping, or targeted sourcing.
9. Paediatric NHS names: no substrate (sec 2.4). S5 served by routing
   prose only unless sourced externally.
10. Nathos residuals: audio-shoe PN for Nathos Nova generation is
    SUSPECTED-STRONG only (M5 sec 7); pre-Auto Nathos generations
    (older NHS Phonak names) absent from substrate - looked in listings
    grep and M5/OEM-map reads. "NHS Phonak Sync" (one listing) is
    unadjudicated.
11. "Danalogic Luvo miniRIE" appears live in GN accessory pricing but on
    no devices page ([UNVERIFIED] whether active or legacy name) - the
    Premium Charger listing depends on it.
12. Oticon names "Synergy Sense, Como, Geno" appear in one shipped
    mixed list without NHS-vs-private labelling; verify each before
    reuse in a reference table.
13. NOT-REACHED groundwork docs (reach map, sec 1): the platform
    consolidation, GN family map and T19 taxonomy own lineage detail
    this index cites second-hand; open them at production before
    printing generation dates or lineage beyond what is quoted here.
