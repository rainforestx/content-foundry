# ACQUISITIONS - the standing fetch queue

What the pipeline needs but cannot reach from this environment. Two intake
routes: the operator drops files into the Google Drive archive (works now,
no egress needed), or a session with open egress fetches the pinned URLs
(magic-byte-verify every PDF; record edition and date). Items leave this
list when their bytes are verified and recorded where they are used.

## Documents

1. Roger Select 3 datasheet - ph-datasheet-roger-select3-210x297-en.pdf
   (phonak.com master-assets path pinned in the Select 3 RESEARCH.md).
   Unblocks: battery/operating time, charge port (resolves the micro-USB
   tension), capsule count (resolves the three-vs-six tension), range,
   weight for article 2.
2. Roger Select 3 user guide - doc 029-1380-02 (URL pinned in the Select 3
   RESEARCH.md). Unblocks: pairing persistence stated for the Select
   itself, TV setup detail, Bluetooth call mechanics.
3. Roger On 3 user guide - doc 029-1379-02 (URL pinned in the On 3
   RESEARCH.md). The Drive file named Roger_On_3_User_Guide.pdf is
   actually the 2021 gen-1/iN guide (validity page checked); the true On 3
   guide is not held. Unblocks: byte-verification of the pairing quote at
   its primary source.

## Imagery (Amendment A1 is signed; assets are the blocker)

4. Roger On 3 official packshots from the supplier portal. The archive's
   Roger On packshot set (asset 056-3010, created 2021-02) is GEN-1; gen 1
   and gen 3 are externally near-identical, so provenance is the only
   reliable generation evidence - a gen-3 asset number or portal folder is
   required, not a visual check.
5. Roger Select 3 official packshots - none held in any generation-marked
   form.
6. Alternative that beats both: operator photography of the held stock
   units (Roger On 3 and Roger Select 3), which is generation-certain,
   licence-free and unique to the property. A phone shot set per unit
   (front, in dock / on table, box contents) is sufficient.

## Standing note

Generation-stable accessory imagery (NeckLoop 042-4001, TV Connector,
PartnerMic packshots) is held and usable once its product identity is
source-confirmed for the article that wants it; each use still gets an
IMAGES row per Amendment A1.

## Ruling 2026-08-06 - operator, via the operator console

Verbatim: "the operator will drop the pinned documents into the Drive
archive. Items leave content-foundry/pilot/ACQUISITIONS.md as their
bytes are verified at point of use."

Two consequences worth stating because they are easy to get wrong. A
document arriving in Drive does not by itself clear its row here: the
row clears when an article actually reads the bytes and verifies the
document's identity by imprint, at the point of use, because a filename
has misidentified a document four separate times in this pilot. And a
row that has been queued for a long time is not evidence of neglect -
the queue is the operator's to service on their own cadence, and the
articles hedge or state absences in the meantime rather than waiting.

## Ruling 2026-08-06 (second, supersedes the routing above) - operator

Verbatim: "an egress-open session is authorised to fetch the pinned URLs,
magic-byte verifying every PDF and recording edition and date. Operator
diverged from the session position - allowed; recorded."

The session's position had been that the operator drops documents into
Drive and rows clear at point of use. The operator diverged and widened
it: a session with working egress may fetch the pinned URLs directly.
Both stand - the Drive route remains open, and this adds a second route
that does not wait on the operator at all. The earlier entry is kept
above rather than edited, per the append-only rule.

Conditions carried by the ruling itself, and they are the whole point of
it: every PDF is magic-byte verified, not trusted by extension or by
content-type header, and the edition and date are recorded with it. That
is the discipline the filename traps in this pilot earned - four
documents so far have been something other than what their filename
said. A fetched file that fails its magic-byte check is not a source; it
is an incident, and it gets recorded as one.

Standing note for whichever session has egress: this repository's own
fetches have returned 403 on every manufacturer and retailer page tried
to date, which is why the queue exists. An egress-open session should
work the pinned list in one pass and record what still refuses, so the
next session inherits a shorter list rather than repeating the wall.
