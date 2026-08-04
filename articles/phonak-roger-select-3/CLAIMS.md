# CLAIMS - Phonak Roger Select 3 article (article 2)

Every factual claim in index.html (body prose, figure captions, SVG text,
JSON-LD) mapped to its source and evidence tier, per ANCHOR-SPEC section 5.
Claims are grouped by article section; JSON-LD answers are condensed twins
of the visible FAQ and inherit the same rows. Sources are abbreviated:

- V9 = research/rogerpedia_source_pdfs/rogerpedia_028-1902-48_V9.00_2024-09_AU
  (.pdf byte-verified genuine per research/SOURCE_ARTEFACT_VERIFICATION.md;
  passages read from the .txt extraction this session; line numbers are .txt
  lines). Edition V9.00, 2024-09, AU.
- GAP4 = research/DL_030_GAP4_RECEIVER_CONNECTION_LIMIT_2026_07_28.md
  (producer fact-sheet; quotes byte-verified against the Phonak Roger Select
  product page and Roger On 3 user guide 029-1379-02 via SourceStore).
- GAP5 = research/DL_030_GAP5_SELECT_IN_LICENCE_COUNT_2026_07_28.md
  (quotes byte-verified against Phonak Rogerpedia adults brochure, 2023-02).
- LISTING = catalogue-view/listings/phonak__phonak-roger-select-3-v1.html
  (operator-reviewed shipped listing, post-DL-030/DL-034/T38 corrections).
- LISTING-iN = catalogue-view/listings/phonak__phonak-roger-select-in-v1.html.
- DOSSIER = research/PHONAK_ROGER_DOSSIER.md rows 9-10.
- OP6 = blockers_research/OP6_ROGER_MIC_AVAILABILITY_2026_07_18.md.
- RESEARCH = this article's RESEARCH.md (2026-08-04), including the Drive
  reads of the original-Select and Select iN user guides (extraction caveat:
  Drive returns extracted text, not bytes).
- SONOVA-PR = Sonova press release 2024-08-29, quoted in DOSSIER rows 10/12
  and DL_030_GAP7 (repo-recorded; not independently fetched this session).
- AUDIENCE = pilot/anchor-spec/AUDIENCE.md (DRAFT, directional - flagged
  where used; used for register and one hedged funding signpost only).
- CONV = /home/user/earx-catalogue/CATALOGUE-CONVENTIONS.md section 5
  (lines 206-230), the CI treatment rule and AirStream ecosystem list.

Tiers per CONV sec.64 as transferred by ANCHOR-SPEC 1.1: CONFIRMED /
SUSPECTED-STRONG / SUSPECTED / UNVERIFIED / ABSENT. "CONFIRMED-substrate"
marks operator-reviewed listing copy or producer fact-sheet interpretation
resting on byte-verified quotes.

## Title, standfirst, scope

| # | Claim | Source | Tier |
|---|-------|--------|------|
| T1 | Roger Select is a wireless microphone placed mid-table that sends talkers' voices into hearing aids and cochlear implant processors | V9 lines 323-341 (portfolio entry); LISTING lede | CONFIRMED |
| T2 | Puck / round form factor | LISTING ("centre-of-table puck"); RESEARCH sec 2 (datasheet field label "Dimensions (diameter x H)" confirms round form) | CONFIRMED-substrate |
| T3 | Third generation ships with unlimited receivers inside the microphone | V9 lines 197-201 ("unlimited digital receivers built inside the transmitter") + line 634 footnote naming Roger Select 3 | CONFIRMED |
| T4 | Follows whichever of up to six seated talkers is speaking | GAP4 sec 2 (byte-verified product-page quotes: six-direction beams; "In small group conversations with up to six participants"); V9 lines 238-244, 331-336 | CONFIRMED |
| T5 | Also takes phone calls over Bluetooth | V9 line 341 ("Bluetooth for wireless phone calls", Select key characteristics) | CONFIRMED |
| T6 | Phonak markets the unit as "Roger Select"; the 3 marks the generation in launch material | SELECT-3-INDEX identity note; V9 footnote line 634 ("Roger Select 3"); SONOVA-PR; Phonak page wording "The third generation of Roger Select" (GAP4 sec 3, byte-verified) | CONFIRMED |
| T7 | Written for Phonak/Unitron wearers on recent platforms and AB CI users | Audience scoping per CONV sec 5; platform facts at M1-M5 below | CONFIRMED (see M rows) |

## What it is, and how it works

| # | Claim | Source | Tier |
|---|-------|--------|------|
| W1 | Hearing aids do their best work close up; in seated groups the aids' microphones take in the whole room | Category mechanism, plain-language framing of the remote-microphone rationale; consistent with V9 Roger technology section (lines 160-190) and the sibling article's sourced near-field passage. No numeric range printed | CONFIRMED (qualitative only) |
| W2 | Phonak positions the Select for "stationary situations where background noise is present" (quoted substring) | V9 line 324, byte-identical substring | CONFIRMED |
| W3 | MultiBeam Technology: multiple microphones, beams in six directions, 360-degree coverage, SNR compared, clearest direction auto-selected | V9 lines 238-244 | CONFIRMED |
| W4 | Tap a segment to lock one direction; release returns to automatic; manual selection when conversations overlap | V9 lines 334-336 ("the listener can manually select whom to listen to"); LISTING ("tap a segment to lock onto one voice"); Drive Select troubleshooting guide (segments, centre touch key - generation-neutral) | CONFIRMED-substrate |
| W5 | Built-in accelerometer selects microphone mode by orientation; presenter use when worn; mutes silently when dropped | V9 lines 220-229 (automatic microphone modes, On and Select), 259-264 (presenter mode: Select and On) | CONFIRMED |
| W6 | Roger protocol: 2.4 GHz licence-free ISM band, each packet broadcast three times on different channels, adaptive frequency hopping | V9 lines 180-188 | CONFIRMED |
| W7 | Hearing devices receive Roger only through a Roger receiver | V9 compatibility guide lines 601-635 (all connection options are receiver paths); LISTING ("Works via Roger receivers") | CONFIRMED |
| W8 | The Select's Bluetooth is listed by Phonak for wireless phone calls; the Bluetooth leg runs phone-to-microphone, the leg into the hearing devices stays Roger | V9 line 341 (the feature); second half is an architecture statement from W7 - no Phonak source describes any Bluetooth path from any Roger mic into hearing devices, and every documented delivery path is a Roger receiver path. Bluetooth call detail beyond this is ABSENT (RESEARCH sec 2/ABSENT) and not printed | CONFIRMED (feature) + CONFIRMED-substrate (architecture) |
| W9 | An aid's consumer Bluetooth is not a Roger receiver; no Roger microphone can transmit into it | W7 architecture; LISTING not-suitable block; AUDIENCE belief baseline 2 names the conflation this corrects | CONFIRMED-substrate |
| W10 | Select 3 belongs to the Roger Unlimited generation Sonova launched in August 2024 | SONOVA-PR 2024-08-29 (repo-recorded, CONFIRMED per RESEARCH sec 3); V9 line 634 footnote | CONFIRMED |
| W11 | Compatible aids held next to the microphone once; receiver installs wirelessly; nothing extra to buy or wear; connection remembered afterwards | GAP4 sec 3 (10 cm pairing, unlimited pool, byte-verified product-page quotes) and sec 6 ("Connecting a receiver is only required once", On 3 user guide - generalised to the gen-3 family per OP7's shared connect mechanic and LISTING pairing section) | CONFIRMED-substrate (persistence quote is On 3 user guide; generalisation flagged) |

## Living with it

| # | Claim | Source | Tier |
|---|-------|--------|------|
| L1 | Product page describes "small group conversations with up to six participants" (quoted substring) | GAP4 sec 2, byte-verified | CONFIRMED |
| L2 | Six is a talker limit (beam directions), not a listener limit | GAP4 sec 2 interpretation + sec 9 DO-NOT-SAY ("do not phrase talker-limit as listener-limit") | CONFIRMED-substrate |
| L3 | Phonak publishes no fixed limit on connected receivers in its consumer guides | GAP4 sec 4 (absence verified across On 3 user guide, Rogerpedia, and three product pages; search terms stated there) | CONFIRMED (absence, location stated) |
| L4 | Several listeners can share one Select; each receiver connects once; all hear the same feed | GAP4 sec 6; LISTING sharing FAQ | CONFIRMED-substrate |
| L5 | Docked in the Roger docking station the Select streams TV; cable into a smartphone streams music | V9 lines 275-279 (Watch TV and more: Table Mic, Select, On; "docking station provided by Roger") | CONFIRMED. No claim is made about Select 3 box contents |
| L6 | Select supports MultiTalker Network (several Roger microphones together) | V9 lines 211-212, 340 | CONFIRMED |
| L7 | (corrected 2026-08-04) No network-size figure was verifiable for the Select 3 this session; the surfaces GAP4 sec 5 searched (Roger On 3 user guide, Rogerpedia, product pages) publish no cap; separately, the Roger On 3 Technical data datasheet publishes "Max. connected microphones Up to 10" FOR THE ON 3, which OVERTURNS the corpus-wide reading of the GAP4 absence (sibling article CLAIMS row 23, Drive read per its RESEARCH.md sec 5, extraction caveat). The article states the On-scoped ten with attribution and extends neither the absence nor the figure to the Select | GAP4 sec 5 (Select-scoped absence, locations stated) + sibling Roger On 3 CLAIMS row 23 / RESEARCH sec 5 (datasheet Drive read) | CONFIRMED (Select-scoped absence, locations stated) + CONFIRMED (On 3 figure, extraction caveat) |
| L8 | A Select 3 technical datasheet exists; we could not verify a copy against the original; secondhand copies disagree on details | RESEARCH sec 1 (Drive search: not present, five patterns), sec 2 (datasheet URL live in SERPs, unfetchable; micro-USB vs USB-C and capsule-count tensions recorded) | CONFIRMED (statement about this research effort) |
| L9 | No battery, weight, dimension, charging or range figures printed; earlier Select's figures do not transfer | RESEARCH sec 2 hard walls (gen-1 figures listed and barred; snippet-tier numerics omitted per spec 1.1) | Deliberate ABSENT |

## Compatibility

| # | Claim | Source | Tier |
|---|-------|--------|------|
| M1 | RogerDirect included in Phonak Infinio, Lumity, Paradise (current) and Marvel (earlier platform, still supported) | V9 lines 566-568; current/earlier split per LISTING and platform de-emphasis convention | CONFIRMED |
| M2 | Virto exception: named Virto custom models (Titanium and no-wireless variants) are outside RogerDirect, T-coil route instead | V9 asterisk footnote (Virto I-10 NW O, I-Titanium, P-312 NW O, P-10 NW O, P-Titanium, M-312 NW O, M-10 NW O, M-Titanium); summarised, not enumerated, in prose | CONFIRMED |
| M3 | Latest Unitron aids carry RogerDirect | V9 line 570 | CONFIRMED |
| M4 | Equivalent Hansaton models carry RogerDirect - attributed in prose to "the catalogue research behind this guide" | GAP4 sec 3 (Gap-1 dossier platform list: "Unitron / HANSATON / Audio Service"); LISTING ("equivalent Unitron and HANSATON models"). V9 AU's own receiver page names only Unitron, so the article attributes this to the research, not to V9 | CONFIRMED-substrate (attribution stated in prose) |
| M5 | Stereo sound only works with hearing aids with RogerDirect | V9 line 297 footnote ("* Stereo sound only works with hearing aids with RogerDirect.") | CONFIRMED |
| M6 | AB Naida CI M (current adult) and Sky CI M (paediatric) include RogerDirect; AB is a Sonova company | V9 lines 570-571 + CI table (RogerDirect column); CONV sec 5 (Sonova family, adult/paediatric roles) | CONFIRMED |
| M7 | Both current AB processors can alternatively use NeckLoop via T-coil | V9 CI table rows Naida CI M, Sky CI M (NeckLoop column) | CONFIRMED |
| M8 | (corrected 2026-08-04) Naida CI Q series: design-integrated Roger 17, Roger X - which per V9 footnote 4 "must be used with a ComPilot" - or NeckLoop; the ComPilot condition is stated in body, visible FAQ and JSON-LD twin | V9 CI table row Naida CI Q (.txt line 660, Roger X cell marked footnote 4) + footnote 4 (.txt line 701) | CONFIRMED |
| M9 | Harmony and Auria: Roger X with iConnect interface, or NeckLoop | V9 CI table row Harmony / Auria | CONFIRMED |
| M10 | Neptune: Roger X with Neptune Connect only; no NeckLoop route listed | V9 CI table row Neptune (NeckLoop column empty) | CONFIRMED |
| M11 | Selected Cochlear and MED-EL processors have documented routes in the same tables | V9 CI table (Nucleus, Kanso, Baha, SONNET, RONDO etc. rows) | CONFIRMED |
| M12 | Phonak's tables document recommended CI profile settings for some older processors (FAQ net-new fact) | V9 CI table footnotes 2-3 ("Recommended CI profile 4 / CI setting 4 and EasyGain +8dB"; "Recommended CI profile 9 / CI Setting 9") | CONFIRMED |
| M13 | Bimodal fittings: published material treats the two sides separately; confirm with audiology team | Hedge preserved from the sibling article's sourced review (target: no single-configuration bimodal Roger statement; context: manufacturer material covers each side separately). Consistent with V9, which tables aids and processors separately | CONFIRMED (absence-shaped hedge, preserved with target and context) |
| M14 | Roger is compatible with virtually every hearing aid and cochlear implant that has a direct audio input, a T-coil or RogerDirect | V9 lines 171-172 (the three-item version; "virtually" hedge kept per AUDIENCE belief baseline 2) | CONFIRMED |
| M15 | T-coil device from any manufacturer wears Roger NeckLoop; DAI/audio-shoe devices or manufacturer-streamer devices take Roger X | V9 compatibility guide lines 606-635 | CONFIRMED |
| M16 | NHS Nathos Nova is Marvel-platform with RogerDirect; earlier Nathos Auto uses Roger X or T-coil route | LISTING NHS paragraph (operator-reviewed); same claims shipped in the sibling article | CONFIRMED-substrate |
| M17 | Original Roger Select: Bluetooth phone calls and docking station, no on-board receivers (separately bought and installed) | RESEARCH sec 1/3 (Drive gen-1 user guide 029-0550 read in full, extraction caveat: Bluetooth button, docking chapter); GAP4 sec 4 gen-2 caveat (non-iN units rely on purchased receivers) | CONFIRMED (extraction caveat noted) |
| M18 | (precision amended 2026-08-04) Select iN: exactly two RogerDirect receiver licences, one pair of compatible aids, installed at 10 cm proximity; pool then empty; third aid requires uninstall | GAP5 sec 2-4. Precision: the two-licence count sits inside the byte-verified Rogerpedia adults quotes; the 10 cm install-proximity figure appears only in GAP5 sec 3 interpretation prose, not inside any quoted string | CONFIRMED (two-licence count, byte-verified) + CONFIRMED-substrate (10 cm, fact-sheet interpretation) |
| M19 | Select iN has no Bluetooth | DOSSIER row 9 ("iN variants lack Bluetooth vs standard"); RESEARCH sec 1 (Drive iN guide: Reset button in place of Bluetooth button, no Bluetooth chapter) | CONFIRMED (dossier + corroborating extraction) |
| M20 | Select iN discontinued by Phonak in 2024, still supported | OP6 (discontinued-products list V1.25); LISTING-iN ("Discontinued by Phonak in 2024 and still fully supported") | CONFIRMED-substrate |
| M21 | Phonak's published material does not number the pre-3 Select units; the article declines to | SELECT-3-INDEX identity note (binding warning); RESEARCH sec 3 (launch dates ABSENT; supersession chain [UNVERIFIED] hedge preserved by not asserting a ladder). Looked for in: Drive archive, repo dossiers, Sonova/AudiologyOnline SERPs per RESEARCH | CONFIRMED (absence, locations stated) |
| M22 | (added 2026-08-04) The earlier Select units "look similar in photographs" to the current one | RESEARCH sec 1/3 hardware descriptions: all three units share the round segmented-puck form, and the distinguishing marks are button-level (gen-1 Bluetooth button vs iN Reset button) or invisible (licence state, on-board receivers); round form for the 3 per T2 | CONFIRMED-substrate (visual-similarity summary of the hardware descriptions) |

## Who it is not for

| # | Claim | Source | Tier |
|---|-------|--------|------|
| N1 | Devices with no RogerDirect platform, no T-coil, no DAI or compatible streamer have no Roger path; population concentrates in small in-canal customs and low-cost OTC aids | LISTING not-suitable block (operator-reviewed); V9 lines 171-172 converse | CONFIRMED-substrate |
| N2 | Pointing mode 2.0, stereo wide pointing, headset mode are currently Roger On only | V9 lines 246-258, 266-274 ("Currently available in the Roger On only"; On via myRogerMic app; headset: Roger On) | CONFIRMED |
| N3 | Roger Table Mic 3 is built for large meeting configurations | V9 lines 348-357 (Table Mic entry: "large meeting configurations and large group conversations") | CONFIRMED |
| N4 | A dedicated TV streamer solves a TV-only need without a microphone attached | Routing statement; TV-streamer product class exists in the catalogue substrate (Phonak TV Connector listings). No model capability claims made | CONFIRMED-substrate (routing only) |

## FAQ (visible and JSON-LD twins)

| # | Claim | Source | Tier |
|---|-------|--------|------|
| F1 | Not a hearing aid; a transmitter that does nothing on its own; needs Roger receivers in worn devices | LISTING ("This is a transmitter, not a hearing aid"); V9 architecture (W7) | CONFIRMED |
| F2 | More than six can listen; six counts talkers; no fixed listener limit; each listener needs a receiver path | L1-L4 rows | CONFIRMED |
| F3 | No receiver purchase needed for Infinio/Lumity/Paradise/Marvel, latest Unitron, Naida CI M / Sky CI M; others need physical receivers, model-specific | M1, M3, M6, M15 | CONFIRMED |
| F4 | Aid Bluetooth vs Roger distinction | W6-W9 | CONFIRMED / CONFIRMED-substrate |
| F5 | CI routes as in compatibility section, plus documented CI profile settings | M6-M13 | CONFIRMED |
| F6 | Select vs On: shared features (table mode, presenter mode, TV/multimedia, MultiTalker, unlimited receivers); Select-side six-segment steering + Bluetooth calls; On-only trio | V9 lines 238-297 feature grid, 323-341, 348ff; N2 | CONFIRMED |
| F7 | Second-hand: Select 3 unlimited pool survives resale (property of the licence pool, GAP4 sec 3/6); iN pool may be consumed, ask licence state (GAP5 sec 2/4); original Select needs separate receivers (M17); iN discontinued 2024, supported (M20) | as cited | CONFIRMED / CONFIRMED-substrate |
| F8a | Worth-it verdict scoped to seated-group listeners with compatible devices; routes others away | Editorial judgment applying AUDIENCE sec 4 register (scoped "worth it", willingness to route away); product facts within it covered by rows above | Register, not a product fact |
| F8b | (softened 2026-08-04) Working-age UK adults in employment can ask about Access to Work; parents of deaf children can ask their local authority about radio aid provision; the article now tells the reader to ask whether each scheme covers Roger equipment - pure signposting. The earlier "routes that can supply Roger equipment at no cost" capability tail was removed per review: SUSPECTED-tier evidence cannot carry it, and AUDIENCE sec 5 item 3 reserves funding-route prominence for an operator ruling still outstanding | AUDIENCE sec 1 funding overlay (DRAFT dossier, snippet-tier evidence). Flagged as a spec/audience friction in the production findings; flag retained deliberately | SUSPECTED (signposting only; no capability or entitlement asserted) |
| F8c | No verified UK retail price available at time of writing; guide quotes none | RESEARCH sec 4 (price observations snippet-tier, internally inconsistent; never-list 17 bars retailer-page facts) | CONFIRMED (absence, location stated) |

## Figure captions and SVG text

| # | Claim | Source | Tier |
|---|-------|--------|------|
| G1 | Fig 1 caption: "Bluetooth for wireless phone calls" is Phonak's listed feature; Bluetooth runs phone-to-microphone; devices receive over Roger through a Roger receiver; aid Bluetooth cannot receive Roger | W6-W9 | CONFIRMED / CONFIRMED-substrate |
| G2 | Fig 2 caption and SVG: six beam directions = talker pickup; tap locks a direction; no fixed listener limit stated in Phonak's published guides; one-time connect remembered | L1-L4, W4, W11 | CONFIRMED / CONFIRMED-substrate |
| G3 | Fig 2 SVG listener icons (three aids + one implant processor) illustrate multiple connected receivers; count is illustrative, not a claimed capacity | L3-L4; no numeric capacity implied or stated | Illustrative (no numeric claim) |
| G4 | Fig 3 caption: shared feature set and the On-only trio; Select adds six-segment steering with tap-to-lock and Bluetooth phone calls | F6 sources | CONFIRMED |
| G5 | Fig 3 SVG: "meetings, family tables, restaurants" (V9 line 332-336 use cases: meetings, restaurants, family gatherings); "one-to-one on the go, bars, cars" (V9 line 306-307: bar, car, bus) | V9 as cited | CONFIRMED |
| G6 | (added 2026-08-04) Fig 3 SVG label "held, worn, pointed" describing Roger On usage postures | V9 lines 220-229 (automatic microphone modes: hand-held and table placement sensed by accelerometer; lapel/presenter wear) and 246-258 (pointing mode: the On aimed at the talker, On-only) | CONFIRMED |

## Sources-and-independence section and footer

| # | Claim | Source | Tier |
|---|-------|--------|------|
| P1 | Rogerpedia V9.00, September 2024, AU edition is the first edition to document Roger Unlimited | SELECT-3-INDEX sec 3 version boundary (LEARNING #218: V7/V8 predate the 2024-08-29 launch); V9 imprint line 973 | CONFIRMED |
| P2 | Sonova press release dated 29 August 2024 announced the third-generation microphones | RESEARCH sec 3; DOSSIER rows 10/12 | CONFIRMED |
| P3 | "Up to six participants" and unlimited-receivers wording byte-verified against Phonak's Roger Select product page in the underlying research | GAP4 sec 2-3 and its verification method sec 11 | CONFIRMED |
| P4 | Rogerpedia adults brochure of February 2023 is the source of the iN two-licence fact | GAP5 sec 2 and sec 10 | CONFIRMED |
| P5 | Phonak discontinued-products list consulted | OP6 (list V1.25) | CONFIRMED |
| P6 | Trademark and group-company attributions (Phonak/Roger/RogerDirect/Naida - Sonova AG; Advanced Bionics/Unitron/Hansaton - Sonova group; Cochlear/MED-EL - respective owners) | CONV sec 38 brand-family map (ANCHOR-SPEC 1.1); mirrors the reviewed sibling footer | CONFIRMED |
| P7 | Published 4 August 2026 | This production run | CONFIRMED |

## Claims deliberately NOT made (hard walls honoured)

- No battery mAh/voltage, operating hours, charging connector, microphone
  capsule count, weight, dimensions, or range for the Select 3 (RESEARCH
  sec 2: snippet-tier or in recorded tension; no byte-verified datasheet).
- No 10 m (original-Select figure) and no 25 m (unverified for Select 3)
  range anywhere.
- No gen-1/gen-2 numbering for the pre-3 Select units (SELECT-3-INDEX
  binding warning); no launch dates for them (ABSENT).
- No 1:1 supersession statement Select iN to Select 3 (DOSSIER hedge
  [UNVERIFIED] preserved by silence).
- No UK price figures (never-list 17; RESEARCH sec 4 observations are
  research-only and internally inconsistent).
- No Select 3 box-contents list (supplied-with is snippet-tier; the shipped
  listing itself declines to enumerate beyond the unit).
- No claim that Select 3 anchors a Pass Around / Touchscreen network
  (GAP6 UNRESOLVED); no network-size number asserted for the Select 3
  (GAP4 sec 5 absence, Select-scoped - the up-to-ten network figure the
  article quotes is the Roger On 3 datasheet's, attributed to the On 3
  and not extended to the Select; see L7).
- No Bluetooth version, profile, or call-mechanism detail (ABSENT in all
  reachable sources).
- No numeric "up to N aids/receivers/mics" for the Select 3 anywhere
  (GAP4 sec 9 DO-NOT-SAY); the only microphone-count figure printed is
  the On 3 datasheet's network cap, On-scoped and attributed (L7).
