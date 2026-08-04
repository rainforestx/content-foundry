# Roger Select 3 - factual substrate index (article 2)

Map of the catalogue's verified material for the Phonak Roger Select 3
article (the table microphone for seated groups). Grounding rule: every
product fact traces to an entry below. All paths are under
/home/user/earx-catalogue/. Surveyed read-only on 2026-08-04.

Identity note, load-bearing: TWO Select generations ship as listings -
Roger Select 3 (gen 3, Roger Unlimited, current; Phonak markets it as
plain "Roger Select") and Roger Select iN (gen 2 iN variant, discontinued
by Phonak 2024, still supported). The non-iN gen-2 Select has NO listing
and exists only inside dossiers. The ladder below 3 is murky: Phonak's
"third generation" label implies two predecessors, yet GAP4 treats Select
and Select iN together as gen 2 - do not assert a gen-1/gen-2 split the
substrate does not draw.

## 1. Listings (evidence standing: verified listing copy)

- catalogue-view/listings/phonak__phonak-roger-select-3-v1.html - the
  subject, 1,022 lines. Brand-tree mirror "Phonak/Wireless
  Microphones/phonak-roger-select-3-v1.html" verified byte-identical by
  diff this survey (literal space in the dir), plus FAMILY_SPEC.md and a
  -v1.md sibling. Copy is the post-DL-030 rebuilt form: "How Roger works"
  four-receiver-path module, unlimited RogerDirect licences framing
  (Marvel/Paradise/Lumity/Infinio), Roger X (02)/(03) split in the match
  table, a "Not suitable - no Roger path" block, "small groups up to six"
  in the lede, and a sharing FAQ using GAP4's "no fixed limit stated in
  Phonak's published guides" phrasing. Carries NO numeric hardware specs
  and does not name MultiBeam.
- catalogue-view/listings/phonak__phonak-roger-select-in-v1.html - the
  gen-2 companion, mirror also verified identical. Carries the GAP5 fact
  ("this iN version ships with two RogerDirect receiver licences - enough
  for one pair"), "Discontinued by Phonak in 2024 and still fully
  supported", earlier-generation banner, successor pills to Select 3.
- Ecosystem, same directory: roger-on-3, roger-clip-on-mic,
  roger-pass-around-mic, roger-table-mic-3 / -ii / -ii-in,
  roger-touchscreen-mic(-3); receiver paths roger-x-02 / -03,
  roger-neckloop-02, roger-design-integrated-receivers.

Quote-check state (DECISION_LEDGER surveyed this pass): the DL-030 row
still reads EXECUTING, but later rows overtake it - W3i shipped the Roger
X option corrections (DL-034) and T38 closed the Gap-1 rework (DL-043),
the item the Roger On index flagged open. The audited defect phrase
"receiver path is a separate item" greps to 0 on both Select listings;
the shipped bytes are post-correction (last touching commit b10be98;
visible history is truncated at 112 commits). Where listing copy and a
producer fact-sheet still conflict, the fact-sheet plus primary source
wins.

## 2. Research dossiers (evidence standing: evidence-tiered dossier)

- research/ROGER_DOSSIER_CHAIN_CONSOLIDATED_INDEX_2026_07_16.md - Select 3
  is census row 8 (SKU PHO-MIC-ROG-SEL3), Select iN row 9
  (PHO-MIC-ROG-SELIN); coverage table lines 207-208.
- research/PHONAK_ROGER_DOSSIER.md rows 9-10 - the factual spine.
  Select iN: two Roger receivers for a pair of Marvel/Paradise aids; iN
  variants lack Bluetooth vs standard; "superseded by Select 3" is tier
  MEDIUM, explicit 1:1 supersession [UNVERIFIED] (item 3). Select 3:
  400 mAh battery, 8-hour operating time, Micro-USB charging, 3 mic
  capsules - sourced to a Select 3 datasheet (V1.00/2024-05) on a
  distributor-mirror URL, PDF NOT committed in-repo (GAPS item 3).
- research/T14_PHONAK_ROGER_DOSSIER.md - currently-shipping lens: "up to
  6 participants" use case; MSRP research USD 750-1,990 retail spread,
  UNVERIFIED tier, no UK figure. T14_PHONAK_ROGER_FAMILY_DOSSIER.md -
  taxonomy, compatibility grid, lifecycle, D-ROG-1 picker.
- DL-030 gap fact-sheets (producer lane, byte-citable, DO-NOT-SAY lists):
  - DL_030_GAP4_RECEIVER_CONNECTION_LIMIT_2026_07_28.md - sec 2 carries
    the Select six-participant facts byte-verified to the Phonak Select
    product page: six-direction beam array, "up to six participants" is a
    TALKER limit, never a listener/receiver limit; sec 4: no numeric
    receiver cap published anywhere first-party; sec 8 draft copy; sec 9
    DO-NOT-SAY list (no "up to N aids", no "serves up to six listeners").
  - DL_030_GAP5_SELECT_IN_LICENCE_COUNT_2026_07_28.md - iN mics carry
    exactly TWO RogerDirect licences, installed by 10 cm proximity from
    the mic, no installer software; the core Select iN vs Select 3 buying
    difference (2 installs vs unlimited pool).
  - GAP1 (+ T38 rework) - unlimited RogerDirect receivers on gen-3 mics;
    version boundary per LEARNING #218. GAP6 - MultiTalker across
    iN/gen-3; Select 3 as Pass Around network parent is UNRESOLVED.
    GAP2 (who Roger does NOT work for), GAP3 (install authority).
- research/OP7_ROGER_PAIRING_DOSSIER_2026_07_18.md - Select iN user guide
  doc 029-0755-03 cited; Select 3 shares the 3-step hold-and-press
  connect mechanic with Table Mic 3 / Clip-On.
- blockers_research/OP6_ROGER_MIC_AVAILABILITY_2026_07_18.md - Select iN
  on Phonak's discontinued-products list V1.25; UK Select page footnote
  "not applicable for Roger Select iN". Same dir: B10_ROG_ACC_PHON and
  PHONAK_ROGER_ACCESSORY_FAMILY (accessory-family context).
- research/operator_briefs/DL_030_ROGER_CONFUSION_AUDIT_2026_07_27.md -
  the negative map of what confuses Roger buyers.

## 3. Rogerpedia V9.00 2024-09 AU (evidence standing: primary source PDF)

research/rogerpedia_source_pdfs/rogerpedia_028-1902-48_V9.00_2024-09_AU.pdf
(+.txt) - registered genuine in research/SOURCE_ARTEFACT_VERIFICATION.md,
1,064,715 B, %PDF-1.4. Select-bearing passages, by .txt line:

- 197-201 (p8): Roger Unlimited - "The Roger On, Roger Select and Roger
  Table Mic now have unlimited digital receivers built inside the
  transmitter." 220-229: automatic microphone modes - On and Select sense
  position via accelerometer (table / hand / neck), silent drop-mute.
- 238-244: Table Mode - MultiBeam "utilises multiple microphones in six
  directions", 360-degree comparison, best signal-to-noise direction
  auto-selected; in On, Select, Table Mic. This is the six-DIRECTION
  behaviour; pair with GAP4's six-PARTICIPANT product-page quote, and
  never conflate the two numbers into a listener cap.
- 259-264: Presenter mode (Select and On); 275-279: Watch TV and more.
- 323-341 (p12): the Roger Select portfolio entry - auto talker
  switching, manual selection when conversations overlap, MultiTalker
  Network, "Bluetooth for wireless phone calls".
- 562-576 (p19-20): Roger Unlimited receivers section; RogerDirect =
  Phonak Infinio/Lumity/Paradise/Marvel, latest Unitron, and AB Naida CI
  M and Sky CI M (the CI primary source).
- 606-635 (p21): compatibility guide; the unlimited footnote naming the
  subject: "** Roger On 3, Roger Select 3, Roger Table Mic 3, Roger
  Touchscreen Mic 3" and the iN dagger naming Roger Select iN.

Version boundary (LEARNING #218): V7/V8 mention Select (26/25 hits) but
predate Roger Unlimited (launched 2024-08-29). Any unlimited or
built-in-receiver claim cites V9 AU or the Sonova press release ONLY.

## 4. CI audience and conventions (evidence standing: convention rule)

- CATALOGUE-CONVENTIONS.md section 5 (lines 206-230): AirStream ecosystem
  list and the REQUIRED CI treatment for Roger-family products - CI in
  lede, scope, chip, featured compat bullets, FAQ with bimodal Naida Link
  M + AB CI, older AB processors (Q-series, Harmony, Neptune, Chorus) in
  not-suitable. Transfer note: the shipped Select 3 listing covers CI
  generically (model-specific receivers for Cochlear, MED-EL, AB) but
  never names Naida CI M90 / Sky CI M90; the article should meet sec 5
  depth, backed by Rogerpedia V9 lines 573-574 for RogerDirect CI.
- Platform de-emphasis pattern and the transfer limits are as the Roger
  On index section 4 states; nothing Select-specific changes them.

## 5. Decisions and learnings

- DECISION_LEDGER.md DL-030 (rebuild directive + audit), DL-031
  (not-suitable rider), DL-034 (14-PR merge, V9 artefact verification,
  W3i), DL-043 (T38 closes Gap-1). LEARNINGS.md #218 (version-URL
  mismatch); #170/#171 (deferral background, not product fact).

## GAPS - what the substrate does NOT hold (source externally, flag)

1. UK GBP pricing. T14 holds USD retail spreads tagged UNVERIFIED; no
   official MSRP, nothing UK. Fresh external sourcing required.
2. Select generation history. Held: iN discontinued 2024 (OP6), gen-3
   launch 2024-08-29 (Sonova PR). NOT held: launch dates for the original
   Select and Select iN, and any authoritative gen-1/gen-2 numbering.
3. Numeric hardware specs. 400 mAh / 8 h / Micro-USB / 3 capsules exist
   only as a dossier claim citing an uncommitted distributor-mirror
   datasheet; re-fetch, magic-byte-check and read before quoting (the
   Micro-USB claim on a 2024 product especially deserves the read).
   Range, weight and charge time are held nowhere at all.
4. Independent review and comparison material (vs Roger On table mode,
   vs competitor table mics) - manufacturer-fact substrate only;
   external sources needed, kept clearly separated.
5. Bluetooth specifics (version, profiles, call detail) - Rogerpedia
   says only "Bluetooth for wireless phone calls".
6. Network-parent question: Select 3 anchoring a Pass Around network is
   unresolved (GAP6); network size caps unpublished (GAP4 sec 5).
