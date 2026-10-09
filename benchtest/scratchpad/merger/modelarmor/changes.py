"""Generate modelarmor_changes.md and modelarmor_summaries_preview.md (run from the repo root after build.py)."""
import json
import re
import subprocess
import sys
from collections import Counter, OrderedDict, defaultdict

sys.path.insert(0, "benchtest/scratchpad/merger/modelarmor")
sys.path.insert(0, "benchtest/tools")
import lib
from check_drafts import words, LABEL

DR = "benchtest/drafts/"
ops = json.load(open("benchtest/scratchpad/merger/modelarmor/ops.json", encoding="utf-8"))
OPS, IOPS = ops["ops"], ops["iops"]
C, _ = lib.parse_cols(DR + "modelarmor_two_level.md")
HEAD = {c: re.sub(r"^## Column MA\d+: ", "", d["head"]) for c, d in C.items()}


def cell(s):
    return s.replace("|", "/").replace("\n", " ")


def sh(s, n=110):
    s = re.sub(r"\s+", " ", s).replace("**", "").replace("|", "/").strip()
    return s if len(s) <= n else s[: n - 1] + "…"


# ------------------------------------------------------------------ preview
def write_preview():
    out = ["# Model Armor: Summary preview (CP2)", "",
           "Generated from modelarmor_two_level.md. Word counts exclude the trailing bold label (limit 45; R7 60). Bullets = top-level Detail bullets (sub-bullets are not counted). Summaries changed at merge are marked [changed at merge] and listed in modelarmor_changes.md, section 2b.", ""]
    changed = {(o["loc"].split()[0], int(o["loc"].split()[1][1:])) for o in OPS if o["kind"] == "summary"}
    for c, d in C.items():
        out.append(f"## {c}: {HEAD[c]}")
        out.append("")
        for n, r in d["rows"].items():
            nb = len([l for l in r["detail"] if l.startswith("• ")])
            mark = " [changed at merge]" if (c, n) in changed else ""
            out.append(f"- **R{n}**{mark} ({words(r['summary'])}w, {nb} bullets): {r['summary']}")
        out.append("")
    open(DR + "modelarmor_summaries_preview.md", "w", encoding="utf-8").write("\n".join(out))


# ------------------------------------------------------------------ section 2 (grouped ops)
def section2():
    groups = OrderedDict()
    for o in OPS:
        col, rest = o["loc"].split(" ", 1)
        row = rest
        wide = 420 if o["kind"] == "summary" else 110
        key = (rest, o["kind"], sh(o["before"], wide) if isinstance(o["before"], str) else "", tuple(sh(a, wide) for a in o["after"][:1]), len(o["after"]), o["reason"])
        groups.setdefault(key, []).append(col)
    # order by column number then row
    def colnum(k):
        return int(k[2:])
    per_col = defaultdict(list)
    for key, cols in groups.items():
        per_col[colnum(sorted(cols, key=colnum)[0])].append((key, cols))
    lines = []
    for n in range(1, 11):
        pass
    # one table: rows grouped, identical changes across columns listed together
    lines.append("| Location | Kind | Before (shortened) | After (shortened) | Reason |")
    lines.append("|---|---|---|---|---|")
    rows = []
    for key, cols in groups.items():
        rest, kind, before, after1, nafter, reason = key
        cols_sorted = sorted(set(cols), key=colnum)
        rown = int(re.match(r"R(\d)", rest).group(1))
        rows.append((colnum(cols_sorted[0]), rown, cols_sorted, rest, kind, before, after1, nafter, reason))
    rows.sort(key=lambda x: (x[0], x[1]))
    for _, _, cols, rest, kind, before, after1, nafter, reason in rows:
        loc = f"{', '.join(cols)} {rest}"
        after = after1[0] if after1 else ""
        if nafter > 1:
            after += f" (+{nafter - 1} more)"
        lines.append(f"| {cell(loc)} | {kind} | {cell(before)} | {cell(after)} | {cell(reason)} |")
    return "\n".join(lines), len(rows)


def section3():
    groups = OrderedDict()
    for o in IOPS:
        groups.setdefault((o["loc"], o["kind"], sh(o["before"]) if isinstance(o["before"], str) else "", sh(o["after"] if isinstance(o["after"], str) else str(o["after"]), 140), o["reason"]), 1)
    by_block = defaultdict(list)
    for (loc, kind, before, after, reason) in groups:
        b = loc[1] if loc.startswith("(") else "scope"
        by_block[b].append(f"| {cell(loc)} | {kind} | {cell(before)} | {cell(after)} | {cell(reason)} |")
    names = {"scope": "Scope paragraph (not parsed)", "a": "(a) Filters and detectors", "b": "(b) Integration paths", "c": "(c) Template and floor-setting parameters", "d": "(d) Locations and feature availability", "e": "(e) Quotas, limits and pricing"}
    out = []
    for b in ["scope", "a", "b", "c", "d", "e"]:
        out.append(f"### {names[b]}")
        out.append("")
        out.append("| Location (row / column) | Kind | Before (shortened) | After (shortened) | Reason |")
        out.append("|---|---|---|---|---|")
        out.extend(by_block[b])
        out.append("")
    return "\n".join(out)


# ------------------------------------------------------------------ triage table parse
def triage_rows():
    t = open(DR + "modelarmor_triage.md", encoding="utf-8").read()
    rows = OrderedDict()
    for m in re.finditer(r"^\| (T\d+) \| (.*?) \| (.*?) \| ([abc])( \(honest gap\))? \| (.*?) \| ([HML]) \|$", t, re.M):
        rows[m.group(1)] = dict(item=m.group(2), loc=m.group(3), cls=m.group(4) + (" (honest gap)" if m.group(5) else ""), pri=m.group(7))
    assert len(rows) == 87, len(rows)
    return rows


STATE = {
    "T1": ("OPEN", "R8 MA1, MA2 (default level; R8 wording now lists the three documented statements); R5 To be verified bullet; INV(a) RAI Default"),
    "T2": ("RESOLVED (documentation half)", "applied: MA1, MA2 R5 (floor-settings bullet, three-default bullet, MA1 R5 Summary); effective default stays T1"),
    "T3": ("PARTLY RESOLVED", "applied: MA3, MA4 R5 (floor default Documented; template default Inferred), INV(a), INV(c); live default in R8 MA3, MA4"),
    "T4": ("RESOLVED (documentation half)", "applied: MA3, MA4 R5 (statement D, Summaries), INV(a), INV(c); trade-off stays T5"),
    "T5": ("OPEN", "R8 MA3, MA4 (which level to use)"),
    "T6": ("OPEN", "R5 To be verified bullets and R8 in MA1, MA2, MA3, MA4; INV(a) Result field"),
    "T7": ("OPEN", "MA4 R5 To be verified bullet, R7, R8"),
    "T8": ("OPEN", "MA2 R5 Detail and R8; the MA2 R5 Summary no longer leads with the sample (style 3c)"),
    "T9": ("RESOLVED (documentation half)", "applied: MA1, MA2 R1 Summary and R2 (four bullets), INV(a) CSAM Default, INV(d) intro; observation stays T10"),
    "T10": ("OPEN", "R8 MA1, MA2 (CSAM in a limited-support location)"),
    "T11": ("PARTLY RESOLVED", "applied: MA1 R3, MA3 R3, MA7 R2, MA8 R2 (quote Documented, filter use Not disclosed), INV(a); test stays T12"),
    "T12": ("OPEN", "R8 MA1, MA3, MA7, MA8, MA10"),
    "T13": ("RESOLVED", "applied: MA4 R1 Summary and Inferred bullet; positive example stays T14"),
    "T14": ("OPEN", "MA4 R1 Not disclosed bullet, R2, R4, R8"),
    "T15": ("OPEN (honest gap)", "MA3, MA4 R2 Not disclosed bullets, R8"),
    "T16": ("CORRECTION applied", "MA2, MA4, MA8 R3, R6, R8, R9 and MA2 R3 Summary; the Go-only claim is gone"),
    "T17": ("OPEN (honest gap)", "MA2, MA4, MA6, MA8 Not disclosed bullets and R8"),
    "T18": ("PARTLY RESOLVED", "applied: MA3, MA4 R4 (Go and Java labelled, lag Inferred), R9; INV(b), INV(c)"),
    "T19": ("PARTLY RESOLVED", "applied: MA3, MA4 R5 (four bullets), INV(c); live acceptance To be verified (R8 MA3, MA4)"),
    "T20": ("RESOLVED", "applied: A R4 x6, MA5, MA6 R4, INV(b); MA6 R8 bullet deleted"),
    "T21": ("OPEN (To be verified, main ruling)", "A R4 x6 and INV(b) Service Extensions: GA date for other load balancers and Secure Web Proxy; Service Extensions page unread (verbatim retry is a P7 option)"),
    "T22": ("RESOLVED", "applied: A R4 x6 (pair), INV(b) MCP, INV(c) floor inline"),
    "T23": ("PARTLY RESOLVED", "applied: INV scope paragraph (rule S premise, banner-free rule); 21 GA [Inferred] cells kept; Terraform, gcloud, console, SCC findings stay Not disclosed"),
    "T24": ("PARTLY RESOLVED", "applied: INV(b) Terraform row (names Documented, stage Not disclosed, arguments To be verified)"),
    "T25": ("PARTLY RESOLVED", "applied: INV(b) client libraries row; one short R4 bullet in A columns (main ruling)"),
    "T26": ("PARTLY RESOLVED", "applied: MA5, MA6 R4, INV(b) x3; forwarding of de-identified text Not disclosed"),
    "T27": ("OPEN (honest gap)", "R4 Not disclosed bullets and R8, MA1 to MA4"),
    "T28": ("OPEN (honest gap)", "MA7, MA8 R2, R4, R8"),
    "T29": ("OPEN (honest gap)", "MA9, MA10 R4 (Summaries relabelled Not disclosed), R8"),
    "T30": ("OPEN", "Not disclosed bullets and R8 in every column"),
    "T31": ("OPEN (honest gap)", "R8 latency bullets"),
    "T32": ("OPEN", "R8 MA1, MA2, MA3"),
    "T33": ("PARTLY RESOLVED", "applied: MA1 to MA4 R2 (two bullets); five locations Not disclosed"),
    "T34": ("OPEN", "MA4 R7, R8"),
    "T35": ("OPEN", "MA1, MA2 R2 (scenario Documented, topicality Documented, configuration Not disclosed, SDP route Inferred), R8; INV(a) intro"),
    "T36": ("PARTLY RESOLVED", "applied: MA2 R2 (absence Not disclosed, two product-page quotes, Inferred reading), MA4 R2, INV(a) intro"),
    "T37": ("RESOLVED", "applied: MA7 R1 Summary and bullets, R8"),
    "T38": ("OPEN", "MA7, MA8 R2 Inferred bullet, R7, R8"),
    "T39": ("OPEN", "MA7, MA8 R2 Not disclosed bullet, R7, R8"),
    "T40": ("OPEN", "MA8 R3 Inferred bullet, R7, R8"),
    "T41": ("PARTLY RESOLVED", "applied: MA5, MA6 R2 (six, seven, Go comment, no reconciliation Not disclosed), INV(a); live list stays T42"),
    "T42": ("OPEN", "MA5, MA6 R8, INV(a)"),
    "T43": ("OPEN", "MA5 R2 Not disclosed + Inferred bullet, R8; INV(a) SDP basic"),
    "T44": ("PARTLY RESOLVED", "applied: MA6 R2 (Summary now Not disclosed; four bullets), R8, R9, INV(a); basic list on responses needs a test"),
    "T45": ("PARTLY RESOLVED", "applied: MA6 R3 (Summary now Not disclosed), R8, INV(a); response-side result shape needs a test"),
    "T46": ("OPEN", "MA5 R5 Inferred bullet, R8"),
    "T47": ("RESOLVED (code at the tag; live check open)", "applied: MA5, MA6 R5, MA5 R8; one test call would confirm the shape"),
    "T48": ("OPEN", "MA5 R5 Not disclosed bullet, R8; INV(a)"),
    "T49": ("OPEN", "R8 MA5, MA6, MA10 (checked list extended)"),
    "T50": ("PARTLY RESOLVED", "applied: MA5 R6 (four bullets), R8, R9; location rule Not disclosed"),
    "T51": ("OPEN (honest gap)", "MA5, MA6 R6 Not disclosed bullets, R8"),
    "T52": ("CORRECTION applied", "MA1 to MA4 R6, MA5, MA6 R5, R6 (Summaries), MA9 R5, INV(a), INV(e)"),
    "T53": ("PARTLY RESOLVED", "applied: MA5, MA6 R6, MA5 R8, INV(b) x4; other routes Not disclosed"),
    "T54": ("RESOLVED", "applied: MA1 to MA4, MA5, MA6 (chunk caveat in three bullets)"),
    "T55": ("CORRECTION applied", "MA5 R7, MA6 R7, R9"),
    "T56": ("RESOLVED", "applied: MA5, MA6, MA10 R1 (link bullet Documented, scope bullet Inferred)"),
    "T57": ("PARTLY RESOLVED", "applied: MA9 R1 (Not disclosed), MA7, MA8 R2, INV(a); antivirus stays inventory only (R017 item 2)"),
    "T58": ("OPEN", "MA9, MA10 R2 (three pages, Not disclosed), INV(a) OCR Limit; test stays T59"),
    "T59": ("OPEN", "MA9, MA10 R8"),
    "T60": ("OPEN", "MA10 R3 (two lists + Not disclosed), R8, INV(b)"),
    "T61": ("OPEN (R017 item 3: no split)", "MA9, MA10 R3, R7, R8 and the other places listed in the triage; unchanged"),
    "T62": ("OPEN", "MA9 R2 Not disclosed, R8"),
    "T63": ("OPEN", "MA9 R5, R6, R8; MA10 R6; INV(e)"),
    "T64": ("OPEN", "MA9, MA10 R2 Not disclosed, R8"),
    "T65": ("OPEN (honest gap)", "MA9, MA10 R4 Not disclosed, R8"),
    "T66": ("PARTLY RESOLVED", "applied: MA9 R2 (four bullets), R8, R9, INV(a)"),
    "T67": ("RESOLVED", "applied: MA9 R2 (Go comment, Inferred typo)"),
    "T68": ("PARTLY RESOLVED", "applied: MA9 R5 (Inferred label-to-container reading, Go ByteDataItem), R8"),
    "T69": ("OPEN (honest gap)", "MA9 R3 bullet, R8; INV(b) LangChain"),
    "T70": ("RESOLVED (list per REST and code; live check open)", "applied: MA10 R5, R8, INV(a)"),
    "T71": ("PARTLY RESOLVED", "applied: MA10 R5 (SDP API field Documented, Model Armor placement Not disclosed), R8, R9"),
    "T72": ("OPEN (honest gap)", "MA10 R2, R8"),
    "T73": ("OPEN", "MA10 R2, R6, R8"),
    "T74": ("OPEN (honest gap)", "MA10 R8; INV(a)"),
    "T75": ("OPEN", "MA10 R6; INV(e) Images per request"),
    "T76": ("PARTLY RESOLVED", "applied: MA9 R6, MA10 R6 (two Documented bullets, Inferred explicit-value reading); INV(c) unchanged"),
    "T77": ("RESOLVED", "applied: INV(d) 20 rows, intro; MA7, MA8 R8"),
    "T78": ("CORRECTION applied", "MA3, MA4 R2 (dated 2026-10-09), MA3 R8; INV scope paragraph; effect on ordinary prompts stays in R8 MA3 (class b)"),
    "T79": ("RESOLVED", "applied: A R4 x6 (three bullets), MA5, MA6 R4, INV(c)"),
    "T80": ("CORRECTION applied", "INV scope paragraph; brief claim recorded in section 1"),
    "T81": ("RESOLVED", "applied: INV(b) SCC findings row"),
    "T82": ("RESOLVED", "applied: A R4 x6 (split bullets + allowance scope Not disclosed), INV(e)"),
    "T83": ("RESOLVED (bookkeeping)", "block counts 10 / 15 / 16 / 20 / 16 (section 7c)"),
    "T84": ("RESOLVED", "naming bullet in the first route-listing row of every column"),
    "T85": ("RESOLVED (R017 item 5)", "applied: MA10 R4, R7; MA3, MA4 R5; INV scope paragraph only (main ruling)"),
    "T86": ("PARTLY RESOLVED; USER QUESTION OPEN at CP2", "applied: R7, R8, R9 of MA1, MA2, MA3, MA4, MA7, MA8, MA10: AUP clause Documented, express permission Not disclosed"),
    "T87": ("RESOLVED", "applied: INV(b) client libraries and Apigee rows"),
}


def section5():
    tr = triage_rows()
    out = ["| Id | Item (triage, shortened) | Class | Pri | Status at merge | Where it stands |", "|---|---|---|---|---|---|"]
    for t, r in tr.items():
        st, where = STATE[t]
        out.append(f"| {t} | {cell(sh(r['item'], 100))} | {r['cls']} | {r['pri']} | {cell(st)} | {cell(where)} |")
    return "\n".join(out), tr


# ------------------------------------------------------------------ self-check tables
def self_checks():
    cols = list(C)
    t = ["| Column | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 |", "|---|---|---|---|---|---|---|---|---|---|"]
    mx = 0
    over = 0
    nsum = 0
    for c, d in C.items():
        vals = []
        for n in range(1, 10):
            w = words(d["rows"][n]["summary"])
            vals.append(str(w))
            nsum += 1
            lim = 60 if n == 7 else 45
            if w > lim:
                over += 1
            mx = max(mx, w)
        t.append(f"| {c} | " + " | ".join(vals) + " |")
    text = open(DR + "modelarmor_two_level.md", encoding="utf-8").read()
    labs = Counter(re.findall(r"\*\*\[((?:Documented|Inferred|To be verified|Not disclosed)[^\]]*)\]\*\*", text))
    lab_rows = ["| Label | Count |", "|---|---|"]
    for k, v in sorted(labs.items(), key=lambda x: (-x[1], x[0])):
        lab_rows.append(f"| [{k}] | {v} |")
    lab_rows.append(f"| Total | {sum(labs.values())} |")
    sumlabs = Counter()
    for c, d in C.items():
        for n in range(1, 8):
            m = re.search(r"\*\*\[([^\]]+)\]\*\*\s*$", d["rows"][n]["summary"])
            sumlabs[m.group(1)] += 1
    nbul = sum(len([l for l in r["detail"] if l.startswith("• ")]) for d in C.values() for r in d["rows"].values())
    nsub = sum(len([l for l in r["detail"] if l.startswith("  – ")]) for d in C.values() for r in d["rows"].values())
    return "\n".join(t), nsum, mx, over, "\n".join(lab_rows), sumlabs, nbul, nsub


def run_check(args):
    p = subprocess.run([sys.executable, "benchtest/tools/check_drafts.py"] + args, capture_output=True, text=True, encoding="utf-8")
    res = [l for l in p.stdout.splitlines() if l.startswith("RESULT") or l.startswith("ERROR") or l.startswith("WARN")]
    return p.returncode, res, [l for l in p.stdout.splitlines() if l.startswith("table")]


def main():
    write_preview()
    s2, ngroups = section2()
    s3 = section3()
    s5, tr = section5()
    sc_tab, nsum, mx, over, lab_tab, sumlabs, nbul, nsub = self_checks()
    rc1, res1, _ = run_check(["columns", DR + "modelarmor_two_level.md", "--final", "--expect", "10"])
    rc2, res2, tables = run_check(["inventory", DR + "modelarmor_inventory_final.md", "--headers", DR + "modelarmor_two_level.md"])
    draftB = open(DR + "modelarmor_cols_b.md", encoding="utf-8").read()
    nread = len(re.findall(r"read 2026-10-09", draftB))
    kinds = Counter(o["kind"] for o in OPS)
    ins_bul = sum(len(o["after"]) for o in OPS if o["kind"] == "insert")
    rep_in = sum(1 for o in OPS if o["kind"] == "replace")
    rep_out = sum(len(o["after"]) for o in OPS if o["kind"] == "replace")
    summ_main = sorted({o["loc"] for o in OPS if o["kind"] == "summary" and not o["loc"].endswith("R9 Summary")})
    summ_r9 = sorted({o["loc"] for o in OPS if o["kind"] == "summary" and o["loc"].endswith("R9 Summary")})
    ikinds = Counter(o["kind"] for o in IOPS)
    notes_a, notes_b, notes_i = ops["notes_a"], ops["notes_b"], ops["notes_i"]

    L = []
    A = L.append
    A("# Model Armor merge: change log (P6)")
    A("")
    A("Date 2026-10-09 (system date 20261009). Merger: gr-merger. Inputs merged: modelarmor_brief.md (context only), modelarmor_cols_a.md (MA1 to MA4, MA7, MA8), modelarmor_cols_b.md (MA5, MA6, MA9, MA10), modelarmor_inventory.md (tables a to e), modelarmor_triage.md (T1 to T87, 3 classes), modelarmor_resolutions_1.md (22 items), modelarmor_resolutions_2.md (32 items), the rulings R002, R011, R012, R013, R015, R017 (CP1), R019, R020, and the resolved-question rows for modelarmor in scratchpad/main/queue.md. Outputs: modelarmor_two_level.md (10 columns), modelarmor_inventory_final.md (5 tables), modelarmor_summaries_preview.md, modelarmor_changes.md (this file). No source file was modified and no new web research was done; every added fact is in a resolution file or in a queue ruling. The merge was applied by scripts kept in benchtest/scratchpad/merger/modelarmor/ (lib.py, edits_a.py, edits_b.py, edits_inv.py, build.py, changes.py); every edit asserts that its anchor text exists exactly once.")
    A("")
    A("Reason codes: Tn = triage id; \"style n\" = Style issues in columns (modelarmor_triage.md); \"hygiene\" = Label hygiene table; \"main ruling\" = scratchpad/main/queue.md Resolved questions. In the tables below bold markers are dropped from quoted bullet text and long text is shortened.")
    A("")
    A("## 0. Headline numbers (for the P8 config and the report)")
    A("")
    A("- Columns: 10 (MA1 to MA10), prefix `Model Armor:`, headers exactly as in the brief. Antivirus scanning and tool-call screening (MCP, Agent Gateway ingress and egress) are inventory only (R017 items 1 and 2); no MA11.")
    A("- Inventory BLOCKS for the P8 config module: (a) 10, (b) 15, (c) 16, (d) 20, (e) 16 data rows (columns 10, 9, 7, 12, 6). The `markers` tuple must include `— (legacy, not in Table 3)`, `— (planned, not in Table 3)` and `— (inventory only, not in Table 3)` (R011). Eight rows carry the inventory-only marker: Antivirus scanning in (a); gcloud, Terraform, Agent Gateway egress, MCP servers, Security Command Center findings, console, monitoring dashboard in (b). The sheet letter is assigned at P8 (R003); the brief's 3f is provisional.")
    A(f"- Column edits: {len(OPS)} operations ({kinds['insert']} insertions adding {ins_bul} bullets, {kinds['replace']} replacements turning {rep_in} bullets into {rep_out}, {kinds['delete']} deletions, {kinds['edit']} in-line edits, {kinds['summary']} Summary changes). In the section 2 table identical changes across columns are merged into one row ({ngroups} rows).")
    A(f"- Inventory edits: {len(IOPS)} operations ({ikinds['edit']} in-cell edits, {ikinds['append']} appends, {ikinds['new row']} new rows), including the scope paragraph.")
    A(f"- Summaries changed: {len(summ_main)} in R1 to R8 and {len(summ_r9)} R9 lines (full list in section 2b).")
    A("- Pin: all google-cloud-go code facts now cite tag `modelarmor/v1.3.0` (commit 8a17bee2); see section 1.")
    A("")
    A("## 1. Global changes")
    A("")
    A("| Scope | Before | After | Reason |")
    A("|---|---|---|---|")
    G = [
        ("Every google-cloud-go citation (R1 to R7 labels, line references, R9 URLs, inventory cells)", "`[Documented: repo googleapis/google-cloud-go@37f936ac]`, `service.pb.go@37f936ac:NNN`, blob URLs with the full sha 37f936ac9d69e173da0ba4123e382c52b2dd741f (HEAD of 2026-10-08)", "`[Documented: repo googleapis/google-cloud-go@modelarmor/v1.3.0]`, `service.pb.go@modelarmor/v1.3.0:NNN`, blob URLs `.../blob/modelarmor/v1.3.0/...`. Line numbers were kept for service.pb.go because resolver 1 recorded `git diff` between the tag (8a17bee208939e0166936a59675414439c47e341) and 37f936ac as touching only apiv1/model_armor_client.go, apiv1beta/model_armor_client.go, go.mod and go.sum; CHANGES.md, version.go, LICENSE and both service.pb.go files are therefore identical. The merger confirmed the tag sha with `git ls-remote --tags` (8a17bee2…) but could not re-read the files at the tag: a sparse clone was refused by the permission layer and was not worked around. The INV scope paragraph names both refs.", "main ruling (modelarmor P5 r1 Q1); README section 3 rule 8"),
        ("Hint style in cols_b (MA5, MA6, MA9, MA10)", f"(overview, read 2026-10-09) ({nread} occurrences of 'read 2026-10-09')", "(overview, 2026-10-09), the form used in cols_a", "triage Label hygiene 'Hint style differs'"),
        ("R7 first Detail bullet in MA1 to MA4, MA7, MA8", "full stop before the label ('... entry. **[Inferred]**')", "no full stop before the label (MA5, MA6, MA9, MA10 already complied)", "style 10"),
        ("Reviewer notes in cols_a, cols_b and the inventory (22 + 29 + 24 lines)", "present in the drafts", "removed from all finals; kept verbatim in section 6", "README section 4 (finals carry no Reviewer notes)"),
        ("R4 'Release status of routes' bullet in MA1 to MA4, MA7, MA8", "one [Documented] bullet holding seven routes", "a parent bullet with seven sub-bullets (one per route, shared label); the MCP floor-settings '(Preview)' label as its own bullet; Apigee and Service Extensions as separate bullets", "hygiene 'One bullet, several facts'; T20, T21, T22"),
        ("R4 pricing and data-handling bullets in MA1 to MA4, MA7, MA8", "one bullet each holding two or three facts", "pricing: three bullets (standalone, Security Command Center, allowance scope Not disclosed); data handling: three bullets (stateless, logging page, overview wording)", "hygiene 'One bullet, several facts'; T79, T82"),
        ("Route naming (all ten columns)", "'Agent Platform', 'Agent Runtime', 'Gemini Enterprise' used side by side", "one Documented naming bullet before the first route list of each column (full name once, short form after)", "style 9; T84 (placed in R3 of MA1 to MA4, MA7, MA8, MA9, MA10 and R4 of MA5, MA6, where each column first lists routes)"),
        ("R4 Summaries of MA5, MA9, MA10 (label); MA9 R3, MA10 R3 (label); MA6 R2, MA6 R3 (label)", "**[Documented]** although the Summary states an absence ('The detectors are not described', 'The OCR engine is not disclosed', 'no response example')", "**[Not disclosed]** (weakest label wins); in MA5 R3, MA5 R5, MA6 R5, MA9 R5, MA10 R5 the absence clause was deleted instead because the gap stays in Detail and R8 and the clause is not central", "style 1, style 2, README section 3 rule 5"),
        ("Code terms in Summaries (MA9 R3, R6; MA10 R3, R6)", "'byte item', 'byte data type', 'typed IMAGE', 'must be IMAGE'", "'data item', 'file type', 'image type', 'data type must be image'", "style 5"),
        ("R9 lines", "URL sets drafted per column", "URLs added where a new bullet cites a page (Apigee release notes, sanitizeModelResponse method page, Go apiv1beta and Java proto, SDP infoTypes, metadata-label and image-redaction pages, FloorSetting reference, apigee-samples shared flow, Google terms pages, products page, blog for MA1 to MA4); R9 Summary lines rewritten to match", "T16, T18, T20, T44, T50, T55, T66, T71, T85, T86; hygiene 'R9 omits a URL'"),
        ("Corrections of draft claims", "A: userPrompt documented only by the Go client; B/A: 'Text over 130,000 tokens is skipped'; MA5/MA6 R7: Singapore NRIC needs a custom detector; release-note entry 'October 10, 2026'; INV intro: every footer 2026-10-06", "userPrompt is in the REST method reference and the Apigee policy page (T16); a match is still returned over the limit, EXECUTION_SKIPPED only when no match (T52); NRIC is a built-in infoType, no custom detector (T55); the entry is dated 2026-10-09 (T78); page footers listed per page (T80). The brief carries the same blanket footer claim (every page 2026-10-06 except release notes); the brief is not a final source and is not edited.", "T16, T52, T55, T78, T80 (CORRECTION verdicts)"),
        ("Release-note date (T78)", "'Release note 2026-10-10 (entry dated 2026-10-10 present on 2026-10-09)' in MA3, MA4 R2; R8 MA3; INV Reviewer note 2; A Reviewer note 11 (C9)", "dated 2026-10-09 in MA3, MA4 R2 and MA3 R8; the INV scope paragraph says the RN footer (2026-10-07) lags the newest entry (October 09, 2026). Conflict C9/C28 is closed. No inventory fact used the entry.", "T78 (main ruling on modelarmor P5 r2 Q4)"),
        ("Page 'Last updated' dates (T80)", "INV intro: 'every docs page footer reads 2026-10-06 except the release notes page (2026-10-07)'", "per-page list: 2026-10-06 (OV, TPL, SAN, FLR, QUO, FAR, DR, LOC, FV, VH, EXC, BP, INT, GE, APG, AGW, VTX, LC, LOG, MON, RTY, NET, MCPD); 2026-10-07 (RN, APU, APR); 2026-10-05 (LIB); 2026-09-24 (RR); 2026-09-07 (RT, DataItem); 2026-08-19 (the two sanitize method pages)", "T80 (main ruling on modelarmor P5 r2 Q4)"),
        ("Status rule S (T23, main ruling)", "'GA [Inferred] (status rule S)' with a general premise; applied unevenly", "premise stated once in the INV scope paragraph with the evidence (Preview features carry a banner; first release note 2025-02-03 has no stage word); the rule is kept only where a page was read and shows no launch-stage banner. The 21 existing GA [Inferred] cells stay (all sit on pages that were read). Terraform, gcloud, console, monitoring logging and SCC findings stay [Not disclosed] because no resolver recorded a banner check on their pages; Apigee is now [Documented] (T20); Service Extensions stays [To be verified] (T21).", "T23; main ruling on modelarmor P5 r1 Q3"),
        ("Pre-GA Offerings Terms (T85)", "no mention", "Inventory: the scope paragraph only (GST short name and one sentence); Status cells keep 'Preview'. Columns: three Documented clauses in MA10 R4, one Inferred bullet in MA10 R7, one Documented bullet in MA3 and MA4 R5 (exclusion rules), GST and products URLs in R9.", "T85; main ruling on modelarmor P5 r2 Q6; R017 item 5"),
        ("Acceptable Use Policy and terms (T86)", "a CSAM caution in MA1 R7 and a Singapore bullet in MA10 R7 only", "AUP clause [Documented] and 'expressly permitted' [Not disclosed] in R7; R8 question; AUP and GST URLs in R9; for MA1, MA2, MA3, MA4, MA7, MA8, MA10. The resolution names MA1, MA3, MA4, MA7, MA8 (R7) and MA1, MA7, MA8, MA10 (R8); the merger extended it to MA2 (all three rows) and to MA3 and MA4 R8 because the test content is the same (jailbreak, injection, harmful text). The CSAM-AUP bullet went to MA1 and MA2 R7. The user question stays open for CP2 (section 5).", "T86; R019; queue 'modelarmor P5 r2 Q1/Q2'"),
        ("T25 client versions (main ruling)", "A R4: 'the C# install line is a pre-release package'", "one short R4 bullet (Java 0.40.0 in the sbt line, C# pre-release) in the six A columns; Python, Node.js, PHP, C# tags and the Java pom in INV(b) only, one repo label per fact", "T25; main ruling on modelarmor P5 r1 Q2"),
        ("T21 Service Extensions (main ruling)", "resolver label [Not disclosed] for the GA date of other load balancers and Secure Web Proxy", "[To be verified]: the Service Extensions configuration page returned no text through fetch_text.py and was read only through a summarising fetch, which cannot carry a label (CLAUDE.md hard rule 4). The release notes, networking and integrations pages were read raw and are named as checked.", "main ruling on modelarmor P5 r1 Q4"),
        ("Inventory title and sheet letter", "'(draft for sheet 3x)'", "'(final, sheet 3x; the sheet letter is assigned at P8)'", "R003"),
        ("Inventory row count", "(a) 10, (b) 15, (c) 16, (d) 18, (e) 16", "(d) 20: rows us-east7 and global added (FAR-only values, other cells Not disclosed)", "T77, T83; main ruling on modelarmor P2 cols_a Q1"),
    ]
    for g in G:
        A("| " + " | ".join(cell(x) for x in g) + " |")
    A("")
    A("## 2. Column and row changes")
    A("")
    A("### 2a. Per-location table")
    A("")
    A("Rows with several columns in the first cell mean the same change was made in each of them. Kind: replace = bullet replaced by one or more bullets; insert = new bullets; edit = in-line text change; summary = Summary line replaced; delete = bullet removed.")
    A("")
    A(s2)
    A("")
    A("### 2b. Summaries changed")
    A("")
    A("R1 to R8 Summaries (marked [changed at merge] in modelarmor_summaries_preview.md): " + ", ".join(summ_main) + ".")
    A("")
    A("R9 Summary lines rewritten for the added URLs: " + ", ".join(summ_r9) + ".")
    A("")
    A("Of these, the following changed in substance (not only a label or a deleted clause): MA1 R1, MA2 R1 (CSAM caveat, T9); MA1 R5 and MA2 R5 (three defaults, T2; MA2 also style 3c); MA2 R3 (REST method reference, T16); MA3 R5, MA4 R5 (T4); MA4 R1 (T13); MA4 R2 (style 3a); MA7 R1 (T37); MA5 R6, MA6 R6 (T52); MA6 R2, MA6 R3 (T44, T45, label now Not disclosed). Label-only or clause-deletion changes: MA5 R3, R4, R5; MA6 R5; MA9 R3, R4, R5, R6; MA10 R3, R4, R5, R6.")
    A("")
    A("### 2c. Triage style and hygiene items not applied (with reason)")
    A("")
    A("| Item | Decision | Reason |")
    A("|---|---|---|")
    NA = [
        ("Style 4: identical Summaries across input/output pairs (MA1 R3 = MA3 R3; R4 of MA1 = MA2 and MA3 = MA4 and MA7 = MA8; R5 of MA7 = MA8; R9 of MA3 = MA4)", "kept; the MA3/MA4 R5 and MA1/MA2 R9 pairs now differ for substantive reasons (T4, T2, R9 URL sets)", "the facts are the same for both directions; forcing different wording would add no information. The brief asks for both columns in full, which they are."),
        ("Style 6: shared boilerplate (387 of 863 R1 to R7 bullets repeated)", "kept", "not an error; the split of columns is settled (R017 item 1)."),
        ("Style 7: cross-references to NeMo, Presidio, Sentinel, Llama Guard", "not added", "no source is in any resolution and the instruction is no new research; sheet 4 carries the cross-product grouping."),
        ("Label hygiene: cells in the inventory mixing two label types (INV(a) 11, (b) 8, (c) 1, (d) 2, (e) 1)", "only where a resolution touched the cell (the touched cells now keep one label per fact)", "a global rewrite was not asked for and would change cells no resolver re-read."),
        ("Settled items table (Apigee flow-variable bullets, Terraform registry, sheet letter, block (d) union, retirement date, token-limit history, v3 date, SKIP_DETECTION history, docs host move)", "applied as settled", "queue rulings and R003."),
        ("T76 optional INV(c) 'modalities' append", "not applied", "the resolution says 'only if the merger wants the premise'; the premise is in MA9 and MA10 R6."),
        ("T85 status-cell suffix 'Pre-GA Offerings Terms apply' on INV Preview rows", "not applied", "main ruling: Pre-GA terms in the INV intro sentence only; Preview rows keep Status 'Preview'."),
    ]
    for r in NA:
        A("| " + " | ".join(cell(x) for x in r) + " |")
    A("")
    A("## 3. Inventory changes (modelarmor_inventory.md to modelarmor_inventory_final.md)")
    A("")
    A(s3)
    A("## 4. Conflict decisions")
    A("")
    A("Both sources are kept with their own label; the chosen text is what the finals say.")
    A("")
    A("| Conflict | Decision | Reason code |")
    A("|---|---|---|")
    CD = [
        ("userPrompt field of sanitizeModelResponse: cols_a (MA2, MA4, MA8) 'only the Go client documents it, the docs pages do not mention it' against cols_b (MA6) and the REST method reference", "cols_b is right. Three Documented bullets (REST method reference, Go struct with repo label, Apigee `<UserPromptSource>` and flow variable); the effect of the field is [Not disclosed] naming the pages checked. The R8 wording no longer says 'the Go client documents it'.", "T16, T17"),
        ("Over-limit behaviour: R6 and Summaries 'skipped' against the quotas page (match still returned)", "Quotas page wins: a match returns MATCH_FOUND, only a no-match returns EXECUTION_SKIPPED [Documented]; 'may be only partly screened' is [Inferred] with its premise. MA5 R6 and MA6 R6 Summaries rewritten. The 2025-07-28 SKIP_DETECTION note stays as history.", "T52"),
        ("Singapore NRIC: 'needs a custom detector' (MA5, MA6 R7) against the SDP built-in infoType", "Built-in SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER [Documented] (Google SDP infoTypes reference, cited as the owner's page); the route through an advanced inspect template is [Inferred]. No custom detector is claimed. Consistent with sdp_cols_a.md SD1 R2 and sdp_cols_b.md SD5.", "T55"),
        ("RAI default level: templates page 'High', REST 'unspecified = Low and above / reasonable default by filterType', floor settings 'Medium and above'", "Three Documented bullets in MA1 and MA2 R5; R5 Summary says 'three different defaults'; which one applies to an API-created template is [To be verified] (R8 lists all three). INV(a) already carried the three.", "T1, T2"),
        ("PI default level: cols_a [Inferred] 'would behave as Low and above' against INV [Documented] floor-setting default", "Both: floor-setting default [Documented] (floor settings page quote); template default [Inferred] with the enum premise. Same split in INV(a) and INV(c).", "T3"),
        ("PI and jailbreak threshold advice: overview Medium (High for Gemini Enterprise), templates page High, overview table Low and above for high-stakes categories, overview considerations 'High or Medium and above'", "Four separate [Documented] bullets (A to D); no page reconciles them. MA3 and MA4 R5 Summaries now say Medium or High, and Low and above for high-stakes categories (MA4: also that the response example shows no level).", "T4, T5"),
        ("CSAM 'cannot be turned off' against the feature table 'No' in seven limited-support locations", "Two [Documented] facts plus the third release-note fact that disabling enforcement enables features; 'CSAM runs there with enforcement off' is [Inferred] because the sentence does not name CSAM. Summaries R1 carry the caveat. INV(a) Default no longer says 'Always on'.", "T9, T10"),
        ("OCR text: INV [Documented] 'follows the template', MA10 [Not disclosed], MA1/MA3/MA7/MA8 [To be verified]", "One treatment everywhere: the REST quote 'depending on the filter configuration' [Documented]; which filters examine OCR text [Not disclosed] naming the pages checked. MA10's Inferred bullet 'probably only OCR text' keeps its premise.", "T11"),
        ("Prompt injection on responses: overview and sample result against the templates page 'in a prompt'", "MA4 R1 Summary stays [Documented] and rests on the overview sentence and the sample result, and states that the templates page describes prompts only; the reading that the filter is active on responses is [Inferred]. A positive example is [Not disclosed]; test stays T14.", "T13, T14"),
        ("Basic SDP infoTypes: six (overview, REST, Go comment) against seven (sanitize page, adds PASSWORD)", "Three bullets: the conflict [Documented]; the Go comment [Documented: repo googleapis/google-cloud-go@modelarmor/v1.3.0]; 'no page reconciles them, no release note mentions PASSWORD' [Not disclosed]. 'US-based regions' undefined [Not disclosed]; probable reading via the jurisdiction column [Inferred].", "T41, T43"),
        ("filterResults shape: REST map against two array examples on the sanitize page", "Go type map[string]*FilterResult at the tag and the REST reference outrank page examples (R007 item 4); the array examples are 'probably an older or abbreviated format' [Inferred]; live shape stays one test call.", "T47"),
        ("Image finding box: boundingBoxes list (REST, Go) against boundingBox object (sanitize example)", "Same pattern: list is the documented and coded shape; the example is [Inferred] to be abbreviated or older; R8 keeps the live check.", "T70"),
        ("Excel type spelling XLYM (REST, Go comment) against XLTM (overview, release note)", "Both spellings [Documented]; 'XLYM is probably a typo' [Inferred] (premise: overview and release note say XLTM; REST text and Go comment share a source comment).", "T67"),
        ("Embedded images in files: overview 'not screened', integrations page 'not screened' (Gemini Enterprise), Gemini Enterprise page 'screened'", "Three [Documented] bullets (MA10 R2 renumbered to match MA9 R2) and 'no page reconciles' [Not disclosed]; the Go container-name comment adds a schema fact in MA9. INV(a) OCR Limit carries all three. Test stays T59.", "T58, T59"),
        ("Gemini Enterprise modalities: integrations table 'Text, documents' against the Gemini Enterprise page (images)", "Two [Documented] bullets and 'no page reconciles' [Not disclosed] in MA10 R3 and INV(b).", "T60"),
        ("MCP integration status: release note 2026-04-22 GA against the floor-settings link '(Preview)'", "Both [Documented]. The dated release note is used because the page label is undated; that preference is [Inferred] in the inventory and stated in the six A R4 bullets. MA6 R4 already held the pair.", "T22; queue rule (dated release note beats undated label)"),
        ("Agent Gateway 'block and redact' against 'allows or blocks'; networking page 'allow, block, or modify'", "Quotes [Documented]; whether de-identified text is forwarded [Not disclosed] in MA5, MA6 R4 and INV(b) (ingress, egress, Service Extensions). Only Apigee documents extracting redacted data.", "T26"),
        ("Apigee policies GA or Preview (no label on the Model Armor pages)", "Apigee release notes: Public Preview 2025-05-22, GA 2025-09-04 [Documented] (Apigee docs, not Model Armor docs); open question removed from R8 of MA6 and from INV(b).", "T20"),
        ("Docs describe fields the Go v1 client lacks", "Go (labelled with the tag) and Java v1 (labelled v1.93.0) absences stated as repo facts, not as Not disclosed; 'the clients lag the documented API' is [Inferred]. Exclusion rules: usage on two pages, REST list without the field and its footer date [Documented]; REST page lag [Inferred]; live acceptance [To be verified].", "T18, T19"),
        ("logSanitizeOperations: 'full content' (logging page) against 'metadata or snippets as configured' (overview)", "Three separate bullets in the six A R4 sections; two in MA5, MA6 R4; INV(c) adds the REST wording.", "T79"),
        ("Security Command Center: INT 'finding for a floor-setting violation' against SCCF catalogue of one finding", "Separate [Documented] facts; 'the INT and AGW sentences describe more than SCCF lists' [Inferred].", "T81"),
        ("Block (d): FAR has 20 rows, LOC and DR list 18", "Union of 20 rows (queue ruling); the two FAR-only rows carry FAR values, every other cell [Not disclosed]; FAR global (Image Yes) against DR and OV recorded as two labelled facts.", "T77"),
        ("Where merger text deviates from a resolver's exact text", "(1) MA9 R5 T68: the container-name quote is already the 'Finding containers' bullet, so only the Inferred and Go bullets replace the file-label bullet. (2) MA10 R7 T85: the three clause bullets are kept in R4; R7 keeps the Inferred 'synthetic images' bullet and points to R4. (3) MA7 R1 T37: the first replacement bullet keeps the 'input-template focus does not name URLs' fact that the original bullet held. (4) T25 labels in A columns reduced to Java and C# (main ruling). (5) T86 extended to MA2/MA3/MA4 as stated in section 1. (6) T84 naming bullet placed in R3 (A columns, MA9, MA10) rather than R4. (7) MA10 R2 embedded-image bullet inserted after the overview bullet and numbered (2), with the Gemini Enterprise bullet renumbered (3).", "merger judgement; none changes a label"),
    ]
    for r in CD:
        A("| " + " | ".join(cell(x) for x in r) + " |")
    A("")
    A("## 5. Remaining open items (by T-id and class)")
    A("")
    cnt = Counter()
    for t, r in tr.items():
        cnt[(r["cls"].split()[0], STATE[t][0].split()[0])] += 1
    A("Class: a = answerable from official docs or code; b = needs testing or vendor access (stays open in R8, as instructed); c = licensing or terms. 'honest gap' = closed vendor internals that no public document is expected to answer. Status: RESOLVED / CORRECTION applied = the final text carries the answer; PARTLY RESOLVED = some half is closed and the rest is labelled in the text; OPEN = unchanged from the draft or only re-labelled.")
    A("")
    A(s5)
    A("")
    A("**Open items that need a user decision (CP2):**")
    A("")
    A("1. Acceptable Use Policy testing clause (T86). Google's AUP bars using the Services \"to test or reverse-engineer the Services in order to find limitations or vulnerabilities, or to evade filtering capabilities, except as expressly permitted in the Agreement\". The finals carry the clause [Documented], the applicability reading [Inferred] only in this log (the column bullet says 'expressly permitted' is [Not disclosed]) and an R8 question. Whether red-team style benchmarking of Model Armor falls under it is a legal reading for the project owner (queue: modelarmor P5 r2 Q1).")
    A("2. Synthetic data only for Preview features (T85, Q2): the Pre-GA terms say not to process personal data in Pre-GA Offerings; MA10 R7 states synthetic images only as [Inferred]. Sensitive test data is decided at bench design (R019).")
    A("3. Terraform, gcloud, console, monitoring and SCC findings status: kept [Not disclosed] (no banner check recorded). If the user wants rule S extended to them, one resolver pass on those pages would be needed.")
    A("")
    A("## 6. Moved Reviewer notes")
    A("")
    A("Verbatim from the drafts. Status at merge follows each block.")
    A("")
    A("### 6a. modelarmor_cols_a.md (22 bullets)")
    A("")
    for l in notes_a:
        if l.strip():
            A(l)
    A("")
    A("Status at merge: bullet 2 (page dates) corrected by T80 (section 1); bullet 3 (repo read) re-pinned to the tag and the UserPrompt claim corrected by T16; bullets 4 (C14 CSAM) reconciled by condition, T9; 5 (C15 locations) resolved, T77; 6 (C16 Go client) T18; 7 (C1) T4; 8 (C3) T2, T3; 9 (C5) unchanged; 10 (C6) unchanged; 11 (C9 date) corrected, T78; 12 (C10 topics) T35; 13 (C11 exclusion rules) T19; 14 (C12 PI on responses) T13; 15 (C13) not used; 16 (Apigee flow variables) kept, attributed 'Apigee docs not Model Armor docs' (queue ruling, R007 item 1); 17 (sample oddities) T6, T8; 18 (region facts) T33; 19 (antivirus) T57; 20 to 22 unchanged.")
    A("")
    A("### 6b. modelarmor_cols_b.md")
    A("")
    for l in notes_b:
        if l.strip():
            A(l)
    A("")
    A("Status at merge: response-side file and image evidence (R017 item 3: no split; T61 stays a test); method-page findings used as drafted; basic SDP infoTypes T41, T44; Agent Gateway T26; MCP status T22; feature-table rows T77; floor-settings RAI default T1, T2; Apigee FunctionResponseSource not used (tool-call screening is inventory only, R017 item 2); include_findings T71; MODALITY_UNSPECIFIED T76; XLYM T67.")
    A("")
    A("### 6c. modelarmor_inventory.md (Reviewer notes 1 to 6)")
    A("")
    for l in notes_i:
        if l.strip():
            A(l)
    A("")
    A("Status at merge: note 1 conflicts handled as in section 4 (1.2 T41; 1.3 T1 to T3; 1.4 T58; 1.6 retirement date unchanged; 1.7 T57; 1.8 T19; 1.9 T81; 1.10 T79; 1.11 T18; 1.12 T77, T33); note 2 (release-note entry) corrected: the entry is dated 2026-10-09 (T78); note 3 row counts now 10/15/16/20/16 (T77, T83) and status rule S per T23; note 4 'not read' list: the Terraform resource page is no longer unread (SCC Terraform page read, T24); note 5 and 6 unchanged (the self-check is superseded by section 7).")
    A("")
    A("## 7. Self-check")
    A("")
    A("### 7a. Summary word counts (excluding the trailing bold label; limit 45, R7 60)")
    A("")
    A(sc_tab)
    A("")
    A(f"{nsum} Summaries counted; maximum {mx} words; Summaries over the limit: {over}.")
    A("")
    A("### 7b. Labels in modelarmor_two_level.md (bold labels, Summaries and Detail)")
    A("")
    A(lab_tab)
    A("")
    A("Labels on the 70 Summaries R1 to R7: " + "; ".join(f"[{k}] {v}" for k, v in sorted(sumlabs.items(), key=lambda x: -x[1])) + ". R8 and R9 Summaries carry no label; R8 and R9 Detail bullets carry no labels.")
    A("")
    A(f"Detail bullets in total: {nbul} top-level bullets and {nsub} sub-bullets (R8 and R9 included).")
    A("")
    A("### 7c. Inventory row counts (modelarmor_inventory_final.md)")
    A("")
    for t in tables:
        A(f"- {t}")
    A("- Block counts for the P8 config: (a) 10, (b) 15, (c) 16, (d) 20, (e) 16")
    A("- Bold markers and backticks in cells: 0; stray table pipes: 0 (checker); labels outside the allowed forms: 0 (checker)")
    A("- Covered by Table 3 column cells in (a) and (b): exact header strings (semicolon-separated) or the inventory-only marker only")
    A("")
    A("### 7d. check_drafts.py and extra checks")
    A("")
    A("Commands (run from the repo root):")
    A("")
    A("```")
    A("python benchtest/tools/check_drafts.py columns drafts/modelarmor_two_level.md --final --expect 10")
    A("python benchtest/tools/check_drafts.py inventory drafts/modelarmor_inventory_final.md --headers drafts/modelarmor_two_level.md")
    A("```")
    A("")
    A("(Paths in the call were given relative to benchtest/ as in the instructions; the files checked are benchtest/drafts/modelarmor_two_level.md and benchtest/drafts/modelarmor_inventory_final.md.)")
    A("")
    for r in res1:
        A(f"- columns: {r}")
    for r in res2:
        A(f"- inventory: {r}")
    A("")
    A("Extra checks (merger script `benchtest/scratchpad/merger/modelarmor/verify.py` and greps):")
    A("")
    A("- Every `[Documented: repo X@ref]` label in R1 to R7 has an R9 URL naming the repo and the same ref, in the same column: pass.")
    A("- No duplicate top-level bullet inside a row; every URL written in R1 to R8 text appears in R9 of the same column: pass.")
    A("- Known-wrong strings (lessons.md item 6) absent from modelarmor_two_level.md and modelarmor_inventory_final.md: 'only the Go client', 'docs pages do not mention', '130,000 tokens is skipped', 'October 10, 2026', '2026-10-10', 'two different defaults', 'not shown anywhere', 'the Go client documents' (0 hits each). 'custom detector' occurs only in 'no custom detector is needed' (NRIC), in the T35 'custom detectors in a Sensitive Data Protection template' Inferred bullet and in a quote of the templates page. The string 37f936ac occurs once, in the INV scope paragraph, where it names the clone HEAD next to the tag.")
    A("- No 'Reviewer notes', 'this draft' or 'I checked' in either final.")
    A("")
    A("### 7e. Handling of the instructions")
    A("")
    A("- Class (b) items stayed in R8; the only R8 bullets removed are the answered Apigee status bullet in MA6 (T20) and none other. Class (b) items whose wording followed a changed documentation half (T1 default level, T3 template default, T16/T17 userPrompt, T47 shape, T70 box shape, T71 include_findings, T44/T45 response-side SDP, T50 floor-setting location, T53 token limits, T77 locations) were reworded in R8, not closed.")
    A("- The pending user question (AUP, T86) is recorded in section 5 and in the final report; no label was upgraded without a quote in the resolutions.")
    open(DR + "modelarmor_changes.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("changes written;", rc1, rc2, res1, res2)


if __name__ == "__main__":
    main()
