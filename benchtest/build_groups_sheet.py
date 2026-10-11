"""Sheet '4. Candidate Comparison Groups' from drafts/groups_v3.md Section A (bulleted rich text), section bands,
plus a formula coverage panel below the table.
Called by build_two_level.main().  The sheet is rebuilt in place (title A1, header row 3, widths, freeze are kept).

Public API: add_sheet(wb) -> ws ; verify(wb, xlsx=None)
"""
import re

from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.cell.text import InlineFont
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

import paths as P
import build_inventory as BI
import inventory_sheet as IS
from build_eval_sheet import split_row

DIR = BI.DIR
MD = str(P.DRAFTS / "groups_v3.md")
S3, S4 = BI.S3, BI.S4
R1 = 4  # first row after the header (the first band)
NMULTI = 14  # C1-C14 are comparison groups (2+ products); C15-C34 are single-product
NROWS = 34
NFN = 62
BAND1, BAND2 = R1, R1 + NMULTI + 1  # band rows 4 and 19
BAND_TXT = {BAND1: "Comparison groups (2+ products)", BAND2: "Single-product functions (no comparator yet)"}
LAST_ROW = 39
WIDTHS = [28, 40] + [42] * 6
BANDFILL = PatternFill("solid", fgColor="D9D9D9")
SGREY, RGREY = "595959", "808080"
FIRST_FN_COL, LAST_FN_COL = 5, 66  # sheet 3 function columns E..BN
SHADE = PatternFill("solid", fgColor="DCE6F2")
ALIGN = Alignment(wrap_text=True, vertical="top")
PANEL_TITLE = "Coverage of sheet 3 functions"
PANEL_HDR = ["Sheet 3 column", "Function (live link)", "Groups listing it"]
# (label, header-prefix substring counted in the group Function column B).  Prompt Guard 2, LlamaFirewall and
# Code Shield count as one product (Meta Purple Llama).
PRODUCT_TOTALS = [
    ("Groups including NeMo Guardrails", ["NeMo Guardrails:"]),
    ("Groups including Llama Guard", ["Llama Guard:"]),
    ("Groups including GovTech Sentinel", ["GovTech Sentinel:"]),
    ("Groups including Presidio", ["Presidio:"]),
    ("Groups including Sensitive Data Protection", ["Sensitive Data Protection:"]),
    ("Groups including Model Armor", ["Model Armor:"]),
    ("Groups including LionGuard", ["LionGuard:"]),
    ("Groups including Purple Llama", ["Prompt Guard 2:", "LlamaFirewall:", "Code Shield:"]),
    ("Groups including Cloak", ["Cloak:"]),
    ("Groups including Amazon Bedrock", ["Amazon Bedrock"]),
]


def _plain_pat(pats):
    return pats


def _formula_for(pats):
    """COUNTIF for one prefix; for several prefixes a sum of per-row OR (SUMPRODUCT, ISNUMBER(SEARCH))."""
    if len(pats) == 1:
        return '=COUNTIF({B},"*%s*")' % pats[0]
    terms = "+".join('ISNUMBER(SEARCH("%s",{B}))' % q for q in pats)
    return "=SUMPRODUCT(--((%s)>0))" % terms


TOTALS = [  # (label, formula template; {B}=group Function range, {C}=panel count range, {H}=last column range)
    ("Functions in no group", '=COUNTIF({C},0)'),
    ("Functions in more than one group", '=COUNTIF({C},">1")'),
] + [(lab, _formula_for(p)) for lab, p in PRODUCT_TOTALS] + [
    ("Single-product rows", '=COUNTIF({H},"*Single-product:*")'),
]


def group_row(i):
    """Sheet row of group index i (0 = C1)."""
    return R1 + 1 + i if i < NMULTI else R1 + 2 + i


def parse_groups(path=MD):
    """Section A table -> (header, rows); cell text stripped; column B one function per line, columns C-H bullet
    lines joined with newlines (the plain text shown in the cell)."""
    return _parse(path)[:2]


def parse_lines(path=MD):
    """(header, rows, lines): lines[row][col-1] = list of lines of columns C-H (None for A, B)."""
    return _parse(path)


def _parse(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    i = next(k for k, l in enumerate(lines) if l.startswith("## A."))
    j = next(k for k in range(i + 1, len(lines)) if lines[k].startswith("|"))
    tbl = []
    while j < len(lines) and lines[j].startswith("|"):
        tbl.append(split_row(lines[j]))
        j += 1
    hdr, rows = tbl[0], tbl[2:]
    assert all(set(c) <= set("-: ") for c in tbl[1]), tbl[1]
    assert len(hdr) == 8 and len(rows) == NROWS, (len(hdr), len(rows))
    out, lns = [], []
    for k, r in enumerate(rows):
        assert len(r) == 8, (len(r), r[0][:30])
        r = [c.strip() for c in r]
        r[1] = "\n".join(p.strip() for p in r[1].split("; "))
        cl = [None, None]
        for c in range(2, 8):
            ls = [x.strip() for x in r[c].split("<br>")]
            for n, x in enumerate(ls):
                if x.startswith("Refs: "):
                    assert n == len(ls) - 1 and len(x) > 6, (r[0][:30], c)
                else:
                    assert x.startswith("\u2022 ") and len(x) > 2, (r[0][:30], c, x[:30])
            cl.append(ls)
            r[c] = "\n".join(ls)
        for c in r:
            assert "**" not in c and "`" not in c and c, r[0][:30]
        single = r[7].startswith("\u2022 Single-product:")
        assert single == (k >= NMULTI), (k, r[0][:30])
        assert r[0].startswith(f"C{k + 1} "), r[0][:20]
        out.append(r)
        lns.append(cl)
    return [h.strip() for h in hdr], out, lns


def fn_headers(ws3):
    """Sheet-3 row-3 headers E..AG with the COUNTIF safety guards."""
    hd = [ws3.cell(row=3, column=c).value for c in range(FIRST_FN_COL, LAST_FN_COL + 1)]
    assert all(isinstance(h, str) and h for h in hd) and len(hd) == NFN, hd
    for h in hd:
        assert not any(ch in h for ch in "*?~") and len(h) + 2 <= 255, h
        assert not any(h != o and h.lower() in o.lower() for o in hd), ("header is a substring of another", h)
    return hd


def panel_cells(ws3, nrows=NROWS):
    """{(row, col): value} of the coverage panel, and its layout (below the table; ranges include the band rows)."""
    last = LAST_ROW
    B, H = f"$B${R1 + 1}:$B${last}", f"$H${R1 + 1}:$H${last}"
    title = last + 2
    first = title + 2
    cells = {(title, 1): PANEL_TITLE}
    for k, h in enumerate(PANEL_HDR):
        cells[(title + 1, 1 + k)] = h
    hd = fn_headers(ws3)
    for i, h in enumerate(hd):
        c = FIRST_FN_COL + i
        r = first + i
        cells[(r, 1)] = get_column_letter(c)
        cells[(r, 2)] = f"='{S3}'!{get_column_letter(c)}3"
        cells[(r, 3)] = f'=COUNTIF({B},"*"&$B{r}&"*")'
    lastfn = first + len(hd) - 1
    C = f"$C${first}:$C${lastfn}"
    tot = {}
    for k, (lab, f) in enumerate(TOTALS):
        r = lastfn + 1 + k
        cells[(r, 1)] = lab
        cells[(r, 3)] = f.format(B=B, C=C, H=H)
        tot[lab] = r
    return cells, dict(last=last, title=title, first=first, lastfn=lastfn, tot=tot, hd=hd)


def python_panel(rows, hd):
    """Python mirror of the panel: per-function group counts and the totals (COUNTIF semantics: case-insensitive)."""
    B = [r[1].lower() for r in rows]
    cnt = [sum(h.lower() in b for b in B) for h in hd]
    grp = lambda pats: sum(any(q.lower() in b for q in pats) for b in B)
    tot = {"Functions in no group": cnt.count(0), "Functions in more than one group": sum(c > 1 for c in cnt)}
    for lab, pats in PRODUCT_TOTALS:
        tot[lab] = grp(pats)
    tot["Single-product rows"] = sum("single-product:" in r[7].lower() for r in rows)
    return cnt, tot


def check_letters(rows, hd):
    """Every function line is '<sheet-3 column letter>: <that column's header>...'; returns {letter: groups}."""
    by = {}
    for gi, r in enumerate(rows):
        for line in r[1].split("\n"):
            m = re.match(r"^([A-Z]{1,2}): ", line)
            assert m, line
            L = m.group(1)
            c = next(i for i in range(1, 80) if get_column_letter(i) == L)
            assert FIRST_FN_COL <= c <= LAST_FN_COL, line
            assert line.startswith(f"{L}: {hd[c - FIRST_FN_COL]}"), ("line does not carry its column header", line)
            by.setdefault(L, set()).add(gi)
    return by


def rich_cell(lines, color):
    """Rich text: bullet lines Arial 10 (colour), a trailing 'Refs: ...' line Arial 8 grey. One run per line, the
    newline kept at the end of the preceding run (whitespace-preserving; no empty runs; every run has rPr)."""
    blocks = []
    for n, ln in enumerate(lines):
        txt = ln + ("\n" if n < len(lines) - 1 else "")
        if ln.startswith("Refs: "):
            f = InlineFont(rFont="Arial", sz=8, color=RGREY)
        elif color:
            f = InlineFont(rFont="Arial", sz=10, color=color)
        else:
            f = InlineFont(rFont="Arial", sz=10)
        blocks.append(TextBlock(f, txt))
    return CellRichText(*blocks)


def add_sheet(wb):
    hdr, rows, lns = parse_lines()
    ws = wb[S4]
    assert wb.sheetnames[-1] == S4
    assert [ws.cell(row=3, column=c).value for c in range(1, 9)] == hdr, "sheet 4 header differs from groups_v3.md"
    for m in list(ws.merged_cells.ranges):  # idempotent: drop a previous panel's merges, then all rows from 4
        ws.unmerge_cells(str(m))
    ws.delete_rows(R1, max(ws.max_row - R1 + 1, 1))
    for br, txt in BAND_TXT.items():
        for c in range(1, 9):
            x = ws.cell(row=br, column=c, value=txt if c == 1 else None)
            x.font, x.alignment, x.border, x.fill = Font(name="Arial", size=10, bold=True), ALIGN, BI.BORDER, BANDFILL
    for i, row in enumerate(rows):
        r = group_row(i)
        color = SGREY if i >= NMULTI else None
        k = i if i < NMULTI else i - NMULTI  # alternate within each section
        for c, v in enumerate(row, 1):
            if c >= 3:
                v = rich_cell(lns[i][c - 1], color)
            x = ws.cell(row=r, column=c, value=v)
            x.font = Font(name="Arial", size=10, bold=(c == 1), color=color)
            x.alignment, x.border = ALIGN, BI.BORDER
            if k % 2 == 0:
                x.fill = SHADE
    for c, w in enumerate(WIDTHS, 1):
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.auto_filter.ref = f"A3:H{LAST_ROW}"
    ws3 = wb[S3]
    hd = fn_headers(ws3)
    check_letters(rows, hd)
    cells, L = panel_cells(ws3, len(rows))
    assert L["last"] == group_row(len(rows) - 1) == LAST_ROW
    IS.panel_title(ws, L["title"], PANEL_TITLE, 3)
    for k, h in enumerate(PANEL_HDR):
        BI._pcell(ws, L["title"] + 1, 1 + k, h, hdr=True)
    for (r, c), v in cells.items():
        if r < L["first"]:
            continue
        BI._pcell(ws, r, c, v, num=(c == 3), bold=(r in L["tot"].values() and c == 1))
    for r in L["tot"].values():
        BI._pcell(ws, r, 2, None)
    return ws


# ------------------------------------------------------------------ verification
def _snap_row(ws, r):
    return [(c.value, c.font.name, c.font.sz, c.font.b, c.font.i, c.fill.fill_type, c.fill.fgColor.rgb,
             c.alignment.wrap_text, c.alignment.vertical, c.border.left.style, c.border.left.color.rgb)
            for c in ws[r][:8]]


def _plain(v):
    if isinstance(v, CellRichText):
        return "".join(b.text if isinstance(b, TextBlock) else str(b) for b in v)
    return "" if v is None else str(v)


def _blocks(v):
    return list(v) if isinstance(v, CellRichText) else [v]


def _rgb(c):
    return None if c is None or c.rgb is None or not isinstance(c.rgb, str) else c.rgb[-6:]


def verify(wb, xlsx=None, bak=None):
    """Checks sheet 4 against groups_v3.md (wb must be loaded with rich_text=True); if bak (the v7 xlsx path) is given
    also title/header row identical to v7."""
    from openpyxl import load_workbook
    print("\n=== build_groups_sheet verification (sheet 4) ===")
    ok = True

    def chk(name, cond, extra=""):
        nonlocal ok
        ok = ok and bool(cond)
        print("  %-4s %s %s" % ("OK" if cond else "FAIL", name, extra))
    ws, ws3 = wb[S4], wb[S3]
    hdr, rows, lns = parse_lines()
    chk("sheet 4 is the last sheet", wb.sheetnames[-1] == S4, str(wb.sheetnames))
    chk("A1 title", ws["A1"].value == "4. Forming Candidate Comparison Groups" and ws["A1"].font.b)
    chk("row 3 header equals groups_v3.md header", [ws.cell(row=3, column=c).value for c in range(1, 9)] == hdr)
    chk("header style (Arial 10 bold white, fill 4472C4)",
        all(ws.cell(row=3, column=c).font.name == "Arial" and ws.cell(row=3, column=c).font.b
            and ws.cell(row=3, column=c).fill.fgColor.rgb.endswith("4472C4") for c in range(1, 9)))
    w = [ws.column_dimensions[get_column_letter(i)].width for i in range(1, 9)]
    chk("widths A=28, B=40, C-H=42", w == [28, 40] + [42] * 6, str(w))
    chk("freeze B4", ws.freeze_panes == "B4")
    chk("autofilter A3:H39", ws.auto_filter.ref == f"A3:H{LAST_ROW}", str(ws.auto_filter.ref))
    grows = [group_row(i) for i in range(NROWS)]
    chk("group rows: C1-C14 = rows 5-18, C15-C34 = rows 20-39", grows == list(range(5, 19)) + list(range(20, 40)))
    chk("last table row is 39", grows[-1] == 39 == LAST_ROW)
    # bands
    for br, txt in BAND_TXT.items():
        cs = ws[br][:8]
        good = (cs[0].value == txt and all(c.value is None for c in cs[1:]) and
                all(c.font.name == "Arial" and c.font.sz == 10 and c.font.b and c.fill.fill_type == "solid"
                    and c.fill.fgColor.rgb.endswith("D9D9D9") and c.border.left.style == "thin"
                    and c.border.left.color.rgb.endswith("8EA9DB") for c in cs))
        chk(f"band row {br}: '{txt}', bold Arial 10, fill D9D9D9 across A:H, table borders", good)
    chk("no merged cells in the table area (bands unmerged)", not [str(m) for m in ws.merged_cells.ranges
                                                                      if m.min_row < 30])
    # content
    mism = 0
    for i, row in enumerate(rows):
        for c, v in enumerate(row, 1):
            mism += _plain(ws.cell(row=grows[i], column=c).value) != v
    chk("rows 5-18 and 20-39: plain text of all 34 x 8 cells equals groups_v3.md Section A (newline joins)",
        mism == 0 and len(rows) == NROWS, f"({mism} mismatches)")
    # fonts / fills / style
    bad_font, bad_fill, bad_sty, nrich, nrefs = [], [], [], 0, 0
    for i in range(NROWS):
        single = i >= NMULTI
        col = SGREY if single else None
        k = i if not single else i - NMULTI
        for c in range(1, 9):
            x = ws.cell(row=grows[i], column=c)
            fcol = _rgb(x.font.color)
            if x.font.name != "Arial" or x.font.sz != 10 or bool(x.font.b) != (c == 1) or fcol != col:
                bad_font.append(x.coordinate)
            if not (x.fill.fill_type == "solid" and str(x.fill.fgColor.rgb).endswith("DCE6F2")) == (k % 2 == 0) \
                    or (k % 2 == 1 and x.fill.fill_type is not None):
                bad_fill.append(x.coordinate)
            if not (x.alignment.wrap_text and x.alignment.vertical == "top" and x.border.left.style == "thin"
                    and x.border.left.color.rgb.endswith("8EA9DB")):
                bad_sty.append(x.coordinate)
            if c >= 3:
                bl = _blocks(x.value)
                nrich += 1
                lines = lns[i][c - 1]
                if not (len(bl) == len(lines) and all(isinstance(b, TextBlock) for b in bl)):
                    bad_font.append(x.coordinate + ":runs")
                    continue
                for n, (b, ln) in enumerate(zip(bl, lines)):
                    f = b.font
                    isref = ln.startswith("Refs: ")
                    nrefs += isref
                    want_sz, want_col = (8, RGREY) if isref else (10, col)
                    if f.rFont != "Arial" or f.sz != want_sz or _rgb(f.color) != want_col or f.b:
                        bad_font.append(x.coordinate + f":run{n}")
            elif c == 2 and _plain(x.value).count("\n") != rows[i][1].count("\n"):
                bad_font.append(x.coordinate + ":B")
    chk("fonts: A bold, text runs Arial 10 (black rows 5-18, 595959 rows 20-39), 'Refs:' runs Arial 8 808080",
        not bad_font, f"({nrich} rich cells, {nrefs} refs runs; bad: {bad_font[:4]})")
    chk("fills: DCE6F2 alternating within each section (rows 5,7,... / 20,22,...), none on the others", not bad_fill,
        str(bad_fill[:4]))
    chk("cells: wrap, top, thin 8EA9DB borders", not bad_sty, str(bad_sty[:4]))
    extra = [c.coordinate for row in ws.iter_rows(min_row=4) for c in row if c.column > 8 and c.value is not None]
    chk("nothing beyond column H", not extra, str(extra[:3]))
    mk = [c.coordinate for row in ws.iter_rows() for c in row
          if "**" in _plain(c.value) or "`" in _plain(c.value)]
    chk("no ** or backticks on sheet 4", not mk, str(mk[:3]))
    nonar = [c.coordinate for row in ws.iter_rows() for c in row
             if type(c).__name__ != "MergedCell" and c.value is not None and c.font.name != "Arial"]
    chk("all cells with values are Arial", not nonar, str(nonar[:3]))
    if xlsx:
        from build_eval_sheet import xml_non_arial
        n, bad = xml_non_arial(xlsx, S4)
        chk("raw-XML font check: all <c> elements Arial", bad == 0, f"({bad} of {n} not Arial)")
    # panel
    cells, L = panel_cells(ws3, len(rows))
    got = {(c.row, c.column): c.value for row in ws.iter_rows(min_row=LAST_ROW + 1) for c in row if c.value is not None}
    chk("panel cells equal the specified formulas", got == cells,
        "" if got == cells else str([(k, got.get(k), cells.get(k)) for k in sorted(set(got) | set(cells))
                                     if got.get(k) != cells.get(k)][:4]))
    chk("panel title row = last table row + 2 (41, one blank row between)", L["title"] == LAST_ROW + 2 == 41 and
        all(c.value is None for c in ws[LAST_ROW + 1]))
    chk("panel title merged across A:C", f"A{L['title']}:C{L['title']}" in {str(m) for m in ws.merged_cells.ranges})
    chk("panel formulas A-letters are E..BN", [cells[(L["first"] + i, 1)] for i in range(NFN)] ==
        [get_column_letter(c) for c in range(5, 67)])
    chk("panel ranges: groups $B$5:$B$39, single-product $H$5:$H$39 with \"*Single-product:*\"",
        cells[(L["tot"]["Single-product rows"], 3)] == '=COUNTIF($H$5:$H$39,"*Single-product:*")' and
        cells[(L["first"], 3)] == f'=COUNTIF($B$5:$B$39,"*"&$B{L["first"]}&"*")')
    chk("no dynamic-array functions in panel", not any(re.search(r"FILTER|UNIQUE|XLOOKUP|LET\(|SORT|SEQUENCE", str(v))
                                                       for v in got.values()))
    pfonts = [c.coordinate for row in ws.iter_rows(min_row=LAST_ROW + 1) for c in row
              if type(c).__name__ != "MergedCell" and c.value is not None and c.font.name != "Arial"]
    chk("panel cells Arial", not pfonts, str(pfonts[:3]))
    hd = L["hd"]
    by = check_letters(rows, hd)
    cnt, tot = python_panel(rows, hd)
    chk("mirror counts equal the lines naming each column (no accidental substring matches)",
        cnt == [len(by.get(get_column_letter(FIRST_FN_COL + i), ())) for i in range(NFN)])
    print("  Python mirror, groups listing each sheet-3 function:")
    for i, h in enumerate(hd):
        print("    %-3s %d  %s" % (get_column_letter(FIRST_FN_COL + i), cnt[i], h))
    print("  Python mirror totals:", tot)
    multi = [get_column_letter(FIRST_FN_COL + i) for i, c in enumerate(cnt) if c > 1]
    print("  functions in more than one group:", multi, "| in no group:",
          [get_column_letter(FIRST_FN_COL + i) for i, c in enumerate(cnt) if c == 0])
    chk("every sheet-3 function is in at least one group", tot["Functions in no group"] == 0)
    # expected values computed from groups_v3.md: lines of column B name each function by its letter
    exp_multi = sum(len(v) > 1 for v in by.values())
    exp_prod = {lab: sum(any(q.lower() in r[1].lower() for q in pats) for r in rows) for lab, pats in PRODUCT_TOTALS}
    chk("mirror totals equal values computed from groups_v3.md (letters lines + product prefixes)",
        tot["Functions in more than one group"] == exp_multi and
        all(tot[k] == v for k, v in exp_prod.items()) and
        tot["Single-product rows"] == NROWS - NMULTI == 20 and len(by) == NFN, str(tot))
    chk("groups_v3.md accounting line: 62 functions, 0 in no group, 23 in more than one group",
        NFN == 62 and tot["Functions in no group"] == 0 and exp_multi == 23, f"(multi={exp_multi})")
    if bak:  # optional: pass a workbook path to compare title and header row with
        old = load_workbook(bak)[S4]
        same = (old["A1"].value == ws["A1"].value and _snap_row(old, 3) == _snap_row(ws, 3))
        chk("title and header row identical to the baseline", same)
    print("sheet 4 overall:", "PASS" if ok else "FAIL")
    assert ok
    return cnt, tot
