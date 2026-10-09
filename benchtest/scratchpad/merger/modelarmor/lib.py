"""Merge helpers for modelarmor P6 (gr-merger). Stdlib only.

Columns are parsed into {col_id: {"head": str, "rows": {n: {"summary": str, "detail": [str]}}}}.
Every edit is an operation that asserts its anchor is found exactly once and appends a record to OPS,
from which the per-location table of the change log is generated.
"""
import re
from collections import OrderedDict

OPS = []          # column ops
IOPS = []         # inventory ops


def short(s, n=120):
    s = re.sub(r"\s+", " ", s).strip()
    s = s.replace("|", "/")
    return s if len(s) <= n else s[: n - 1] + "…"


def parse_cols(path):
    cols = OrderedDict()
    cur = None
    rn = None
    mode = None
    notes = []
    in_notes = False
    for ln in open(path, encoding="utf-8").read().splitlines():
        if ln.startswith("## Reviewer notes"):
            in_notes = True
            cur = None
            continue
        if in_notes:
            notes.append(ln)
            continue
        if ln.startswith("## Column"):
            m = re.match(r"^## Column ([A-Z]+\d+): ", ln)
            cur = {"head": ln, "rows": OrderedDict()}
            cols[m.group(1)] = cur
            rn = None
            continue
        m = re.match(r"^### R([1-9])\s*$", ln)
        if m and cur is not None:
            rn = int(m.group(1))
            cur["rows"][rn] = {"summary": None, "detail": []}
            mode = None
            continue
        if cur is None or rn is None:
            continue
        if ln.startswith("Summary: "):
            cur["rows"][rn]["summary"] = ln[len("Summary: "):]
        elif ln.strip() == "Detail:":
            mode = "d"
        elif mode == "d" and (ln.startswith("• ") or ln.startswith("  – ")):
            cur["rows"][rn]["detail"].append(ln)
    return cols, notes


def _cl(cols):
    return [cols] if isinstance(cols, str) else list(cols)


def _find(det, sub, top_only=True):
    idx = [i for i, l in enumerate(det) if sub in l and (l.startswith("• ") or not top_only)]
    return idx


def _end(det, i):
    j = i + 1
    while j < len(det) and det[j].startswith("  – "):
        j += 1
    return j


def _bul(x):
    return x if isinstance(x, list) else [x]


def rep(C, cols, row, sub, new, reason, keep_children=False, expect=1):
    """Replace the single top-level bullet containing `sub` (and its sub-bullets unless keep_children)."""
    for c in _cl(cols):
        det = C[c]["rows"][row]["detail"]
        idx = _find(det, sub)
        assert len(idx) == expect, f"{c} R{row}: anchor {sub[:60]!r} matched {len(idx)} lines"
        i = idx[0]
        j = i + 1 if keep_children else _end(det, i)
        before = det[i]
        det[i:j] = _bul(new)
        OPS.append(dict(loc=f"{c} R{row}", kind="replace", before=before, after=_bul(new), reason=reason))


def edit(C, cols, row, sub, old, new, reason):
    """Substring edit inside the single top-level bullet containing `sub`."""
    for c in _cl(cols):
        det = C[c]["rows"][row]["detail"]
        idx = _find(det, sub)
        assert len(idx) == 1, f"{c} R{row}: anchor {sub[:60]!r} matched {len(idx)} lines"
        i = idx[0]
        assert old in det[i], f"{c} R{row}: old text {old[:60]!r} not in line"
        b = det[i]
        det[i] = det[i].replace(old, new, 1)
        OPS.append(dict(loc=f"{c} R{row}", kind="edit", before=old, after=[new], reason=reason))


def ins_after(C, cols, row, sub, new, reason):
    for c in _cl(cols):
        det = C[c]["rows"][row]["detail"]
        idx = _find(det, sub)
        assert len(idx) == 1, f"{c} R{row}: anchor {sub[:60]!r} matched {len(idx)} lines"
        j = _end(det, idx[0])
        det[j:j] = _bul(new)
        OPS.append(dict(loc=f"{c} R{row}", kind="insert", before="(none)", after=_bul(new), reason=reason))


def ins_before(C, cols, row, sub, new, reason):
    for c in _cl(cols):
        det = C[c]["rows"][row]["detail"]
        idx = _find(det, sub)
        assert len(idx) == 1, f"{c} R{row}: anchor {sub[:60]!r} matched {len(idx)} lines"
        i = idx[0]
        det[i:i] = _bul(new)
        OPS.append(dict(loc=f"{c} R{row}", kind="insert", before="(none)", after=_bul(new), reason=reason))


def dele(C, cols, row, sub, reason):
    for c in _cl(cols):
        det = C[c]["rows"][row]["detail"]
        idx = _find(det, sub)
        assert len(idx) == 1, f"{c} R{row}: anchor {sub[:60]!r} matched {len(idx)} lines"
        i = idx[0]
        j = _end(det, i)
        before = det[i]
        del det[i:j]
        OPS.append(dict(loc=f"{c} R{row}", kind="delete", before=before, after=["(deleted)"], reason=reason))


def setsum(C, col, row, text, reason):
    r = C[col]["rows"][row]
    before = r["summary"]
    r["summary"] = text
    OPS.append(dict(loc=f"{col} R{row} Summary", kind="summary", before=before, after=[text], reason=reason))


def editsum(C, col, row, old, new, reason):
    r = C[col]["rows"][row]
    assert old in r["summary"], f"{col} R{row} summary lacks {old[:50]!r}"
    before = r["summary"]
    r["summary"] = before.replace(old, new, 1)
    OPS.append(dict(loc=f"{col} R{row} Summary", kind="summary", before=old, after=[new], reason=reason))


def r9add(C, cols, urls, reason, after=None):
    for c in _cl(cols):
        det = C[c]["rows"][9]["detail"]
        have = {l[2:].strip() for l in det}
        new = [f"• {u}" for u in _bul(urls) if u not in have]
        if not new:
            continue
        if after:
            idx = [i for i, l in enumerate(det) if after in l]
            assert len(idx) == 1, f"{c} R9 after-anchor {after!r}"
            det[idx[0] + 1:idx[0] + 1] = new
        else:
            det.extend(new)
        OPS.append(dict(loc=f"{c} R9", kind="insert", before="(none)", after=new, reason=reason))


def r9sum(C, col, text, reason="R9 Summary updated for added URLs"):
    r = C[col]["rows"][9]
    before = r["summary"]
    r["summary"] = text
    OPS.append(dict(loc=f"{col} R9 Summary", kind="summary", before=before, after=[text], reason=reason))


def serialise_cols(C):
    out = []
    for c, d in C.items():
        out.append(d["head"])
        for n, r in d["rows"].items():
            out.append(f"### R{n}")
            out.append(f"Summary: {r['summary']}")
            out.append("Detail:")
            out.extend(r["detail"])
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


# ---------------------------------------------------------------- inventory
def parse_inv(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    blocks = []
    pre = []
    cur = None
    notes = []
    in_notes = False
    for ln in lines:
        if ln.startswith("## Reviewer notes"):
            in_notes = True
            cur = None
            continue
        if in_notes:
            notes.append(ln)
            continue
        if ln.startswith("## (") :
            cur = {"head": ln, "intro": [], "hdr": None, "rows": []}
            blocks.append(cur)
            continue
        if cur is None:
            pre.append(ln)
            continue
        if ln.startswith("|"):
            if re.fullmatch(r"\|[-:| ]+\|", ln.strip()):
                continue
            cells = [x.strip() for x in ln.strip().strip("|").split(" | ")]
            if cur["hdr"] is None:
                cur["hdr"] = cells
            else:
                cur["rows"].append(cells)
        elif ln.strip():
            cur["intro"].append(ln)
    return pre, blocks, notes


def _col(block, name):
    idx = [i for i, h in enumerate(block["hdr"]) if name.lower() in h.lower()]
    assert len(idx) == 1, f"column {name!r} in {block['head']}: {idx}"
    return idx[0]


def _row(block, key):
    idx = [i for i, r in enumerate(block["rows"]) if key in r[0]]
    assert len(idx) == 1, f"row {key!r} in {block['head']}: {len(idx)} matches"
    return idx[0]


def blk(blocks, letter):
    b = [x for x in blocks if x["head"].startswith(f"## ({letter})")]
    assert len(b) == 1
    return b[0]


def iedit(blocks, letter, rowkey, colname, old, new, reason):
    b = blk(blocks, letter)
    r = _row(b, rowkey)
    c = _col(b, colname)
    cell = b["rows"][r][c]
    assert cell.count(old) == 1, f"({letter}) {rowkey[:30]!r}/{colname}: old {old[:60]!r} count {cell.count(old)}"
    b["rows"][r][c] = cell.replace(old, new, 1)
    IOPS.append(dict(loc=f"({letter}) {rowkey[:45]} / {b['hdr'][c][:30]}", kind="edit", before=old, after=new, reason=reason))


def iapp(blocks, letter, rowkey, colname, text, reason):
    b = blk(blocks, letter)
    r = _row(b, rowkey)
    c = _col(b, colname)
    cell = b["rows"][r][c]
    if colname.lower().startswith("source url"):
        b["rows"][r][c] = cell + " ; " + text.strip()
    else:
        base = cell.rstrip()
        if not base.endswith("."):
            base += "."
        b["rows"][r][c] = base + " " + text.strip()
    IOPS.append(dict(loc=f"({letter}) {rowkey[:45]} / {b['hdr'][c][:30]}", kind="append", before="(none)", after=text, reason=reason))


def iintro(blocks, letter, old, new, reason):
    b = blk(blocks, letter)
    joined = "\n".join(b["intro"])
    assert joined.count(old) == 1, f"({letter}) intro: {old[:60]!r} count {joined.count(old)}"
    b["intro"] = joined.replace(old, new, 1).split("\n")
    IOPS.append(dict(loc=f"({letter}) intro", kind="edit", before=old, after=new, reason=reason))


def iaddrow(blocks, letter, cells, reason, after_key=None):
    b = blk(blocks, letter)
    assert len(cells) == len(b["hdr"]), f"new row has {len(cells)} cells, header {len(b['hdr'])}"
    if after_key is None:
        b["rows"].append(cells)
    else:
        r = _row(b, after_key)
        b["rows"].insert(r + 1, cells)
    IOPS.append(dict(loc=f"({letter}) new row {cells[0][:40]}", kind="new row", before="(none)", after=cells[0], reason=reason))


def serialise_inv(pre_lines, blocks):
    out = list(pre_lines)
    for b in blocks:
        out.append(b["head"])
        out.append("")
        if b["intro"]:
            out.extend(b["intro"])
            out.append("")
        out.append("| " + " | ".join(b["hdr"]) + " |")
        out.append("|" + "|".join(["---"] * len(b["hdr"])) + "|")
        for r in b["rows"]:
            assert len(r) == len(b["hdr"]), (b["head"], r[0][:40], len(r), len(b["hdr"]))
            out.append("| " + " | ".join(r) + " |")
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"
