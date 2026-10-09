"""Sheet '3h. Model Armor Inventory' from drafts/modelarmor_inventory_final.md. Called by build_two_level.main().

Thin config over inventory_sheet.py (shared with 3d to 3g).
Public API: add_sheet(wb, ws3) -> ws ; verify(wb, xlsx=None)
Blocks: (a) filters and detectors (10), (b) integration paths (15), (c) template and floor-setting parameters (16),
(d) locations and feature availability (20), (e) quotas, limits and pricing (16).
Covered-by is in (a) and (b) only. Markers: legacy, planned and inventory only (R011); the md uses inventory only (8 rows).
"""
import paths as P
import inventory_sheet as IS
import build_inventory as BI

MD = str(P.DRAFTS / "modelarmor_inventory_final.md")
S3H = "3h. Model Armor Inventory"
TITLE = "3h. Model Armor Inventory (Google Cloud prompt and response screening service)"
NOTE = ("Source: Google Cloud Model Armor documentation (docs.cloud.google.com/model-armor), the pricing, quotas and "
        "release-notes pages, the REST reference and the googleapis/google-cloud-go client (modelarmor/v1.3.0), read on "
        "2026-10-09. Model Armor is a managed API service. Covered-by maps each row to a Table 3 column; "
        "inventory-only rows are marked. Preview features are tested with synthetic data only (user rule, 2026-10-09).")
WIDTHS = [34, 44, 40, 36, 36, 40, 44, 40, 40, 50]
LEGACY = "— (legacy, not in Table 3)"
PLANNED = "— (planned, not in Table 3)"
INV_ONLY = "— (inventory only, not in Table 3)"
COV = "Covered by Table 3 column"
BLOCKS = [  # (md section marker, bold block title or None, expected rows)
    ("## (a) Filters and detectors", None, 10),
    ("## (b) Integration paths", "Integration paths", 15),
    ("## (c) Template and floor-setting parameters", "Template and floor-setting parameters", 16),
    ("## (d) Locations and feature availability", "Locations and feature availability", 20),
    ("## (e) Quotas, limits and pricing", "Quotas, limits and pricing", 16),
]
NCOV = 2  # blocks (a)-(b) carry the Covered-by column


def validate_markers(ctx):
    """Every Covered-by cell is either marker-only or a list of real headers (no marker mixed with headers)."""
    ws, hdr3 = ctx["ws"], ctx["hdr3"]
    bad, nm = [], 0
    for b, (h, rows) in zip(ctx["blocks"][:NCOV], ctx["pos"][:NCOV]):
        cc = b["hdr"].index(COV) + 1
        for r in rows:
            parts = [v.strip() for v in str(ws.cell(row=r, column=cc).value).split(";")]
            ms = [v for v in parts if v in (LEGACY, PLANNED, INV_ONLY)]
            nm += len(ms)
            if ms and len(parts) > 1:
                bad.append((r, "mixed"))
            bad += [(r, v) for v in parts if v not in ms and v not in hdr3]
    return not bad, ["markers: %d marker cells; invalid or mixed values: %d %s" % (nm, len(bad), bad[:3])]


PANEL = dict(prefix="Model Armor:", n=10, title="Coverage of Table 3 columns",
             first_hdr="Table 3 column (live link)",
             counts=[("Filters and detectors covering it", 0), ("Integration paths covering it", 1)],
             totals=[("Rows marked inventory only", [(bi, COV, "*inventory only*") for bi in range(NCOV)]),
                     ("Rows marked legacy", [(bi, COV, "*legacy*") for bi in range(NCOV)]),
                     ("Rows marked planned", [(bi, COV, "*planned*") for bi in range(NCOV)])])
CFG = dict(md=MD, sheet=S3H, title=TITLE, note=NOTE, after="3g. SDP Inventory", blocks=BLOCKS,
           widths=WIDTHS, center={}, covered=COV, markers=(LEGACY, PLANNED, INV_ONLY), order=BI.ORDER,
           validators=[validate_markers], panel=PANEL)


def parse_md(path=MD):
    return IS.parse_md(dict(CFG, md=path))


def add_sheet(wb, ws3=None):
    return IS.add_sheet(wb, CFG)


def verify(wb, xlsx=None):
    return IS.verify(wb, CFG, xlsx)
