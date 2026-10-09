#!/usr/bin/env python
"""Generator for benchtest/diagrams/lionguard-explained.html (scratch tool, not committed).
Reads the shared CSS (lines 6-110) byte for byte from sentinel-explained.html and emits the page.
Facts come only from benchtest/drafts/lionguard_two_level.md and lionguard_inventory_final.md.
Page body parts live in parts.py (imported) to keep this file short.
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
SENTINEL = os.path.join(ROOT, "benchtest", "diagrams", "sentinel-explained.html")
OUT = os.path.join(ROOT, "benchtest", "diagrams", "lionguard-explained.html")

import parts

with io.open(SENTINEL, encoding="utf-8", newline="") as f:
    s_lines = f.read().split("\n")
base_css = "\n".join(s_lines[5:110])  # lines 6..110

page = "".join([parts.HEAD, base_css, parts.ADDITIONS, parts.HEADER, parts.OVERVIEW, parts.POSITION,
                parts.HOW, parts.MAKERS, parts.INPUT, parts.OUTPUT, parts.LANG, parts.SCORE,
                parts.LIMITS, parts.FOOTER])
with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(page)
print("wrote", OUT, len(page))
