# RESEARCH: Phonak TV Connector

Research stage output, article 3. Access date for all Drive reads and web claims:
2026-08-05 (UTC, `date -u`, 00:46Z). Form follows the two prior RESEARCH.md files;
standing lessons applied from the start: Drive route first, a filename's generation
claim is never trusted over the document's own imprint, snippets are secondary-tier,
failures recorded honestly.

## 0. SPEC-DIV-1 resolution evidence (2026-08-05 ~01:00Z, appended after grounding)

Targeted web search on the power-connector divergence. FOR micro-USB: the
official datasheet snippet (datasheet_phonak_tv_connector.pdf, phonak.com
master-assets and phonakpro mirrors) states power supply 5 VDC, max
500 mA, micro-USB plug, "microUSB power socket"; both user-guide
generations are consistent with it - gen 1 is doc 029-0515 (V1.00) and
the current guide is doc 029-0737 (V2.00 in the live URL - the SAME
document line held in the Drive archive, so its 2018 CE mark is the
product's certification date, not evidence the guide predates the shipped
unit). AGAINST micro-USB: a counter-search deliberately hunting any
USB-C attribution to any TV Connector revision in any year returned
ZERO sources. Verdict: micro-USB is corroborated by the datasheet
(snippet tier) plus the Drive primaries (CONFIRMED with extraction
caveat) plus the absence of any USB-C source; the shipped listing's
USB-C claim has no discoverable basis, and its likely origin is the
Bernafon TV-A donor clone noted in T15 sec 6.1. Listing-side correction
is the operator's lane (SPEC-DIV-1 remains theirs to close, ideally with
a physical-unit check as final confirmation); for the ARTICLE, micro-USB
charging may be stated with this combined citation, though the physical
check is noted as outstanding. Bonus from the same pass: the two
user-guide doc numbers (029-0515 gen 1, 029-0737 current) pin the guide
generations the version-history section could not previously separate.

## 1. The Drive route (operator archive, read this session)

Standing extraction caveat, stated once for every Drive file below: the Drive tool
returns EXTRACTED TEXT, not bytes, so no %PDF magic-byte check is possible.
Corroboration is operator curation, internal document structure, and agreement
between independent files.

The archive holds a dedicated "Phonak TV Connector" folder (id
1jTvUS2xQibx5iZmnKtaIb2xtU_-zfZm3) with a "TV Connector Support Docs" subfolder
(1UBkbqVoB31d-TpTC18_SrY7jVfRhFnMT). It holds MORE than the known packshots: user
guide, quick guide, and two product-information docs. Files used:

- user-guide-connector-92x125-gb-v2.00-029-0737-02-tv.pdf, id
  1NUKb3osGxjIIUAW5uoHHlJ007btdp7k-, 3,887,933 bytes. READ IN FULL. Own imprint:
  "CE mark applied: 2018"; doc 029-0737-02 V2.00 GB per filename (no version string
  visible in extract; the 2018 CE line is the document's own). Duplicate copy
  1wUU0tOJbzQztPFSdCKDAi7YDGcFgIJdf, same byte count. A second copy titled
  user_guide_tv_connector_029-0737.pdf (1J59Q-X2nrdhspwLskhKju87VDjJBn797,
  3,891,206 bytes, DIFFERENT byte count) was read in full as a generation check:
  content-identical, same "CE mark applied: 2018" - one guide, two exports.
- product-information-phonak-marvel-wireless-accessories-210x280-v1.00-027-0511-02-gb.pdf,
  id 1jWi33VMC0-S6-7YEvCyzYa_nQXhxyGTr, 1,393,244 bytes. Marvel-era product
  information (doc 027-0511-02 V1.00 GB per filename; body confirms Marvel context).
  Carries the TV Connector feature/spec page incl. housing size.
- PHAU_Product_Information_Phonak_Wi.pdf, id 1tedgOdC7ATdCsLjO-_a6oslbfFbbj6da,
  1,450,646 bytes. AU Paradise+Marvel-era product information; same TV Connector
  page, same figures - independent in-archive corroboration.
- FILENAME TRAP RECORDED: Product-Information-TV-Streamer-V2.pdf
  (1_eRGxGTMdlbKS0_pfpn_JyT7P_5-8AsL, 54,724 bytes) is NOT a "TV Streamer V2"
  document. Its text is the same TV Connector page as the Marvel product info,
  word for word, and nowhere says "V2". Do not cite it for any V2-specific claim.
- Quick guides present, unread (duplicative): quick-guide-tv-connector
  029-3235 V2.00 (168qyufOh_zVAKAFR48MY0iA9NGFrT-Rf) and an older export
  (1nS20o7UyVHKoDY98mwaGIJIWdfIfGK-v).
- Imagery: packshots for BOTH asset generations - Packshot_TV_Connector_*_076-3002
  (gen 1) and packshot-connector-d-*-076-3006-0612-tv (V2/"connector d", incl. the
  known 076-3006 asset). No datasheet: searched the folder listing plus title
  queries 'tv connector', 'connector'; datasheet_phonak_tv_connector is NOT in
  the archive.

Repo substrate (read-only): shipped listing
catalogue-view/listings/phonak__phonak-tv-connector-v1.html (operator-reviewed;
title "Phonak TV Connector V2 - Wireless TV Audio Streamer") and
unitron__unitron-tv-connector-v1.html; research/AIRSTREAM_FIRMWARE_LOCK_SCOPE.md
(Phonak/Unitron TV Connector hardware CONFIRMED shared, AirStream locked against
non-Sonova brands only); research/T57 (Unitron TV Connector part 076-5049-06,
byte-verified in two Sonova AU order forms).

## 2. Numeric specs

CONFIRMED (manufacturer primary, Drive user guide 029-0737 read in full, with the
extraction caveat):
- Wireless range: sends audio "within a 15 meter (50 ft) radius"; line of sight
  not required; walls/furniture and large metallic structures may reduce range.
- Pairing distance: aids within 1 meter (3 ft) of the unit during connect.
- Connect confirmation may take up to 10 seconds.
- Inputs: one audio socket taking optical (Toslink) OR analog 3.5 mm jack cable
  (optical cable supplied pre-installed; analog optional). Power: microUSB, 5 VDC
  min 500 mA charger, or powered from the TV's USB port.
- Audio formats: receives and transmits Dolby Audio, stereo or mono. DTS NOT
  supported - blinking red LED; fix is PCM/stereo in TV audio menu or the analog
  cable. (Dolby Audio is a licensed trademark in the guide's own imprint.)
- Radio: 2400 - 2483.5 MHz, sub-20 mW conducted power (compliance section).
- Operating conditions 0 to +40 C; transport/storage -20 to +60 C; humidity
  under 90 percent non-condensing; atmospheric pressure 500-1500 hPa.
- LED states: green transmitting, white standby (no audio input), blinking blue
  connecting, blinking red wrong format (DTS), off = powered off.
CONFIRMED (Drive Marvel + AU product information docs, mutually corroborating):
- Housing L 63 x W 63 x H 12 mm; streams to an unlimited number of listeners
  simultaneously; can be mounted behind the TV; "lowest streaming latency" is
  Phonak's qualitative wording - no ms figure anywhere in these docs.
SUSPECTED (search snippets attributed to the official datasheet
datasheet_phonak_tv_connector.pdf / Datasheet_TV_Connector_210x297_GB_V2.00.pdf;
bytes unfetchable, see section 6):
- Weight 30 g; colour black. Snippet dimensions 63 x 63 x 12 mm agree with the
  Drive primaries.
ABSENT: latency in ms (no consumer figure found anywhere; do not print a number).

## 3. Version history

- Gen 1 TV Connector: introduced with Audeo B-Direct, launch completed US/UK/IE
  September 2017 (SWORD chip era). Source class: trade press (Hearing Review
  "Sonova Announces New SWORD Made for All Platform; Phonak Audeo B-Direct";
  hearingaidknow.com) as snippets. Tier: SUSPECTED for the date. Packshot asset
  076-3002 (Drive) is this generation.
- TV Connector V2: the currently sold unit. Identity CONFIRMED at retail/part
  level: Connevans SKU 3P0763006 titled "Phonak Wireless TV Connector V2 (Dolby)"
  embeds part 076-3006, matching the Drive "connector-d" packshot asset number;
  the shipped catalogue listing (operator-reviewed) sells it as TV Connector V2.
  Launch date: tied to the Marvel launch era (Marvel announced November 2018,
  trade-press snippets) - no press release naming "TV Connector V2" with a date
  surfaced. Tier: SUSPECTED for the date; ABSENT for a primary.
- What changed gen 1 to V2: NOT pinned. A search synthesis says "TV Connector V2
  is also known as TV Connector-D - they are the same product" (SUSPECTED); the
  "d" naming recurs in the Drive asset filenames and Connevans' Unitron title
  ("TV Connector D Easy Line", part 076-5049-06 = repo T57). No primary document
  states the delta; the user guide (CE 2018) describes only the current unit.
- Both user-guide exports in Drive are the same 2018-CE document - the archive
  holds no gen-1-only user guide to diff against. Writer guidance: describe the
  V2 as the product; name gen 1 only as history, without a feature-delta claim.

## 4. UK pricing (indicative, dated observations only - never article facts)

All snippet/SERP-tier, observed 2026-08-05; no retailer page fetchable (403).
- Crystal Hearing (crystalhearinguk.co.uk): "Phonak TV Connector (v2) - 144 GBP"
  (verbatim SERP title, pound sign in original).
- Hearing Aid Accessories (hearingaidaccessories.co.uk): TV Connector + Remote
  Control bundle 279.99 GBP (snippet).
- Connevans (connevans.co.uk, SKU 3P0763006): stocks it; no price in snippet.
- Carried practice: most UK buyers with hearing loss qualify for VAT relief -
  quote inc and ex VAT when pricing appears; re-verify all figures before print.

## 5. Practical hookup material (the audience-research gap)

Primary-sourced (user guide 029-0737, read in full) - unusually, most of the
practical material manufacturer PAGES skip is in the user GUIDE:
- Optical vs analog: always connect to an audio OUTPUT; optical is preferred
  (guide's troubleshooting says switch from analog to optical for volume issues).
  Volume memory is stored independently per input type.
- TV headphone-out behaviour, stated by Phonak: "Some TVs will switch off their
  loudspeakers when using the headset socket - the TV will not be audible for
  other people." Fix in guide: enable parallel loudspeaker use in TV audio
  settings, or use the optical cable.
- Lip-sync/delay: if TV loudspeaker audio lags the streamed audio, REDUCE the
  TV's loudspeaker delay setting in its audio menu (guide FAQ). If streamed audio
  drifts from picture, set TV output to PCM/stereo rather than surround (shipped
  listing wording, catalogue substrate).
- Multiple listeners: one TV Connector serves an unlimited number of compatible
  aids simultaneously (product info docs, CONFIRMED); the guide adds it connects
  to ANY compatible aid in range during the connect process - a two-edged fact
  (easy family setup; accidental pairing of a visitor's aids is possible). Each
  wearer's volume is set on their own aids; unit volume buttons calibrate the
  stream. Shipped listing: each user sets their own volume (substrate).
- Phone calls: aids interrupt the TV stream for an incoming phone call and
  return to it after the call (guide, CONFIRMED).
- Auto behaviour: streams whenever audio is present; standby (white LED) when
  the source goes silent; resumes automatically when aids re-enter range.
- Soundbar/AV receiver: NOT covered by any primary read this session. Community
  practice is an optical splitter from the TV, or a spare optical output on the
  AV receiver/soundbar (forums.tomsguide.com threads, SUSPECTED snippet-tier).
  HDMI ARC setups leave no free optical out - splitter route (same tier). Flag
  as verify-with-professional language if used.
- CI audience (required for AirStream coverage): shipped listing (operator
  reviewed substrate) - AB Naida CI M90 and Sky CI M90 pair like Phonak aids;
  bimodal Naida Link M + AB CI stream from one TV Connector simultaneously;
  older AB processors (Naida CI Q-series, Harmony, Neptune) lack AirStream. No
  manufacturer primary re-verified this session; catalogue-substrate tier.

## 6. ABSENT / failures (looked for, not found or not reachable)

- Datasheet bytes: WebFetch HTTP 403 on phonak.com master-assets datasheet, on
  thehearclinic.co.uk mirror, and on product-support.phonak.com (egress proxy,
  same failure class as both prior articles). Drive archive lacks the datasheet.
  Pinned for acquisition:
  https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/accessories/tv-connector/datasheet_phonak_tv_connector.pdf.coredownload.pdf
  https://www.phonakpro.com/content/dam/phonakpro/gc_hq/nl/products_solutions/wireless_accessories/tv_connector/Datasheet_TV_Connector_210x297_GB_V2.00.pdf
  https://www.phonakpro.com/content/dam/phonakpro/gc_hq/nl/products_solutions/wireless_accessories/tv_connector/Fast_Facts_Phonak_Phonak_TV_Connector_210x280_GB_V2.00_028-1683-02.pdf
- Latency in milliseconds: not in Drive primaries, datasheet snippets, or trade
  articles reached. Only qualitative "lowest streaming latency" exists.
- Weight from a primary: 30 g is snippet-only (section 2).
- Gen-1 vs V2 feature delta from a primary; V2 launch date press release;
  gen-1-specific user guide (archive holds only the 2018-CE guide).
- Datasheet edition imprint: V2.00 appears only in mirror FILENAMES - per the
  standing lesson, filename version claims are recorded as unverified.
