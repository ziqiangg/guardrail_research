# -*- coding: utf-8 -*-
"""Builds benchtest/drafts/groups_v3.md from the data_*.py modules and groups_v2.md (carried rows).
Run from the repo root:  PYTHONIOENCODING=utf-8 python benchtest/scratchpad/grouper/gen_v3.py
Reads the workbook only through the sheet3.json snapshot taken read-only with openpyxl."""
import json, os, re, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "benchtest"))
sys.path.insert(0, HERE)
from build_eval_sheet import split_row  # parser helper only
import data_multi_a, data_multi_b, data_single_new, data_rationale

OUT = os.path.join(ROOT, "benchtest", "drafts", "groups_v3.md")
MARKER = "Single-product: no comparator among the ten products yet"
ALSO = "Also checked against the later columns (AH to BN): no comparator"
TXT = ["inputs", "truth", "outputs", "metrics", "arch", "diffs"]
HDRS = ["Common test inputs", "Ground truth", "Outputs to capture", "Common metrics",
        "Minimum architecture", "Material differences or limitations"]
S3 = json.load(open(os.path.join(HERE, "sheet3.json"), encoding="utf-8"))
SUFFIX = {"E": " (template example column)"}

# v2 -> v3 carried rows: v3 id -> v2 id
CARRY = {"C12": "C6", "C15": "C7", "C16": "C8", "C17": "C11", "C18": "C12", "C19": "C13", "C20": "C14", "C21": "C15",
         "C22": "C16", "C23": "C17", "C24": "C19", "C25": "C20", "C26": "C21", "C27": "C22", "C28": "C23",
         "C29": "C24"}
# Refs added to carried cells that had none in v2
ADD_REFS = {
 ("C6", "truth"): "I R2, AC R2, AC R6",
 ("C7", "truth"): "J R2, J R5, 3c Datasets",
 ("C8", "truth"): "M R2, M R5", ("C8", "metrics"): "M R5, 3c Tools",
 ("C11", "truth"): "P R2, P R5", ("C11", "metrics"): "P R5, 3c Published results",
 ("C12", "truth"): "O R2, O R5", ("C12", "metrics"): "O R5, 3c Published results",
 ("C13", "truth"): "Q R2, Q R5", ("C13", "metrics"): "Q R5, 3c Published results",
 ("C14", "truth"): "R R2, R R5", ("C14", "metrics"): "R R5, 3c Published results",
 ("C15", "truth"): "U R2, U R5", ("C15", "metrics"): "U R5, 3c Tools",
 ("C16", "truth"): "S R2, S R5",
 ("C20", "truth"): "Y R2, Y R5",
 ("C21", "truth"): "Z R2, Z R5", ("C21", "metrics"): "Z R5, Z R8",
 ("C22", "truth"): "Z R2, Z R3", ("C22", "metrics"): "Z R5, Z R8",
 ("C23", "truth"): "AD R2, AD R5", ("C23", "metrics"): "AD R5, AD R8",
 ("C24", "truth"): "AE R2, AE R5", ("C24", "metrics"): "AE R5, AE R8",
}
# Small additions to carried rows (v3 id, cell) -> (bullet, ref)
ADD_BULLET = {
 ("C25", "inputs"): ("Possible seed: CyberSecEval interpreter set, 500 prompts in five attack types", "3k Datasets"),
 ("C29", "inputs"): ("Litmus refusal-based tests could suggest themes; it publishes no prompts", "3n Reuse"),
}
# cross-references to renumbered groups inside carried text
XREF = {"C24": [("Input side is C18", "Input side is C13 (with AS)"), ("Same limits as C18", "Same limits as C13")],
        "C26": [("Response side is C22", "Response side is C27")],
        "C27": [("Input side is C21", "Input side is C26"), ("Same limits as C21", "Same limits as C26")]}


def v2_rows():
    lines = open(os.path.join(ROOT, "benchtest", "drafts", "groups_v2.md"), encoding="utf-8").read().splitlines()
    out = {}
    for l in lines:
        if re.match(r"\| C\d+ ", l):
            cells = [c.strip() for c in split_row(l)]
            if len(cells) == 8:
                cid = cells[0].split()[0]
                if cid not in out:
                    out[cid] = cells
    return out


V2 = v2_rows()


def split_cell(txt):
    parts = [x.strip() for x in txt.split("<br>")]
    refs = []
    if parts and parts[-1].startswith("Refs: "):
        refs = [r.strip() for r in parts.pop()[6:].split(",")]
    return [p[2:] if p.startswith("• ") else p for p in parts], refs


def carried(v3, v2):
    cells = V2[v2]
    name = cells[0].split(" ", 1)[1]
    funcs = [f.split(":", 1)[0].strip() for f in cells[1].split("; ")]
    g = dict(name=name, funcs=funcs)
    for i, k in enumerate(TXT):
        b, r = split_cell(cells[2 + i])
        if k == "diffs" and b and b[0].startswith("Single-product:"):
            b = b[1:]
        for old, new in XREF.get(v3, []):
            b = [x.replace(old, new) for x in b]
        if (v3, k) in ADD_BULLET:
            b = b + [ADD_BULLET[(v3, k)][0]]
            r = r + [ADD_BULLET[(v3, k)][1]]
        if not r:
            r = [x.strip() for x in ADD_REFS[(v2, k)].split(",")]
            USED.append((v2, k))
        g[k] = (b, r)
    return g


USED = []
GROUPS = {}
GROUPS.update(data_multi_a.G)
GROUPS.update(data_multi_b.G)
GROUPS.update(data_single_new.G)
for v3, v2 in CARRY.items():
    GROUPS[v3] = carried(v3, v2)
ORDER = [f"C{i}" for i in range(1, 35)]
NMULTI = 14
assert set(ORDER) == set(GROUPS), set(ORDER) ^ set(GROUPS)
for i, cid in enumerate(ORDER):
    single = i >= NMULTI
    d = GROUPS[cid]
    if single:
        b, r = d["diffs"]
        b = [x for x in b if not x.startswith("Single-product:")]
        d["diffs"] = ([MARKER] + b, r)
    d["single"] = single


def hdr(letter):
    return S3[letter]["hdr"] + SUFFIX.get(letter, "")


def cell_md(d, k):
    b, r = d[k]
    return "<br>".join(["• " + x for x in b] + ["Refs: " + ", ".join(r)])


def table():
    out = ["| Candidate group | Guardrail functions included | " + " | ".join(HDRS) + " |",
           "|" + "---|" * 8]
    for cid in ORDER:
        d = GROUPS[cid]
        row = [f"{cid} {d['name']}", "; ".join(f"{L}: {hdr(L)}" for L in d["funcs"])]
        row += [cell_md(d, k) for k in TXT]
        out.append("| " + " | ".join(row) + " |")
    return out


def col_index(letter):
    n = 0
    for ch in letter:
        n = n * 26 + ord(ch) - 64
    return n


def col_letter(n):
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


ALL = [col_letter(n) for n in range(5, 67)]
ALL = [x for x in ALL if x in S3]
assert len(ALL) == 62, len(ALL)


def membership():
    m = {L: [] for L in ALL}
    for cid in ORDER:
        for L in GROUPS[cid]["funcs"]:
            m[L].append(cid)
    return m


def rationale():
    out = []
    R = data_rationale.R
    SING = data_rationale.SINGLES
    for cid in ORDER:
        d = GROUPS[cid]
        out.append(f"### {cid} {d['name']}")
        out.append("")
        out.append("Functions: " + ", ".join(d["funcs"]) + (" (single product)" if d["single"] else f" ({len(d['funcs'])} functions)"))
        out.append("")
        if cid in R:
            r = R[cid]
            for lab, mark, text in r["crit"]:
                out.append(f"- {lab} {mark}: {text}")
            out.append("- Checked and left out: " + " ".join(r["left"]))
            out.append("- Recorded open items (listed, not decided): " + " ".join(r["terms"]))
        else:
            letter, partner = SING[cid]
            f = d["funcs"][0] if len(d["funcs"]) == 1 else d["funcs"][0]
            out.append(f"- Test inputs {data_rationale.Y}, ground truth {data_rationale.Y}, metrics {data_rationale.Y}, minimum architecture {data_rationale.Y}: met within the function itself (sheet 3 {d['funcs'][0]} R3, R5, R6, R7).")
            out.append(f"- Why it has no partner {data_rationale.N}: {partner}")
            terms = data_rationale.SINGLE_TERMS.get(cid, "none beyond those in the Material differences cell and column " + d["funcs"][0] + " R8.")
            out.append("- Recorded open items (listed, not decided): " + terms)
        out.append("")
    return out


from part_de import part_de


def main():
    mem = membership()
    multi = [c for c in ORDER[:NMULTI]]
    single = [c for c in ORDER[NMULTI:]]
    L = []
    L.append("# Sheet 4 — Candidate Comparison Groups (draft v3, bulleted)")
    L.append("")
    L.append("Regrouped once across all ten products (R006), from the sheet 3 columns E to BN. Bench content in new and changed rows (columns C to G) is "
             "worded as proposals (R032); rows carried from v2 keep their v2 wording (see D2). Nothing here decides the bench design. Evaluation tools CyberSecEval (3k) and Litmus (3n) have no "
             "sheet 3 columns and are cited only as possible sources of test inputs or ground truth.")
    L.append("")
    L.append("## A. Group table")
    L.append("")
    L.append(f"Bands applied by the builder: C1 to C{NMULTI} are comparison groups (2+ products); C{NMULTI + 1} to C{len(ORDER)} are single-product functions (no comparator yet).")
    L.append("")
    L += table()
    L.append("")
    L.append("## B. Rationale per group")
    L.append("")
    L.append("Criteria are the docx section 4 tests: same type of test inputs, same ground truth, same or comparable metrics, common minimum architecture. "
             "A tick means the members meet it; a cross marks the criterion that keeps a candidate out. Input and output are separate groups (R002); a "
             "function that takes any string is listed in each side it applies to. References are sheet 3 column and row (for example AH R5) or inventory/evaluation sheet sections.")
    L.append("")
    L += rationale()
    L.append("## C. Accounting of sheet 3 columns")
    L.append("")
    L.append("| Sheet 3 column | Function (sheet 3 row 3) | Groups listing it |")
    L.append("|---|---|---|")
    for x in ALL:
        L.append(f"| {x} | {S3[x]['hdr']} | {', '.join(mem[x])} |")
    L.append("")
    nm = sum(len(v) > 1 for v in mem.values())
    L.append(f"Totals: {len(ALL)} functions (E to BN); {sum(1 for v in mem.values() if not v)} in no group; {nm} in more than one group; "
             f"{len(ORDER)} groups ({len(multi)} multi-product, {len(single)} single-product).")
    L.append("")
    L += part_de(mem, GROUPS, ORDER, NMULTI, USED, ADD_BULLET, CARRY)
    open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
    return mem


if __name__ == "__main__":
    mem = main()
    print("groups", len(ORDER))
