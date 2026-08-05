# BRAND TOKENS - the publisher design system

STATUS: PROPOSED, unsigned. This file freezes the de facto design system
the first three articles already share into a named token set. On operator
signature it becomes the interim publisher brand: the brand_tokens machine
gate then enforces it on every article, and any change to it is a signed
amendment here first, propagated to articles second. If a real brand
identity exists or arrives later (palette, type, name treatment), it
replaces this section by amendment and the gate follows automatically.

## Colour tokens (complete census of the shipped corpus, 2026-08-05)

| Token | Hex | Role |
|-------|-----|------|
| ink | #1d1d1b | body text, headings, diagram line work |
| ink-soft | #52514e | standfirst, captions, secondary text |
| ink-faint | #6e6d69 | footer text (5.1:1 on paper, AA) |
| paper | #ffffff | page background |
| paper-tint | #f6f5f1 | scope box, diagram panels |
| rule | #d9d6cd | hairlines, borders, diagram furniture |
| accent | #1f5f3f | links, kicker, diagram emphasis (7.6:1 on paper) |
| accent-soft | #e8f0ea | highlighted diagram fills, text on accent |
| print-black | #000 | print stylesheet borders only |

No other colour literal may appear in an article. Contrast: every
text-bearing pair in the corpus computes AA or better (worst case
ink-faint on paper at 5.1:1); a new pairing must be computed before use.

## Type

One stack everywhere, including SVG text:
-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial,
sans-serif. Body 17px/1.65 (16px under 480px); scale and component sizes
live in the shared style block the articles carry.

## Components (the shared furniture)

Masthead with kicker; scope box; In brief box with On this page nav;
figbox-wrapped inline SVG figures with fact-checked captions; FAQ
definition list; sources block; independence footer. New articles carry
all of them; a new component class enters here by amendment before it
ships.

## Enforcement

Mechanical: the brand_tokens check in gates/article_gates.py (colour
literals subset of the token set; canonical font stack present; no other
font-family). Judgment ("does it feel right") stays with the operator's
rendered review and VOICE.md rulings - the gate checks conformance, not
taste.
