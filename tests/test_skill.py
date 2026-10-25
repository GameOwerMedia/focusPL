"""Testy struktury skilla focus-pl. Tylko biblioteka standardowa: python -m unittest discover -s tests"""

import json
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "skills", "focus-pl")
DASHES = ("—", "–")


def read(*parts):
    with open(os.path.join(*parts), encoding="utf-8") as fh:
        return fh.read()


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out, key = {}, None
    for line in m.group(1).split("\n"):
        kv = re.match(r"^([a-z][a-z0-9_-]*):\s*(.*)$", line)
        if kv:
            key = kv.group(1)
            out[key] = kv.group(2).strip()
        elif key and line.startswith(" "):
            out[key] = (out[key] + " " + line.strip()).strip()
    return out


def text_files():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
        for f in files:
            if f.endswith((".md", ".json", ".yml")):
                yield os.path.join(base, f)


class TestSkill(unittest.TestCase):
    def setUp(self):
        self.text = read(SKILL, "SKILL.md")
        self.fm = frontmatter(self.text)

    def test_frontmatter(self):
        self.assertEqual(self.fm.get("name"), "focus-pl")
        desc = self.fm.get("description", "").lstrip(">").strip()
        self.assertGreater(len(desc), 100)
        self.assertLessEqual(len(desc), 1024, "opis musi zmieścić się w limicie 1024 znaków")

    def test_sekcje(self):
        for heading in ("Panel A", "Panel B", "Wspólna synteza", "Zasady, które obowiązują zawsze"):
            self.assertIn(heading, self.text)
        self.assertIn("Wszystkie persony są fikcyjne", self.text)
        for label in ("TAK / NIE / MOŻE", "INWESTUJĘ / WARUNKOWO / ODPADA"):
            self.assertIn(label, self.text)

    def test_pliki_z_odnosnikow_istnieja(self):
        for ref in re.findall(r"`(references/[^`]+\.md)`", self.text):
            self.assertTrue(os.path.exists(os.path.join(SKILL, ref)), ref)

    def test_bez_polpauz_i_pauz(self):
        for path in text_files():
            text = read(path)
            for d in DASHES:
                self.assertNotIn(d, text, "%s zawiera półpauzę albo pauzę" % os.path.relpath(path, ROOT))


class TestPlugin(unittest.TestCase):
    def test_manifesty_sa_zgodne(self):
        plugin = json.loads(read(ROOT, ".claude-plugin", "plugin.json"))
        market = json.loads(read(ROOT, ".claude-plugin", "marketplace.json"))
        self.assertEqual(plugin["name"], "focus-pl")
        entry = [p for p in market["plugins"] if p["name"] == "focus-pl"][0]
        self.assertEqual(entry["version"], plugin["version"])
        self.assertIn("## [%s]" % plugin["version"], read(ROOT, "CHANGELOG.md"))


class TestPrzyklady(unittest.TestCase):
    def test_wynik_ma_ksztalt_ze_skilla(self):
        for name in ("wynik-pelny.md", "wynik-lite.md"):
            text = read(ROOT, "examples", "larder", name)
            self.assertIn("Wszystkie persony są fikcyjne", text)
            self.assertIn("## Panel A", text)
            self.assertIn("## Panel B", text)
            self.assertIn("## Synteza", text)

    def test_liczby_w_przykladach_sie_zgadzaja(self):
        for name, size in (("wynik-pelny.md", 10), ("wynik-lite.md", 3)):
            text = read(ROOT, "examples", "larder", name)
            self.assertEqual(len(re.findall(r"^### A\d+\. ", text, re.M)), size, name)
            self.assertEqual(len(re.findall(r"^### B\d+\. ", text, re.M)), size, name)
            synteza = text[text.index("## Synteza"):]
            for labels in (("TAK", "MOŻE", "NIE"), ("INWESTUJĘ", "WARUNKOWO", "ODPADA")):
                line = re.search(r"^.*\b%s \d+.*$" % labels[0], synteza, re.M).group(0)
                counts = [int(re.search(r"\b%s (\d+)" % label, line).group(1)) for label in labels]
                self.assertEqual(sum(counts), size, "%s: %s" % (name, line))


if __name__ == "__main__":
    unittest.main()
