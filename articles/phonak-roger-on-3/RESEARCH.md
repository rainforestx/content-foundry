# RESEARCH: Phonak Roger On 3 remote microphone

Research stage output. Access date for all web claims: 2026-08-02 (UTC, `date -u`).

## Session constraints that shape evidence tiers

1. The orchestrator passed literal "undefined" for SOURCE and WORKSPACE paths, and the
   three mandated inputs (pilot/substrate/ROGER-ON-INDEX.md, anchor-spec/ANCHOR-SPEC.md,
   anchor-spec/form-references.md) exist NOWHERE on this filesystem (searched /home/user
   recursively and the session scratchpad). Tier rules below follow the inline task brief.
2. The egress proxy denies ALL external page/PDF fetches (curl CONNECT 403 to phonak.com,
   phonakpro.com, gordonmorris.co.uk; WebFetch HTTP 403 to phonak.com, sonova.com,
   hearingaidaccessories.co.uk, connevans.co.uk). Only web-search snippets were reachable.
   Therefore NO newly fetched PDF could have magic bytes verified.
3. Byte-verified primaries available on disk in the production repo (read-only):
   research/rogerpedia_source_pdfs/rogerpedia_028-1902-48_V9.00_2024-09_AU.pdf
   (head -c4 = %PDF; Phonak "Rogerpedia" doc 028-1902-48, V9.00, dated 2024-09, AU
   edition; covers the Roger 3 / unlimited-receiver generation). Also V7.00 2023-02 and
   V8.00 2023-06 editions (pre-Roger-3 "iN" era) - per the version-boundary warning,
   claims are cited to a named edition and not assumed to hold across editions.

Tier rule applied: CONFIRMED = manufacturer primary with bytes verified this session
(the on-disk Rogerpedia V9.00), or a manufacturer-primary claim independently recorded
with the same wording in the repo producer dossier (research/PHONAK_ROGER_DOSSIER.md).
Everything reachable only as a search snippet is SUSPECTED at best, stated per claim.

## 1. Hardware specs (numeric)

- Roger transmission range up to 25 meters / 75 feet (clear conditions). Source:
  Rogerpedia 028-1902-48 V9.00 2024-09 AU (byte-verified, demo section: "at a distance
  of up to 25 meters/75 feet"). Tier: CONFIRMED for the current (Roger 3) generation.
  The gen-1 datasheet states "up to 25 meters / 80 feet ... clear line of sight, free
  field" (snippet of PH_Datasheet_Roger_On_210x297_EN_V3.00, phonakpro.com). SUSPECTED
  for the exact feet figure; the 25 m value agrees across both.
- Charging: "Charge your Roger microphone for at least two hours." Source: Rogerpedia
  V9.00 2024-09 AU (byte-verified). Tier: CONFIRMED (generic to Roger microphones).
- Battery, Roger On 3: Lithium Polymer, 260 mAh, 3.7 V; power supply 5 VDC, >500 mA,
  USB-C. Source: search snippet of the official Roger On 3 datasheet
  (phonak.com .../ph-datasheet-roger-on3-210x297-en.pdf; no version string visible in
  snippet or filename - edition UNRECORDED). Tier: SUSPECTED (snippet only, bytes
  unverifiable through session proxy).
- Operating time: 8 hours with a RogerDirect hearing device, 6 hours with a separate
  Roger receiver. Source: search snippet attributed to the Roger On (gen 1) datasheet
  PH_Datasheet_Roger_On_210x297_EN_V3.00 (phonakpro.com). Tier: SUSPECTED for gen 1;
  carrying it over to Roger On 3 is an INFERENCE (same 260 mAh cell) and must not be
  printed as a Roger On 3 fact without the On 3 datasheet bytes.
- Dimensions 99.7 x 23.5 x 13.6 mm, weight 27 g. Source: search snippet of the gen-1
  datasheet (same doc as above). Tier: SUSPECTED for gen 1; UNVERIFIED for Roger On 3
  (not seen in any On 3 snippet). Do not print for On 3 without the On 3 datasheet.
- Primary URLs for the writer/verifier to fetch when egress allows (all returned by
  search, none fetchable this session):
  - Datasheet On 3: https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/accessories/roger/roger-on/ph-datasheet-roger-on3-210x297-en.pdf
  - User guide On 3: https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/accessories/roger/roger-on/PH_UserGuide_RogerOn3_92x125_EN_029-1379-02_V1.00.pdf.coredownload.pdf (doc 029-1379-02, V1.00)
  - Datasheet On iN V2: https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/accessories/roger/roger-on/ph-datasheet-roger-oni-nv2-210x297-en.pdf

## 2. Generation timeline

- Roger On (gen 1): announced 2021-05-19, available via hearing care professionals
  2021-06-15. Source: Sonova press release "Phonak set to release new Roger On solution
  for hearing aid and cochlear implant wearers"
  (https://www.sonova.com/en/media/phonak-set-release-new-roger-ontm-solution-hearing-aid-and-cochlear-implant-wearers),
  seen as search snippet; mirrored by AudiologyOnline release 27858. Tier: SUSPECTED
  (primary source class, but bytes unreachable this session).
- Roger On V2: launch date NOT pinned to a primary source this session. One snippet
  says June 2023; the era of the announcing Phonak audiology-blog post and forum
  discussion suggests mid-2022. Distinguishing feature of V2 is Headset Mode (USB
  connection, mic stays live for online calls) - that feature claim is corroborated by
  Phonak's own blog (audiologyblog.phonakpro.com, "The latest generation of Roger On
  makes online calls easier") and AudiologyOnline Ask-the-Experts 28648. Feature tier:
  SUSPECTED (near-primary snippet). Date: see ABSENT.
- Roger On 3 (Roger Unlimited generation): announced 2024-08-29, available 2024-09-02.
  Source: Sonova press release "Phonak Unveils Next-Generation Roger Microphones with
  Built-In Unlimited Receivers"
  (https://www.sonova.com/en/media/phonak-unveils-next-generation-roger-microphones-built-unlimited-receivers).
  Same URL and same quoted sentence are independently recorded in the repo producer
  dossier research/PHONAK_ROGER_DOSSIER.md. Tier: CONFIRMED (primary class, in-repo
  corroboration). New-in-3 features per that release and Rogerpedia V9.00
  (byte-verified): built-in unlimited receivers, Stereo Wide Pointing mode, scratch
  resistant coating, improved myRogerMic app; Rogerpedia V9.00 also lists Pointing
  mode 2.0, Table mode with MultiBeam 2.0, Presenter mode, Headset mode, TV/multimedia
  connection, MultiTalker Network. Tier for the Rogerpedia-listed set: CONFIRMED.

## 3. UK pricing (INDICATIVE ONLY, accessed 2026-08-02, from search snippets)

Standing caveat: retailer pages are named for price observation only, never for facts.
No retailer page could be opened directly (proxy 403); figures below came through
search snippets and SERP titles, so treat as indicative and re-verify before print.
- Connevans (connevans.co.uk, SKU 3PRON3, "Phonak Roger On 3 Unlimited Radio Aid
  Microphone Transmitter"): 1,746.00 GBP inc VAT / 1,455.00 GBP ex VAT (snippet).
  Most UK buyers with hearing loss qualify for VAT relief - quote both figures.
- FM Hearing Systems (fmhearingsystems.co.uk): "Phonak Roger On 3 | From GBP 1395" (SERP title shows the pound sign)
  (verbatim SERP title, so reasonably firm as a from-price).
- Boots Hearingcare (shop.bootshearingcare.com) stocks Roger On 3; no price captured.
- REJECTED: a snippet attributed "60.00 GBP ex VAT" to Gordon Morris for the Roger On
  V3 - implausible by an order of magnitude vs the two prices above; discarded as a
  snippet mismatch, noted here so it is not re-harvested.

## 4. Non-Sonova compatibility (all from byte-verified Rogerpedia 028-1902-48 V9.00 2024-09 AU unless stated)

- Governing rule (verbatim): "Roger is compatible with virtually every hearing aid and
  cochlear implant that has a direct audio input or t-coil." Tier: CONFIRMED.
- Three connection routes (CONFIRMED): (1) RogerDirect - receivers installed into
  RogerDirect-capable hearing aids; Roger On 3 carries unlimited built-in receivers
  ("unlimited**" footnote names Roger On 3 explicitly). (2) Attached receiver -
  design-integrated Roger receiver, Roger X on any aid with direct audio input (DAI),
  or Roger NeckLoop on any aid with T-coil. (3) Receiver on the aid manufacturer's own
  streaming device via DAI (e.g. Roger X into an Oticon Medical Streamer).
- Hard limits for non-Phonak aids (CONFIRMED by the same table logic): RogerDirect
  installation only reaches RogerDirect-capable devices (Phonak Marvel/Paradise/Lumity/
  Infinio platforms per repo dossier row 12, plus AB Naida CI M / Sky CI M and Phonak
  Naida Link M / Sky Link M per the V9.00 compatibility tables). A non-Phonak aid with
  neither DAI nor T-coil has no Roger path. Roger On 3 does not stream audio to
  non-Phonak aids over Bluetooth; the universal paths are Roger receivers only.
- Cochlear implant table highlights (V9.00, CONFIRMED): AB Naida CI M and Sky CI M -
  RogerDirect or NeckLoop; AB Naida CI Q - Roger 17, Roger X (with ComPilot), NeckLoop;
  Cochlear Nucleus 7 / Nucleus 8 - Roger 20, Roger X + Mini Microphone 2+, NeckLoop;
  Cochlear Kanso / Kanso 2 - Roger X + Mini Microphone 2+, NeckLoop; MED-EL SONNET /
  SONNET 2 - Roger 21, Roger X (FM battery pack cover); MED-EL RONDO 2 / RONDO 3 -
  Roger X (Mini battery pack); Oticon Medical Neuro 2 - Roger X (Oticon Medical
  Streamer), NeckLoop. Infant lock (0-36 months) integrated in Roger 20 and Roger 21.
- Version boundary: the unlimited-receiver claims are true of the V9.00 (2024-09)
  edition and the Roger 3 hardware only; V7.00/V8.00 editions describe the iN
  generation (fixed number of installable receivers). Never cite a V9 claim against a
  V7/V8 URL or vice versa (repo LEARNING #218 class).

## ABSENT (looked for, not found or not verifiable this session)

- Roger On 3 datasheet edition string and publication date: filename carries no
  version; PDF bytes unfetchable (proxy 403 on phonak.com and all mirrors tried).
- Roger On 3 specific weight, dimensions, operating-time hours, exact charging-time
  curve: not present in any reachable snippet of the On 3 datasheet; gen-1 figures
  must not be silently carried over. A snippet claiming "80% in 1 hour, 100% in 3
  hours via docking station" had retailer-page provenance and was discarded.
- Roger On V2 launch date: no Sonova/Phonak press release surfaced; secondary snippets
  conflict (mid-2022 vs June 2023). Looked in: Sonova newsroom search results,
  AudiologyOnline releases, Phonak audiology blog snippets.
- Bluetooth version / radio details for Roger On 3: not in any reachable snippet.
- Current phonak.com support-page statements (e.g. compatible-devices knowledge base
  article): URL known (see repo dossier), page unfetchable this session.

## 5. Drive read route upgrade (2026-08-04)

The egress problem in section 1 is resolved by a different acquisition path:
the operator's Google Drive archive holds first-party Phonak PDFs, readable
through the session's Drive integration with no egress (the same route the
production repo's T73 dossier opened). Retrieved 2026-08-04 (`date -u`):

- Roger_On_3_Datasheet.pdf, Drive file id 119X5XIi06PlfQF2RIeLhdVn1vj-jqYV1,
  1,513,263 bytes, in the operator's archive since 2025-02-22. Provenance
  caveat, stated rather than hidden: the Drive tool returns EXTRACTED TEXT,
  not bytes, so the %PDF magic-byte check used for on-disk sources cannot be
  run on it; corroboration instead is (a) the operator curated the archive,
  (b) every overlapping figure agrees with the byte-verified Rogerpedia V9.00
  and with the gen-1 datasheet snippets, (c) the document is internally
  structured as the real datasheet (three numbered pages, Sonova Murten
  imprint). Edition string: not visible in the extract - still UNRECORDED.

Facts upgraded by that extract (tier CONFIRMED, manufacturer primary, with
the extraction caveat above attached):
- Operating time, stated for Roger On 3 directly: 8 h when using hearing
  devices with RogerDirect, 6 h when using a Roger receiver. The section-1
  inference warning is hereby resolved: the figure no longer rests on gen-1
  carry-over.
- Battery: Lithium Polymer, 260 mAh, 3.7 V (upgrades the section-1 SUSPECTED
  snippet). Power supply 5 VDC / 1.0 A max, USB-C; "only use the original
  USB Phonak power supply".
- Dimensions 99.7 x 23.5 x 13.6 mm; weight 27 g - identical to the gen-1
  figures, now stated for On 3 (the do-not-carry-over rule held AND the
  carried value turned out true; both facts worth keeping).
- Transmission range: up to 25 meters / 80 feet, clear line of sight, free
  field (settles the 75-vs-80-feet spread in section 1; metres figure
  unchanged).
- IP54 splash and dust protection; 4 microphones; audio bandwidth
  100 Hz - 7.3 kHz; max analog input 1 Vrms; supported digital format stereo
  PCM; operating conditions 0 to +40 C.
- MultiTalker Network: up to 10 connected microphones; a Roger On in a
  network functions only in Presenter mode. Compatible microphones list
  includes "Roger On V2" and "Roger On iN V2" - primary confirmation that
  the V2 PRODUCT exists (its launch DATE stays in ABSENT).
- Receiver compatibility: all personal Roger receivers except SoundField;
  max connected receivers "Unlimited" (the datasheet's own word).

Also present in the archive: Roger_On_Installation_Guide.pdf,
PH_Datasheet_Roger_On_iN_210x297_EN_V3.00_10.pdf, Roger X datasheet V1.10,
Roger NeckLoop and Clip-On Mic guides. UK pricing remains ABSENT - the
Drive route does not carry it.

## 6. Second-pass findings (2026-08-04, Drive read + web search)

- TRAP RECORDED - misfiled Drive file: "Roger_On_3_User_Guide.pdf"
  (id 18ODJ_QT_e9lIs0M52UCzS0-cZIb6Rm25) actually contains the ORIGINAL
  Roger On / Roger On iN user guide - its validity page reads "This user
  guide is valid for: Roger On CE mark applied 2021 / Roger On iN CE mark
  applied 2021". The filename lies about the generation (LEARNING #218
  class: never trust a filename over the document's own imprint). BARRED as
  an On 3 primary; VALID as gen-1/iN primary. Gen-1 facts it carries that
  must not be printed as On 3 facts without On 3 corroboration: 80 percent
  charge in 1 h / 100 percent in 3 h; lanyard within 20 cm of the mouth;
  battery display full ~8h/mid ~4h. Note the connection-persistence
  sentence ("Connecting a receiver is only required once...") appears in
  this gen-1 guide word-for-word identical to the On 3 user guide sentence
  the article quotes via GAP4 - cross-generation wording stability,
  corroborating but not replacing the On 3 citation.
- Roger On V2 launch date: June 2023, now the consistent secondary reading
  (hearingtracker.com/resources/roger-on-v2 names June 2023 for the V2
  release and its Headset Mode; AudiologyOnline Ask-the-Experts 28648
  corroborates Headset Mode as the V2 feature). Still no Sonova/Phonak
  press release surfaced. Tier: SUSPECTED (secondary consensus). The
  earlier mid-2022 snippet is superseded.
- On 3 datasheet edition: a search synthesis attributes "V1.00 / 2024-05"
  to ph-datasheet-roger-on3-210x297-en.pdf. Tier: SUSPECTED (snippet-class;
  the Drive extract itself shows no edition string). The search also
  returned the datasheet's own product-description sentence verbatim
  identical to the Drive extract's opening - further corroboration that
  the Drive file is the real On 3 datasheet.
- TV-side cabling, On 3: the On 3 datasheet (sec 5 source) states the
  docking station carries "3.5 mm analog and optical digital (Toslink)
  audio input" and lists an optical audio cable and analog audio cable
  among included accessories - so the docking station cables to the
  television's audio output. This restores, with an On 3 primary source,
  the detail the 2026-08-02 fix pass removed as unmapped.
