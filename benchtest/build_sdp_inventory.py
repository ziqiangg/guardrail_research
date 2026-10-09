"""Sheet '3g. SDP Inventory' from drafts/sdp_inventory_final.md. Called by build_two_level.main().

Thin config over inventory_sheet.py (shared with 3d, 3e, 3f).
Public API: add_sheet(wb, ws3) -> ws ; verify(wb, xlsx=None)
Blocks: (a) components and methods (15), (b) infoType groups (24), (c) de-identification transformations (12),
(d) integration and access paths (13), (e) limits, quotas and pricing (16), (f) region and availability (7).
Covered-by is in (a)-(d) only. Markers: inventory only (R011) and legacy (Apigee row).
"""
import paths as P
import inventory_sheet as IS
import build_inventory as BI

MD = str(P.DRAFTS / "sdp_inventory_final.md")
S3G = "3g. SDP Inventory"
TITLE = "3g. Sensitive Data Protection Inventory (Google Cloud sensitive-data detection and de-identification)"
NOTE = ("Source: Google Cloud Sensitive Data Protection documentation (docs.cloud.google.com/sensitive-data-protection), "
        "the pricing, SLA and limits pages, the DLP API reference and the googleapis/google-cloud-python client "
        "(google-cloud-dlp-v3.40.0), read on 2026-10-09. SDP is a managed API service, not a guardrail product. "
        "Covered-by maps each row to a Table 3 column; legacy and inventory-only rows are marked.")
WIDTHS = [34, 44, 40, 36, 36, 40, 44, 46]
LEGACY = "— (legacy, not in Table 3)"
INV_ONLY = "— (inventory only, not in Table 3)"
COV = "Covered by Table 3 column"
BLOCKS = [  # (md section marker, bold block title or None, expected rows)
    ("## (a) Method and component catalogue", None, 15),
    ("## (b) InfoType group catalogue", "InfoType group catalogue", 24),
    ("## (c) De-identification transformation catalogue", "De-identification transformation catalogue", 12),
    ("## (d) Integration and access paths", "Integration and access paths", 13),
    ("## (e) Limits, quotas and pricing", "Limits, quotas and pricing", 16),
    ("## (f) Region and availability", "Region and availability", 7),
]
NCOV = 4  # blocks (a)-(d) carry the Covered-by column


def validate_markers(ctx):
    """Every Covered-by cell is either marker-only or a list of real headers (no marker mixed with headers)."""
    ws, hdr3 = ctx["ws"], ctx["hdr3"]
    bad, nm = [], 0
    for b, (h, rows) in zip(ctx["blocks"][:NCOV], ctx["pos"][:NCOV]):
        cc = b["hdr"].index(COV) + 1
        for r in rows:
            parts = [v.strip() for v in str(ws.cell(row=r, column=cc).value).split(";")]
            ms = [v for v in parts if v in (LEGACY, INV_ONLY)]
            nm += len(ms)
            if ms and len(parts) > 1:
                bad.append((r, "mixed"))
            bad += [(r, v) for v in parts if v not in ms and v not in hdr3]
    return not bad, ["markers: %d marker cells; invalid or mixed values: %d %s" % (nm, len(bad), bad[:3])]


PANEL = dict(prefix="Sensitive Data Protection:", n=6, title="Coverage of Table 3 columns",
             first_hdr="Table 3 column (live link)",
             counts=[("Methods and components covering it", 0), ("InfoType groups covering it", 1),
                     ("Transformations covering it", 2), ("Integration paths covering it", 3)],
             totals=[("Rows marked inventory only", [(bi, COV, "*inventory only*") for bi in range(NCOV)]),
                     ("Rows marked legacy", [(bi, COV, "*legacy*") for bi in range(NCOV)])])
CFG = dict(md=MD, sheet=S3G, title=TITLE, note=NOTE, after="3f. Presidio Inventory", blocks=BLOCKS,
           widths=WIDTHS, center={}, covered=COV, markers=(LEGACY, INV_ONLY), order=BI.ORDER,
           validators=[validate_markers], panel=PANEL)


def parse_md(path=MD):
    return IS.parse_md(dict(CFG, md=path))


def add_sheet(wb, ws3=None):
    return IS.add_sheet(wb, CFG)


def verify(wb, xlsx=None):
    return IS.verify(wb, CFG, xlsx)
