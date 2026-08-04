# RESEARCH: Phonak Roger Select 3 table microphone

Research stage output, article 2. Access date for all Drive reads and web claims:
2026-08-04 (UTC, `date -u`, 21:59Z). Form follows the Roger On 3 RESEARCH.md; its
section 5-6 lessons applied from the start: Drive route first, filenames never
trusted over the document's own imprint, search snippets secondary-tier.

## 1. The Drive route (operator archive, read this session)

Standing extraction caveat, stated once and applying to every Drive file below: the
Drive tool returns EXTRACTED TEXT, not bytes, so the %PDF magic-byte check used for
on-disk sources cannot be run on any of them. Corroboration is operator curation of
the archive plus internal document structure plus agreement with byte-verified
on-disk sources where they overlap.

Files used (id, title, size, generation check against the document's own content):
- 1kx-PhrRyrnhZ2tmoYvMBsCIwpaZ7Kmqq, user_guide_roger_select_029-0550.pdf,
  4,080,831 bytes. Read in full. No edition string or validity page visible in the
  extract; generation identified from the document's own hardware description:
  Bluetooth button + micro-USB socket + "Connecting Roger Select to your hearing
  aids" chapter = ORIGINAL (gen 1) Roger Select. Duplicate copy at
  1fIK4qdyhM8OxqVuGkE622fXI4WWojt-- (same title, same byte count).
- 1xC2EPNn_vh5mDQL1WZfRxkJxFo99FrNa,
  User_Guide_Roger_Select_iN_92x125_EN_V1.00_029-0755-02.pdf, 4,005,956 bytes.
  Doc 029-0755-02 V1.00. Content check: "Reset button" in place of the gen-1
  Bluetooth button, no Bluetooth chapter = Select iN (iN variants lack Bluetooth,
  corroborated by repo dossier row 9). Two more copies exist (1LyK8HlXYR6QtQ3c...,
  1MnXYF-1_D_d9..., both 3,889,575 bytes - same title, DIFFERENT byte count from
  the 4,005,956 copy; contents indistinguishable in extract; noted, not resolved).
- 1AbK1S0HBW_vCk4EDwMY395TGqlvHmWdd, Roger Select troubleshooting guide.pdf,
  550,954 bytes. Short doc, extract appears complete; no imprint, no date, no
  generation named ANYWHERE in it - generation-neutral Select-family mechanics
  (segments, center touch key, on/off + Connect 10 s reboot). Do not cite it for
  any generation-specific claim.
- Searched for a Select 3 datasheet under 'select 3', 'select3', 'Select_3',
  'select-3', 'datasheet'+'select', and fullText 'Roger Select 3': NOT PRESENT in
  the archive (unlike the On 3, whose datasheet the archive holds). A
  rogerpedia.pdf (10raEFlj9GTA6sHkCke28zFPZ0YH7ZMFe, 4,028,740 bytes) exists but
  matches no repo edition by size; unread, unneeded - the repo's byte-verified
  V9.00 covers the same ground.

Byte-verified primary on disk in the production repo (read-only):
research/rogerpedia_source_pdfs/rogerpedia_028-1902-48_V9.00_2024-09_AU.pdf
(%PDF verified in the prior session per the On 3 research; doc 028-1902-48, V9.00,
2024-09, AU edition). Its footnote maps the "unlimited**" feature to, verbatim:
"** Roger On 3, Roger Select 3, Roger Table Mic 3, Roger Touchscreen Mic 3".

## 2. Roger Select 3 numeric specs

No Select 3 primary was readable end-to-end this session (Drive lacks the
datasheet; proxy 403 on phonak.com, gordonmorris.co.uk, manuals.plus). Everything
below the Rogerpedia line is snippet-tier from searches against
ph-datasheet-roger-select3-210x297-en.pdf and the Select 3 user guide
PH_UserGuide_Roger-Select3_92x125_EN_029-1380-02.pdf (both URLs confirmed live in
SERPs; neither fetchable).

- Battery 400 mAh, 3.7 V; operating time 8 hours. Source: search synthesis
  attributed to the official Select 3 datasheet. Tier: SUSPECTED. Independently
  recorded in repo research/PHONAK_ROGER_DOSSIER.md row 10 and
  research/audioservice_roger.md (both citing the Gordon Morris mirror
  datasheet-roger-select3-en.pdf, doc string "V1.00/2024-05/sm (c) 2024 Sonova
  AG") - repo corroboration lifts this to SUSPECTED-STRONG, not CONFIRMED
  (the mirror's bytes were never verified in this repo either).
- Transmission range: "up to 25 meters / 80 feet to your hearing aids" attributed
  by search synthesis to the Select 3 user guide 029-1380-02. Tier: SUSPECTED.
  This is a GENERATION CHANGE if true: the gen-1 guide (Drive, read in full) says
  10 meters / 33 feet. Never print 25 m for Select 3 without the 029-1380-02 or
  datasheet bytes; never print 10 m for Select 3 at all (gen-1 figure).
- Dimensions: datasheet SERP title shows the field label "Dimensions (diameter x
  H)" (the label uses the diameter symbol; round form factor confirmed); the
  VALUES never surfaced in any snippet. ABSENT.
- Weight: not in any reachable snippet. ABSENT.
- Charging connector: repo dossiers record "Micro-USB charging" for Select 3
  (audioservice_roger.md, from the Gordon Morris datasheet). Tier: SUSPECTED.
  Flag for the writer: the sibling Roger On 3 moved to USB-C, so micro-USB on a
  2024 Select would be a real cross-sibling difference - verify against datasheet
  bytes before printing either way; do not carry the On 3's USB-C over.
- Number of microphones: repo dossier says "3 microphone capsules" (same source).
  Tier: SUSPECTED. Tension flag: gen-1 hardware has microphones in six steering
  segments; do not print a capsule count without the datasheet bytes.
- Participants: "Groups of up to six" is what the shipped catalogue listing
  (catalogue-view/listings/phonak__phonak-roger-select-3-v1.html) states, sourced
  per repo T14 dossier to phonak.com's Roger Select page ("...a group of up to six
  people"). Tier: CONFIRMED as catalogue substrate (operator-reviewed listing +
  repo-recorded phonak.com wording).
- Datasheet edition: "V1.00/2024-05" per the repo's recorded Gordon Morris doc
  string. The EN phonak.com filename carries no version. Tier: SUSPECTED.

Gen-1 figures that must NOT be carried to Select 3 (from the Drive gen-1 guide,
read in full): range 10 m / 33 feet; distant-talker use 10 m / 30 feet; ~8 h
battery (agrees with the Select 3 claim but cite the Select 3 source, not this);
charge at least 2 hours; Bluetooth Class 2, ~3 m; clip/lanyard within 20 cm /
8 inches of the mouth; docking max analog input 1.4 Vrms; operating 0 to +40 C;
charger 5 VDC max 2000 mA. Valid as gen-1 facts with the extraction caveat.

## 3. Generation timeline

- Roger Select (gen 1): launch date NOT pinned to a primary source. Secondary era
  reading is 2018 (a 2018-01-04 packshot exists in the operator's Drive - file
  metadata, circumstantial only; no Sonova/Phonak press release surfaced in
  searches). Tier: ABSENT for the date; the product itself CONFIRMED (Drive user
  guide 029-0550 read in full). Distinguishing hardware: Bluetooth phone calls,
  micro-USB, six steering segments, docking station.
- Roger Select iN: product CONFIRMED (Drive user guide 029-0755-02 V1.00; repo
  dossier row 9). iN = two installable RogerDirect receiver codes, NO Bluetooth,
  Reset button replaces the Bluetooth button. Launch date not pinned: ABSENT.
- Roger Select 3 (Roger Unlimited generation): announced 2024-08-29, available
  2024-09-02, in the Sonova press release "Phonak Unveils Next-Generation Roger
  Microphones with Built-In Unlimited Receivers" - already CONFIRMED in the repo
  (research/PHONAK_ROGER_DOSSIER.md rows 10/12 quote it; AudiologyOnline release
  29125 mirrors it). Select 3 named as part of that launch: CONFIRMED by the
  byte-verified Rogerpedia V9.00 footnote (section 1) and repo
  DL_030_GAP7 dossier ("Phonak launched Roger Unlimited in September 2024, adding
  On 3, Select 3, Table Mic 3, and Touchscreen Mic 3").
- Supersession chain Select -> Select iN -> Select 3 is an inference from naming
  and feature pattern; repo dossier marks it [UNVERIFIED] as an explicit Phonak
  1:1 statement. Preserve that hedge (target: 1:1 supersession claim; context: no
  phonak.com page states it).

## 4. UK pricing (indicative, price-observation only, accessed 2026-08-04)

All snippet-tier; no retailer page fetchable (proxy 403). Never cite retailers for
product facts.
- Connevans (connevans.co.uk, SKU 3PRSEL3, "Phonak Roger Select 3 Unlimited
  Microphone Transmitter", product id 43096502): search synthesis returned
  "GBP 1,494.00 (GBP 1,166.66 ex VAT)". ARITHMETIC FLAG: 1,494.00 / 1.2 =
  1,245.00, not 1,166.66 - the pair as returned is internally inconsistent and at
  least one figure is a snippet mangle. 1,245.00 ex VAT would reconcile with both
  the inc-VAT figure and the FM Hearing from-price below. Treat 1,494.00 inc VAT
  as the observation; re-verify before print.
- FM Hearing Systems (fmhearingsystems.co.uk): verbatim SERP title "Phonak Roger
  Select 3 | From GBP 1245.00" (pound sign in the original) - reasonably firm as
  a from-price; VAT-relief-eligible buyers typically see ex-VAT pricing.
- Connevans supplied-with (snippet): transmitter, docking station, optical audio
  cable, audio input lead, clip, lanyard, pouch, user guide.
- Most UK buyers with hearing loss qualify for VAT relief - quote both figures
  when pricing appears (carried practice from the On 3 research).

## 5. Select-vs-On positioning (for the comparison; cross-links Roger On 3 article)

Both are catalogue-verified products: phonak__phonak-roger-select-3-v1.html and
phonak__phonak-roger-on-3-v1.html both ship in catalogue-view/listings/.
From the byte-verified Rogerpedia V9.00 (all CONFIRMED, current generation):
- Both carry unlimited built-in receivers, MultiTalker Network, TV/multimedia
  connection, and automatic mode selection via accelerometer ("The Roger On and
  Roger Select automatically recognise the sound environment and their
  positions").
- MultiBeam Technology (six-direction table mode): Roger On, Roger Select, Roger
  Table Mic. Select's identity: "Ideal microphone for stationary situations where
  background noise is present"; auto-selects the talker, manual segment selection
  when multiple conversations run, "small to large group conversations".
- Presenter mode: Select and On (and Clip-On Mic).
- On-ONLY modes per V9.00: Pointing mode 2.0 ("Currently available in the Roger
  On only"), Stereo wide pointing (On via myRogerMic app), Headset mode for
  online calls (On only). The article must not give Select 3 any of these.
- Select-side differentiators: dedicated six-segment steering; Bluetooth phone
  calls listed among Select key characteristics in V9.00; ships with a TV docking
  station (Connevans supplied-with, snippet; gen-1 and iN guides confirm the
  docking accessory for their generations).
- Shipped listing framing (operator-reviewed substrate): Select 3 "Best for
  meetings - small groups up to six - TV and media"; RogerDirect installs onto
  Marvel / Paradise / Lumity / Infinio; other devices need Roger X or NeckLoop
  receiver classes. Mirrors the On 3 article's three-connection-route logic.

## ABSENT (looked for, not found or not verifiable this session)

- Select 3 datasheet in the operator's Drive archive (searched five title/fullText
  patterns, section 1) - not present.
- Select 3 dimensions and weight values - not in any reachable snippet of the
  datasheet; ABSENT, never inherit from gen 1/iN.
- Select 3 charging connector and microphone count - repo-recorded SUSPECTED
  claims only (section 2), datasheet bytes needed.
- Gen-1 Select and Select iN launch dates - no press release surfaced (Sonova
  newsroom SERPs, AudiologyOnline, Phonak pages searched).
- Bluetooth version / radio detail for Select 3 - nowhere reachable.
- Primary URLs for the writer/verifier when egress allows:
  https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/accessories/roger/roger-select/ph-datasheet-roger-select3-210x297-en.pdf
  https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/accessories/roger/roger-select/PH_UserGuide_Roger-Select3_92x125_EN_029-1380-02.pdf
  https://gordonmorris.co.uk/wp-content/uploads/2024/09/datasheet-roger-select3-en.pdf
