"""Sabotage tests for article_gates: every check must fire on a broken
fixture and stay quiet on a clean one. A gate that cannot be made to fire
is not a gate."""

import importlib
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import article_gates  # noqa: E402


CLEAN_HTML = """<html><body><main>
<div class="inbrief"><ul><li>Runs a stated 8 hours on a charge.</li></ul></div>
<p>The battery runs a stated 8 hours when streaming. The network takes
up to ten connected microphones. Phonak writes: "Connecting a receiver is
only required once for every device you own."</p>
<dl class="faq"><dt>Does it stream TV?</dt><dd><p>Yes - up to ten connected
microphones can join, and the battery runs 8 hours.</p></dd></dl>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Does it stream TV?",
 "acceptedAnswer":{"@type":"Answer",
 "text":"Yes - up to ten connected microphones can join, and the battery runs 8 hours."}}]}
</script>
</main></body></html>"""

CLEAN_CLAIMS = """# CLAIMS
| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| 1 | Body | Network takes up to 10 connected microphones | datasheet | CONFIRMED |
| 2 | Body | Battery runs 8 hours streaming | datasheet | CONFIRMED |
"""

CLEAN_HTML_B = CLEAN_HTML.replace("Does it stream TV?", "Is it heavy?")

CLEAN_CLAIMS_B = """# CLAIMS
| # | Where | Claim | Source | Tier |
|---|-------|-------|--------|------|
| 1 | Body | Weight is 27 grams per the datasheet | datasheet | CONFIRMED |
"""


class GateHarness(unittest.TestCase):
    def build(self, articles):
        """articles: {name: (html, claims)} -> corpus dir."""
        import tempfile
        root = Path(tempfile.mkdtemp())
        (root / "articles").mkdir()
        for name, (html, claims) in articles.items():
            d = root / "articles" / name
            d.mkdir()
            (d / "index.html").write_text(html)
            (d / "CLAIMS.md").write_text(claims)
        return root

    def run_gates(self, root, only=None):
        importlib.reload(article_gates)
        article_gates.ROOT = root
        article_gates.ARTICLES = sorted(
            p for p in (root / "articles").iterdir() if p.is_dir())
        article_gates.ALLOWLIST_PATH = root / "allowlist.txt"
        article_gates.findings = []
        for check in article_gates.CHECKS:
            if only and check.__name__ != only:
                continue
            check()
        return article_gates.findings

    def test_clean_corpus_is_clean(self):
        root = self.build({"a": (CLEAN_HTML, CLEAN_CLAIMS),
                           "b": (CLEAN_HTML_B, CLEAN_CLAIMS_B)})
        self.assertEqual(self.run_gates(root), [])

    def test_ascii_style_fires_on_emdash_and_entity(self):
        bad = CLEAN_HTML.replace("on a charge", "on a charge — easily")
        root = self.build({"a": (bad, CLEAN_CLAIMS)})
        found = self.run_gates(root, "check_ascii_style")
        self.assertTrue(any(f[0] == "ascii_style" for f in found))
        bad2 = CLEAN_HTML.replace("on a charge", "on a charge &mdash; easily")
        root2 = self.build({"a": (bad2, CLEAN_CLAIMS)})
        found2 = self.run_gates(root2, "check_ascii_style")
        self.assertTrue(any("entity" in f[2] for f in found2))

    def test_jsonld_fires_on_question_mismatch(self):
        bad = CLEAN_HTML.replace(
            '"name":"Does it stream TV?"', '"name":"Does it stream radio?"')
        root = self.build({"a": (bad, CLEAN_CLAIMS)})
        found = self.run_gates(root, "check_jsonld_twin_sync")
        self.assertTrue(any(f[0] == "jsonld_twin_sync" for f in found))

    def test_jsonld_fires_on_new_numeral_in_twin(self):
        bad = CLEAN_HTML.replace(
            "battery runs 8 hours.\"}}]}",
            "battery runs 8 hours or 6 with a receiver.\"}}]}")
        self.assertNotEqual(bad, CLEAN_HTML)
        root = self.build({"a": (bad, CLEAN_CLAIMS)})
        found = self.run_gates(root, "check_jsonld_twin_sync")
        self.assertTrue(any("introduces numerals" in f[2] for f in found),
                        found)

    def test_inbrief_fires_on_orphan_numeral(self):
        bad = CLEAN_HTML.replace("a stated 8 hours on a charge",
                                 "a stated 9 hours on a charge")
        root = self.build({"a": (bad, CLEAN_CLAIMS)})
        found = self.run_gates(root, "check_inbrief_sync")
        self.assertTrue(any(f[0] == "inbrief_sync" for f in found))

    def test_quote_consistency_fires_on_diverging_tail(self):
        b = CLEAN_HTML_B.replace(
            "only required once for every device you own",
            "only required once for each microphone you buy")
        root = self.build({"a": (CLEAN_HTML, CLEAN_CLAIMS),
                           "b": (b, CLEAN_CLAIMS_B)})
        found = self.run_gates(root, "check_quote_consistency")
        self.assertTrue(any(f[0] == "quote_consistency" for f in found))

    def test_absence_vs_figure_fires_and_allowlist_suppresses(self):
        absent = CLEAN_CLAIMS_B + (
            "| 2 | Body | No published cap on connected microphones for the "
            "network | searched guide | ABSENCE |\n")
        root = self.build({"a": (CLEAN_HTML, CLEAN_CLAIMS),
                           "b": (CLEAN_HTML_B, absent)})
        found = self.run_gates(root, "check_absence_vs_figure")
        self.assertTrue(any(f[0] == "absence_vs_figure" for f in found))
        (root / "allowlist.txt").write_text("b row 2 (ABSENCE) vs a row 1\n")
        found2 = self.run_gates(root, "check_absence_vs_figure")
        self.assertEqual([f for f in found2 if f[0] == "absence_vs_figure"],
                         [])

    def test_upto_conflict_fires_on_same_noun_different_number(self):
        b = CLEAN_HTML_B.replace("up to ten connected\nmicrophones",
                                 "up to six connected\nmicrophones")
        root = self.build({"a": (CLEAN_HTML, CLEAN_CLAIMS),
                           "b": (b, CLEAN_CLAIMS_B)})
        found = self.run_gates(root, "check_upto_phrase_conflict")
        self.assertTrue(any(f[0] == "upto_phrase_conflict" for f in found))


if __name__ == "__main__":
    unittest.main(verbosity=2)
