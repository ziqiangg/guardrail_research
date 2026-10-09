import sys, yaml, os, json, re, collections
root = sys.argv[1]
R = os.path.join(root, "CodeShield/insecure_code_detector/rules")
cfg = yaml.safe_load(open(os.path.join(R, "config.yaml"), encoding="utf-8"))["config"]
default8 = ["c","cpp","csharp","java","javascript","php","python","rust"]
def norm(c):
    c=str(c).strip()
    m=re.findall(r"CWE-\d+",c,re.I)
    return set(x.upper() for x in m) or {c}
def regex_pats(l, uc):
    en = set(cfg[uc].get(l,{}).get("regex",{}).get("rules",[]) or [])
    p=os.path.join(R,"regex",l+".yaml")
    pats = (yaml.safe_load(open(p,encoding="utf-8")) or []) if os.path.exists(p) else []
    res=[x for x in pats if x.get("pattern_id") in en]
    if l=="cpp": res+=regex_pats("c",uc)
    elif l in("objective_c","objective_cpp"): pass
    else:
        res+=[x for x in (yaml.safe_load(open(os.path.join(R,"regex","language_agnostic.yaml"),encoding="utf-8")) or []) if x.get("pattern_id") in set(cfg[uc].get("language_agnostic",{}).get("regex",{}).get("rules",[]))]
    return res
def sem(l, uc):
    p=os.path.join(R,"semgrep","_generated_",f"{l}_{uc}.json")
    if not os.path.exists(p): return []
    return json.load(open(p,encoding="utf-8")).get("rules",[])
for uc in ["codeshield","cyberseceval"]:
    allc=set(); 
    print("=== usecase",uc)
    for l in default8:
        rp=regex_pats(l,uc); sp=sem(l,uc)
        cw=set()
        for x in rp: cw|=norm(x["cwe_id"])
        for x in sp: cw|=norm(x.get("metadata",{}).get("cwe_id",""))
        allc|=cw
        # which semgrep applies per analyzer map
        print(f"{l:11} regex_effective={len(rp)} semgrep_json_rules={len(sp)} cwes={len(cw)}")
    print("distinct CWEs across default 8:",len(allc))
    # all 16 incl non-default
    allc2=set()
    for l in ["c","cpp","csharp","hack","java","javascript","kotlin","objective_c","objective_cpp","php","python","ruby","rust","swift","xml"]:
        for x in regex_pats(l,uc): allc2|=norm(x["cwe_id"])
        for x in sem(l,uc): allc2|=norm(x.get("metadata",{}).get("cwe_id",""))
    print("distinct CWEs across all enum languages:",len(allc2))
# entire repo rule files (regardless of enabled)
allr=set()
for f in os.listdir(os.path.join(R,"regex")):
    for x in yaml.safe_load(open(os.path.join(R,"regex",f),encoding="utf-8")) or []:
        allr|=norm(x["cwe_id"])
for f in os.listdir(os.path.join(R,"semgrep","_generated_")):
    for x in json.load(open(os.path.join(R,"semgrep","_generated_",f),encoding="utf-8")).get("rules",[]):
        allr|=norm(x.get("metadata",{}).get("cwe_id",""))
print("distinct CWE ids across all regex yaml + generated json:",len(allr))
