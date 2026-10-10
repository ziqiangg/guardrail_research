"""Sheet '3j. Purple Llama Inventory' from drafts/purplellama_inventory_final.md. Called by build_two_level.main().

Thin config over inventory_sheet.py (shared with 3d to 3i).
Public API: add_sheet(wb, ws3) -> ws ; verify(wb, xlsx=None)
Blocks: (a) components and variants (16), (b) LlamaFirewall scanner catalogue (8), (c) roles, use cases and default
scanner map (11), (d) Code Shield language and analyzer matrix (16), (e) integration and access paths (12),
(f) licences, gating and terms (8), (g) published metrics and latency statements (12), (h) adjacent and
cross-reference items (5). 88 rows. Covered-by is in blocks (a), (b), (c) and (e) only (indexes 0, 1, 2, 4).
Markers: legacy and inventory only (R011); planned is not used. The panel counts all four Covered-by blocks; its
last count column (access paths) is non-zero for all seven columns, as the shared panel check needs.
The product has three header prefixes (R030); the panel matches them with a tuple prefix and checks n = 7 contiguous columns.
"""
import paths as P
import inventory_sheet as IS
import build_inventory as BI

MD = str(P.DRAFTS / "purplellama_inventory_final.md")
S3J = "3j. Purple Llama Inventory"
TITLE = "3j. Purple Llama Inventory (Meta Prompt Guard 2, LlamaFirewall, Code Shield and CyberSecEval)"
NOTE = ("Source: Meta Purple Llama repository meta-llama/PurpleLlama at commit 172c1074, the Meta documentation pages, "
        "the Hugging Face gate pages and the LlamaFirewall paper, read on 2026-10-09 and 2026-10-10. Code facts were read, "
        "not run. Covered-by maps each row to Table 3 columns; legacy and inventory-only rows are marked. Llama Guard "
        "stays under sheet 3d and CyberSecEval is on sheet 3k.")
WIDTHS = [34, 40, 40, 40, 40, 36, 36, 40, 50, 44]
LEGACY = "— (legacy, not in Table 3)"
INV_ONLY = "— (inventory only, not in Table 3)"
COV = "Covered by Table 3 column"
BLOCKS = [  # (md section marker, bold block title or None, expected rows)
    ("## (a) Components and variants", None, 16),
    ("## (b) LlamaFirewall scanner catalogue", "LlamaFirewall scanner catalogue", 8),
    ("## (c) Roles, use cases and default scanner map", "Roles, use cases and default scanner map", 11),
    ("## (d) Code Shield language and analyzer matrix", "Code Shield language and analyzer matrix", 16),
    ("## (e) Integration and access paths", "Integration and access paths", 12),
    ("## (f) Licences, gating and terms", "Licences, gating and terms", 8),
    ("## (g) Published metrics and latency statements", "Published metrics and latency statements", 12),
    ("## (h) Adjacent and cross-reference items", "Adjacent and cross-reference items", 5),
]
COV_BLOCKS = (0, 1, 2, 4)  # blocks that carry the Covered-by column


def validate_markers(ctx):
    """Every Covered-by cell is either marker-only or a list of real headers; blocks without the column have none."""
    ws, hdr3 = ctx["ws"], ctx["hdr3"]
    bad, nm = [], 0
    for bi, (b, (h, rows)) in enumerate(zip(ctx["blocks"], ctx["pos"])):
        if bi not in COV_BLOCKS:
            if COV in b["hdr"]:
                bad.append((h, "unexpected Covered-by column"))
            continue
        cc = b["hdr"].index(COV) + 1
        for r in rows:
            parts = [v.strip() for v in str(ws.cell(row=r, column=cc).value).split(";")]
            ms = [v for v in parts if v in (LEGACY, INV_ONLY)]
            nm += len(ms)
            if ms and len(parts) > 1:
                bad.append((r, "mixed"))
            bad += [(r, v) for v in parts if v not in ms and v not in hdr3]
    return not bad, ["markers: %d marker cells; invalid or mixed values: %d %s" % (nm, len(bad), bad[:3])]


PANEL = dict(prefix=("Prompt Guard 2:", "LlamaFirewall:", "Code Shield:"), n=7, title="Coverage of Table 3 columns",
             first_hdr="Table 3 column (live link)",
             counts=[("Components covering it", 0), ("Scanners covering it", 1), ("Roles and use cases covering it", 2),
                     ("Access paths covering it", 4)],
             totals=[("Rows marked inventory only", [(bi, COV, "*inventory only*") for bi in COV_BLOCKS]),
                     ("Rows marked legacy", [(bi, COV, "*legacy*") for bi in COV_BLOCKS])])
CFG = dict(md=MD, sheet=S3J, title=TITLE, note=NOTE, after="3i. LionGuard Inventory", blocks=BLOCKS,
           widths=WIDTHS, center={}, covered=COV, markers=(LEGACY, INV_ONLY), order=BI.ORDER,
           validators=[validate_markers], panel=PANEL)


def parse_md(path=MD):
    return IS.parse_md(dict(CFG, md=path))


def add_sheet(wb, ws3=None):
    return IS.add_sheet(wb, CFG)


def verify(wb, xlsx=None):
    return IS.verify(wb, CFG, xlsx)
