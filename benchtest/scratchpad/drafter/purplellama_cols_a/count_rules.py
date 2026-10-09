import sys, yaml, os, json, re, collections
root = sys.argv[1]
R = os.path.join(root, "CodeShield/insecure_code_detector/rules")
cfg = yaml.safe_load(open(os.path.join(R, "config.yaml"), encoding="utf-8"))["config"]
print("usecases:", list(cfg.keys()))
langs = ["c","cpp","csharp","hack","java","javascript","kotlin","objective_c","objective_cpp","php","python","ruby","rust","swift","xml","language_agnostic"]
tot = collections.Counter()
allcwe = collections.defaultdict(set)
for uc in cfg:
    print("== usecase", uc)
    for l in langs:
        c = cfg[uc].get(l, {})
        nr = len(c.get("regex", {}).get("rules", [])) if c else 0
        ns = len(c.get("semgrep", {}).get("rules", [])) if c else 0
        print(f"{l:18} cfg regex={nr} semgrep={ns} keys={list(c.keys()) if c else None}")
# regex yaml files: counts and how many with/without pattern_id and enabled per codeshield
for l in langs:
    p = os.path.join(R, "regex", l + ".yaml")
    if not os.path.exists(p):
        print(l, "no regex file"); continue
    pats = yaml.safe_load(open(p, encoding="utf-8")) or []
    en = set(cfg.get("codeshield", {}).get(l, {}).get("regex", {}).get("rules", []))
    n_noid = sum(1 for x in pats if "pattern_id" not in x)
    n_en = sum(1 for x in pats if x.get("pattern_id") in en)
    sev = collections.Counter(x["severity"] for x in pats)
    print(f"regex/{l}.yaml total={len(pats)} noid={n_noid} enabled_codeshield_with_id={n_en} sev={dict(sev)}")
    for x in pats:
        if "pattern_id" not in x or x["pattern_id"] in en:
            allcwe[l].add(x["cwe_id"])
