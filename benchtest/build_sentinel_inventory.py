"""Sheet '3e. GovTech Sentinel Inventory' from drafts/sentinel_inventory_final.md. Called by build_two_level.main().

Thin config over inventory_sheet.py (shared with 3d).
Public API: add_sheet(wb, ws3) -> ws ; verify(wb, xlsx=None)
Blocks: (a) model variants (16 cols, autofilter), (b) Sentinel guardrail catalogue, (c) LionGuard category crosswalk,
(d) access and integration paths. Covered-by header appears in (a) and (b) only.
"""
import re

import paths as P
import inventory_sheet as IS
import build_inventory as BI
from build_inventory import S3D, S3E

DIR = BI.DIR
MD = str(P.DRAFTS / "sentinel_inventory_final.md")
TITLE = "3e. GovTech Sentinel Inventory (Guardrails as a Service + GovTech models)"
NOTE = ("Source: aiguardian.gov.sg Sentinel docs, GovTech Responsible AI playbook, govtech Hugging Face repos and "
        "GovTech arXiv papers, with the refs pinned in each cell. Sentinel is in closed beta for Singapore public "
        "officers. Covered-by maps each variant or guardrail to a Table 3 column; LionGuard 1 is legacy and "
        "hallucination and prompt-guard are planned.")
WIDTHS = [30, 42, 46, 38, 36, 40, 36, 46, 40, 46, 36, 36, 46, 40, 40, 46]
LEGACY = "— (legacy, not in Table 3)"
PLANNED = "— (planned, not in Table 3)"
BLOCKS = [  # (md section marker, bold block title or None, expected rows)
    ("## (a) Model variant table", None, 9),
    ("## (b) Sentinel guardrail catalogue", "Sentinel guardrail catalogue (one row per guardrail ID)", 24),
    ("## (c) LionGuard category crosswalk", "LionGuard category crosswalk (harm concept by LionGuard version)", 12),
    ("## (d) Access and integration paths", "Access and integration paths", 9),
]
LG1_KEYS = {"binary", "hateful", "harassment", "public_harm", "self_harm", "sexual", "toxic", "violent"}
LG2_KEYS = {"binary", "hateful_l1", "hateful_l2", "insults", "sexual_l1", "sexual_l2", "physical_violence",
            "self_harm_l1", "self_harm_l2", "all_other_misconduct_l1", "all_other_misconduct_l2"}


def validate_catalogue(ctx):
    """(b): 24 unique guardrail IDs; Available rows map to real sheet-3 headers; Planned rows use the planned marker."""
    ws, b, (h, rows), hdr3 = ctx["ws"], ctx["blocks"][1], ctx["pos"][1], ctx["hdr3"]
    hd = b["hdr"]
    ic, istat, icov = hd.index("Guardrail ID"), hd.index("Status (Available/Planned)"), hd.index(
        "Covered by Table 3 column")
    ids = [ws.cell(row=r, column=ic + 1).value for r in rows]
    uniq = len(ids) == len(set(ids)) == 24
    nav = npl = 0
    bad = []
    for r in rows:
        st = ws.cell(row=r, column=istat + 1).value
        vals = [v.strip() for v in str(ws.cell(row=r, column=icov + 1).value).split(";")]
        if st.startswith("Available"):
            nav += 1
            bad += [(r, v) for v in vals if v not in hdr3 or v in (LEGACY, PLANNED)]
        elif st.startswith("Planned"):
            npl += 1
            bad += [(r, v) for v in vals if v != PLANNED]
        else:
            bad.append((r, "status? " + st[:20]))
    ok = uniq and not bad and nav + npl == 24
    return ok, ["catalogue: %d rows, IDs unique=%s | Available %d, Planned %d | Available rows with non-header or "
                "marker covered-by / Planned rows without planned marker: %d %s"
                % (len(rows), uniq, nav, npl, len(bad), bad[:3])]


def validate_crosswalk(ctx):
    """(c): all 8 LionGuard 1 keys and all 11 LionGuard 2 keys appear in the respective key columns."""
    ws, b, (h, rows) = ctx["ws"], ctx["blocks"][2], ctx["pos"][2]
    hd = b["hdr"]
    c1, c2 = hd.index("LionGuard 1 key") + 1, hd.index("LionGuard 2 output key") + 1

    def toks(col):
        s = set()
        for r in rows:
            s |= set(re.findall(r"[a-z][a-z0-9_]*", str(ws.cell(row=r, column=col).value)))
        return s
    t1, t2 = toks(c1), toks(c2)
    m1, m2 = sorted(LG1_KEYS - t1), sorted(LG2_KEYS - t2)
    return (not m1 and not m2 and len(rows) == 12), [
        "crosswalk rows: %d (12) | LG1 keys missing: %s (of 8) | LG2 keys missing: %s (of 11)" % (len(rows), m1, m2)]


def validate_partitions(ctx):
    """Panel totals partition the 24 guardrail IDs: Available+Planned, the three owners, the three Input/Output groups."""
    _, t = IS.python_panel(ctx["cfg"], ctx["ws"], ctx["ws3"], ctx["blocks"], ctx["pos"])
    g = lambda *keys: sum(v for k, v in t.items() if any(k.startswith(x) for x in keys))
    st, ow, io = (g("Guardrail IDs Available", "Guardrail IDs Planned"), g("Guardrail IDs owned"),
                  g("Guardrail IDs: Input", "Guardrail IDs: Output"))
    return st == ow == io == 24, ["panel partitions of the 24 IDs: status %d, owner %d, input/output %d (all 24)" % (st, ow, io)]


COV = "Covered by Table 3 column"
STAT, OWN, IO = "Status (Available/Planned)", "Owner (GovTech/AWS/Meta)", "Input/Output"
# Owner cells start with "GovTech" (16), "AWS" (7) or, for the Prompt-Guard row, "Listed under owner govtech ..."
# (the model is Meta's). Input/Output cells start with "Input/Output" (13), "Input " (8) or "Output" (3): first-stated value.
PANEL = dict(prefix="GovTech Sentinel:", n=7, title="Coverage of Table 3 columns",
             first_hdr="Table 3 column (live link)",
             counts=[("Model variants covering it", 0), ("Guardrail IDs covering it", 1)],
             totals=[("Guardrail IDs Available", [(1, STAT, "Available*")]),
                     ("Guardrail IDs Planned", [(1, STAT, "Planned*")]),
                     ("Guardrail IDs owned by GovTech", [(1, OWN, "GovTech*")]),
                     ("Guardrail IDs owned by AWS", [(1, OWN, "AWS*")]),
                     ("Guardrail IDs owned by Meta (model; listed under owner govtech)",
                      [(1, OWN, "Listed under owner govtech*")]),
                     ("Guardrail IDs: Input/Output (first stated)", [(1, IO, "Input/Output*")]),
                     ("Guardrail IDs: Input only (first stated)", [(1, IO, "Input *")]),
                     ("Guardrail IDs: Output only (first stated)", [(1, IO, "Output*")]),
                     ("Covered-by values marked planned", [(0, COV, "*planned*"), (1, COV, "*planned*")]),
                     ("Covered-by values marked legacy", [(0, COV, "*legacy*"), (1, COV, "*legacy*")])])
CFG = dict(md=MD, sheet=S3E, title=TITLE, note=NOTE, after=S3D, blocks=BLOCKS, widths=WIDTHS,
           center={}, covered="Covered by Table 3 column", markers=(LEGACY, PLANNED), order=BI.ORDER,
           validators=[validate_catalogue, validate_crosswalk, validate_partitions], panel=PANEL)


def parse_md(path=MD):
    return IS.parse_md(dict(CFG, md=path))


def add_sheet(wb, ws3=None):
    return IS.add_sheet(wb, CFG)


def verify(wb, xlsx=None):
    return IS.verify(wb, CFG, xlsx)
