"""Sheet '3c. NeMo Evaluation Tooling' from drafts/eval_tooling.md. Called by build_two_level.main().

Public API: add_sheet(wb) -> ws ; verify(wb, bak=None)
"""
import re
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

import paths as P
from products import ORDER

DIR = str(P.ROOT)
MD = str(P.DRAFTS / "eval_tooling.md")
S3, S3B, S3C, S4 = ("3. Guardrail Research Table", "3b. NeMo Rail Inventory",
                    "3c. NeMo Evaluation Tooling", "4. Candidate Comparison Groups")
TITLE = "3c. NeMo Guardrails Evaluation Tooling (v0.24.1)"
NOTE = ("Built-in evaluation tools, datasets, published results and reuse assessment for the test bench. "
        "Labels as in sheet 3.")
SKIP = {"Revision"}
MIN_W = 6
thin = Side(style="thin", color="8EA9DB")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
HFILL = PatternFill("solid", fgColor="4472C4")
SFILL = PatternFill("solid", fgColor="DCE6F2")
ALIGN = Alignment(wrap_text=True, vertical="top")
NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"


# ------------------------------------------------------------------ parsing
def split_row(line):
    """Split a markdown table row on unescaped pipes; unescape \\| inside cells."""
    s = line.strip()
    assert s.startswith("|") and s.endswith("|"), line[:60]
    cells = re.split(r"(?<!\\)\|", s[1:-1])
    return [c.strip().replace("\\|", "|") for c in cells]


def parse_md(path=MD):
    """Return ordered list of sections: {name, items}. Item kinds:
    summary(text) | detail(list of bullet strings, subs folded in) | table(hdr, rows) | note(text) | bullet(text)."""
    lines = open(path, encoding="utf-8").read().splitlines()
    secs, cur, mode = [], None, None
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^## (.+?)\s*$", line)
        if m:
            name = m.group(1)
            cur = {"name": name, "items": []} if name in SECTION_NAMES else None
            if cur is not None:
                secs.append(cur)
            mode = None
            i += 1
            continue
        if cur is None or not line.strip():
            i += 1
            continue
        if line.startswith("|"):
            tbl = []
            while i < len(lines) and lines[i].startswith("|"):
                tbl.append(split_row(lines[i]))
                i += 1
            hdr, rows = tbl[0], tbl[2:]
            assert all(set(c) <= set("-: ") for c in tbl[1]), tbl[1]
            for r in rows:
                assert len(r) == len(hdr), (cur["name"], len(r), len(hdr), r[:2])
            cur["items"].append(("table", hdr, rows))
            mode = None
            continue
        if line.startswith("Summary: "):
            cur["items"].append(("summary", line[len("Summary: "):].strip()))
            mode = None
        elif line.strip() == "Detail:":
            mode = "d"
            cur["items"].append(("detail", []))
        elif line.startswith("• "):
            if mode == "d":
                cur["items"][-1][1].append(line.rstrip())
            else:
                cur["items"].append(("bullet", line[2:].rstrip()))
        elif line.startswith("  – "):
            if mode == "d":
                cur["items"][-1][1].append(line.rstrip())
            else:
                kind, txt = cur["items"][-1]
                assert kind == "bullet", (cur["name"], line[:50])
                cur["items"][-1] = ("bullet", txt + "\n" + line.rstrip())
        else:
            cur["items"].append(("note", line.strip()))
            mode = None
        i += 1
    secs = [s for s in secs if s["name"] not in SKIP]
    assert [s["name"] for s in secs] == SECTION_ORDER, [s["name"] for s in secs]
    return secs


SECTION_ORDER = ["Overview", "Tools", "Datasets", "Published results", "Red-teaming", "Engine coverage",
                 "Reuse for the test bench", "Open questions"]
SECTION_NAMES = set(SECTION_ORDER) | SKIP


def strip_marks(t):
    return t.replace("`", "").replace("**", "")


# ------------------------------------------------------------------ writing
def _val(text, where):
    """Rich text when '**' present, else plain string with backticks removed."""
    if "**" in text:
        from build_two_level import rich
        v, _ = rich(text, 10, where)
        return v
    return text.replace("`", "")


def _style(c, fill=None, bold=False, hdr=False):
    c.font = Font(name="Arial", size=10, bold=bold or hdr, color="FFFFFF" if hdr else None)
    c.border, c.alignment = BORDER, ALIGN
    if hdr:
        c.fill = HFILL
    elif fill is not None:
        c.fill = fill


def _text_row(ws, r, label, text, W, where):
    for ci in range(1, W + 1):
        _style(ws.cell(row=r, column=ci))
    if label:
        ws.cell(row=r, column=1, value=label).font = Font(name="Arial", size=10, bold=True)
    ws.cell(row=r, column=2).value = _val(text, where)
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=W)


def add_sheet(wb):
    secs = parse_md()
    ncols = max(len(it[1]) for s in secs for it in s["items"] if it[0] == "table")
    W = max(MIN_W, ncols)
    if S3C in wb.sheetnames:
        wb.remove(wb[S3C])
    ws = wb.create_sheet(S3C, wb.sheetnames.index(S3B) + 1)
    ws["A1"] = TITLE
    ws["A1"].font = Font(name="Arial", size=13, bold=True)
    ws["A2"] = NOTE
    ws["A2"].font = Font(name="Arial", size=10, italic=True, color="808080")
    r = 3
    for s in secs:
        name = s["name"]
        for ci in range(1, W + 1):
            _style(ws.cell(row=r, column=ci), fill=SFILL, bold=True)
        ws.cell(row=r, column=1, value=name)
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=W)
        r += 1
        has_summary = any(it[0] == "summary" for it in s["items"])
        for it in s["items"]:
            where = f"{name}"
            k = it[0]
            if k == "summary":
                _text_row(ws, r, "Summary", it[1], W, where + " summary")
                r += 1
            elif k == "detail":
                if name == "Overview":
                    _text_row(ws, r, "Detail", "\n".join(it[1]), W, where + " detail")
                    r += 1
                else:  # one row per top-level bullet, sub-bullets folded into the parent cell
                    for b in _group_bullets(it[1]):
                        _text_row(ws, r, "Detail", b, W, where + " bullet")
                        r += 1
            elif k == "bullet":
                _text_row(ws, r, "Detail" if has_summary else None, it[1], W, where + " bullet")
                r += 1
            elif k == "note":
                _text_row(ws, r, "Note", it[1], W, where + " note")
                r += 1
            elif k == "table":
                hdr, rows = it[1], it[2]
                for ci, h in enumerate(hdr, 1):
                    c = ws.cell(row=r, column=ci, value=h.replace("`", ""))
                    _style(c, hdr=True)
                r += 1
                for row in rows:
                    for ci, v in enumerate(row, 1):
                        c = ws.cell(row=r, column=ci)
                        c.value = _val(v, f"{name} r{r} c{ci}")
                        _style(c)
                    r += 1
    # cell-level Arial on every cell of the used block (incl. empty ones)
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=1, max_col=W):
        for c in row:
            if c.font.name != "Arial":
                c.font = Font(name="Arial", size=10)
    for ci in range(1, W + 1):
        ws.column_dimensions[get_column_letter(ci)].width = 30 if W > MIN_W else (22 if ci == 1 else 38)
    ws.freeze_panes = "A3"
    return ws


def _group_bullets(lines):
    out = []
    for ln in lines:
        if ln.startswith("• "):
            out.append(ln[2:])
        else:
            out[-1] += "\n" + ln
    return out


# ------------------------------------------------------------------ verification
def _plain(v):
    if isinstance(v, CellRichText):
        return "".join(b.text if isinstance(b, TextBlock) else str(b) for b in v)
    return "" if v is None else str(v)


def expected_texts(secs):
    """Per section: ordered list of content strings, and list of table row counts."""
    out = []
    for s in secs:
        texts, tables = [], []
        for it in s["items"]:
            k = it[0]
            if k == "summary":
                texts.append(strip_marks(it[1]))
            elif k == "detail":
                if s["name"] == "Overview":
                    texts.append(strip_marks("\n".join(it[1])))
                else:
                    texts += [strip_marks(b) for b in _group_bullets(it[1])]
            elif k in ("bullet", "note"):
                texts.append(strip_marks(it[1]))
            elif k == "table":
                texts += [strip_marks(h) for h in it[1]]
                for row in it[2]:
                    texts += [strip_marks(v) for v in row]
                tables.append(len(it[2]))
        out.append((s["name"], texts, tables))
    return out


def xml_non_arial(xlsx, sheet_name):
    """Raw-XML font check of every <c> (incl. merged-away cells, which openpyxl's reader does not style)."""
    import zipfile
    from lxml import etree
    z = zipfile.ZipFile(xlsx)
    RN = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
    wbx = etree.fromstring(z.read("xl/workbook.xml"))
    rid = next(e.get(RN) for e in wbx.iter(NS + "sheet") if e.get("name") == sheet_name)
    rels = etree.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    tgt = next(e.get("Target") for e in rels if e.get("Id") == rid).lstrip("/")
    tgt = tgt if tgt.startswith("xl/") else "xl/" + tgt
    st = etree.fromstring(z.read("xl/styles.xml"))
    fonts = [(f.find(NS + "name").get("val") if f.find(NS + "name") is not None else None)
             for f in st.find(NS + "fonts")]
    xfs = [int(x.get("fontId", 0)) for x in st.find(NS + "cellXfs")]
    sh = etree.fromstring(z.read(tgt))
    n = bad = 0
    for c in sh.iter(NS + "c"):
        n += 1
        if fonts[xfs[int(c.get("s", 0))]] != "Arial":
            bad += 1
    return n, bad


def verify(wb, bak=None, xlsx=None):
    print("\n=== build_eval_sheet verification (3c) ===")
    secs = parse_md()
    exp = expected_texts(secs)
    exp_order = ORDER
    print("sheet order:", wb.sheetnames, "OK" if wb.sheetnames == exp_order else "FAIL (want %s)" % exp_order)
    ws = wb[S3C]
    print("A1:", ws["A1"].value, "| bold/size:", ws["A1"].font.b, ws["A1"].font.sz)
    print("A2:", ws["A2"].value[:50], "... italic/color:", ws["A2"].font.i, ws["A2"].font.color.rgb)
    print("freeze:", ws.freeze_panes, "(A3)  widths:",
          [ws.column_dimensions[get_column_letter(i)].width for i in range(1, 9)])
    W = max(MIN_W, max(len(it[1]) for s in secs for it in s["items"] if it[0] == "table"))
    print("block width:", W, " max_row:", ws.max_row, " row heights set:",
          sum(1 for d in ws.row_dimensions.values() if d.height is not None), "(0)")

    merged = {(m.min_row, m.min_col): m for m in ws.merged_cells.ranges}

    def is_heading(r):
        c = ws.cell(row=r, column=1)
        return c.fill.fill_type == "solid" and str(c.fill.fgColor.rgb).endswith("DCE6F2")

    def is_hdr(r):
        c = ws.cell(row=r, column=1)
        return c.fill.fill_type == "solid" and str(c.fill.fgColor.rgb).endswith("4472C4")

    def is_text(r):
        m = merged.get((r, 2))
        return m is not None and m.max_col == W and m.max_row == r

    heads = [(r, ws.cell(row=r, column=1).value) for r in range(3, ws.max_row + 1) if is_heading(r)]
    names = [n for _, n in heads]
    print("section headings:", names, "OK" if names == SECTION_ORDER else "FAIL")
    bad_merge = [r for r, _ in heads if not (merged.get((r, 1)) and merged[(r, 1)].max_col == W)]
    print("heading rows not merged across width:", bad_merge)

    mism = rowbad = 0
    total_cmp = 0
    for idx, (hr, name) in enumerate(heads):
        end = heads[idx + 1][0] if idx + 1 < len(heads) else ws.max_row + 1
        got, tcounts, r = [], [], hr + 1
        while r < end:
            if is_hdr(r):
                n = 0
                ncol = sum(1 for c in ws[r][:W] if c.value is not None)
                got += [_plain(ws.cell(row=r, column=ci).value) for ci in range(1, ncol + 1)]
                r += 1
                while r < end and not is_text(r):
                    got += [_plain(ws.cell(row=r, column=ci).value) for ci in range(1, ncol + 1)]
                    n += 1
                    r += 1
                tcounts.append(n)
            else:
                assert is_text(r), (name, r)
                got.append(_plain(ws.cell(row=r, column=2).value))
                r += 1
        _, want, wt = exp[idx]
        total_cmp += len(want)
        if got != want:
            mm = sum(1 for a, b in zip(got, want) if a != b) + abs(len(got) - len(want))
            mism += mm
            for a, b in zip(got, want):
                if a != b:
                    print("  MISMATCH in", name, repr(a[:70]), "!=", repr(b[:70]))
                    break
        if tcounts != wt:
            rowbad += 1
        print(f"  {name}: md tables rows {wt} vs sheet {tcounts}", "OK" if tcounts == wt else "FAIL")
    print("table row-count failures:", rowbad)

    marks = [c.coordinate for row in ws.iter_rows() for c in row
             if "**" in _plain(c.value) or "`" in _plain(c.value)]
    print("cells with ** or backtick:", len(marks), marks[:5])
    nonar, ws_blocks, nonar_runs, rich_n, bold_n = [], 0, 0, 0, 0
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=1, max_col=W):
        for c in row:
            if c.font.name != "Arial" and type(c).__name__ != "MergedCell":
                nonar.append(c.coordinate)
            if isinstance(c.value, CellRichText):
                rich_n += 1
                for b in c.value:
                    if isinstance(b, TextBlock):
                        ws_blocks += not b.text.strip()
                        nonar_runs += (b.font.rFont != "Arial")
                        bold_n += bool(b.font.b)
    print("non-Arial cells:", len(nonar), nonar[:5], "| non-Arial rich runs:", nonar_runs,
          "| whitespace-only TextBlocks:", ws_blocks, "| rich cells:", rich_n, "bold runs:", bold_n)
    if xlsx:
        n, bad = xml_non_arial(xlsx, S3C)
        print("raw-XML font check (all %d <c> elements incl. merged-away cells): non-Arial = %d" % (n, bad))
    print("plain-text mismatches vs md (%d content strings compared): %d" % (total_cmp, mism))
    # (sheet 4 is verified by build_groups_sheet.verify since the groups fill; no v3 identity check any more)
    return mism
