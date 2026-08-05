#!/usr/bin/env python3
"""Article gates: style, twin-sync, and corpus consistency.

Runs six named checks over every article under articles/*/ (an article is a
directory holding index.html and CLAIMS.md). Exit 0 = clean; exit 1 =
findings, each printed with file and location. A finding is a flag for
human review, not always a defect - reviewed-and-accepted pairs go in
gates/consistency_allowlist.txt (one substring per line, '#' comments),
which suppresses corpus findings whose text contains the line.

Checks, by name:
  1 ascii_style          - non-ASCII bytes, dash/ellipsis entities, in
                           index.html and CLAIMS.md.
  2 jsonld_twin_sync     - FAQPage JSON-LD questions exactly match the
                           visible <dt> set both directions; a twin answer
                           may not introduce a numeral its visible <dd>
                           lacks (condensation may drop facts, never add).
  3 inbrief_sync         - a numeral in the In brief box must appear in
                           the article body outside the box (the box only
                           restates).
  4 quote_consistency    - corpus: long quoted strings that open
                           identically across articles must be identical
                           throughout (a diverging tail means one article
                           misquotes).
  5 absence_vs_figure    - corpus: an ABSENCE-tier claims row in one
                           article vs another article's row sharing enough
                           distinctive vocabulary AND carrying a numeral -
                           the class of the network-cap incident.
  6 upto_phrase_conflict - corpus: 'up to <N> <noun>' with the same noun
                           but a different N across articles.

Declared blind spots: prose contradictions that share no vocabulary or use
no numerals; factual drift inside a single article; claims tables that
describe the article wrongly (the adversarial review battery owns those);
JSON-LD answer meaning vs visible answer meaning (only numerals and
question names are machine-checked here).
"""

import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = sorted(p for p in (ROOT / "articles").iterdir()
                  if p.is_dir() and (p / "index.html").exists())
ALLOWLIST_PATH = Path(__file__).resolve().parent / "consistency_allowlist.txt"

NUMWORDS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
            "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"}
STOPWORDS = set("""a an the and or of to in on for with from by at as is are
was were be been it its this that these those not no never any all every
same other than then when where which who whose you your we our per one may
can could must should into out over under between across""".split())

findings = []


def flag(check, where, message):
    findings.append((check, where, message))


def allowlist():
    if not ALLOWLIST_PATH.exists():
        return []
    lines = []
    for line in ALLOWLIST_PATH.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            lines.append(line)
    return lines


def numerals(text):
    """Digit tokens plus number-words, normalised to digit strings.

    'one' is excluded from word matching: in prose it is usually a pronoun
    ('a used one'), and counting it produced the gate's first live false
    positive. Digit '1' is still detected; 'up to one X' is still caught
    by the upto check, which uses NUMWORDS directly."""
    found = set(re.findall(r"\d+(?:\.\d+)?", text))
    for word, digit in NUMWORDS.items():
        if word == "one":
            continue
        if re.search(r"\b" + word + r"\b", text, re.I):
            found.add(digit)
    return found


def soup_of(article):
    return BeautifulSoup((article / "index.html").read_text(), "html.parser")


def body_text(soup):
    s = BeautifulSoup(str(soup), "html.parser")
    for tag in s.find_all(["script", "style", "svg"]):
        tag.decompose()
    return s.get_text(" ")


# 1 ascii_style ----------------------------------------------------------
def check_ascii_style():
    bad_entities = re.compile(r"&(mdash|ndash|hellip|#8211|#8212|#8230);")
    for article in ARTICLES:
        for name in ("index.html", "CLAIMS.md"):
            path = article / name
            if not path.exists():
                continue
            data = path.read_bytes()
            for i, line in enumerate(data.splitlines(), 1):
                if any(b > 0x7F for b in line):
                    flag("ascii_style", f"{path.relative_to(ROOT)}:{i}",
                         "non-ASCII byte")
            for m in bad_entities.finditer(data.decode("ascii", "replace")):
                flag("ascii_style", str(path.relative_to(ROOT)),
                     f"dash/ellipsis entity {m.group(0)}")


# 2 jsonld_twin_sync -----------------------------------------------------
def check_jsonld_twin_sync():
    for article in ARTICLES:
        soup = soup_of(article)
        blocks = soup.find_all("script", type="application/ld+json")
        faq = None
        for b in blocks:
            try:
                data = json.loads(b.string)
            except (json.JSONDecodeError, TypeError):
                flag("jsonld_twin_sync", str(article.name),
                     "JSON-LD block does not parse")
                continue
            if data.get("@type") == "FAQPage":
                faq = data
        dts = [dt.get_text(" ", strip=True) for dt in soup.select("dl.faq dt")]
        if faq is None:
            if dts:
                flag("jsonld_twin_sync", article.name,
                     "visible FAQ present but no FAQPage JSON-LD")
            continue
        twins = {q["name"]: q["acceptedAnswer"]["text"]
                 for q in faq.get("mainEntity", [])}
        for name in twins:
            if name not in dts:
                flag("jsonld_twin_sync", article.name,
                     f"JSON-LD question not in visible FAQ: {name!r}")
        for dt in dts:
            if dt not in twins:
                flag("jsonld_twin_sync", article.name,
                     f"visible FAQ question missing from JSON-LD: {dt!r}")
        dds = {dt.get_text(" ", strip=True):
               dt.find_next_sibling("dd").get_text(" ", strip=True)
               for dt in soup.select("dl.faq dt")
               if dt.find_next_sibling("dd")}
        for name, twin_answer in twins.items():
            visible = dds.get(name, "")
            extra = numerals(twin_answer) - numerals(visible)
            if extra:
                flag("jsonld_twin_sync", article.name,
                     f"twin answer for {name!r} introduces numerals "
                     f"{sorted(extra)} its visible answer lacks")


# 3 inbrief_sync ---------------------------------------------------------
def check_inbrief_sync():
    for article in ARTICLES:
        soup = soup_of(article)
        box = soup.find(class_="inbrief")
        if box is None:
            continue
        box_nums = numerals(box.get_text(" "))
        box.extract()
        rest_nums = numerals(body_text(soup))
        orphans = box_nums - rest_nums
        if orphans:
            flag("inbrief_sync", article.name,
                 f"In brief numerals {sorted(orphans)} appear nowhere in "
                 "the article body - the box may only restate")


# 4 quote_consistency ----------------------------------------------------
def check_quote_consistency():
    quote_re = re.compile(r'"([^"]{30,})"')
    openings = {}
    for article in ARTICLES:
        text = body_text(soup_of(article))
        for m in quote_re.finditer(text):
            quote = " ".join(m.group(1).split())
            words = quote.split()
            if len(words) < 6:
                continue
            key = " ".join(words[:5]).lower()
            openings.setdefault(key, []).append((article.name, quote))
    for key, entries in openings.items():
        texts = {q for _, q in entries}
        if len(texts) > 1 and len({a for a, _ in entries}) > 1:
            arts = ", ".join(sorted({a for a, _ in entries}))
            flag("quote_consistency", arts,
                 f"quotes opening {key!r} diverge across articles")


# 5 absence_vs_figure ----------------------------------------------------
def parse_claims_rows(article):
    rows = []
    path = article / "CLAIMS.md"
    if not path.exists():
        return rows
    for line in path.read_text().splitlines():
        if not line.startswith("|") or line.startswith("|-"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 5 and cells[0] not in ("#", ""):
            rows.append({"id": cells[0], "where": cells[1],
                         "claim": cells[2], "source": cells[3],
                         "tier": cells[4]})
    return rows


def distinctive_terms(text):
    words = re.findall(r"[a-z]{4,}", text.lower())
    return {w for w in words if w not in STOPWORDS}


def check_absence_vs_figure():
    allowed = allowlist()
    per_article = {a.name: parse_claims_rows(a) for a in ARTICLES}
    for a_name, a_rows in per_article.items():
        for row in a_rows:
            if "ABSENCE" not in row["tier"].upper():
                continue
            a_terms = distinctive_terms(row["claim"])
            for b_name, b_rows in per_article.items():
                if b_name == a_name:
                    continue
                for other in b_rows:
                    if "ABSENCE" in other["tier"].upper():
                        continue
                    if not numerals(other["claim"]):
                        continue
                    shared = a_terms & distinctive_terms(other["claim"])
                    if len(shared) >= 3:
                        text = (f"{a_name} row {row['id']} (ABSENCE) vs "
                                f"{b_name} row {other['id']} (figure) share "
                                f"{sorted(shared)[:6]}")
                        if any(sub in text for sub in allowed):
                            continue
                        flag("absence_vs_figure", f"{a_name}/{b_name}", text)


# 6 upto_phrase_conflict -------------------------------------------------
def check_upto_phrase_conflict():
    allowed = allowlist()
    upto_re = re.compile(
        r"up to (?:about |roughly )?(\d+|" + "|".join(NUMWORDS) + r")"
        r"\s+([a-z]+(?:\s+[a-z]+)?)", re.I)
    seen = {}
    for article in ARTICLES:
        text = " ".join(body_text(soup_of(article)).split())
        for m in upto_re.finditer(text):
            n = NUMWORDS.get(m.group(1).lower(), m.group(1))
            noun = m.group(2).lower().strip()
            noun = " ".join(w for w in noun.split() if w not in STOPWORDS)
            if not noun:
                continue
            seen.setdefault(noun, {}).setdefault(n, set()).add(article.name)
    for noun, by_number in seen.items():
        if len(by_number) > 1:
            arts = {a for s in by_number.values() for a in s}
            if len(arts) > 1:
                detail = "; ".join(f"{n} in {', '.join(sorted(s))}"
                                   for n, s in sorted(by_number.items()))
                text = f"'up to N {noun}' disagrees: {detail}"
                if any(sub in text for sub in allowlist()):
                    continue
                flag("upto_phrase_conflict", noun, text)


# 7 brand_tokens ---------------------------------------------------------
BRAND_HEXES = {"#1d1d1b", "#52514e", "#6e6d69", "#ffffff", "#f6f5f1",
               "#d9d6cd", "#1f5f3f", "#e8f0ea", "#000"}
BRAND_FONT = ("-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, "
              "Helvetica, Arial, sans-serif")


def check_brand_tokens():
    """Colour literals must stay inside the BRAND-TOKENS.md set and every
    font-family must be the canonical stack. Spec: the token table in
    pilot/anchor-spec/BRAND-TOKENS.md - amend there first, here second."""
    hex_re = re.compile(r"#[0-9a-fA-F]{3,6}\b")
    font_re = re.compile(r"font-family:\s*([^;}]+)")
    for article in ARTICLES:
        html = (article / "index.html").read_text()
        for m in hex_re.finditer(html):
            if m.group(0).lower() not in BRAND_HEXES:
                line = html.count("\n", 0, m.start()) + 1
                flag("brand_tokens", f"{article.name}:{line}",
                     f"colour {m.group(0)} is outside the brand token set")
        for m in font_re.finditer(html):
            stack = " ".join(m.group(1).split())
            if stack not in (BRAND_FONT, "inherit"):
                line = html.count("\n", 0, m.start()) + 1
                flag("brand_tokens", f"{article.name}:{line}",
                     f"non-canonical font stack: {stack[:60]}")


CHECKS = [check_ascii_style, check_jsonld_twin_sync, check_inbrief_sync,
          check_quote_consistency, check_absence_vs_figure,
          check_upto_phrase_conflict, check_brand_tokens]


def main():
    if not ARTICLES:
        print("article_gates: no articles found under articles/")
        return 0
    for check in CHECKS:
        check()
    names = [c.__name__.replace("check_", "") for c in CHECKS]
    if findings:
        print(f"article_gates: {len(findings)} finding(s) across "
              f"{len(ARTICLES)} article(s)")
        for check, where, message in findings:
            print(f"  [{check}] {where}: {message}")
        return 1
    print(f"article_gates: clean ({len(ARTICLES)} articles, "
          f"checks run by name: {', '.join(names)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
