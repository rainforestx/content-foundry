# Proposals - staging, not behaviour

**Nothing reads this directory.** That is its safety property. An agent may
write here unattended, mid-task, without asking, precisely because writing here
changes nothing. `gates/overlay_gate.py` fails if any skill or live overlay
points at this path.

Write an **observation**, not a rule: what you ran, what came back, when, and
what you were doing. Every entry carries a date, because an observation that
cannot age cannot be re-tested, and one that cannot be re-tested is a verdict
wearing a timestamp.

Never write standing claims about the world - "X is blocked", "the network is
open", "that never works". The gate rejects these by phrase.

Something leaves here when a second occurrence in a different task appends
alongside the first, a different actor generalises it, it **moves** into
`../<skill>.md`, and the owner signs it off. Entries older than 90 days fail
the gate: promote or delete.
