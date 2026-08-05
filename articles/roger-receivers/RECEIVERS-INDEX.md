# Roger receivers - factual substrate index (article 4)

How a Roger mic's signal gets INTO a hearing device: NeckLoop, Roger X,
design-integrated receivers, RogerDirect licences, second-hand buying. Every
fact traces to an entry below; paths under /home/user/earx-catalogue/. Surveyed
read-only 2026-08-05.

Identity notes, load-bearing: (a) "Design-integrated receivers" = physical
snap-on family (Roger 10-21 + AS variants); "RogerDirect" = a firmware licence
in Marvel-class-and-later aids, never a shippable object (B9/B10); the shipped
listing retitles the family "Phonak Roger Model-Specific Receivers". (b)
NeckLoop "02": Rogerpedia byte-null on any 02/03 NeckLoop suffix (GAP8);
user-guide corroboration is browser-agent-tier, byte verification PENDING -
never settled. (c) "Education tier"/"adult tier" for the Options: invented,
retired W3c - never reuse.

## 1. Listings (evidence standing: post-correction shipped copy)

- catalogue-view/listings/phonak__phonak-roger-x-03-v1.html ("Phonak Roger X
  (03)") and ...roger-x-02-v1.html. FAQ set (x-03 lines 975-982) encodes the
  buyer questions: genuine; not a hearing aid (does nothing alone);
  "Marvel/Paradise/Lumity/Infinio - do I need this?" (usually not -
  RogerDirect); "(02) vs (03)?" (mic lists PLUS (02)-only EasyGain, Check, link
  quality; caveat that the 2023 table predates the Roger 3 mics - load-bearing,
  keep); no own battery, draws from the aid, remove when unused; pairing from
  the mic's Connect at 10 cm, remembered; no-sound checklist (aid's
  Roger/FM/DAI/EXT/AUX program); warranty 1 yr standard / 2 yr serialised Roger
  devices.
- ...phonak-roger-neckloop-02-v1.html, FAQ 971-978: non-Phonak T-coil aids work
  (cross-industry standard, message-us hedge); one-time connect (T-coil program
  on, 10 cm, Connect ON THE MIC not the loop); T-coil program may need HCP
  ENABLING (off by default is common); lanyard-worn, charged like a phone, "a
  full charge covers the day"; volume limiter via pin tool within 30 s of
  startup (child safety).
- ...phonak-roger-design-integrated-receivers-v1.html, FAQ 978-985:
  is-this-RogerDirect FAQ; snap-on self-fit, confirm-first by message
  (model-specific receiver numbers); hygiene no-return-once-fitted (CCR 2013
  reg 28); fits selected Cochlear/MED-EL/AB processors AND older Phonak
  Belong/Venture aids; Marvel+ aids do not need one.
- All four mirrors under "Phonak/Wireless Accessories/" diff-verified
  byte-identical this survey. The shipped W10 "How Roger works" block
  (design-integrated listing line 869) is the FOUR-PATH mental model to mirror:
  RogerDirect licence / Roger X (DAI, shoe, Europlug streamer) / NeckLoop or
  MyLink (any telecoil) / model-specific snap-ons, plus the none-of-the-four
  dead end, stated honestly.

Quote-check state: these pages carried LIVE errors until 2026-07-28 - 02/03
compatibility INVERTED (buyers steered to 03; Phonak lists 02 as universal),
03's missing features unstated (fixed W3i). DL-034 re-derived the V8 p26 table
cell-by-cell at primary tier, so CURRENT copy is byte-cited; pre-2026-07-28
quotations of these pages are poisoned. data/claim_sources.csv holds ZERO Roger
rows; SOURCE_ARTEFACT_VERIFICATION.md registers the Rogerpedia PDFs genuine.

## 2. Licence / install doctrine (evidence-tiered fact-sheets)

- research/DL_030_GAP1_ROGERDIRECT_UNLIMITED_RECEIVERS_2026_07_27.md - four
  Roger 3 SKUs ship unlimited built-in receivers (Sonova PR 2024-08-29, HIGH);
  install onto Marvel/Paradise/Lumity/Infinio + latest Unitron/Hansaton + Naida
  CI M; stereo needs a binaural RogerDirect pair; SDF1 = V9 omits Touchscreen
  (resolved all-four). Version boundary (T38, LEARNING #218): only V9 documents
  Roger Unlimited - never cite V7/V8 for it. DO-NOT-SAY (7): incl. no
  "unlimited" for pre-3/iN units; never steer RogerDirect-platform owners to a
  Roger X; never extend RogerDirect below Marvel.
- research/DL_030_GAP3_INSTALL_AUTHORITY_2026_07_27.md - Path 1 (unlimited/iN
  mic auto-install) buyer-scope; Path 2 (Roger X + Roger Installer) HCP-gated:
  Phonak enumerates "HCP..., School Audiologist, School Personnel", never
  consumers. SDF1: the KB verb "check" = Full/Empty diagnostic, distinct from
  install. SDF3 serial cutoff: verbatim "via a Roger X (with serial number
  higher than 1744xxxx) and the Roger Installer", V8 txt lines 719 and 855,
  cross-ref B10 sec 3. Second-hand load-bearing quote: "Once a Roger receiver's
  license is transferred to one hearing device, the Roger X is empty."
  DO-NOT-SAY (4): incl. Installer is not retail; not every Roger X qualifies.
- research/DL_030_GAP5_SELECT_IN_LICENCE_COUNT_2026_07_28.md - iN mics contain
  EXACTLY TWO receivers (Rogerpedia p12 byte-quote), pool then empty; uninstall
  reversible (aid -> Roger X via Installer); iN path is Sonova-only; the 10 cm
  figure is interpretation-tier. DO-NOT-SAY: no "unlimited" on iN; audiologist
  optional for the iN mic-based install.
- research/DL_030_GAP8_NECKLOOP_02_MEANING_2026_07_28.md - NeckLoop is a T-coil
  bridge, not an installable receiver; its sec 4 uses the retired tier labels -
  superseded, do not carry.
- blockers_research/: B8 - "iN" = built-in receiver install traded against
  Bluetooth, NOT a network feature. B9 - design-integrated anatomy; current
  phonak.com narrows documented compat to CIs; best mapping is a 2021 AU order
  form (stale). B10 - RogerDirect is never purchasable; paths are an
  iN/unlimited mic or a Roger X.
- Gap-7's EasyGain/Check contradiction resolved for its own sec 4 by DL-034's
  V8 re-fetch; V8 p26 footnotes: "Option (03) not available in certain
  countries", "* except Roger NeckLoop" (EasyGain). T26: V9 drops the Option
  split entirely (zero hits).

## 3. Rogerpedia by txt line (research/rogerpedia_source_pdfs/)

V9 AU (rogerpedia_028-1902-48_V9.00_2024-09_AU.txt), registered genuine:
- p19 receivers section lines 558-590: Roger Unlimited; "RogerDirect applies to
  Phonak Infinio, Lumity, Paradise and Marvel"; "latest hearing aids from
  Unitron" + Naida CI M / Sky CI M (V9 AU names Unitron only, NOT Hansaton -
  Hansaton rests on V7/V8 + user guide); 8-model Virto t-coil-only exclusion
  footnote, lines 584-586.
- p21 compatibility guide lines 595-635: "virtually every hearing aid and
  cochlear implant that has a direct audio input or t-coil" (hedge
  load-bearing); three connect routes; footnotes 631-633 name the four
  unlimited and three iN mics.
- p22 CI table lines 640-706: columns RogerDirect / Roger 14 / 17 / 20 / 21 /
  Roger X / Roger X interface / NeckLoop; rows AB (Naida CI M, Q, Sky CI M,
  Harmony/Auria + iConnect, Neptune + Neptune Connect), Cochlear (Nucleus 5-8,
  Kanso, Baha 3-6, Osia 2, via Euro adapter or Mini Microphone 2+), MED-EL
  (SONNET, RONDO, ADHEAR, SAMBA), Oticon Medical (Neuro, Ponto +
  Streamer/EduMic). Footnotes 698-701: 4 = "Roger X must be used with a
  ComPilot" (Naida CI Q); 2/3 are CI profile settings. Neptune has NO NeckLoop
  mark; infant lock in 20/21.
- p23 Naida Link / Sky Link table lines 710-722: Link M = RogerDirect +
  NeckLoop; Link RIC = Roger X + AS15; Link UP = Roger X + AS10. NeckLoop
  speech study ref line 926.

V8 intl (rogerpedia_028-1902-02_V8.00_2023-06.txt) carries tables V9 AU lacks
(GAP2's "p20/p25" - cite by edition + txt line, page numerals drift across
editions):
- design-integrated-for-AIDS table lines 726-800: Roger 18/19 + AS18/AS19
  audio shoes across Belong-era Audeo/Bolero/Sky/Naida/CROS/Virto/Vitus;
  footnotes "Roger X must be used with a ComPilot II" and "Only with T-Coil";
  IP68 + tamperproof kit (0-36 months) for 18/19.
- third-party overview lines 885-905: telecoil -> NeckLoop; DAI/audio shoe,
  Euro streamer (Oticon Streamer Pro) or remote mic (GN ReSound MultiMic,
  Starkey Remote Microphone +, Oticon EduMic) -> Roger X. Option (02)/(03)
  table lines 945-963, feature definitions 930-943; serial-cutoff lines 719 and
  855; receiver colours 965+.

## 4. CI audience - CONVENTIONS section 5 is LAW (lines 206-230)

Six required placements: lede, scope, chip, FEATURED compat bullets, dedicated
AB FAQ incl. bimodal Naida Link M + AB CI from one source, not-suitable naming
Naida CI Q-series / Harmony / Neptune / Chorus. The sec 3 tables are the CI
reader's entire route map - the spine, not a bolt-on. CONV says Naida CI M90;
Rogerpedia prints "Naida CI M" - use the source's form. NHS stays
"AirStream-equipped".

## 5. Already covered by the shipped articles (link, do not repeat)

- Article 1 (phonak-roger-on-3/CLAIMS.md claims 9-15, 26-46, 52-53): four-SKU
  unlimited receivers + install-once quote; no-published-cap absence claim;
  platform list + Virto exclusions; Unitron/Hansaton; full CI subsection (incl.
  Q + ComPilot footnote, Neptune no-NeckLoop); one-paragraph paths 2-3 summary;
  Installer HCP list; NHS Nathos Nova/Auto; serial cutoff as ONE FAQ (claim
  53); not-for class. Article 4 is the deep treatment these link into.
- Article 2 (phonak-roger-select-3/CLAIMS.md M1-M18, N1): same ground plus M18
  Select iN two-licence precision; M4's Hansaton attribution pattern ("the
  catalogue research behind this guide") - reuse it. Article 3 (tv-connector):
  no receiver-path treatment; Correction #20 = receivers-page citation drift.
- NOT yet treated anywhere: buyer-side receiver decision tree; full 02/03
  feature table; NeckLoop as a product (charging, volume limiter, wearing,
  headphones); design-integrated family detail (Roger 14-21, infant security,
  IP68, colours); the V8 aid-level table; licence movement/uninstall;
  second-hand buying.

## GAPS - what the substrate does NOT hold (source externally, flag)

1. Prices: none in listings or research. External.
2. NeckLoop and Roger X datasheet numerics (battery, weight, dimensions, loop
   length, range): qualitative listing copy only, no datasheet banked; the V8
   2023 Option table predates Roger 3 mics - the shipped caveat must survive.
3. Serial cutoff: "higher than 1744xxxx" IS in-repo byte-tier; what it encodes
   and how a buyer reads a Roger X serial is unsourced.
4. Second-hand market: forum anxiety is pointers only (GAP3 SDF2, B8), no
   committed byte-quotes; whether an emptied Roger X can be re-loaded (GAP5 sec
   4 implies aid -> X re-install) needs external confirmation.
5. NeckLoop 02 vs 03 split: byte-verification pending (GAP8). Roger MyLink:
   in shipped W10 copy and GAP3 draft, zero dossier substrate; unsourced.
6. Design-integrated current-day scope: B9's two [UNVERIFIED] items (2026
   model-receiver mapping; whether any current aid ships one).
