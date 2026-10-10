"""Independent verification of the Cloak apply (sheet 3 BL-BN, sheet 3l, all other sheets vs the
previous commit). One-shot like the other verify_*_apply scripts.

Baseline = the workbook at git HEAD (the previous commit), not a frozen file under baselines/.
Writes drafts/cloak_urls.txt (R9 cells and inventory Source URL cells only).
"""
import contextlib
import io
import os
import re
import subprocess
import sys
import tempfile
from urllib.parse import urlparse

from openpyxl import load_workbook
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.utils import get_column_letter

import build_two_level as B2
import build_inventory as BI
import build_cloak_inventory as BP
import build_eval_sheet as ES
import inventory_sheet as IS
import products
from fill_nemo_columns import LABEL_RE

XLSX = B2.XLSX
URLS = str(BI.P.DRAFTS / "cloak_urls.txt")
OLD_SHEETS = ["3. Guardrail Research Table", "3b. NeMo Rail Inventory", "3c. NeMo Evaluation Tooling",
              "3d. Llama Guard Inventory", "3e. GovTech Sentinel Inventory", "3f. Presidio Inventory",
              "3g. SDP Inventory", "3h. Model Armor Inventory", "3i. LionGuard Inventory",
              "3j. Purple Llama Inventory", "3k. CyberSecEval Eval Tooling",
              "4. Candidate Comparison Groups"]
S3, S3L = OLD_SHEETS[0], BP.S3L
NEW_SHEETS = [S3L]
RESULTS = []


def check(name, ok, extra=""):
    RESULTS.append(bool(ok))
    print(("PASS" if ok else "FAIL"), "-", name, extra)


plain = B2.plain_of


def runs_of(v):
    return [(b.text, bool(b.font.b)) for b in v] if isinstance(v, CellRichText) else [(plain(v), False)]


def _col(c):
    return None if c is None else (c.rgb if c.type == "rgb" else (c.type, c.theme if c.type == "theme" else c.indexed))


def style_of(c):
    b = c.border
    return (c.font.name, c.font.sz, c.font.b, c.font.i, _col(c.font.color), c.fill.fill_type, _col(c.fill.fgColor),
            c.alignment.wrap_text, c.alignment.vertical, c.alignment.horizontal,
            tuple((s.style, _col(s.color)) if s is not None else None for s in (b.left, b.right, b.top, b.bottom)))


def full_snap(w):
    cells = [(c.coordinate, plain(c.value), runs_of(c.value), style_of(c)) for row in w.iter_rows() for c in row]
    layout = (sorted(str(m) for m in w.merged_cells.ranges), w.freeze_panes, w.auto_filter.ref,
              {k: v.width for k, v in w.column_dimensions.items()},
              {k: (v.height, v.outline_level, v.hidden) for k, v in w.row_dimensions.items()},
              (w.max_row, w.max_column))
    return cells, layout


# ---------------------------------------------------------------- previous commit's workbook
prev = os.path.join(tempfile.mkdtemp(), "prev.xlsx")
with open(prev, "wb") as f:
    f.write(subprocess.run(["git", "show", 'HEAD:benchtest/AI Guardrails Research and Comparison.xlsx'],
                           capture_output=True, check=True, cwd=str(BI.P.ROOT)).stdout)
new = load_workbook(XLSX, rich_text=True)
old = load_workbook(prev, rich_text=True)
print("previous-commit sheet names:", old.sheetnames)
want_order = OLD_SHEETS[:11] + NEW_SHEETS + OLD_SHEETS[11:]
check("sheet order (3l right after 3k, sheet 4 last)", new.sheetnames == list(BI.ORDER) == want_order,
      str(new.sheetnames))
check("previous sheets all present, in order, plus only 3l",
      [n for n in new.sheetnames if n not in NEW_SHEETS] == old.sheetnames == OLD_SHEETS)

# ---------------------------------------------------------------- ranges from drafts
mds = [B2.parse_md(m) for m in B2.MDS]
n_each = [len(m) for m in mds]
assert len(mds) == 9, n_each
OLD_LAST = 5 + sum(n_each[:8])            # BK = 63
PL0 = OLD_LAST + 1                        # BL = 64
md_pl = mds[8]
LAST = PL0 + len(md_pl) - 1               # BN = 66
print("derived: old last col %s (%d), Cloak %s-%s (%d), last col %d" % (
    get_column_letter(OLD_LAST), OLD_LAST, get_column_letter(PL0), get_column_letter(LAST), len(md_pl), LAST))

ws, wo = new[S3], old[S3]
check("sheet 3: %d columns (A-%s)" % (LAST, get_column_letter(LAST)),
      ws.max_column == LAST == 66 and OLD_LAST == 63 and len(md_pl) == 3, str(ws.max_column))
check("sheet 3: max_row 21", ws.max_row == 21, str(ws.max_row))
check("27 merges equal to previous commit",
      len(ws.merged_cells.ranges) == 27 and sorted(map(str, ws.merged_cells.ranges)) == sorted(map(str, wo.merged_cells.ranges)))
lv = [r for r in range(1, 23) if ws.row_dimensions[r].outline_level == 1]
check("outline levels (rows 5,7,..,21 level 1)", lv == list(range(5, 22, 2)), str(lv))
check("freeze panes E4 (as previous)", ws.freeze_panes == wo.freeze_panes == "E4")
check("summaryBelow False", ws.sheet_properties.outlinePr.summaryBelow is False)
widths = [ws.column_dimensions[get_column_letter(i)].width for i in range(1, LAST + 1)]
check("column widths 6/28/32/10 then 48", widths == [6, 28, 32, 10] + [48] * (LAST - 4), str(widths[-3:]))
check("old column widths A-%s identical to previous commit" % get_column_letter(OLD_LAST),
      all(ws.column_dimensions[get_column_letter(i)].width == wo.column_dimensions[get_column_letter(i)].width
          for i in range(1, OLD_LAST + 1)))
pl_hdrs = [c["header"] for c in md_pl]
got_h = [ws.cell(row=3, column=c).value for c in range(PL0, LAST + 1)]
check("BL3:BN3 are the three Cloak headers in md order, exactly as ruled (R037, changes 5b)",
      got_h == pl_hdrs == ["Cloak: Free-text PII detection and anonymisation",
                           "Cloak: Custom entity detection in free text (lists, regex and LLM)",
                           "Cloak: Reversible anonymisation and decryption (encrypt and restore)"], str([h[:26] for h in pl_hdrs]))
check("old header row identical (A3:BK3)", [ws.cell(row=3, column=c).value for c in range(1, OLD_LAST + 1)]
      == [wo.cell(row=3, column=c).value for c in range(1, OLD_LAST + 1)])

# ---------------------------------------------------------------- A-BK vs previous commit (all rows)
diff = sum(plain(ws.cell(row=r, column=c).value) != plain(wo.cell(row=r, column=c).value)
           for r in range(1, 23) for c in range(1, OLD_LAST + 1))
check("A-BK plain text vs previous commit: 0 diffs", diff == 0, f"({diff} diffs)")
rdiff = sum(runs_of(ws.cell(row=r, column=c).value) != runs_of(wo.cell(row=r, column=c).value)
            for r in range(4, 22) for c in range(6, OLD_LAST + 1))
check("F-BK rows 4-21 rich-text runs (text+bold) vs previous commit: 0 diffs", rdiff == 0, f"({rdiff} diffs)")
sdiff = sum(style_of(ws.cell(row=r, column=c)) != style_of(wo.cell(row=r, column=c))
            for r in range(1, 23) for c in range(1, OLD_LAST + 1))
check("A-BK cell styles vs previous commit: 0 diffs", sdiff == 0, f"({sdiff} diffs)")

# ---- BL-BN vs md
mism = ncells = 0
for n in range(1, 10):
    sr, dr = 4 + 2 * (n - 1), 5 + 2 * (n - 1)
    for ci, col in enumerate(md_pl):
        cc = PL0 + ci
        d = col["R"][n]
        _, sp = B2.rich(d["summary"], 10, "v")
        _, dp = B2.rich("\n".join(d["detail"]), 9, "v")
        mism += plain(ws.cell(row=sr, column=cc).value) != sp
        mism += plain(ws.cell(row=dr, column=cc).value) != dp
        ncells += 2
check("BL-BN plain text vs cloak_two_level.md parse: 0 mismatches (%d cells)" % ncells,
      mism == 0 and ncells == 54, f"({mism})")
fails = nsum = 0
for n in range(1, 10):
    sr = 4 + 2 * (n - 1)
    for cc in range(PL0, LAST + 1):
        nsum += 1
        c = ws.cell(row=sr, column=cc)
        blocks = list(c.value) if isinstance(c.value, CellRichText) else [c.value]
        p = plain(c.value)
        probs = []
        if n <= 8 and not (isinstance(blocks[0], TextBlock) and blocks[0].font.b):
            probs.append("first-not-bold")
        if n <= 7 and not any(isinstance(b, TextBlock) and b.font.b and LABEL_RE.search(b.text) for b in blocks):
            probs.append("no-bold-label")
        if any(s in p for s in ("**", "`", "_", "$")):
            probs.append("marker")
        nw = len(p.split())  # counts the trailing label (lessons 18)
        if nw > 60:
            probs.append("words=%d" % nw)
        if "\n" in p:
            probs.append("newline")
        if probs:
            fails += 1
            print("   ", c.coordinate, probs)
check("BL-BN Summary style checks (%d cells; first bold, bold label R1-R7, no markers, <=60 words, no newline)" % nsum,
      fails == 0 and nsum == 27,
      f"({fails} failing; word limit counts the trailing label)")
bad_md = [ws.cell(row=r, column=c).coordinate for r in range(4, 22) for c in range(PL0, LAST + 1)
          if any(s in plain(ws.cell(row=r, column=c).value) for s in ("**", "`"))]
check("BL-BN no ** or backticks (rows 4-21)", not bad_md, str(bad_md[:5]))
nonar = [ws.cell(row=r, column=c).coordinate for r in range(3, 22) for c in range(PL0, LAST + 1)
         if ws.cell(row=r, column=c).font.name != "Arial"]
rich_nonar = sum(1 for r in range(4, 22) for c in range(PL0, LAST + 1)
                 for b in (ws.cell(row=r, column=c).value if isinstance(ws.cell(row=r, column=c).value, CellRichText) else [])
                 if isinstance(b, TextBlock) and b.font.rFont != "Arial")
check("BL-BN non-Arial cells / rich runs: 0", not nonar and rich_nonar == 0, f"({nonar[:5]}, rich runs {rich_nonar})")
check("BL-BN cell styles equal the BK styles row by row (same house format)",
      all(style_of(ws.cell(row=r, column=PL0 + k)) == style_of(ws.cell(row=r, column=OLD_LAST))
          for r in range(1, 22) for k in range(3)))

# ---------------------------------------------------------------- every other sheet identical to previous commit
for nm in OLD_SHEETS[1:]:
    a, al = full_snap(new[nm])
    b, bl = full_snap(old[nm])
    nd = sum(1 for x, y in zip(a, b) if x != y) + abs(len(a) - len(b))
    check(f"{nm}: values (incl. formulas), rich text, styles identical to previous commit", a == b,
          f"({len(a)} cells, {nd} diffs)")
    check(f"{nm}: merges, freeze, autofilter, widths, row heights/outline, extents identical", al == bl,
          "" if al == bl else str([(i, x, y) for i, (x, y) in enumerate(zip(al, bl)) if x != y])[:300])

# ---- 3l
w3l = new[S3L]
blocks = IS.parse_md(BP.CFG)
pos, prev_last = [], 2
for b in blocks:
    h, rows = IS.block_rows(w3l, b["hdr"][0], prev_last + 1)
    pos.append((h, rows))
    prev_last = rows[-1]
cnt = [len(p[1]) for p in pos]
check("3l block row counts 10/8/26/9/28/4 = 85", cnt == [10, 8, 26, 9, 28, 4] and sum(cnt) == 85,
      f"{cnt} sum {sum(cnt)}")
mm = tot = 0
for b, (h, rows) in zip(blocks, pos):
    got = [[w3l.cell(row=r, column=c).value for c in range(1, len(b["hdr"]) + 1)] for r in [h] + rows]
    want = [b["hdr"]] + b["rows"]
    tot += sum(len(x) for x in want)
    mm += sum(1 for g, w in zip(got, want) for x, y in zip(g, w) if x != y) + abs(len(got) - len(want))
check("3l every cell equals cleaned md text (%d cells)" % tot, mm == 0, f"({mm} mismatches)")
h0, r0 = pos[0]
check("3l autofilter = block (a) only",
      w3l.auto_filter.ref == f"A{h0}:{get_column_letter(len(blocks[0]['hdr']))}{r0[-1]}", w3l.auto_filter.ref)
has_cov = [BP.COV in b["hdr"] for b in blocks]
check("3l Covered-by column in all six blocks; block widths 7/8/7/6/5/6",
      has_cov == [True] * 6 and [len(b["hdr"]) for b in blocks] == [7, 8, 7, 6, 5, 6],
      str([len(b["hdr"]) for b in blocks]))
hdr3 = {ws.cell(row=3, column=c).value for c in range(1, ws.max_column + 1)}
badc, ncov, amber_bad, nleg, ninv_m, npl = [], 0, 0, 0, 0, 0
for b, (h, rows) in zip(blocks, pos):
    if BP.COV not in b["hdr"]:
        continue
    cc = b["hdr"].index(BP.COV) + 1
    for r in rows:
        v = w3l.cell(row=r, column=cc)
        mk = v.value in (BP.LEGACY, BP.INV_ONLY, BP.PLANNED)
        nleg += v.value == BP.LEGACY
        ninv_m += v.value == BP.INV_ONLY
        npl += v.value == BP.PLANNED
        amber_bad += mk != (v.fill.fill_type == "solid" and str(v.fill.fgColor.rgb).endswith("FFF2CC"))
        for part in str(v.value).split(";"):
            part = part.strip()
            ncov += 1
            if part not in hdr3 and part not in (BP.LEGACY, BP.INV_ONLY, BP.PLANNED):
                badc.append((r, part))
check("3l Covered-by values valid (real sheet-3 header or legacy/inventory-only marker; no marker mixed)", not badc,
      f"({ncov} values; bad {badc[:3]})")
check("3l markers: legacy 1 (enCRYPT), inventory only 7, planned 1 (Sentinel integration row)",
      (nleg, ninv_m, npl) == (1, 7, 1), f"(legacy {nleg}, inventory only {ninv_m}, planned {npl})")
check("3l amber fill exactly on marker cells", amber_bad == 0)
ctx = dict(ws=w3l, ws3=ws, cfg=BP.CFG, blocks=blocks, pos=pos, hdr3=hdr3)
for fn in BP.CFG["validators"]:
    ok_, msgs = fn(ctx)
    check("3l validator " + fn.__name__, ok_, "| " + " ".join(msgs)[:300])
ok_p, counts, totals = IS.verify_panel(new, BP.CFG, w3l, ws, blocks, pos)
check("3l coverage panel equals spec; all 3 Table 3 columns covered; inventory-only 7, legacy 1, planned 1",
      ok_p and len(counts) == 3 and totals["Rows marked inventory only"] == 7 and totals["Rows marked legacy"] == 1
      and totals["Rows marked planned"] == 1, str(totals))
mk = [c.coordinate for row in w3l.iter_rows() for c in row if isinstance(c.value, str) and ("**" in c.value or "`" in c.value)]
check("3l no ** or backticks", not mk, str(mk[:5]))
nonar = [c.coordinate for row in w3l.iter_rows() for c in row
         if type(c).__name__ != "MergedCell" and c.value is not None and c.font.name != "Arial"]
nx, bx = ES.xml_non_arial(XLSX, S3L)
check("3l all Arial (cells + raw XML <c> check)", not nonar and bx == 0, f"(openpyxl {len(nonar)}, raw XML {bx} of {nx})")
check("3l A1 bold 13; A2 italic grey; freeze A4",
      w3l["A1"].font.b and w3l["A1"].font.sz == 13 and w3l["A2"].font.i and w3l["A2"].font.color.rgb.endswith("808080")
      and w3l.freeze_panes == "A4")

# ---------------------------------------------------------------- registry
ck = products.PRODUCTS[8]
check("registry: cloak entry (prefix 'Cloak:', 3l, build_cloak_inventory); HDR_RE matches exactly its 3 column headings; "
      "the 8 earlier products unchanged",
      ck["slug"] == "cloak" and products.prefixes(ck) == ("Cloak:",) and ck["inventory_sheet"] == S3L
      and ck["inventory_builder_module"] == "build_cloak_inventory"
      and sum(bool(products.HDR_RE.match(l)) for l in open(str(ck["two_level_md"]), encoding="utf-8")
              .read().splitlines()) == 3 and len(products.PRODUCTS) == 9
      and [p["slug"] for p in products.PRODUCTS[:8]] == ["nemo", "llamaguard", "sentinel", "presidio", "sdp",
                                                         "modelarmor", "lionguard", "purplellama"])

# ---------------------------------------------------------------- XML hygiene
ssp, emp, norpr, n, wf = BI.hygiene(XLSX)
check("XML hygiene (all parts well-formed; worksheets + sharedStrings)", ssp == 0 and emp == 0 and norpr == 0 and wf,
      f"(unpreserved <t>={ssp}, <r> without rPr={norpr}, empty <t>={emp}, parts checked={n}, well-formed={wf})")

# ---------------------------------------------------------------- URLs (R9, Source URL cells, eval sheet only)
urls, seen = [], set()


def add(t):
    for u in BI.URL_RE.findall(t or ""):
        u = u.rstrip(".:,;)")
        p = urlparse(u)
        host = p.hostname or ""
        if ("{" in u or "}" in u or host.endswith("googleapis.com") or host.startswith("api.")
                or (host == "huggingface.co" and p.path.startswith("/api"))):
            continue
        if u not in seen:
            seen.add(u)
            urls.append(u)


for r in (20, 21):  # R9 Summary and Detail rows
    for c in range(PL0, LAST + 1):
        add(plain(ws.cell(row=r, column=c).value))
n9 = len(urls)
for b, (h, rows) in zip(blocks, pos):
    cc = b["hdr"].index("Source URL") + 1
    for r in rows:
        add(w3l.cell(row=r, column=cc).value)
ninv = len(urls) - n9
open(URLS, "w", encoding="utf-8", newline="\n").write("\n".join(urls) + "\n")
print(f"urls: {len(urls)} unique ({n9} from BL20:BN21, {ninv} new from 3l Source URL cells) -> {URLS}")
check("URL list written, no skipped host/template entries",
      bool(urls) and not any("{" in u or "googleapis.com" in u or urlparse(u).hostname.startswith("api.") for u in urls),
      f"({len(urls)} URLs)")

print("\nSUMMARY: %d/%d checks passed" % (sum(RESULTS), len(RESULTS)))
sys.exit(0 if all(RESULTS) else 1)
