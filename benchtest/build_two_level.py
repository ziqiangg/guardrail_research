"""Rebuild sheet 3 in two-level (Summary/Detail) format from the docx + drafts/two_level.md."""
import os, re, shutil, sys
from docx import Document
from openpyxl import load_workbook
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.cell.text import InlineFont
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.properties import Outline

import extract_tables as ET
from fill_nemo_columns import HDR_RE, LABEL_RE, BORDER, ALIGN

DIR = ET.DIR
XLSX = DIR + r"\AI Guardrails Research and Comparison.xlsx"
BAK = DIR + r"\AI Guardrails Research and Comparison.v2.xlsx"
BAK3 = DIR + r"\AI Guardrails Research and Comparison.v3.xlsx"
BAK6 = DIR + r"\AI Guardrails Research and Comparison.v6.xlsx"  # state before the sheet-4 fill and the 3d/3e panels
BAK7 = DIR + r"\AI Guardrails Research and Comparison.v7.xlsx"  # state before the sheet-4 readability update
MDS = [DIR + r"\drafts\two_level_v2.md", DIR + r"\drafts\lg_two_level.md",
       DIR + r"\drafts\sentinel_two_level.md"]  # NeMo columns first, then Llama Guard, then GovTech Sentinel
# override with a single draft: python build_two_level.py <md path> (e.g. drafts\two_level.md)
S3, S4 = "3. Guardrail Research Table", "4. Candidate Comparison Groups"
GREY = "808080"


def parse_md(path, expect=None):
    cols, cur, rn, mode = [], None, None, None
    for line in open(path, encoding="utf-8").read().splitlines():
        m = HDR_RE.match(line)
        if m:
            cur = {"header": re.sub(r"\s*\(expanded\)\s*$", "", m.group(1).strip()), "R": {}}
            cols.append(cur)
            rn = mode = None
            continue
        m = re.match(r"^### R([1-9])\s*$", line)
        if m and cur is not None:
            rn = int(m.group(1))
            mode = None
            assert rn not in cur["R"], (cur["header"], rn)
            cur["R"][rn] = {"summary": None, "detail": []}
            continue
        if cur is None or rn is None:
            continue
        if line.startswith("Summary: "):
            cur["R"][rn]["summary"] = line[len("Summary: "):].strip()
            mode = None
        elif line.strip() == "Detail:":
            mode = "d"
        elif mode == "d" and (line.startswith("• ") or line.startswith("  – ")):
            cur["R"][rn]["detail"].append(line.rstrip())
    if expect is not None:
        assert len(cols) == expect, len(cols)
    for c in cols:
        assert sorted(c["R"]) == list(range(1, 10)), c["header"]
        for n, d in c["R"].items():
            assert d["summary"] and d["detail"], (c["header"], n)
    return cols


def to_runs(text, where):
    text = text.replace("`", "")
    parts = text.split("**")
    if len(parts) % 2 == 0:
        raise SystemExit(f"Unbalanced ** in {where}: {text[:80]}")
    runs = [(p, i % 2 == 1) for i, p in enumerate(parts) if p]
    if "**" in "".join(t for t, _ in runs):
        raise SystemExit(f"Leftover ** in {where}")
    return runs


def rich(text, sz, where):
    raw = to_runs(text, where)
    runs, pend = [], ""
    for t, b in raw:
        if not t.strip():
            if runs:
                runs[-1] = (runs[-1][0] + t, runs[-1][1])
            else:
                pend += t
            continue
        runs.append((pend + t, b))
        pend = ""
    val = CellRichText(*[TextBlock(InlineFont(rFont="Arial", sz=sz, b=True) if b
                                   else InlineFont(rFont="Arial", sz=sz), t) for t, b in runs])
    return val, "".join(t for t, _ in runs)


def plain_of(v):
    if isinstance(v, CellRichText):
        return "".join(b.text if isinstance(b, TextBlock) else str(b) for b in v)
    return "" if v is None else str(v)


def main(md=None):
    mds = [md] if md else MDS
    if not os.path.exists(BAK):
        shutil.copy2(XLSX, BAK)
        print("backup created")
    else:
        print("backup exists, not overwritten")

    if not os.path.exists(BAK3):
        shutil.copy2(XLSX, BAK3)
        print("v3 backup created")
    else:
        print("v3 backup exists, not overwritten")

    doc = Document(ET.SRC)
    t0 = doc.tables[0]
    cols = [c for p in mds for c in parse_md(p)]
    NCOLS = 5 + len(cols)  # 33 with the default drafts: A-E, NeMo F-U, Llama Guard V-Z, GovTech Sentinel AA-AG

    wb = load_workbook(XLSX, rich_text=True)
    old = wb[S3]
    bedrock_hdr = ET.plain_text(t0.rows[0].cells[3])
    old_hdr = [c.value for c in old[3] if c.value is not None]
    old_hdr = old_hdr[old_hdr.index(bedrock_hdr):]
    new_hdr = [bedrock_hdr] + [c["header"] for c in cols]
    print("header diffs vs current sheet 3:")
    nd = 0
    for i, (a, b) in enumerate(zip(old_hdr, new_hdr)):
        if a != b:
            nd += 1
            print("  DIFF", i, repr(a), "!=", repr(b))
    if len(old_hdr) != len(new_hdr):
        nd += 1
        print("  length differs", len(old_hdr), len(new_hdr))
    print("  total differences:", nd)

    idx = wb.sheetnames.index(S3)
    wb.remove(old)
    ws = wb.create_sheet(S3, idx)
    assert wb.sheetnames.index(S3) == 0 and S4 in wb.sheetnames

    ws["A1"] = "3. Guardrail Research Table"
    ws["A1"].font = Font(name="Arial", size=13, bold=True)
    headers = ["No.", "Research question", "Why it affects the test-bench scope", "Level"] + new_hdr
    assert len(headers) == NCOLS
    for ci, h in enumerate(headers, 1):
        x = ws.cell(row=3, column=ci, value=h)
        x.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
        x.fill = PatternFill("solid", fgColor="4472C4")
        x.alignment, x.border = ALIGN, BORDER

    WHITE = PatternFill("solid", fgColor="FFFFFF")
    LGREY = PatternFill("solid", fgColor="F2F2F2")
    expected = {}
    for n in range(1, 10):
        sr, dr = 4 + 2 * (n - 1), 5 + 2 * (n - 1)
        for r, fill, sz in ((sr, WHITE, 10), (dr, LGREY, 9)):
            for c in range(1, NCOLS + 1):
                x = ws.cell(row=r, column=c)
                x.fill, x.alignment, x.border = fill, ALIGN, BORDER
                x.font = Font(name="Arial", size=sz)
        row = t0.rows[n]
        for c in range(3):
            ws.cell(row=sr, column=c + 1).value = ET.cell_value(row.cells[c])
            ws.merge_cells(start_row=sr, start_column=c + 1, end_row=dr, end_column=c + 1)
        ws.cell(row=sr, column=4, value="Summary").font = Font(name="Arial", size=10, bold=True)
        ws.cell(row=dr, column=4, value="Detail").font = Font(name="Arial", size=9, bold=True, color=GREY)
        for r in (sr, dr):
            ws.cell(row=r, column=4).alignment = Alignment(wrap_text=True, vertical="top", horizontal="center")
        ws.cell(row=sr, column=5).value = ET.cell_value(row.cells[3])
        ws.cell(row=dr, column=5, value="— (example column; detail not researched)").font = \
            Font(name="Arial", size=9, italic=True, color=GREY)
        for ci, col in enumerate(cols):
            cc = 6 + ci
            d = col["R"][n]
            where = f"{col['header']} R{n}"
            sv, sp = rich(d["summary"], 10, where + " summary")
            dv, dp = rich("\n".join(d["detail"]), 9, where + " detail")
            ws.cell(row=sr, column=cc).value = sv
            ws.cell(row=dr, column=cc).value = dv
            expected[(sr, cc)] = sp
            expected[(dr, cc)] = dp
        ws.row_dimensions[dr].outline_level = 1

    for ci in range(1, NCOLS + 1):
        ws.column_dimensions[get_column_letter(ci)].width = {1: 6, 2: 28, 3: 32, 4: 10}.get(ci, 48)
    ws.freeze_panes = "E4"
    if ws.sheet_properties.outlinePr is None:
        ws.sheet_properties.outlinePr = Outline()
    ws.sheet_properties.outlinePr.summaryBelow = False
    import build_inventory
    build_inventory.add_sheet(wb, ws)
    import build_eval_sheet
    build_eval_sheet.add_sheet(wb)
    import build_lg_inventory
    build_lg_inventory.add_sheet(wb, ws)
    import build_sentinel_inventory
    build_sentinel_inventory.add_sheet(wb, ws)
    import build_groups_sheet
    build_groups_sheet.add_sheet(wb)
    wb.save(XLSX)

    def post_check(xlsx):
        """Re-verify sheet 3 after an external rewrite (LibreOffice recalc). Returns True when intact."""
        w = load_workbook(xlsx, rich_text=True)
        s3 = w[S3]
        mm = 0
        for (r, cc), exp in expected.items():
            mm += plain_of(s3.cell(row=r, column=cc).value) != exp
        mm += sum(plain_of(s3.cell(row=4 + 2 * (n - 1), column=5).value) != ET.plain_text(t0.rows[n].cells[3])
                  for n in range(1, 10))
        sample = [(4, 6), (4, 10), (6, 8), (10, 15), (18, 21), (4, 22), (18, 26), (4, 27), (18, 33)]
        nb = 0
        for r, cc in sample:
            v = s3.cell(row=r, column=cc).value
            if not (isinstance(v, CellRichText) and any(isinstance(b, TextBlock) and b.font.b for b in v)):
                nb += 1
        fonts = sum(1 for row in s3.iter_rows(min_row=4, max_row=21, max_col=NCOLS) for c in row
                    if c.font.name != "Arial")
        print("  post-recalc: sheet 3 plain-text mismatches (F-%s + E):" % get_column_letter(NCOLS), mm,
              "| sample cells lacking rich bold:", nb, "of", len(sample), "| non-Arial cells rows 4-21:", fonts)
        return mm == 0 and nb == 0 and fonts == 0

    # ---------------- verification ----------------
    wb2 = load_workbook(XLSX, rich_text=True)
    ws = wb2[S3]
    print("sheet order:", wb2.sheetnames)
    print("A3:%s3:" % get_column_letter(NCOLS), [c.value for c in ws[3][:NCOLS]])
    print("max_row:", ws.max_row, "(21)  max_column:", ws.max_column, "(%d)" % NCOLS)
    print("freeze_panes:", ws.freeze_panes)
    mr = sorted(str(m) for m in ws.merged_cells.ranges)
    print("merged count:", len(mr), "(27)", mr)
    bad = [r for r in range(4, 22) if ws.row_dimensions[r].outline_level != (1 if r % 2 == 1 else 0)
           or ws.row_dimensions[r].hidden]
    print("outline problems:", bad, "summaryBelow:", ws.sheet_properties.outlinePr.summaryBelow)

    fails = mism = 0
    for n in range(1, 10):
        sr = 4 + 2 * (n - 1)
        for cc in range(6, NCOLS + 1):
            c = ws.cell(row=sr, column=cc)
            blocks = list(c.value) if isinstance(c.value, CellRichText) else [c.value]
            plain = plain_of(c.value)
            probs = []
            first = blocks[0]
            if n <= 8 and not (isinstance(first, TextBlock) and first.font.b):
                probs.append("first-not-bold")
            if n <= 7 and not any(isinstance(b, TextBlock) and b.font.b and LABEL_RE.search(b.text)
                                  for b in blocks):
                probs.append("no-bold-label")
            if any(s in plain for s in ("**", "`", "_", "$")):
                probs.append("marker")
            if len(plain.split()) > 60:
                probs.append(f"words={len(plain.split())}")
            if "\n" in plain:
                probs.append("newline")
            if probs:
                fails += 1
                print("  FAIL", c.coordinate, probs)
    print("summary check failures:", fails)
    for (r, cc), exp in expected.items():
        if plain_of(ws.cell(row=r, column=cc).value) != exp:
            mism += 1
            print("  MISMATCH", ws.cell(row=r, column=cc).coordinate)
    print("F-%s plain-text mismatches:" % get_column_letter(NCOLS), mism)

    mb = 0
    for n in range(1, 10):
        exp = ET.plain_text(t0.rows[n].cells[3])
        if plain_of(ws.cell(row=4 + 2 * (n - 1), column=5).value) != exp:
            mb += 1
            print("  MISMATCH E", n)
    print("Bedrock E mismatches:", mb)

    nonar = [c.coordinate for row in ws.iter_rows(min_row=4, max_row=21, max_col=NCOLS) for c in row
             if c.font.name != "Arial"]
    print("non-Arial cells rows 4-21:", len(nonar), nonar[:5])
    import zipfile
    from lxml import etree
    z = zipfile.ZipFile(XLSX)
    sheet = [n for n in z.namelist() if n.startswith("xl/worksheets/sheet")]
    wbx = z.read("xl/workbook.xml").decode("utf8")
    print("worksheet parts:", sheet)
    ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    xml = "{http://www.w3.org/XML/1998/namespace}space"
    ssp = norpr = emp = 0
    for part in z.namelist():
        if part.endswith(".xml") or part.endswith(".rels"):
            etree.fromstring(z.read(part))  # well-formed check on every part
    print("all", len(z.namelist()), "parts well-formed")
    for part in sheet:
        root = etree.fromstring(z.read(part))
        for t in root.iter(ns + "t"):
            tx = t.text or ""
            if tx == "":
                emp += 1
            if tx != tx.strip() and t.get(xml) != "preserve":
                ssp += 1
        norpr += sum(1 for r in root.iter(ns + "r") if r.find(ns + "rPr") is None)
    print("inline <t> ws w/o xml:space=preserve:", ssp, " <r> without rPr:", norpr, " empty <t>:", emp)
    assert ssp == 0 and norpr == 0 and emp == 0
    print("F10:", plain_of(ws["F10"].value))
    print("F11:", plain_of(ws["F11"].value))
    build_eval_sheet.verify(wb2, BAK3, XLSX)
    build_lg_inventory.verify(wb2, XLSX)
    build_sentinel_inventory.verify(wb2, XLSX)
    build_inventory.verify(XLSX, wb2, BAK, post_check=post_check)
    # sheet 4 is no longer the docx template: verified against drafts/groups_v2.md (and v7 for title/header)
    build_groups_sheet.verify(load_workbook(XLSX, rich_text=True), XLSX, BAK7)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
