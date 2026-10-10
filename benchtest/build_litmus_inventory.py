"""Sheet '3m. Litmus Inventory' from drafts/litmus_inventory_final.md. Called by build_two_level.main().

Thin config over inventory_sheet.py (shared with 3d to 3l).
Public API: add_sheet(wb, ws3=None) -> ws ; verify(wb, xlsx=None)
Blocks: (a) access paths (4), (b) test suites (5), (c) integration parameters (6) = 15 rows. Covered-by is in all three
blocks and every cell carries the single marker 'inventory only' (R011): Litmus is an evaluation tool with NO Table 3
columns (R003, R038), so the panel has zero Table 3 rows (inventory_sheet panel with n=0): live row counts per block
and the number of inventory-only rows.
3m follows 3l (Cloak Inventory); the eval sheet 3n follows 3m; sheet 4 stays last (R003).
"""
import paths as P
import inventory_sheet as IS
import build_inventory as BI

MD = str(P.DRAFTS / "litmus_inventory_final.md")
S3M = "3m. Litmus Inventory"
TITLE = "3m. GovTech Litmus Inventory (hosted AI testing service, evaluation tool)"
NOTE = ("Source: GovTech AI Guardian docs pages, the GovTech developer portal Litmus pages and the govtech-responsibleai "
        "playbook, read on 2026-10-10. Litmus is a hosted service with no published release; nothing was signed in to or "
        "called. It is an evaluation tool, so it has no Table 3 columns: every Covered-by cell carries the "
        "inventory-only marker. Tests, published results and reuse are on sheet 3n.")
WIDTHS = [32, 46, 36, 40, 36, 44, 36, 44]
INV_ONLY = "— (inventory only, not in Table 3)"
COV = "Covered by Table 3 column"
BLOCKS = [  # (md section marker, bold block title or None, expected rows)
    ("## (a) Access paths", None, 4),
    ("## (b) Test suites", "Test suites", 5),
    ("## (c) Integration parameters", "Integration parameters", 6),
]


def validate_markers(ctx):
    """Every Covered-by cell is exactly the inventory-only marker (no Table 3 headers exist to cite)."""
    ws = ctx["ws"]
    bad = []
    for b, (h, rows) in zip(ctx["blocks"], ctx["pos"]):
        cc = b["hdr"].index(COV) + 1
        bad += [r for r in rows if str(ws.cell(row=r, column=cc).value).strip() != INV_ONLY]
    return not bad, ["markers: every Covered-by cell is the inventory-only marker; violations: %d %s"
                     % (len(bad), bad[:3])]


PANEL = dict(prefix=None, n=0, title="Coverage and size of this inventory (no Table 3 columns)",
             first_hdr="Block", counts=[("Rows", None)],
             block_rows=[("Access paths (a)", 0), ("Test suites (b)", 1), ("Integration parameters (c)", 2)],
             totals=[("Rows marked inventory only", [(bi, COV, "*inventory only*") for bi in range(3)])])
CFG = dict(md=MD, sheet=S3M, title=TITLE, note=NOTE, after="3l. Cloak Inventory", blocks=BLOCKS,
           widths=WIDTHS, center={}, covered=COV, markers=(INV_ONLY,), order=BI.ORDER,
           validators=[validate_markers], panel=PANEL)


def parse_md(path=MD):
    return IS.parse_md(dict(CFG, md=path))


def add_sheet(wb, ws3=None):
    return IS.add_sheet(wb, CFG)


def verify(wb, xlsx=None):
    return IS.verify(wb, CFG, xlsx)
