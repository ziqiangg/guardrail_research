"""Sheet '3d. Llama Guard Inventory' from drafts/lg_inventory_final.md. Called by build_two_level.main().

Thin config over inventory_sheet.py (shared with 3e).
Public API: add_sheet(wb, ws3) -> ws ; verify(wb, xlsx=None)
"""
import re

import paths as P
import inventory_sheet as IS
import build_inventory as BI
from build_inventory import S3C, S3D

DIR = BI.DIR
MD = str(P.DRAFTS / "lg_inventory_final.md")
TITLE = "3d. Llama Guard Inventory (Llama Guard 1 to 4)"
NOTE = ("Source: Meta PurpleLlama model cards, Hugging Face, dev.meta.ai docs, llama-cookbook and OGX, with the "
        "refs pinned in each cell. Covered-by maps each variant to a Table 3 column; LG1 and LG2 are legacy.")
WIDTHS = [28, 30, 34, 30, 26, 45, 50, 40, 34, 30, 34, 32, 30, 40, 40, 50]
LEGACY = "— (legacy, not in Table 3)"
BLOCKS = [  # (md section marker, bold block title or None, expected rows)
    ("## (a) Variant table", None, 8),
    ("## (b) Category crosswalk", "Category crosswalk (hazard concept by Llama Guard version)", 14),
    ("## (c) Integration paths", "Integration paths", 9),
]


def validate_crosswalk(ctx):
    """S1-S14 (LG3/4), S1-S11 (LG2), O1-O6 (LG1) codes in the crosswalk; variant, crosswalk and integration counts."""
    ws, (_, r1), (_, r2), (_, r3) = ctx["ws"], *ctx["pos"]

    def codes(col, pat):
        s = set()
        for r in r2:
            s |= set(re.findall(pat, str(ws.cell(row=r, column=col).value)))
        return s
    lg34 = codes(4, r"\bS(\d+)\b")
    lg2 = codes(3, r"\bS(\d+)\b")
    lg1 = codes(2, r"\bO(\d+)\b")
    ok34 = lg34 == {str(i) for i in range(1, 15)}
    ok2 = lg2 == {str(i) for i in range(1, 12)}
    ok1 = lg1 == {str(i) for i in range(1, 7)}
    msgs = ["crosswalk rows: %d (14) | LG3/4 codes: %d (14) %s | LG2 codes: %d (11) %s | LG1 codes: %d (6) %s"
            % (len(r2), len(lg34), "OK" if ok34 else "FAIL", len(lg2), "OK" if ok2 else "FAIL",
               len(lg1), "OK" if ok1 else "FAIL"),
            "variant rows: %d (8) | integration rows: %d (9)" % (len(r1), len(r3))]
    ok = ok34 and ok2 and ok1 and len(r1) == 8 and len(r2) == 14 and len(r3) == 9
    return ok, msgs


COV = "Covered by Table 3 column"
PANEL = dict(prefix="Llama Guard:", n=5, title="Coverage of Table 3 columns", first_hdr="Table 3 column (live link)",
             counts=[("Variants covering it", 0)],  # (count header, block index of the Covered-by column)
             totals=[("Variants marked legacy", [(0, COV, "*legacy*")])])  # (label, [(block, column header, criterion)])
CFG = dict(md=MD, sheet=S3D, title=TITLE, note=NOTE, after=S3C, blocks=BLOCKS, widths=WIDTHS,
           center={0: (2,)}, covered="Covered by Table 3 column", markers=(LEGACY,), order=BI.ORDER,
           validators=[validate_crosswalk], panel=PANEL)


def parse_md(path=MD):
    return IS.parse_md(dict(CFG, md=path))


def add_sheet(wb, ws3=None):
    return IS.add_sheet(wb, CFG)


def verify(wb, xlsx=None):
    return IS.verify(wb, CFG, xlsx)
