# CLAIMS - Phonak TV Connector article (article 3)

Every factual claim in index.html (body prose, figure captions, SVG text,
JSON-LD, In brief box) mapped to its source and evidence tier, per
ANCHOR-SPEC section 5. JSON-LD answers are condensed twins of the visible
FAQ and inherit the same rows; the In brief box and page navigation are
restatements of tabled claims (layout note at the end). No raster imagery
is used (Amendment A1: gen-verified assets not yet available; inline SVG
only), so this file carries no IMAGES section. Sources are abbreviated:

- UG = Phonak TV Connector user guide, doc 029-0737, read IN FULL from the
  operator Drive archive (ids 1NUKb3osGxjIIUAW5uoHHlJ007btdp7k- and the
  content-identical second export 1J59Q-X2nrdhspwLskhKju87VDjJBn797). Own
  imprint "CE mark applied: 2018". Standing extraction caveat: Drive
  returns extracted text, not bytes; corroboration is operator curation,
  document structure, and agreement between independent files.
- PI = Phonak product information for wireless accessories, TWO mutually
  corroborating Drive editions read this research pass: Marvel-era doc
  027-0511-02 V1.00 GB (id 1jWi33VMC0-S6-7YEvCyzYa_nQXhxyGTr) and the AU
  Paradise+Marvel edition PHAU_Product_Information_Phonak_Wi.pdf (id
  1tedgOdC7ATdCsLjO-_a6oslbfFbbj6da). Same TV Connector page, same figures.
- LISTING = /home/user/earx-catalogue/catalogue-view/listings/
  phonak__phonak-tv-connector-v1.html (operator-reviewed shipped listing;
  brand-tree mirror byte-identical per the substrate index).
- CONV = /home/user/earx-catalogue/CATALOGUE-CONVENTIONS.md section 5
  (lines 206-230), the AirStream ecosystem list and required CI treatment -
  LAW for this article per TV-CONNECTOR-INDEX.md.
- LOCK = /home/user/earx-catalogue/research/AIRSTREAM_FIRMWARE_LOCK_SCOPE.md
  (AirStream locked against non-Sonova brands; Sonova SWORD chip anchor).
- MATRIX = /home/user/earx-catalogue/research/STREAMER_CROSS_COMPAT_MATRIX.md
  (Phonak-Unitron TV Connector hardware CONFIRMED shared; sec 7.1
  terminology law: the product is the TV Connector, never "TV streamer" as
  its name).
- T15 = /home/user/earx-catalogue/research/T15_PHONAK_FAMILY_TAXONOMY.md
  (sec 6.1 flags the listing compat span SUSPECTED-STRONG pending
  re-verification; sec 7.3 AB is a distinct business, not a rebadge).
- INDEX = TV-CONNECTOR-INDEX.md in this directory (substrate map; binding
  warnings: SPEC-DIV-1, lifecycle tension, V2 label handling).
- RESEARCH = this article's RESEARCH.md (2026-08-05).
- SIBLING-ON / SIBLING-SEL = the reviewed sibling articles
  phonak-roger-on-3 and phonak-roger-select-3 (their CLAIMS tables carry
  the underlying V9/Rogerpedia rows).
- AUDIENCE = pilot/anchor-spec/AUDIENCE.md (SIGNED 2026-08-05; register and
  segment framing, plus the multi-manufacturer retail-range baseline).

Tiers per CONV sec.64 as transferred by ANCHOR-SPEC 1.1: CONFIRMED /
SUSPECTED-STRONG / SUSPECTED / UNVERIFIED / ABSENT. "CONFIRMED-substrate"
marks operator-reviewed listing copy or catalogue-research interpretation.
ABSENCE = a stated absence, with the places searched named. DIVERGENT =
a live unresolved divergence between sources, deliberately not printed in
either direction.

## Title, standfirst, scope

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| T1 | Standfirst | Small box wired to a television's audio output, sending the sound by radio directly into compatible hearing aids and CI sound processors | UG (function chapters); PI (TV Connector page); LISTING lede | CONFIRMED |
| T2 | Standfirst, Fig 1, FAQ 1 | Each listener hears at a volume set on their own devices; the TV's own speakers keep playing for everyone else | UG (per-wearer volume on aids; unit buttons calibrate the stream); LISTING ("listen at a comfortable level while others watch at theirs"). The headphone-out exception (some TVs mute their speakers on that route) is stated in the AV subsection, and FAQ 1 plus its JSON-LD twin carry an inline scoping clause (usual optical or non-headphone hookup; headphone-socket caveat) so the unconditional form is not exported without context (added 2026-08-05 review) | CONFIRMED / CONFIRMED-substrate |
| T3 | Standfirst | "The long-standing dedicated TV accessory of Phonak's wireless ecosystem" - deliberately neither current-flagship nor discontinued | INDEX identity note (T19 LEGACY tag vs live phonak.com listing conflict); hard wall (b). Lifecycle asserted in NEITHER direction anywhere in the article | CONFIRMED (framing that avoids the unresolved lifecycle question) |
| T4 | Scope, versions paragraph, FAQ 7 | The unit on sale today is labelled V2 by retailers; the operator-reviewed catalogue behind this guide sells it as the TV Connector V2 | RESEARCH sec 3 (Connevans SKU 3P0763006 embeds part 076-3006, matching the Drive "connector-d" packshot asset); LISTING title. Presented only as label/identity, never as a settled version history, per INDEX warning | CONFIRMED (retail/part-level identity); version LABEL only |

## What it is, and how it works

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| H1 | Opening paragraph | TV listening through aids alone is a distance problem: the aids amplify the room's version of the sound; turning the set up starts a household volume war | Category mechanism, qualitative framing only; consistent with the sibling articles' sourced near-field passages. No numeric range printed | CONFIRMED (qualitative only) |
| H2 | Body, Fig 1 | Housing 63 x 63 x 12 mm; can be mounted behind the television | PI (both editions, mutually corroborating) | CONFIRMED |
| H3 | Body, Fig 2 SVG | AirStream is Phonak's own 2.4 GHz streaming radio, built into recent Phonak-family devices at manufacture; proprietary (not receivable by non-Sonova devices) | UG compliance section (2400 - 2483.5 MHz, stated in prose as the 2.4 GHz band); LOCK (SWORD chip anchor; locked against non-Sonova brands); CONV ecosystem list; LISTING | CONFIRMED |
| H4 | Body, In brief, Fig 1 | Streams to compatible devices within a 15 metre (50 ft) radius; line of sight not required; walls, furniture and large metallic structures can shorten reach | UG ("within a 15 meter (50 ft) radius"; obstacles wording). Phrased as "within a ... radius", never "up to N metres" | CONFIRMED |
| H5 | Body, In brief, Fig 1, FAQ 1 | An unlimited number of listeners can stream simultaneously | PI (both editions: "unlimited amount" - "of users" in the Marvel edition, "of listeners" in the AU edition; the article paraphrases as "unlimited number", indirect speech, no quotation marks) | CONFIRMED |
| H6 | Body, In brief | An aid's ordinary Bluetooth cannot receive AirStream; not a substitute | Architecture statement from H3: AirStream is a proprietary Phonak protocol and every documented receiving device carries AirStream hardware (LOCK, CONV, LISTING "AirStream wireless is required") | CONFIRMED-substrate (architecture) |
| H7 | Body, In brief, FAQ 6 | No Phonak document we consulted describes a way of adding AirStream to an aid that lacks it | ABSENCE - looked in: UG (read in full), both PI editions, LISTING, LOCK, MATRIX, T15, INDEX. Phrased in the article as an absence about consulted documents, not a claim about the world | ABSENCE (stated, locations here) |
| H8 | Body, Fig 1 | One audio socket; optical (Toslink) cable described by the user guide as supplied already fitted, or a 3.5 mm analog jack cable | UG (input chapter: one socket, optical pre-installed, analog optional) | CONFIRMED |
| H9 | Body, In brief | Receives and passes on Dolby Audio, stereo or mono; DTS not supported; blinking red light on wrong format; fix is PCM/stereo in the TV audio menu or the analog cable | UG (formats and LED/troubleshooting chapters; "Dolby Audio" is the guide's own naming - the article uses it, not the listing's "Dolby Digital") | CONFIRMED |
| H10 | Versions paragraph, FAQ 7 | More than one hardware version exists; no primary document we could verify states what changed between them | Existence: RESEARCH sec 1/3 (Drive holds packshots for both asset generations, 076-3002 and the connector-d 076-3006 set). Delta: ABSENCE - RESEARCH sec 3/6 (no primary names the delta; the listing's V1-vs-V2 FAQ carries no cited source and is deliberately NOT used). Hard wall (d) honoured: no feature delta asserted, no launch dates printed | CONFIRMED (existence) + ABSENCE (delta, locations stated) |

## Living with it

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| L1 | Body | First connection: aids within 1 metre (3 ft) of the unit | UG (connect chapter) | CONFIRMED |
| L2 | Body | Connection confirmation can take up to 10 seconds | UG | CONFIRMED |
| L3 | Body | Connection is remembered; aids reconnect automatically on re-entering range while audio plays; unit streams when audio present and stands by when silent | UG (automatic behaviour chapter) | CONFIRMED |
| L4 | Body | LED states: green transmitting, white standby (no audio), blinking blue connecting, blinking red wrong format | UG (LED table) | CONFIRMED |
| L5 | Body | Unit buttons adjust the stream level; volume memory stored separately per input type | UG (volume chapter) | CONFIRMED |
| L6 | FAQ 1 | During the connection process the unit connects to any compatible aid in range (family setup in one pass; a visitor's compatible aids can join) | UG (connect chapter); two-edged reading per RESEARCH sec 5 | CONFIRMED |
| L7 | Body, FAQ 3 | Aids interrupt the TV stream for an incoming phone call and return to it automatically afterwards | UG (FAQ/behaviour section) | CONFIRMED |
| L8 | Body, In brief, FAQ 2, Sources | Phonak's latency wording is qualitative - "lowest streaming latency" - and no millisecond figure is published anywhere we could verify; the article prints no number | Phrase: PI (both editions). ABSENCE of a figure: RESEARCH sec 2/6 (looked in: UG in full, both PI editions, datasheet snippets, trade articles reached). Hard wall (c) honoured | CONFIRMED (phrase) + ABSENCE (figure, locations stated) |
| L9 | Body, FAQ 2 | If the TV's loudspeakers lag behind the streamed audio, reduce the TV's loudspeaker delay setting in its audio menu | UG (FAQ: TV-loudspeaker delay adjustment) | CONFIRMED |
| L10 | Body, FAQ 2 | If streamed audio drifts against the picture on surround formats, set the TV's output to PCM or stereo - attributed in prose to the catalogue behind this guide | LISTING (operator-reviewed sync FAQ); consistent with UG's PCM/stereo format fix (H9) | CONFIRMED-substrate (attribution stated in prose) |
| L11 | Body | Powered from the mains via a USB power supply, or from a USB socket on the television; on some sets it then powers up and down with the TV | UG (power chapter: charger or TV USB port); the with-the-TV detail is LISTING wording ("some TVs power the unit on with the TV; others stay always-on") | CONFIRMED + CONFIRMED-substrate (with-the-TV detail) |
| L12 | Body, FAQ 7, JSON-LD Q7 (updated 2026-08-05) | The unit's power socket is micro-USB; no manufacturer source names a USB-C variant | UG 029-0737 (Drive, CONFIRMED with extraction caveat: microUSB, 5 VDC min 500 mA) + official datasheet snippet (micro-USB plug) + the RESEARCH.md sec 0 counter-search returning ZERO USB-C sources in any year. The prior version of this row recorded the SPEC-DIV-1 omission; the paper case is now one-sided and the article states micro-USB. LISTING-side correction (its USB-C x4) remains the operator's, with a physical-unit check as final confirmation | CONFIRMED (combined; physical check outstanding) |
| L13 | AV subsection | Connect the unit to an audio output, never an input | UG | CONFIRMED |
| L14 | AV subsection | Optical is preferred; the guide's troubleshooting routes volume problems from the analog cable to optical | UG (troubleshooting) | CONFIRMED |
| L15 | AV subsection | Some TVs switch off their own loudspeakers when the headset socket is in use, leaving the set inaudible for others - PARAPHRASED, no quotation marks. The guide's sentence carries an en-dash, which house ASCII style cannot reproduce inside a quotation, so per CONV S-72 the fact is paraphrased instead of quoted. (Corrected 2026-08-05 review: an earlier draft quoted the sentence with the dash silently normalised inside the quote marks, and this row wrongly said "quotation unaltered".) | UG (full read, RESEARCH sec 5) | CONFIRMED |
| L16 | AV subsection | Fixes: enable parallel loudspeaker use in the TV's audio settings, or use the optical cable | UG (same passage) | CONFIRMED |
| L17 | AV subsection | Soundbar/AV receiver setups are not covered by the primary documents read; spare-optical-out or optical-splitter routes are community practice, flagged as unverified with confirm-before-buying framing | ABSENCE (primaries: UG in full, both PI editions) + RESEARCH sec 5 (forum threads, SUSPECTED snippet-tier). Never-list 10 honoured: presented only in explicitly-unverified form | ABSENCE (stated) + SUSPECTED (flagged as such in prose) |
| L18 | AV subsection | Sky Glass televisions provide no usable audio output for external streamers; the TV Connector cannot be used with Sky Glass; Sky Q, Sky Stream and TVs with optical/headphone outputs are unaffected - attributed in prose to the operator-reviewed catalogue | LISTING (Sky Glass note, operator-reviewed) | CONFIRMED-substrate (attribution stated in prose) |

## Compatibility

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| C1 | Section opener, Fig 2 caption | The platform-by-platform span rests on catalogue research that itself flags the span for re-verification against Phonak's current pages; readers told to confirm their exact model | T15 sec 6.1 (SUSPECTED-STRONG flag); INDEX binding warning. Hedge preserved with TARGET (the platform span) and EVIDENCE CONTEXT (flagged for re-verification) per CONV sec.66 | CONFIRMED (statement about the evidence) |
| C2 | Body, Fig 2 | Phonak AirStream platforms: Infinio (incl. Audeo Infinio Ultra and Sphere Infinio), Lumity, Paradise current; Marvel and Audeo B-Direct earlier; Quest, Venture and standard Belong excluded | LISTING compat panels; INDEX sec 4 verified span. SUSPECTED-STRONG per T15, carried inside the C1 hedge frame; current-flagship naming per LEARNING #152 (Audeo Infinio Ultra) | SUSPECTED-STRONG (hedged per C1) |
| C3 | Body, Fig 2 | Naida, Bolero, Sky and Virto models on those platforms included - "the platform, not the shape of the aid, decides"; attributed to the catalogue research | LISTING ("Naida, Bolero, Sky, Virto on Infinio / Lumity / Paradise / Marvel platforms") | CONFIRMED-substrate (attribution stated in prose) |
| C4 | Body, Fig 2, FAQ 4 | UK NHS Phonak (sometimes branded Nathos Nova) is AirStream-equipped as a family - never platform-tied; NHS provision varies by region and some fittings use models without AirStream; region named in-surface per Amendment A3 | CONV sec 5 NHS rule (LAW: "AirStream-equipped", no platform name); LISTING NHS panel + caveat | CONFIRMED-substrate (rule-compliant framing) |
| C5 | Fig 2, FAQ 4 | Costco Kirkland Signature KS9 and KS10 are made by Sonova and sit inside the compatible family - attributed to the catalogue research | CONV sec 5 ecosystem list; LISTING. Supplier statement only; no ownership claim (CONV sec.62) | CONFIRMED-substrate |
| C6 | FAQ 4 | Other retail own-brand ranges mix manufacturers model by model; ask the retailer who made the aids and whether they carry AirStream | AUDIENCE S4 (some retailer ranges multi-manufacturer, substrate lens); LISTING's Vitus+ spans-manufacturers caveat is the catalogue's worked example. No retailer range is named as compatible or incompatible | CONFIRMED-substrate (generic guidance; no per-range claim) |
| C7 | Body, Fig 2 | Phonak and Unitron TV Connector units share their hardware | MATRIX (CONFIRMED, "the strongest cluster in the whole matrix") | CONFIRMED |
| C8 | Body | Unitron sells the same product under its own packaging as the Unitron TV Connector; buy the brand matching the aids | MATRIX; the shipped Unitron listing (catalogue-view/listings/unitron__unitron-tv-connector-v1.html) evidences the branded product's existence | CONFIRMED |
| C9 | Body | Recent wireless Unitron platforms receive AirStream; the model-by-model ladder is less firmly documented than Phonak's - confirm your specific model | WIRELESS_ACCESSORY_COMPATIBILITY_MATRIX sec 2.7 via INDEX (existence CONFIRMED, ladder SUSPECTED); hedge preserved with target (the ladder) and context (less firmly documented) | CONFIRMED (existence) + SUSPECTED ladder, hedged |
| C10 | Body | Advanced Bionics is a Sonova company | CONV sec 5; T15 sec 7.3 (stated as group membership only - no rebadge or hardware-supply claim made in either direction, CONV sec.62) | CONFIRMED |
| C11 | Body, Fig 2, FAQ 5 | AB Naida CI M90 (current adult sound processor) and Sky CI M90 (paediatric) carry AirStream and connect like Phonak aids | CONV sec 5 (LAW: named CI treatment); LISTING CI FAQ and compat panel; RESEARCH sec 5 notes no manufacturer primary re-verified this session - catalogue-substrate tier | CONFIRMED-substrate |
| C12 | Body, Fig 2, FAQ 5 | Bimodal: a Phonak Naida Link M hearing aid alongside an AB implant streams from a single TV Connector to both devices simultaneously | LISTING FAQ (operator-reviewed), cited in the INDEX-prescribed shape: one TV Connector, both devices, simultaneous. Paraphrased, not quoted (the listing spelling "Naida" carries a non-ASCII accent) | CONFIRMED-substrate |
| C13 | Body, Fig 2, FAQ 5 | Older AB processors - Naida CI Q series, Harmony, Neptune, Chorus - do not include AirStream and cannot connect | CONV sec 5 (names all four, LAW); LISTING not-suitable block (all four) | CONFIRMED-substrate |
| C14 | Not-for, Fig 2 | Phonak Lyric has no wireless connectivity at all | LISTING not-suitable block | CONFIRMED-substrate |
| C15 | Not-for, Fig 2 | Non-Sonova brands cannot receive AirStream from any transmitter; each major maker sells its own dedicated TV accessory - buy inside the family | LOCK (AirStream locked against non-Sonova); LISTING not-suitable ("check the manufacturer's accessory range"). No specific rival model named or characterised | CONFIRMED (boundary) + CONFIRMED-substrate (routing) |
| C16 | FAQ 6 | Older Phonak wearers once streamed via the ComPilot and TVLink S accessories; the catalogue records list both as discontinued | LISTING FAQ ("the discontinued ComPilot or TVLink S"); attributed in prose to the catalogue records | CONFIRMED-substrate (attribution stated in prose) |

## Who it is not for, and the Roger comparison

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| N1 | Body | The TV Connector has no microphone and never leaves the television; it does nothing for conversation | Product identity: neither UG nor PI documents any microphone function or portable use; the entire documented feature set is TV/audio-source streaming | CONFIRMED (feature-set identity from the primaries read in full) |
| N2 | Body | Roger Select 3 is the product built for seated group conversation; Roger On 3 is the all-situations microphone | SIBLING-SEL and SIBLING-ON (their sourced positioning rows: V9 "stationary situations..." for Select; all-situations for On) | CONFIRMED (via reviewed sibling corpus) |
| N3 | Body, Fig 3, FAQ 6 | The Roger On 3, docked, also streams television; it delivers through Roger receiver paths and so reaches many devices the TV Connector cannot (older Phonak, other manufacturers with T-coil/DAI routes) | SIBLING-ON (V9-sourced dock/TV claims and the four receiver paths; "virtually every" compatibility floor) | CONFIRMED (via reviewed sibling corpus) |
| N4 | Body, Fig 3 | TV Connector is mains-powered and permanently in place ("nothing to charge"); the Roger On 3 is a battery-powered multi-role tool | UG (mains/TV-USB power, no battery documented in UG or PI); SIBLING-ON (built-in rechargeable battery per its datasheet rows). No battery-life figures restated here | CONFIRMED |

## FAQ (visible and JSON-LD twins)

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| F1 | FAQ 1 | Unlimited simultaneous listeners; own volume each; connect-in-range behaviour | H5, T2, L6 | CONFIRMED |
| F2 | FAQ 2 | Sync intent qualitative; no figure printed; delay-setting and PCM/stereo fixes | L8, L9, L10 | CONFIRMED / CONFIRMED-substrate / ABSENCE as tabled |
| F3 | FAQ 3 | Phone-call interruption and automatic return; only the call-taker's aids leave the stream | L7; the only-your-aids reading follows from per-device call handling (each wearer's aids interrupt for THEIR call) - UG describes the behaviour per aid pair | CONFIRMED |
| F4 | FAQ 4 | NHS and high-street routing | C4, C5, C6 | CONFIRMED-substrate |
| F5 | FAQ 5 | CI answers | C10-C13 | CONFIRMED-substrate |
| F6 | FAQ 6 | Older Phonak models; no retrofit described; legacy accessories discontinued; Roger route | C2, H7, C16, N3 | as tabled |
| F7 | FAQ 7 | Second-hand: no licence or installation-count system appears in the user guide or product information read for this guide; connection is unlimited and re-runnable; version and cable cautions | ABSENCE (looked in: UG read in full, both PI editions) + H5/L6 (re-runnable, unlimited); H10 (version caution); L12 (cable caution). Contrast with Roger licence machinery is the sibling corpus's | ABSENCE (stated) + as tabled |

## Figures (captions and SVG text)

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| G1 | Fig 1 caption + SVG | Cable-in (optical or 3.5 mm analog, one socket), radio-out within a 15 metre (50 ft) radius; unlimited listeners; own volume each; TV speakers keep playing; walls/furniture/metal reduce range | H2, H4, H5, H8, T2 | CONFIRMED / CONFIRMED-substrate |
| G2 | Fig 1 SVG | Three listener figures are illustrative of multiple listeners, not a claimed capacity | H5 (the stated capacity is "unlimited") | Illustrative (no numeric claim) |
| G3 | Fig 2 caption + SVG | The AirStream boundary: the three receiving groups and the excluded strip; span hedge restated in caption | C1-C5, C7, C9, C11-C15 | as tabled |
| G4 | Fig 3 caption + SVG | TV Connector vs Roger On 3 dock decision: one-job mains-powered box vs battery-powered multi-role microphone; Roger reaches devices the TV Connector cannot; wearers whose only problem is the TV rarely need the microphone | N1, N3, N4; the "rarely need" is routing judgment consistent with the sibling's "a dedicated TV streamer solves that one job" | CONFIRMED (via tabled rows) + routing judgment |

## Sources-and-independence section and footer

| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| P1 | Sources | The user guide carries the manufacturer's own "CE mark applied: 2018" imprint; doc 029-0737 | RESEARCH sec 1 (imprint is the document's own; the V2.00 filename version claim is deliberately NOT cited, per the filename-trap lesson) | CONFIRMED (imprint) |
| P2 | Sources | Two independent product-information editions agree on dimensions, unlimited listeners and the latency wording | RESEARCH sec 1-2 (Marvel 027-0511-02 + AU edition) | CONFIRMED |
| P3 | Sources | The five honesty statements: no latency figure; power connector not named; no version delta; lifecycle not asserted; no UK price | L8, L12, H10, T3, and RESEARCH sec 4 (prices snippet-tier, research-only; never-list 17) | ABSENCE / DIVERGENT as tabled |
| P4 | Footer | Trademark and group attributions: Phonak, AirStream, TV Connector, Roger, RogerDirect, Audeo, Naida - Sonova AG; Advanced Bionics, Unitron - Sonova group companies; Dolby, Dolby Audio - Dolby Laboratories; others respective owners | CONV section 6 trademark line (via INDEX); CONV sec 38 family map; Dolby attribution per UG's own imprint practice | CONFIRMED |
| P5 | Footer | Published 5 August 2026 | This production run | CONFIRMED |

## Claims deliberately NOT made (hard walls honoured)

- POWER CONNECTOR: no USB-C and no micro-USB claim anywhere, in prose, SVG,
  alt text or JSON-LD (SPEC-DIV-1, live buyer-facing divergence,
  waiting-on-operator; the deciding datasheet is uncommitted). The article
  states the omission to the reader (charging exists; the port type is
  unsettled) and routes them to the supplied cable.
- LIFECYCLE: neither "current flagship" nor "discontinued" (T19 LEGACY tag
  vs live product page conflict). Framing used: "long-standing dedicated
  TV accessory".
- LATENCY: no millisecond figure (ABSENT everywhere reached). Only the
  manufacturer's qualitative phrase, marked as qualitative, plus the
  user guide's delay-adjustment feature.
- VERSION HISTORY: no V1-to-V2 feature delta (no primary states one; the
  listing's delta FAQ is uncited and deliberately unused); no gen-1 launch
  date (2017 / Audeo B-Direct association is SUSPECTED trade-press tier -
  omitted rather than hedged); no "V2 = TV Connector D" naming equivalence
  (SUSPECTED synthesis); no V2 launch date (ABSENT).
- PRICES: none (RESEARCH sec 4 observations are snippet-tier and
  research-only; never-list 17 bars retailer-page facts).
- WEIGHT (30 g) and COLOUR: snippet-attributed to an unfetched datasheet -
  not printed (never-list 6).
- HANSATON: not mentioned at all - AirStream is SUSPECTED-STRONG at
  platform level only and no Hansaton TV Connector SKU exists (LOCK:
  "never assert one").
- SPECSAVERS and other named retail ranges: no compatibility claim for any
  (Specsavers "Sonova Advance" exists only inside a quoted forum post,
  INDEX sec 4); the article gives only the generic ask-the-retailer test.
- VITUS+ by name: the listing's Vitus+ "message us" caveat is
  retail-operational; the article folds the underlying fact (retail ranges
  span manufacturers) into the generic guidance instead.
- WARRANTY: omitted as retail-adjacent scope, not for lack of a primary -
  UG section 6.2 does state a one year limited international warranty,
  valid as of the date of purchase; the listing's warranty FAQ remains
  retail fine-print. (Rationale corrected 2026-08-05 review: an earlier
  version of this entry wrongly claimed no primary had been re-verified
  this session.)
- UNITRON PART NUMBER 076-5049-06 (T57): part numbers stay
  non-reader-facing (CONV sec.11).
- The pre-discipline Perplexity note's "Relate" compatibility and 1 m
  auto-pairing radius: historical colour, NOT evidence (INDEX sec 3) -
  unused.
- No numeric claims are made about the Roger On 3 in this article (its
  battery, weight and network figures live in its own reviewed article).

## Layout note: the In brief box and page navigation

The In brief box and On this page links are restatements for skimming
readers, not new claims: every bullet condenses claims tabled above (the
one-job identity and radius H4, unlimited listeners H5, the AirStream
boundary H3/H6/H7, the input/format facts H8/H9, the latency honesty L8,
the Roger On 3 routing N3). Same drift rule as the JSON-LD twins: a future
edit to any restated fact updates its in-brief twin in the same commit.
