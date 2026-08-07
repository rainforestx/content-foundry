# Skill overlays

A skill named `X` reads `.claude/overlays/X.md` when it runs here and applies
it over its own defaults. The filename is the binding, so there is nothing to
register and nothing to keep in sync.

**The doctrine is not restated here.** It lives in one place:
`skills/instruction-overlays/SKILL.md` in rainforestx/agentic-app-architecture.
Read it before adding an overlay. What follows is only what is local.

## The short version

- An overlay is a **specialisation**, never an entry point. Plain markdown, no
  frontmatter, no description, no triggers, so it cannot collide with the skill
  it modifies.
- It may **narrow, never weaken** the parent skill's evidence discipline.
- New local knowledge goes to `_proposed/` as a dated observation, not
  straight into an overlay. See `_proposed/README.md`.
- `gates/overlay_gate.py` enforces the checkable half and states in its own
  output that it cannot verify whether the parent skill actually looks.

## Current overlays

| Overlay | Parent skill | Covers |
|---|---|---|
| `perplexity.md` | `perplexity` (user level) | Claims-table evidence bar, provenance over appearance for product generations, UK region, the acquisitions queue, and the earx read-only guarantee |
