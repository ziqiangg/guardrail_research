import re, sys, json
sys.stdout.reconfigure(encoding="utf-8")
D = "benchtest/drafts/"
LABEL = r"\[(?:Documented(?:: (?:repo [^\]]+|develop/unreleased))?|Inferred|To be verified|Not disclosed)\]"
BOLD_END = re.compile(r"\*\*" + LABEL + r"\*\*\s*$")

def words(s):
    s = re.sub(r"\*\*" + LABEL + r"\*\*\s*$", "", s).replace("**", "")
    return len(s.split())

def parse(path):
    cols, cur, rn = [], None, None
    for ln in open(path, encoding="utf-8").read().splitlines():
        if ln.startswith("## Column"):
            m = re.match(r"^## Column ([A-Z]+\d+): (.+)$", ln)
            cur = {"id": m.group(1), "header": m.group(2), "R": {}}
            cols.append(cur); rn = None
        elif cur is not None and re.match(r"^### R([1-9])\s*$", ln):
            rn = int(ln.split("R")[1]); cur["R"][rn] = {"s": None, "d": []}
        elif cur is not None and rn is not None:
            if ln.startswith("Summary: "): cur["R"][rn]["s"] = ln[9:].strip()
            elif ln.startswith("• ") or ln.startswith("  – "): cur["R"][rn]["d"].append(ln)
    return cols

def column_report(path):
    cols = parse(path)
    out = {"cols": cols, "grid": {}, "problems": []}
    for c in cols:
        for n in range(1, 10):
            r = c["R"][n]
            out["grid"][(c["id"], n)] = (words(r["s"]), len([d for d in r["d"] if d.startswith("• ")]))
        # pins vs R9
        txt_1_8 = "\n".join(d for n in range(1, 9) for d in c["R"][n]["d"])
        r9 = "\n".join(c["R"][9]["d"])
        for m in set(re.findall(r"\[Documented: repo ([^\]@]+)@([^\]]+)\]", txt_1_8)):
            repo, ref = m
            if not re.search(r"(github\.com|huggingface\.co(/datasets)?)/%s/(blob|tree|raw)/%s" % (re.escape(repo), re.escape(ref)), r9):
                out["problems"].append("%s: label repo %s@%s has no R9 URL" % (c["id"], repo, ref))
        # file@ref cites -> basename present in R9
        for fm in set(re.findall(r"([A-Za-z0-9_./-]+\.(?:py|md|yml|yaml|toml|json|sh|ipynb))@(172c1074)", txt_1_8)):
            base = fm[0].split("/")[-1]
            if base not in r9:
                out["problems"].append("%s: cited %s@%s but no R9 URL contains %s" % (c["id"], fm[0], fm[1], base))
    return out

if __name__ == "__main__":
    rep = column_report(D + "purplellama_two_level.md")
    for p in rep["problems"]: print("PROBLEM", p)
    print("columns", len(rep["cols"]), "problems", len(rep["problems"]))
