import yaml, json, glob, os, sys
base = sys.argv[1]
os.chdir(base)
cfg = yaml.safe_load(open("rules/config.yaml"))["config"]
regex = {}
for f in glob.glob("rules/regex/*.yaml"):
    lang = os.path.basename(f)[:-5]
    regex[lang] = yaml.safe_load(open(f)) or []
def cw(r): 
    c = r.get("cwe_id") or (r.get("metadata") or {}).get("cwe_id")
    return c
def rx_enabled(uc, lang):
    ids = set(((cfg.get(uc,{}).get(lang) or {}).get("regex") or {}).get("rules") or [])
    return [r for r in regex.get(lang,[]) if r.get("pattern_id") in ids]
default = ["c","cpp","csharp","java","javascript","php","python","rust"]
out = {}
for uc in ("codeshield","cyberseceval"):
    print(uc, "langs in config:", list(cfg.get(uc,{}).keys()))
    s_cfg=set(); s_gen=set(); none=[]
    for lang in default + ["language_agnostic"]:
        for r in rx_enabled(uc, lang):
            (s_cfg.add(cw(r)) if cw(r) else none.append(r.get("pattern_id")))
            (s_gen.add(cw(r)) if cw(r) else None)
    # semgrep via config list
    for lang in default:
        ids = set(((cfg.get(uc,{}).get(lang) or {}).get("semgrep") or {}).get("rules") or [])
        p = f"rules/semgrep/_generated_/{lang}_{uc}.json"
        gen = json.load(open(p))["rules"] if os.path.exists(p) else []
        for r in gen:
            c = cw(r)
            if r["id"] in ids:
                if c: s_cfg.add(c)
                else: none.append(r["id"])
            if c: s_gen.add(c)
    print(" regex-config + semgrep-config:", len(s_cfg), " regex-config + generated json:", len(s_gen), " no-cwe:", set(none))
# all rule files
s=set(); none=set()
for lang,rs in regex.items():
    for r in rs:
        (s.add(cw(r)) if cw(r) else none.add(r.get("pattern_id")))
for f in glob.glob("rules/semgrep/*/*.yaml"):
    d=yaml.safe_load(open(f)) or {}
    for r in d.get("rules",[]):
        (s.add(cw(r)) if cw(r) else none.add(r.get("id")))
s2=set(s)
for f in glob.glob("rules/semgrep/_generated_/*.json"):
    for r in json.load(open(f))["rules"]:
        (s2.add(cw(r)) if cw(r) else none.add(r.get("id")))
print("all regex yaml + semgrep yaml:", len(s), " + generated:", len(s2), " no cwe:", none)
# Error-severity enabled regex rules in codeshield
err=[(l,r["pattern_id"]) for l in default+["language_agnostic"] for r in rx_enabled("codeshield",l) if str(r.get("severity","")).lower()=="error"]
print("codeshield regex Error:", err)
print("java_codeshield ERROR:", sum(1 for r in json.load(open("rules/semgrep/_generated_/java_codeshield.json"))["rules"] if r.get("severity")=="ERROR"))
print("regex enabled counts:", {l:len(rx_enabled("codeshield",l)) for l in default+["language_agnostic"]}, "pattern counts:", {l:len(v) for l,v in regex.items()})
