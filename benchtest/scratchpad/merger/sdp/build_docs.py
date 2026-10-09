import json, re, subprocess, sys, collections
sys.path.insert(0, "/home/user/guardrail_research/benchtest/scratchpad/merger/sdp")
from selfcheck import parse, words, BOLD
ROOT = "/home/user/guardrail_research/benchtest/drafts/"
SP = "/home/user/guardrail_research/benchtest/scratchpad/merger/sdp/"
LOG = json.load(open(SP + "log.json"))
cols = parse(ROOT + "sdp_two_level.md")


def esc(s):
    return s.replace("|", "\\|").replace("\n", " // ")


def short(s, n=190):
    s = s.strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


# ------------------------------------------------------------------ summaries preview
out = ["# Sensitive Data Protection: Summary preview (CP2)", "",
       "Generated from `sdp_two_level.md` on 2026-10-09. Each line gives the word count (excluding the trailing bold label; limit 45, R7 60) and the number of top-level Detail bullets (sub-bullets are not counted). Summaries changed at merge are marked `[changed at merge: T-ids]`.", ""]
changed = collections.defaultdict(list)
for e in LOG:
    if e["full"]:
        m = re.match(r"(SD\d) (R\d)", e["loc"])
        changed[(m.group(1), m.group(2))].append(re.sub(r" \(.*\)", "", e["tid"]))
for c in cols:
    out.append(f"## {c['header']}")
    out.append("")
    for n in range(1, 10):
        s = c["R"][n]["s"]
        nb = sum(1 for l in c["R"][n]["d"] if l.startswith("• "))
        tag = ""
        if (c["id"], f"R{n}") in changed:
            tag = f" `[changed at merge: {', '.join(changed[(c['id'], f'R{n}')])}]`"
        out.append(f"- **R{n}** ({words(s)}w, {nb} bullets): {s}{tag}")
    out.append("")
open(ROOT + "sdp_summaries_preview.md", "w", encoding="utf-8").write("\n".join(out))

# ------------------------------------------------------------------ change log pieces
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd="/home/user/guardrail_research", env={"PYTHONIOENCODING": "utf-8", "PATH": "/usr/bin:/bin:/usr/local/bin"})
    return r.stdout.strip().split("\n")


c_out = run(["python", "benchtest/tools/check_drafts.py", "columns", "benchtest/drafts/sdp_two_level.md", "--final", "--expect", "6"])
i_out = run(["python", "benchtest/tools/check_drafts.py", "inventory", "benchtest/drafts/sdp_inventory_final.md", "--headers", "benchtest/drafts/sdp_two_level.md"])
c_res = [l for l in c_out if l.startswith("RESULT")][0]
i_res = [l for l in i_out if l.startswith("RESULT")][0]
tables = [l for l in i_out if l.startswith("table")]

# per-location tables
def col_rows(sd):
    rows = []
    for e in LOG:
        if e["file"] != "cols" or not e["loc"].startswith(sd):
            continue
        n = 400 if e["full"] else 170
        b = e["before"] if e["full"] else short(e["before"], n)
        a = e["after"] if e["full"] else short(e["after"], n)
        if e["full"]:
            wb = words(re.sub(r"^Summary: ", "", e["before"]))
            wa = words(re.sub(r"^Summary: ", "", e["after"]))
            b = re.sub(r"^Summary: ", "", b)
            a = re.sub(r"^Summary: ", "", a)
            b += f" ({wb}w)"
            a += f" ({wa}w)"
        rows.append((e["loc"], b, a, f"{e['tid']}: {e['reason']}"))
    return rows


sec2 = []
for c in cols:
    sec2.append(f"### {c['id']}: {c['header']}")
    sec2.append("")
    sec2.append("| Location | Before | After | Reason |")
    sec2.append("|---|---|---|---|")
    for loc, b, a, r in col_rows(c["id"]):
        sec2.append(f"| {esc(loc)} | {esc(b)} | {esc(a)} | {esc(r)} |")
    sec2.append("")

# inventory: group per-row cell edits by (block, cell no, tid, reason)
groups = collections.OrderedDict()
for e in LOG:
    if e["file"] != "inv":
        continue
    m = re.match(r"(\(\w\)|head) row '(.+)' cell (\d+)$", e["loc"])
    if m:
        key = (m.group(1), m.group(3), e["tid"], e["reason"])
        groups.setdefault(key, []).append((m.group(2), e))
    else:
        groups.setdefault((e["loc"], "", e["tid"], e["reason"]), []).append((None, e))
sec3 = ["| Location | Before | After | Reason |", "|---|---|---|---|"]
for (blk, cell, tid, reason), items in groups.items():
    if items[0][0] is None:
        e = items[0][1]
        sec3.append(f"| {esc(blk)} | {esc(short(e['before'], 260))} | {esc(short(e['after'], 260))} | {esc(tid)}: {esc(reason)} |")
    else:
        names = [n for n, _ in items]
        e = items[0][1]
        loc = f"{blk} {', '.join(names)} (cell {cell})" if len(names) <= 3 else f"{blk} {len(names)} rows (cell {cell}): {', '.join(names)}"
        sec3.append(f"| {esc(loc)} | {esc(short(e['before'], 260))} | {esc(short(e['after'], 260))} | {esc(tid)}: {esc(reason)} |")

gs = {}
for e in LOG:
    if e["loc"] == "(many)":
        n = int(re.search(r"\((\d+) replacements\)", e["reason"]).group(1))
        gs[e["tid"] + "|" + e["before"][:40]] = (e, n)

# open items
tri = open(ROOT + "sdp_triage.md", encoding="utf-8").read().split("\n")
items = {}
for ln in tri:
    m = re.match(r"^\| (T\d+) \| (.*) \| ([^|]*) \| ([abcD]) \| (.*) \| ([HML]) \|$", ln)
    if m:
        items[m.group(1)] = dict(item=m.group(2), loc=m.group(3), cls=m.group(4), pri=m.group(6))
assert len(items) == 98, len(items)
verd = {}
for fn in ["sdp_resolutions_1.md", "sdp_resolutions_2.md"]:
    txt = open(ROOT + fn, encoding="utf-8").read()
    tail = txt[txt.rfind("## Summary table"):]
    for ln in tail.split("\n"):
        m = re.match(r"^\| (T\d+) \| ([^|]+) \|", ln)
        if m:
            verd[m.group(1)] = m.group(2).strip()
closed = [t for t, v in verd.items() if v.startswith("RESOLVED") or v.startswith("CORRECTION")]
openl = []
for t in sorted(items, key=lambda x: int(x[1:])):
    v = verd.get(t, "not handled (class b: needs testing)")
    if t in closed:
        continue
    it = items[t]
    openl.append((t, it["cls"], it["pri"], v, short(re.sub(r"`", "", it["item"]), 150), short(re.sub(r"`", "", it["loc"]), 120)))
stay = ["| T-id | Class | Priority | Status after P5 | Item (short) | Where it stays (triage location) |", "|---|---|---|---|---|---|"]
for r in openl:
    stay.append("| " + " | ".join(esc(x) for x in r) + " |")

by_class = collections.Counter(r[1] for r in openl)

# self-check tables
sc1 = ["| Column | " + " | ".join(f"R{n}" for n in range(1, 10)) + " |", "|---|" + "---|" * 9]
for c in cols:
    sc1.append(f"| {c['id']} | " + " | ".join(f"{words(c['R'][n]['s'])}" for n in range(1, 10)) + " |")
lab = collections.Counter()
for c in cols:
    for n in range(1, 8):
        for l in c["R"][n]["d"]:
            for m in re.finditer(r"\[(Documented(?:: repo [^\]]+)?|Inferred|To be verified|Not disclosed)\]", l):
                lab[(c["id"], m.group(1).split(":")[0] if m.group(1).startswith("Documented") else m.group(1), "repo" if "repo" in m.group(1) else "")] += 1
sc2 = ["| Column | [Documented] | [Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0] | [Inferred] | [Not disclosed] | [To be verified] | Detail bullets (R1 to R9) | R9 URLs | Summaries (labelled R1 to R7) |", "|---|---|---|---|---|---|---|---|---|"]
tot = collections.Counter()
for c in cols:
    d = lab[(c["id"], "Documented", "")]
    r = lab[(c["id"], "Documented", "repo")]
    i = lab[(c["id"], "Inferred", "")]
    nd = lab[(c["id"], "Not disclosed", "")]
    tv = lab[(c["id"], "To be verified", "")]
    nb = sum(1 for n in range(1, 10) for l in c["R"][n]["d"] if l.startswith("• "))
    nu = sum(1 for l in c["R"][9]["d"] if l.startswith("• "))
    ns = sum(1 for n in range(1, 8) if BOLD.search(c["R"][n]["s"]))
    sc2.append(f"| {c['id']} | {d} | {r} | {i} | {nd} | {tv} | {nb} | {nu} | {ns} of 7 |")
    for k, v in zip(["d", "r", "i", "nd", "tv", "nb", "nu"], [d, r, i, nd, tv, nb, nu]):
        tot[k] += v
sc2.append(f"| Total | {tot['d']} | {tot['r']} | {tot['i']} | {tot['nd']} | {tot['tv']} | {tot['nb']} | {tot['nu']} | 42 of 42 |")

# known-wrong strings
cols_txt = open(ROOT + "sdp_two_level.md", encoding="utf-8").read()
inv_txt = open(ROOT + "sdp_inventory_final.md", encoding="utf-8").read()
pats = [
    ("1000-character", "T20: SD2 R6 Summary unit invented"),
    ("hard cap", "T20: 3,000 findings is not a hard limit"),
    ("capped at 0.5 MB and 3,000", "T20: SD1 R6 Summary old wording"),
    ("only the client describes", "T57: transformationErrorHandling is in the REST reference"),
    ("documented outside the client", "T57: R8 old wording"),
    ("formerly called", "T1/R018: Summary sentence dropped (Detail keeps 'Formerly Cloud DLP')"),
    ("of any length", "T14: SD4 R4 Summary old wording"),
    ("an apply operation exists", "T9: removed inference"),
    ("evaluation call is not exposed", "T9: intro wording"),
    ("no evaluation method", "T91/T9: absence worded as [Not disclosed]"),
    ("Other harm categories are not listed", "T16: SD6 R2 Summary old sentence"),
    ("unnamed models", "T16: SD6 R4 Summary old sentence"),
    ("no worked example of an image safety response", "T16: SD6 R5 Summary old sentence"),
    ("redacted, replaced, masked, bucketed or date-shifted", "T12: SD3 R4 Summary old wording"),
    ("masks, buckets, date-shifts", "T12: SD3 R1 Summary old wording"),
    ("There is no verdict", "T17: SD2 R5 Summary old wording"),
    ("may be older", "T49: weakened inference"),
    ("latest, with the old behaviour on stable", "T44: INV(b) Health row correction"),
    ("my count", "T89: first-person wording"),
    ("my own", "T89: first-person wording"),
    ("this sheet", "T89/T90: process wording and self-referential label"),
    ("read-only rule", "T89: process wording"),
    ("Not read [To be verified]", "T79: S3/JDBC row"),
    ("were not read", "T96/T79: stale 'not read' statements"),
    ("terms pages were not read", "T92: INV(f)"),
    ("customer data terms were not read", "T92"),
    ("audit-logging page was not read", "T64"),
    ("named only generally", "T63"),
    ("Reviewer notes", "README: no Reviewer notes in finals"),
    ("provisional", "T6/T1: frozen headers and prefix"),
    ("ruling R0", "style: ruling ids are not cited in cells"),
    ("the detection column", "style 4: column pointers use header words"),
    ("SD1 column", "style 4"), ("SD2 column", "style 4"), ("SD3 column", "style 4"), ("SD5 column", "style 4"), ("SD6 column", "style 4"),
    ("packages/google-cloud-dlp/google", "T97: citation form (the R9 blob URLs keep the full repo path)"),
    ("[grpc]", "T90 (INV): bracket pair that is not a label"),
]
gr = []
for p, why in pats:
    a = cols_txt.count(p)
    b = inv_txt.count(p)
    note = ""
    if p == "packages/google-cloud-dlp/google":
        a = sum(1 for l in cols_txt.split("\n") if p in l and not l.startswith("• https://"))
        b = sum(1 for l in inv_txt.split("\n") if p in l and "https://" not in l)
    if p == "[grpc]":
        note = " (1 match in SD1 R7 Detail: a quoted dependency spec in backticks, not an inventory cell)"
    gr.append(f"| `{p}` | {a} | {b} | {why}{note} |")

json.dump(dict(c_res=c_res, i_res=i_res, tables=tables, n_open=len(openl), by_class=by_class, closed=len(closed)), open(SP + "build_state.json", "w"), default=dict)

open(SP + "pieces.json", "w").write(json.dumps(dict(
    sec2="\n".join(sec2), sec3="\n".join(sec3), stay="\n".join(stay), sc1="\n".join(sc1), sc2="\n".join(sc2), grep="\n".join(gr),
    c_res=c_res, i_res=i_res, tables=tables, c_out=c_out, i_out=i_out,
    gs={k: [v[0]["reason"], v[1]] for k, v in gs.items()},
    by_class=dict(by_class), n_open=len(openl), n_closed=len(closed),
    n_cols=sum(1 for e in LOG if e["file"] == "cols" and e["loc"] != "(many)"),
    n_inv=sum(1 for e in LOG if e["file"] == "inv"),
    n_gsub=sum(1 for e in LOG if e["loc"] == "(many)"),
)))
print(c_res, i_res)
print("open:", len(openl), dict(by_class), "closed:", len(closed))
print("gsub counts:", {k: v[1] for k, v in gs.items()})
