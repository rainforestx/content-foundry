# Gates

Machine-enforced checks for the article corpus - the top rung of the
growth ladder in pilot/reviewer/CHECKLISTS.md (defect class caught twice
becomes a named check; a named check that can be mechanized becomes a
gate). CI runs everything here on every push (.github/workflows/gates.yml):
the sabotage tests first, then the live gates, so a gate that has silently
lost the ability to fire fails the build before its clean verdict is
trusted.

## article_gates.py - six checks, by name

1. ascii_style - non-ASCII bytes and dash/ellipsis entities in every
   article's index.html and CLAIMS.md. House style is pure ASCII.
2. jsonld_twin_sync - the FAQPage JSON-LD question set must exactly match
   the visible FAQ both directions, and a condensed twin answer may drop
   facts but never introduce a numeral its visible answer lacks.
3. inbrief_sync - a numeral in the In brief box must appear in the
   article body outside the box; the box only restates.
4. quote_consistency - long quoted strings that open identically across
   articles must be identical throughout; a diverging tail means one
   article misquotes its source.
5. absence_vs_figure - an ABSENCE-tier claims row in one article against
   another article's figure-bearing row sharing enough distinctive
   vocabulary. Graduated from the live incident where article 2 asserted
   no published network cap hours after article 1 printed the datasheet's
   up-to-ten.
6. upto_phrase_conflict - 'up to N <noun>' with the same noun and a
   different N across articles.

## Findings and the allowlist

A finding is a flag for human review, not automatically a defect. When a
flagged pair is reviewed and accepted as consistent, add a substring of
the finding text to consistency_allowlist.txt with a comment saying who
accepted it and why. The allowlist's suppression behaviour is itself
covered by a sabotage test.

## Declared blind spots

Prose contradictions sharing no vocabulary or using no numerals;
meaning-level drift between a twin and its visible answer; factual drift
inside a single article; a claims table that describes its article
wrongly. Those stay with the adversarial review battery - the gates
narrow the reviewer's load, they do not replace it.

## Tests

gates/tests/test_article_gates.py - eight sabotage tests. Every check is
proven able to fire on a broken fixture, and a clean two-article corpus
is proven silent. A check that cannot be made to fail is not a check.
