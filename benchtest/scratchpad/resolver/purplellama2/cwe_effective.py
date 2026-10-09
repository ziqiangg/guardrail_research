"""Read-only re-count of effective Code Shield rules at pin. Data files only (yaml/json); no Meta code executed.
Usage: python -I cwe_effective.py <CodeShield/insecure_code_detector dir>"""
import sys, json, glob, os, re, collections, yaml
base = sys.argv[1]
rules = os.path.join(base, 'rules')
cfg = yaml.safe_load(open(os.path.join(rules,'config.yaml'),encoding='utf-8'))['config']
LANG = {'c':'c','cpp':'cpp','csharp':'csharp','hack':'hack','java':'java','javascript':'javascript','kotlin':'kotlin','objective_c':'objective_c','objective_cpp':'objective_cpp','php':'php','python':'python','ruby':'ruby','rust':'rust','swift':'swift','xml':'xml'}
DEFAULT8 = ['c','cpp','csharp','java','javascript','php','python','rust']
def enabled(usecase, lang, an='regex'):
    return set(((cfg.get(usecase,{}).get(lang,{}) or {}).get(an,{}) or {}).get('rules',[]) or [])
def load_patterns(fn, lang, usecase):
    en = enabled(usecase, lang)
    try: pats = yaml.safe_load(open(fn,encoding='utf-8')) or []
    except FileNotFoundError: return []
    out=[]
    for p in pats:
        if 'pattern_id' in p and p['pattern_id'] not in en: continue
        out.append(p)
    return out
def load(lang, usecase):
    fn = os.path.join(rules,'regex',lang+'.yaml')
    res = load_patterns(fn, lang, usecase)
    if lang=='cpp': res += load('c', usecase)
    elif lang=='objective_c': res += load('c', usecase)
    elif lang=='objective_cpp': res += load('objective_c', usecase)+load('cpp',usecase)
    else: res += load_patterns(os.path.join(rules,'regex','language_agnostic.yaml'),'language_agnostic',usecase)
    return res
for usecase in ('codeshield','cyberseceval'):
    print('=== usecase', usecase)
    allcwe=set(); d8=set()
    for lang in LANG:
        rx = load(lang, usecase)
        rxc = {p['cwe_id'] for p in rx}
        sgf = os.path.join(rules,'semgrep','_generated_',f'{lang}_{usecase}.json')
        sg=[]
        if os.path.exists(sgf):
            sg = json.load(open(sgf,encoding='utf-8')).get('rules',[])
        sgc = {r.get('metadata',{}).get('cwe_id') for r in sg} - {None}
        # semgrep cwe_id may be like 'CWE-78: ...'
        norm=lambda s: set(re.findall(r'CWE-\d+', s if isinstance(s,str) else ' '.join(s)))
        sgn=set()
        for r in sg:
            c=r.get('metadata',{}).get('cwe_id')
            if c: sgn |= norm(c if isinstance(c,str) else ' '.join(map(str,c)))
        rxn=set()
        for c in rxc: rxn |= norm(c)
        sev = collections.Counter(p['severity'] for p in rx)
        print(f'{lang:14s} regex_eff={len(rx):3d} sev={dict(sev)} semgrep_json_rules={len(sg):3d} cwe_regex={len(rxn)} cwe_semgrep={len(sgn)}')
        allcwe |= rxn|sgn
        if lang in DEFAULT8: d8 |= rxn|sgn
    print('distinct CWE (all enum languages incl. via files):', len(allcwe), ' (8 default languages):', len(d8))
