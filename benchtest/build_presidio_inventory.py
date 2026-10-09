"""Sheet '3f. Presidio Inventory' from drafts/presidio_inventory_final.md. Called by build_two_level.main().

Thin config over inventory_sheet.py (shared with 3d, 3e).
Public API: add_sheet(wb, ws3) -> ws ; verify(wb, xlsx=None)
Blocks: (a) components and variants (14), (b) recognizer catalogue (31 families), (c) anonymizer operators (10),
(d) integration paths (14). Every block has a Covered-by column. Markers: legacy and inventory only (R011).
"""
import paths as P
import inventory_sheet as IS
import build_inventory as BI

MD = str(P.DRAFTS / "presidio_inventory_final.md")
S3F = "3f. Presidio Inventory"
TITLE = "3f. Presidio Inventory (PII detection and de-identification toolkit)"
NOTE = ("Source: Presidio documentation (microsoft.github.io/presidio), the data-privacy-stack/presidio and "
        "data-privacy-stack/presidio-research repositories (pinned at 2.2.364 and 0.3.2), and the Microsoft Learn "
        "pages for the Azure services Presidio can call. Presidio is a library and set of services, not a "
        "guardrail product. Covered-by maps each row to a Table 3 column; legacy and inventory-only rows are marked.")
WIDTHS = [34, 44, 48, 36, 36, 40, 44, 46]
LEGACY = "— (legacy, not in Table 3)"
INV_ONLY = "— (inventory only, not in Table 3)"
COV = "Covered by Table 3 column"
BLOCKS = [  # (md section marker, bold block title or None, expected rows)
    ("## (a) Components and variants", None, 14),
    ("## (b) Recognizer catalogue", "Recognizer catalogue (grouped by family)", 31),
    ("## (c) Anonymizer operators", "Anonymizer operators", 10),
    ("## (d) Integration paths", "Integration paths", 14),
]


def validate_markers(ctx):
    """Every Covered-by cell is either marker-only or a list of real headers (no marker mixed with headers)."""
    ws, hdr3 = ctx["ws"], ctx["hdr3"]
    bad, nm = [], 0
    for b, (h, rows) in zip(ctx["blocks"], ctx["pos"]):
        cc = b["hdr"].index(COV) + 1
        for r in rows:
            parts = [v.strip() for v in str(ws.cell(row=r, column=cc).value).split(";")]
            ms = [v for v in parts if v in (LEGACY, INV_ONLY)]
            nm += len(ms)
            if ms and len(parts) > 1:
                bad.append((r, "mixed"))
            bad += [(r, v) for v in parts if v not in ms and v not in hdr3]
    return not bad, ["markers: %d marker cells; invalid or mixed values: %d %s" % (nm, len(bad), bad[:3])]


PANEL = dict(prefix="Presidio:", n=6, title="Coverage of Table 3 columns", first_hdr="Table 3 column (live link)",
             counts=[("Recognizer families covering it", 1), ("Operators covering it", 2),
                     ("Integration paths covering it", 3), ("Components covering it", 0)],
             totals=[("Rows marked inventory only", [(bi, COV, "*inventory only*") for bi in range(4)]),
                     ("Rows marked legacy", [(bi, COV, "*legacy*") for bi in range(4)])])
CFG = dict(md=MD, sheet=S3F, title=TITLE, note=NOTE, after="3e. GovTech Sentinel Inventory", blocks=BLOCKS,
           widths=WIDTHS, center={}, covered=COV, markers=(LEGACY, INV_ONLY), order=BI.ORDER,
           validators=[validate_markers], panel=PANEL)


def parse_md(path=MD):
    return IS.parse_md(dict(CFG, md=path))


def add_sheet(wb, ws3=None):
    return IS.add_sheet(wb, CFG)


def verify(wb, xlsx=None):
    return IS.verify(wb, CFG, xlsx)
