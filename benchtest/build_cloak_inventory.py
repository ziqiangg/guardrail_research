"""Sheet '3l. Cloak Inventory' from drafts/cloak_inventory_final.md. Called by build_two_level.main().

Thin config over inventory_sheet.py (shared with 3d to 3j).
Public API: add_sheet(wb, ws3) -> ws ; verify(wb, xlsx=None)
Blocks: (a) variants and modules (10), (b) access and integration paths (8), (c) free-text entity types (26),
(d) anonymisation techniques (9), (e) limits and terms (28), (f) open-source components named in Cloak's own pages (4).
85 rows. Covered-by is in all six blocks. Markers: legacy (1 cell), inventory only (7 cells) and planned (1 cell: the
Sentinel integration row, R011); the planned marker is amber like the other two. The panel counts all six blocks; its
last count column (access paths) is non-zero for all three columns, as the shared panel check needs.
3l follows 3k (CyberSecEval Eval Tooling) and precedes sheet 4 (R003).
"""
import paths as P
import inventory_sheet as IS
import build_inventory as BI

MD = str(P.DRAFTS / "cloak_inventory_final.md")
S3L = "3l. Cloak Inventory"
TITLE = "3l. Cloak Inventory (GovTech Cloak, closed hosted data-anonymisation service)"
NOTE = ("Source: GovTech Cloak Guide pages, the Cloak product site, the Developer Portal Cloak pages, the Terms of Use "
        "and Privacy Statement PDFs and mirage.gov.sg, read on 2026-10-10. Cloak is a closed government service with no "
        "public repository; the API Guide and OpenAPI pages sit behind a login, so their content is not disclosed. "
        "Covered-by maps each row to Table 3 columns; legacy, inventory-only and planned rows are marked.")
WIDTHS = [34, 46, 36, 40, 40, 36, 44, 44]
LEGACY = "— (legacy, not in Table 3)"
INV_ONLY = "— (inventory only, not in Table 3)"
PLANNED = "— (planned, not in Table 3)"
COV = "Covered by Table 3 column"
BLOCKS = [  # (md section marker, bold block title or None, expected rows)
    ("## (a) Variants and modules", None, 10),
    ("## (b) Access and integration paths", "Access and integration paths", 8),
    ("## (c) Free-text entity types", "Free-text entity types", 26),
    ("## (d) Anonymisation techniques", "Anonymisation techniques", 9),
    ("## (e) Limits and terms", "Limits and terms", 28),
    ("## (f) Open-source components", "Open-source components named in Cloak's own pages (not GovTech docs)", 4),
]
NCOV = 6  # all blocks carry the Covered-by column


def validate_markers(ctx):
    """Every Covered-by cell is either marker-only or a list of real headers (no marker mixed with headers)."""
    ws, hdr3 = ctx["ws"], ctx["hdr3"]
    bad, nm = [], 0
    for b, (h, rows) in zip(ctx["blocks"], ctx["pos"]):
        cc = b["hdr"].index(COV) + 1
        for r in rows:
            parts = [v.strip() for v in str(ws.cell(row=r, column=cc).value).split(";")]
            ms = [v for v in parts if v in (LEGACY, INV_ONLY, PLANNED)]
            nm += len(ms)
            if ms and len(parts) > 1:
                bad.append((r, "mixed"))
            bad += [(r, v) for v in parts if v not in ms and v not in hdr3]
    return not bad, ["markers: %d marker cells; invalid or mixed values: %d %s" % (nm, len(bad), bad[:3])]


PANEL = dict(prefix="Cloak:", n=3, title="Coverage of Table 3 columns",
             first_hdr="Table 3 column (live link)",
             counts=[("Modules covering it", 0), ("Entity types covering it", 2), ("Techniques covering it", 3),
                     ("Limits and terms covering it", 4), ("Components covering it", 5),
                     ("Access paths covering it", 1)],
             totals=[("Rows marked inventory only", [(bi, COV, "*inventory only*") for bi in range(NCOV)]),
                     ("Rows marked legacy", [(bi, COV, "*legacy*") for bi in range(NCOV)]),
                     ("Rows marked planned", [(bi, COV, "*planned*") for bi in range(NCOV)])])
CFG = dict(md=MD, sheet=S3L, title=TITLE, note=NOTE, after="3k. CyberSecEval Eval Tooling", blocks=BLOCKS,
           widths=WIDTHS, center={}, covered=COV, markers=(LEGACY, INV_ONLY, PLANNED), order=BI.ORDER,
           validators=[validate_markers], panel=PANEL)


def parse_md(path=MD):
    return IS.parse_md(dict(CFG, md=path))


def add_sheet(wb, ws3=None):
    return IS.add_sheet(wb, CFG)


def verify(wb, xlsx=None):
    return IS.verify(wb, CFG, xlsx)
