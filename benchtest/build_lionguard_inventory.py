"""Sheet '3i. LionGuard Inventory' from drafts/lionguard_inventory_final.md. Called by build_two_level.main().

Thin config over inventory_sheet.py (shared with 3d to 3h).
Public API: add_sheet(wb, ws3) -> ws ; verify(wb, xlsx=None)
Blocks: (a) variant table (4), (b) output keys and taxonomy (11), (c) dependencies and access (8),
(d) artefacts and references (11), (e) cross-reference to Sentinel (4). 38 rows.
Covered-by is in all five blocks; the panel counts blocks (a)-(c) only, because rows of (d) and (e) are all
inventory only and the shared panel check needs a non-zero last count column. Markers: legacy (2 cells) and inventory only (15 cells); planned is not used.
"""
import paths as P
import inventory_sheet as IS
import build_inventory as BI

MD = str(P.DRAFTS / "lionguard_inventory_final.md")
S3I = "3i. LionGuard Inventory"
TITLE = "3i. LionGuard Inventory (GovTech localised content-moderation classifier, self-hosted models)"
NOTE = ("Source: GovTech LionGuard model cards, datasets, playbook page, papers and blog posts on the govtech Hugging Face "
        "organisation and the GovTech sites, read on 2026-10-09. LionGuard is published as classifier heads that need a "
        "separate embedding model. Covered-by maps each row to a Table 3 column; legacy and inventory-only rows are "
        "marked. The hosted Sentinel API stays under sheet 3e.")
WIDTHS = [34, 40, 40, 40, 36, 24, 30, 30, 44, 30, 40, 50]
LEGACY = "— (legacy, not in Table 3)"
INV_ONLY = "— (inventory only, not in Table 3)"
COV = "Covered by Table 3 column"
BLOCKS = [  # (md section marker, bold block title or None, expected rows)
    ("## (a) Variant table", None, 4),
    ("## (b) Output keys and taxonomy", "Output keys and taxonomy", 11),
    ("## (c) Dependencies and access", "Dependencies and access", 8),
    ("## (d) Artefacts and references", "Artefacts and references", 11),
    ("## (e) Cross-reference to Sentinel", "Cross-reference to Sentinel", 4),
]
NCOV = 5  # all blocks carry the Covered-by column


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


PANEL = dict(prefix="LionGuard:", n=1, title="Coverage of Table 3 columns",
             first_hdr="Table 3 column (live link)",
             counts=[("Variants covering it", 0), ("Output keys covering it", 1), ("Dependencies covering it", 2)],
             totals=[("Rows marked inventory only", [(bi, COV, "*inventory only*") for bi in range(NCOV)]),
                     ("Rows marked legacy", [(bi, COV, "*legacy*") for bi in range(NCOV)])])
CFG = dict(md=MD, sheet=S3I, title=TITLE, note=NOTE, after="3h. Model Armor Inventory", blocks=BLOCKS,
           widths=WIDTHS, center={}, covered=COV, markers=(LEGACY, INV_ONLY), order=BI.ORDER,
           validators=[validate_markers], panel=PANEL)


def parse_md(path=MD):
    return IS.parse_md(dict(CFG, md=path))


def add_sheet(wb, ws3=None):
    return IS.add_sheet(wb, CFG)


def verify(wb, xlsx=None):
    return IS.verify(wb, CFG, xlsx)
