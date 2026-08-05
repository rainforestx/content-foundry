# CLAIMS - Roger receivers article (article 4)

Every factual claim in index.html (body prose, figure SVG text, captions,
JSON-LD) mapped to its source and evidence tier, per ANCHOR-SPEC section 5.
Paths are under /home/user/earx-catalogue/ unless absolute. Source keys:

- V9 = research/rogerpedia_source_pdfs/rogerpedia_028-1902-48_V9.00_2024-09_AU
  (.pdf byte-verified genuine per research/SOURCE_ARTEFACT_VERIFICATION.md;
  line numbers are .txt-extract lines; edition V9.00, 2024-09, AU). Table
  column assignments were re-derived THIS SESSION with coordinate-aware
  extraction (pdfminer.six over the committed PDF, pages 22-23), because
  plain-text extraction misaligns bullet columns; every table cell cited
  below carries its x/y-verified column, not a whitespace guess.
- V8 = research/rogerpedia_source_pdfs/rogerpedia_028-1902-02_V8.00_2023-06
  (same verification; edition V8.00, 2023-06, international). Cited by
  edition + txt line per the substrate index binding warning - never by
  page numeral.
- GAP3 = research/DL_030_GAP3_INSTALL_AUTHORITY_2026_07_27.md (producer
  fact-sheet; Phonak knowledge-base quotes byte-verified there).
- GAP5 = research/DL_030_GAP5_SELECT_IN_LICENCE_COUNT_2026_07_28.md.
- GAP8 = research/DL_030_GAP8_NECKLOOP_02_MEANING_2026_07_28.md (its sec 4
  retired-tier wording NOT carried, per the fact-sheet's own supersession).
- T26 = research/T26_ROGER_X_02_03_AUTHORITATIVE_AMENDMENT (Option table
  CONFIRMED against V8).
- LIST-X03 / LIST-NL / LIST-DI = shipped operator-reviewed listings
  catalogue-view/listings/phonak__phonak-roger-x-03-v1.html /
  ...-neckloop-02-v1.html / ...-design-integrated-receivers-v1.html, all
  post-2026-07-28 copy (the 02/03 inversion correction). No claim below
  rests on pre-correction listing copy.
- RESEARCH = this article's RESEARCH.md (Drive reads 2026-08-05). Standing
  extraction caveat: the Drive route returns extracted text, not bytes;
  stated once here and inherited by every RESEARCH-sourced row.
- DS-X = Drive "Technical Data Roger X (02)" datasheet (RESEARCH sec 1).
- DS-NL = Drive Roger NeckLoop (02/03) datasheet + user guide + quick guide
  + speech-to-text installation guide (RESEARCH sec 1).
- CONV = /home/user/earx-catalogue/CATALOGUE-CONVENTIONS.md (section 5 CI
  rules; sec 38 brand families).
- SIB-1 / SIB-2 = shipped sibling articles phonak-roger-on-3/CLAIMS.md and
  phonak-roger-select-3/CLAIMS.md (checked for contradiction, and for the
  claims this article must deepen rather than repeat).

Tiers: CONFIRMED = quoted or derived from a primary source committed
in-repo or byte-verified by a producer fact-sheet, no disagreement on
record. CONFIRMED (extraction caveat) = Drive-read primary, corroborated
by imprint/structure but not magic-byte-verified. CONFIRMED-substrate =
operator-reviewed listing copy or fact-sheet interpretation resting on
byte-verified quotes. CONVENTION = identity fact owned by CONV. ABSENCE =
stated absence with search locations named. Nothing below CONFIRMED-
substrate appears in the article in confident form.

## Standfirst, scope, in-brief

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| 1 | Standfirst | A Roger system is two halves - microphone plus a receiver path into hearing aids and CI processors; the receiver path determines compatibility | V9 lines 601-635 (all connection options are receiver paths); LIST-DI "How Roger works" four-path block | CONFIRMED |
| 2 | Standfirst, scope | AB processors named in lede; CI users a required audience | CONV section 5 (lines 206-230); VOICE ruling 3 strict lede naming | CONVENTION |
| 3 | In brief | All six bullets restate rows below (4, 8, 16, 18, 19, 23, 21, 34, 41-42, 57, 58, 66) - the box only restates; the drift rule from the sibling articles applies: any edit to a restated fact updates its in-brief twin in the same commit | as cited | Derived (restatement) |

## The four ways in

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| 4 | Paths P1 | Roger transmits on Phonak's own 2.4 GHz protocol; an aid's consumer Bluetooth cannot receive it; reception requires a Roger receiver (licence or hardware) | V9 lines 180-188 (protocol) and 601-635 (every path is a receiver path); SIB-1 claim 7 (GAP2 DO-NOT-SAY: Roger 2.4 GHz separate from consumer BT) | CONFIRMED |
| 5 | Paths P2, Fig 1 | RogerDirect included in Phonak Infinio, Lumity, Paradise, Marvel | V9 lines 566-568 ("RogerDirect applies to Phonak Infinio, Lumity, Paradise and Marvel hearing aids") | CONFIRMED |
| 6 | Paths P2, Fig 1 | Latest Unitron aids carry RogerDirect; the Hansaton extension is attributed in prose to "the catalogue research behind this guide" | V9 line 570 (Unitron; V9 AU does NOT name Hansaton); Hansaton per GAP-1 dossier platform list via SIB-2 M4 pattern (attribution stated, exactly as ratified for article 2) | CONFIRMED (Unitron) + CONFIRMED-substrate (Hansaton, attributed) |
| 7 | Paths P2, Fig 1 | AB Naida CI M and Sky CI M carry RogerDirect | V9 lines 570-571 + CI table p22 (RogerDirect column marked, coordinate-verified x=177.9) | CONFIRMED |
| 8 | Paths P2 | RogerDirect is a licence, never a shippable object; not purchasable alone; installed from a microphone or professionally from a Roger X | blockers_research/B10 (RogerDirect never purchasable); V9 line 607 ("Alternatively, a receiver can also be installed using a Roger X and a Roger Installer"); LIST-DI is-this-RogerDirect FAQ | CONFIRMED |
| 9 | Paths P2 | A small set of Phonak Virto custom models excluded from RogerDirect, T-coil route instead (summarised, not enumerated) | V9 footnote lines 584-586 (eight Virto models listed) | CONFIRMED |
| 10 | Paths P3, Fig 1 | NeckLoop serves any manufacturer's device with a T-coil program, implant processors included | V8 third-party compatibility overview lines 885-905 (Telecoil row -> NeckLoop); V9 CI table NeckLoop column; LIST-NL non-Phonak FAQ | CONFIRMED |
| 11 | Paths P3 | Roger X serves DAI/audio-shoe devices and Europlug streamers; examples Oticon Streamer Pro, GN ReSound MultiMic, Starkey Remote Microphone + | V8 lines 885-905 (third-party overview names all three) | CONFIRMED |
| 12 | Paths P3, Fig 1 | Design-integrated receivers are snap-ons shaped for one device, chosen by model-specific receiver number | LIST-DI (model-specific receiver numbers, confirm-first); V9 CI table "Design-integrated for implants" header | CONFIRMED-substrate |
| 13 | Paths P3, Fig 1 strip | A device with none of the four paths cannot receive Roger; population concentrates among smallest in-canal customs and low-cost OTC aids | LIST-DI dead-end statement (operator-reviewed); SIB-1 claim 42 (GAP2 class-level HIGH) | CONFIRMED-substrate |
| 14 | Paths P3 | NHS routing pointer to the Roger On 3 guide (no NHS facts asserted here) | Routing only; NHS facts live in SIB-1 claim 41 | Routing, no new claim |
| 15 | Fig 1 caption | Compatibility floor: Roger works with virtually every hearing aid and CI with DAI or T-coil - manufacturer's "virtually" hedge kept | V9 lines 598-600 (hedge load-bearing per substrate index) | CONFIRMED |

## The licence system

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| 16 | Licences P1, Fig 2 | The four Roger 3 microphones (On 3, Select 3, Table Mic 3, Touchscreen Mic 3) carry unlimited receivers built inside the transmitter | V9 lines 197-201 and 566 ("unlimited receivers built inside the transmitter"); footnote lines 631-633 naming the four unlimited SKUs; version boundary honoured - Roger Unlimited cited only to V9 (LEARNING #218 / T38 rule) | CONFIRMED |
| 17 | Licences P1 | What unlimited removes: no uninstalling after a trial, no re-ordering when an aid is lost or replaced | V9 lines 203-205 (paraphrase, meaning preserved) | CONFIRMED |
| 18 | Licences P1, Fig 2 | iN microphones carry exactly two receivers; pool then empty; one pair of aids | GAP5 secs 2-4 (Rogerpedia adults byte-quote); SIB-2 M18 (same fact shipped) | CONFIRMED |
| 19 | Licences P2, Fig 2 | Verbatim quote: "Once a Roger receiver's license is transferred to one hearing device, the Roger X is empty." | GAP3 sec 2 (Phonak KB, byte-verified); grep -F byte-identical between article and fact-sheet THIS SESSION. American spelling flagged in prose per quotation fidelity | CONFIRMED |
| 20 | Licences P2, Fig 2 | The move is reversible: Phonak's demonstration workflow uninstalls receivers from hearing aids and re-installs into a Roger X | V8 lines 601-607 (demo table: "Uninstall Roger from both hearing devices and re-install into Roger X / Roger On iN trial") | CONFIRMED |
| 21 | Licences P2, Fig 2 | Roger Installer users enumerated by Phonak: HCP, School Audiologist, School Personnel - never consumers; not retail equipment | GAP3 secs 1, 3 (Phonak KB verbatim: "The HCP (Hearing Care Professional), School Audiologist, School Personnel can use the Roger Installer to check") | CONFIRMED (via byte-verified fact-sheet) |
| 22 | Licences P2 | Unlimited/iN microphones install directly into RogerDirect devices, held next to each aid; no tool | V9 line 607 ("Microphones with the unlimited or iN feature can install receivers directly into hearing aids which are RogerDirect capable"); proximity kept qualitative ("held next to") - the 10 cm install figure for iN is interpretation-tier (GAP5 sec 3) and is not printed for installs | CONFIRMED |
| 23 | Licences P3, Fig 2 | Verbatim quote: "via a Roger X (with serial number higher than 1744xxxx) and the Roger Installer"; datasheet attaches the same serial condition to its install feature | V8 line 719 (grep -F byte-identical THIS SESSION; also V8 line 855, V7 lines 727/1082); DS-X install row footnote (RESEARCH sec 3, extraction caveat) | CONFIRMED |
| 24 | Licences P3, Fig 2, sources | Hedge carried in print: V9 AU keeps the Roger X + Installer path (line 607) but does not restate the serial sentence - cutoff presented as Phonak's 2023-era published position | RESEARCH sec 3 (recorded hedge; counter-claim search found no alternative boundary); hedge target and evidence context preserved per CONV sec 66 layer 3 | CONFIRMED (hedge stated) |
| 25 | Licences P3 | The serial boundary is published against the install feature specifically, not against ordinary plug-in use | Scoping of the sources themselves: the DS-X footnote qualifies the "Able to install" row only; V8/V9 state the boundary only inside the RogerDirect-install sentence. No source applies it elsewhere; no converse invented | CONFIRMED (source-scoping) |

## The hardware

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| 26 | NeckLoop P1 | NeckLoop is not an installable receiver; a T-coil bridge outside the RogerDirect system | GAP8 (NeckLoop is a T-coil bridge, not an installable receiver) | CONFIRMED |
| 27 | NeckLoop P1 | (02) and (03) are Phonak's own designations; the user guide imprint covers both | DS-NL user guide imprint "valid for: Roger NeckLoop (02) 2020, Roger NeckLoop (03) 2020" (RESEARCH sec 1 - the byte-adjacent verification GAP8 sec 9 wanted) | CONFIRMED (extraction caveat) |
| 28 | NeckLoop P1, Fig 3 caption | One datasheet covers both; exactly two features marked (02)-only: Check readout via mic with Check function, and Roger Pass-around compatibility | DS-NL datasheet footnote (RESEARCH sec 2: "Only valid for Roger NeckLoop (02) version") | CONFIRMED (extraction caveat) |
| 29 | NeckLoop P2, Fig 3 | Numerics: 70 x 39 x 18 mm; 34 g / 52 g with standard 750 mm loop; 550 mm short loop; 250 mAh fixed (non-removable) battery; USB-C; 80 percent in 1 h, full under 3 h; more than 10 h operating; delay under 20 ms; adaptive gain up to 20 dB; 3.5 mm headphone jack | DS-NL datasheet + user guide (RESEARCH sec 2; charge-curve figures are the guide's) | CONFIRMED (extraction caveat) |
| 30 | NeckLoop P2, Fig 3 | Connect once: T-coil program on, within 10 cm of the microphone, Connect pressed on the microphone (not the loop); link remembered | DS-NL quick guide ("max. 10 cm"); LIST-NL one-time connection FAQ (per Phonak user guide) | CONFIRMED (extraction caveat) + CONFIRMED-substrate |
| 31 | NeckLoop P2 | T-coil program often not enabled by default; HCP activation may be needed | LIST-NL FAQ ("per Phonak's guide, the T-coil program may not be enabled by default and can require a hearing care professional to activate it") | CONFIRMED-substrate |
| 32 | NeckLoop P2, Fig 3 | Volume limiter set with pin tool within 30 seconds of startup; intended for headphone use; child-relevant | LIST-NL FAQ (per Phonak's guide) | CONFIRMED-substrate |
| 33 | Roger X P1 | 9 x 9 x 9.65 mm; under a gram (datasheet: 0.97 g); industry-standard three-pin Europlug | DS-X (RESEARCH sec 2); the cross-industry "industry-standard" qualifier per V8 lines 885-905 (third-party overview: Oticon, GN ReSound, Starkey Europlug streamers take the same connector) | CONFIRMED (extraction caveat) + CONFIRMED (qualifier, V8) |
| 34 | Roger X P1 | No own battery; draws from the aid: 2.7 mA active, 0.5 mA sleep; Phonak guidance to remove when not in use | DS-X (current drain rows); LIST-X03 battery FAQ (remove-when-unused guidance) | CONFIRMED (extraction caveat) + CONFIRMED-substrate |
| 35 | Roger X P1 | Pairing from the microphone at 10 cm, Connect once, remembered; receiver has no controls | LIST-X03 pairing FAQ (operator-reviewed, post-correction) | CONFIRMED-substrate |
| 36 | Roger X P2, FAQ 2 | Option (02) listed with all Roger microphones; Option (03) against named set (iN generation, Roger Select, Roger On, Roger Table Mic II, Roger Clip-On Mic); three (02)-only features: EasyGain, Check, link quality measurement; adaptive gain and stand-by shared; "Option (03) not available in certain countries" | V8 lines 930-963 (feature definitions + Option overview table); T26 (CONFIRMED amendment); LIST-X03 02-vs-03 FAQ | CONFIRMED |
| 37 | Roger X P2, FAQ 2 | The Option table is 2023-edition and predates the Roger 3 microphones; it does not settle (03) behaviour with them - caveat kept deliberately | V8 edition date (2023-06) vs Roger 3 launch 2024-08-29 (SIB-1 claim 9); LIST-X03 FAQ carries the same caveat, called load-bearing by the substrate index | CONFIRMED |
| 38 | Roger X P2 | (03) is not the newer or better tier; it is the reduced-feature option | T26 / RESEARCH sec 2 ("Never write 03 is the newer tier"); direction follows the V8 table itself | CONFIRMED |
| 39 | Design-integrated | Current set: Roger 14, 17, 20, 21, all serving implant processors | V9 CI table p22 header "Design-integrated for implants" with exactly those four columns (coordinate-verified) | CONFIRMED |
| 40 | Design-integrated, FAQ | Tamperproof lock for 0-36 months integrated in Roger 20 and 21; protection sleeve available for Roger 14 | V9 lines 644-646 (infant security note, coordinate-verified on page 22) | CONFIRMED |
| 41 | Design-integrated, FAQ 6 | V8 maps Belong-era Audeo B, Bolero B, Sky B, Naida B and Vitus models to Roger 18 / Roger 19 / AS18 / AS19 audio shoes / NeckLoop | V8 lines 726-800 (design-integrated for Phonak hearing aids table) | CONFIRMED |
| 42 | FAQ 6 | On many small RIC models a Roger X must be used with a ComPilot II | V8 line ~795 footnote 1 ("Roger X must be used with a ComPilot II"), marker on Audeo B-312/B-R and similar rows | CONFIRMED |
| 43 | Design-integrated | Confirm the model-specific receiver number before ordering; wrong-model receiver not adaptable | LIST-DI confirm-first FAQs (operator-reviewed) | CONFIRMED-substrate |

## Cochlear implants

All table cells in this section were coordinate-verified this session
(see V9 source key). Ordering: current processors first, legacy last.

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| 44 | Implants P1, FAQ 5 | Naida CI M (adult) and Sky CI M (paediatric) take RogerDirect; NeckLoop as worn alternative; AB is a Sonova company | V9 CI table rows (RogerDirect + NeckLoop columns); roles per CONV section 5 | CONFIRMED + CONVENTION |
| 45 | Implants P1, FAQ 5 | Naida CI Q series: Roger 17, NeckLoop, or Roger X which must be used with a ComPilot (footnote 4) | V9 CI table Q row (Roger 17 x=257.2, Roger X footnote 4 x=390.3, NeckLoop x=532.2) + footnote line "4 Roger X must be used with a ComPilot" | CONFIRMED |
| 46 | Implants P1, FAQ 5 | Harmony and Auria: Roger X + iConnect, or NeckLoop | V9 CI table Harmony / Auria row | CONFIRMED |
| 47 | Implants P1, FAQ 5 | Neptune: no NeckLoop route; Roger X + Neptune Connect only; a CI profile setting recommended alongside (footnote 2) | V9 CI table Neptune row (NeckLoop column empty, coordinate-verified) + footnote 2 (recommended CI profile 4 / setting 4, EasyGain +8dB - summarised, not enumerated) | CONFIRMED |
| 48 | Implants P2 | Link table: Naida Link M and Sky Link M take RogerDirect, Roger X or NeckLoop; Naida Link RIC Roger X + AS15 or NeckLoop; Naida Link UP Roger X + AS10 or NeckLoop | V9 page 23 table, all four rows coordinate-verified (Link M rows carry Roger X marks at x=358 - the substrate index's shorter summary omitted them; the bytes win) | CONFIRMED |
| 49 | Implants P2, FAQ 5 | Bimodal use routed device by device; no single-configuration statement in published material; confirm with audiology team | Hedge inherited from SIB-1 claim 37 / SIB-2 M13 with target (no single-configuration statement) and context (material tables devices separately) preserved; consistent with V9 table structure | CONFIRMED (absence-shaped hedge, preserved) |
| 50 | Implants P3 | Nucleus 7/8: Roger 20, Roger X + Mini Microphone 2+, or NeckLoop; Nucleus 5/6: Roger 14, Roger X + Euro accessory adapter (CI setting footnote 3), or NeckLoop | V9 CI table (Nucleus 7/8 design-integrated mark at x=296.9 = Roger 20 column; Nucleus 5/6 at x=217.6 = Roger 14 column) | CONFIRMED |
| 51 | Implants P3 | Kanso, Baha and Osia 2 have rows of their own; Freedom keeps a NeckLoop route | V9 CI table (Kanso, Baha 3-6, Osia 2 rows; Freedom row: NeckLoop only) | CONFIRMED |
| 52 | Implants P3 | MED-EL SONNET: Roger 21, or Roger X + FM battery pack cover; RONDO, ADHEAR, SAMBA each name their interface | V9 CI table (SONNET design-integrated mark at x=336.6 = Roger 21 column; RONDO Mini battery pack; ADHEAR adapter cable; SAMBA miniTek / SAMBA 2 GO) | CONFIRMED |
| 53 | Implants P3 | Oticon Medical Neuro and most Ponto models route through Roger X + Oticon Medical Streamer or EduMic; the Ponto Pro / Ponto Pro Power row carries the NeckLoop only, no Roger X; Neuro One's Roger X mark names no interface | V9 CI table lines ~683-690 (Neuro 2, Neuro One, Ponto 4, Ponto 3, Ponto Plus, Ponto Pro rows) | CONFIRMED |
| 54 | Implants P3 | Processors in no row - e.g. AB Chorus - have no documented Roger route "in the editions we read" | ABSENCE - grep of all three committed Rogerpedia texts (V7, V8, V9 AU) returns zero hits for Chorus THIS SESSION; claim scoped to those editions, locations named | ABSENCE (stated, editions named) |

## Second-hand, who-should-not-buy, remaining FAQ

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| 55 | Second-hand P1 | Used Roger equipment sells at a discount (qualitative only; no figures) | AUDIENCE dossier sec 2 item 6 (second-hand at well below retail - communities lens); kept qualitative, no percentage printed | Register-level, qualitative |
| 56 | Second-hand P1 | NeckLoop has no licence pool; battery health is the used question since the cell is non-removable | Rows 26, 29 (datasheet: embedded non-removable) | CONFIRMED (derived) |
| 57 | Second-hand P2, FAQ 3, In brief, sources | No consumer-usable method is published for reading a used Roger X's licence state; the full-or-empty diagnostic belongs to the professional-only Installer tool | ABSENCE - searched: DS-X and DS-NL sheets and guides (Drive, RESEARCH secs 1-2), V7/V8/V9 texts, GAP3's byte-verified KB quotes (the "check" verb is the Installer's Full/Empty diagnostic, SDF1), RESEARCH sec 6 fetch failures (Installer guide 403, pinned for acquisition). Presented as the honest answer with real workarounds (professional check via seller, returns), never as a hidden trick | ABSENCE (stated, locations named) + CONFIRMED (Installer check, row 21) |
| 58 | Second-hand P2 | Warranty: one year standard, two years for serialised Roger devices, attributed to the catalogue records | LIST-X03 / LIST-NL / LIST-DI warranty FAQ (identical wording, operator-reviewed) | CONFIRMED-substrate (attributed in prose) |
| 59 | Second-hand P2, FAQ 1, FAQ 3 | On RogerDirect platforms a Roger 3 microphone removes the receiver purchase entirely | Rows 5-8, 16; LIST-X03 "do I need this?" FAQ ("Usually not") | CONFIRMED |
| 60 | Not-for P1 | RogerDirect-platform owners should usually not buy any receiver; never steered toward a Roger X | GAP-1 DO-NOT-SAY (never steer RogerDirect-platform owners to a Roger X) via substrate index; LIST-X03 FAQ | CONFIRMED-substrate |
| 61 | Not-for P2 | TV-only need routes to the TV Connector; microphone choice routes to the two microphone guides | Routing statements; product facts live in the linked sibling articles | Routing, no new claim |
| 62 | FAQ 2 | The pairing procedure is identical for Option (02) and (03) | LIST-X03 02-vs-03 FAQ ("the pairing procedure is identical") | CONFIRMED-substrate |
| 63 | FAQ 4 | NeckLoop documented as USB audio interface for third-party speech-to-text apps (computer or phone) | DS-NL speech-to-text installation guide (RESEARCH sec 1: computer, USB-C phone/tablet via OTG, Lightning via adapter) | CONFIRMED (extraction caveat) |
| 64 | FAQ 5 | "Every AB processor in Phonak's current tables has a documented receiver route" - scoped to the table's own rows | Rows 44-47 (all five AB rows carry at least one marked column); the universal is bounded BY the table, not extended beyond it | CONFIRMED (scoped universal) |
| 65 | Sources | Edition identities: V8.00 June 2023 international; V9.00 September 2024 Australian; what each sources | Edition + date per file imprints (SOURCE_ARTEFACT_VERIFICATION.md); per-fact split as tabled above (CONV sec 66-adjacent edition discipline, LEARNING #218) | CONFIRMED |
| 66 | Sources (verbatim template) | "No verified UK retail price was available at the time of writing, so this guide carries none." | Ratified template furniture (CHECKLISTS.md, operator 2026-08-05) - shared verbatim BY DESIGN. RESEARCH sec 5 price observations are snippet-tier and internally inconsistent; never-list 17 bars retailer-page facts | ABSENCE (price) + template |
| 67 | Footer | Trademark/group attributions; independence statement; published 5 August 2026 | CONV sec 38 brand families; footer pattern mirrors ratified sibling footers | CONVENTION |

## Figure captions as claims

Figure 1 caption = rows 5-7, 10-13, 15. Figure 2 caption = rows 16, 18-21,
23-24. Figure 3 caption = rows 27-30, 32 (and the (02)-only delta, row 28).
Every SVG text label restates a tabled row; no figure is the sole carrier
of any fact (Amendment A1 principle applied to diagrams).

## Claims deliberately NOT made (the register)

- PRICES. No UK or any price figures. RESEARCH sec 5 holds dated indicative
  SERP observations (60-155 GBP spread, unreconciled, all fetches 403) -
  research-only, below the tier bar, and barred by never-list 17. The
  ratified price-disclosure sentence is carried instead.
- LED SEMANTICS. Nothing about any light on any device. The shipped Roger X
  listing carries green-means-licence-present for the Installer; a SERP
  synthesis contradicts it on the empty state (RESEARCH sec 4 UNSETTLED);
  the primary Installer guide is unfetched (403, pinned). Rather than print
  the permitted fragment next to a known tension, the article omits LED
  behaviour entirely.
- LICENCE-CHECK ROUTES THAT DO NOT EXIST. No consumer check route is
  described or implied; the Check feature is NOT presented as a
  licence-state reader (GAP3 SDF1: the KB "check" verb belongs to the
  Installer's Full/Empty diagnostic; the Touchscreen-mic Check feature
  reads device data and is (02)-only). Roger Upgrader is not mentioned:
  it reads firmware/serial over USB and the Roger X has no USB port
  (RESEARCH sec 4) - naming it would invite exactly the wrong inference.
- LEGACY RECEIVER MODELS. No Roger 10/11/13/15/16 content, and no
  sizes/weights from the Drive design-integrated portfolio document -
  its own imprint shows it is the earlier (Roger inspiro era) portfolio
  (RESEARCH sec 1 trap note). Roger 18/19 appear only as cited V8-edition
  table content for earlier Phonak aids, tagged to the 2023 edition.
- IP RATINGS for design-integrated receivers: V8 line 727 states IP68 for
  Roger 18/19; the legacy Drive portfolio doc states IP67 for its era's
  units (RESEARCH sec 2). Recorded tension between sources of different
  eras - omitted rather than adjudicated.
- WHAT 1744 ENCODES. Plausible readings exist; published nowhere reached
  (RESEARCH sec 3). The article says so and declines to guess.
- ROGER MYLINK. Present in shipped W10 listing copy; zero dossier
  substrate (substrate index GAP 5). Not mentioned.
- NECKLOOP 02-vs-03 BEYOND THE DATASHEET DELTA. No launch dates, no
  supersession ladder, no claim either is newer; the only delta printed is
  the datasheet's own footnote (row 28).
- CURRENT-AID DESIGN-INTEGRATED CLAIMS. No claim that any current Phonak
  hearing aid ships with or takes a design-integrated receiver (B9
  [UNVERIFIED] items); the current four units are framed as
  implant-serving, per V9's own table header.
- RE-LOADING AN EMPTIED ROGER X beyond the sourced direction: the article
  states only what V8's demo workflow documents (uninstall re-installs
  into a Roger X, professional tool); no general refill/reuse promises.
- MICROPHONE-SIDE FACTS owned by the siblings: no receiver-count caps, no
  network sizes, no "up to six participants", no mode or battery facts for
  any microphone - those claims live in articles 1-3 and are linked, not
  repeated (substrate index sec 5 deepen-not-repeat rule).
- RETIRED VOCABULARY. "Education tier" / "adult tier" (retired W3c) appear
  nowhere, including this file except as this register entry.

## Never-list self-check (ANCHOR-SPEC section 4, checked BY NAME)

1. Em/en-dashes, smart quotes, ellipsis: LC_ALL=C grep -nP '[^\x00-\x7F]'
   returns zero on index.html and this file; detector control-tested
   against a planted em-dash (found it). PASS.
2. Wax guard/filter colour identification: no wax content. PASS (n/a).
3. Platform-cutoff framing for wax filters: no wax content. PASS (n/a).
4. Adjacent-mechanism confusion: RogerDirect / Roger X / NeckLoop /
   design-integrated kept distinct throughout (rows 8, 12, 26); unlimited
   vs iN vs single-licence distinguished (rows 16, 18, 19); Roger radio vs
   Bluetooth distinguished (row 4); Check-the-feature vs check-the-
   Installer-diagnostic separated (row 57, register). PASS.
5. Current platform called "older" / unlabelled sister-brand names:
   Infinio/Lumity/Paradise/Marvel per V9 wording; "earlier" applied only
   to iN microphones, Belong-era aids and legacy AB processors; Unitron,
   Hansaton, AB, Cochlear, MED-EL always brand-labelled. PASS.
6. Numeric specs without primary/near-primary source: every numeral traces
   to DS-X, DS-NL, V8 or V9 (rows 23, 29, 33-34, 36, 40-42); extraction
   caveat carried where the source is Drive-read. PASS.
7. Tool/procedure claims unverified: connect/pairing procedures cite the
   quick guide and operator-reviewed listings (rows 30, 35); Installer
   authority cites the byte-verified KB list (row 21). PASS.
8. Ownership inferred from supply: none; family facts from CONV sec 38
   (rows 44, 67). PASS.
9. Cross-brand compatibility outside verified family: third-party claims
   limited to Phonak's own third-party and CI tables (rows 10-11, 50-53).
   PASS.
10. SUSPECTED/[UNVERIFIED]/NONE in confident prose: none. Price
    observations, LED tension, B9 unverifieds, MyLink all excluded (see
    register). The one register-level qualitative claim (row 55) asserts
    no figure. PASS.
11. Hedge stripped or detached: "virtually" kept with its exclusion
    context (rows 13, 15); serial-cutoff hedge carries target and evidence
    context (row 24); bimodal hedge preserved with both (row 49). PASS.
12. Quoted text altered: both verbatim quotes byte-verified by grep -F
    against their committed sources this session (rows 19, 23); the
    American spelling inside the KB quote is flagged outside the marks.
    PASS.
13. "Whitelabel"/"OEM rebrand": absent. PASS.
14. Prose referencing page structure: navigation references are positional
    or topic-named ("above", "below", "set out below"); no table is
    claimed where prose runs, and no banned structure word ("callout")
    remains in reader-facing text including SVG descs. PASS.
15. FAQ leading with warnings where positive answer defensible: FAQs 1, 2,
    4, 5, 6 lead with the answer; FAQ 3's honest "not by yourself" leads
    with the answer to the question asked, then service framing. PASS.
16. CI audience omitted: standfirst names AB; scope names AB, Cochlear,
    MED-EL; a dedicated implants section is the article's spine; the
    ratified CONV-worded AB FAQ is present verbatim; Neptune and ComPilot
    conditions carried (rows 44-54). PASS.
17. Phrasing or facts from form references / manufacturer marketing /
    retailer pages: none; all facts trace to the sources tabled above.
    PASS.
18. Invented manufacturer facts: absences stated with locations instead
    (rows 54, 57, 66; register). PASS.
19. Rendered review: NOT COMPLETED as specified - no browser is available
    in this environment (Chromium download blocked by the egress proxy,
    same class as RESEARCH sec 6 failures). Substituted: gates exit 0,
    HTML parse check, and a mechanical SVG text-bounds pass (two overflow
    defects found and fixed: Figure 1 dead-end strip, Figure 2 uninstall
    label). The rendered pass at desktop and phone widths remains OWED to
    review before ship; the operator's rendered review is the acceptance
    test. FLAGGED, not passed.

## Production notes

- Machine gates: python3 gates/article_gates.py exit 0 with this article
  included (all seven checks by name), run after every edit wave.
- Body prose measures 3,050 words (method: index.html text minus script/
  style/svg/figcaption and minus scope box, in-brief box and page nav).
  This exceeds the brief's 1,500-2,500 nominal band; the three shipped
  siblings measure 2,730-2,997 by the identical method, and this article
  carries four product families plus the licence and second-hand
  treatments the brief requires. Deviation reported to the orchestrator
  rather than silently absorbed; further cuts would cost required
  substance (CI table depth, licence mechanics, the NOT-made walls).
- The In brief box and JSON-LD twins are restatements under the sibling
  drift rule: any edit to a restated fact updates its twin in the same
  commit.
- V9 CI/Link table cells were coordinate-verified (pdfminer x/y) because
  the .txt extract misaligns bullet columns; the substrate index's Link
  summary ("Link M = RogerDirect + NeckLoop") under-reports the Roger X
  marks the PDF carries - the bytes win, and the article follows the PDF.
