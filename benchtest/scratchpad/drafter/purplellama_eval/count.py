import json,sys,os,collections
base=sys.argv[1]
files="""autocomplete/autocomplete.json
instruct/instruct.json
instruct/instruct-v2.json
mitre/mitre_benchmark_100_per_category_with_augmentation.json
mitre/mitre_prompts_multilingual_machine_translated.json
mitre_frr/mitre_frr.json
mitre_frr/frr_multilingual_machine_translated.json
prompt_injection/prompt_injection.json
prompt_injection/prompt_injection_multilingual_machine_translated.json
interpreter/interpreter.json
spear_phishing/multiturn_phishing_challenges.json
crwd_meta/malware_analysis/questions.json
crwd_meta/threat_intel_reasoning/report_questions.json
autonomous_uplift/in/cyber_range_pairs_sample.json
autonomous_uplift/out/autonomous_prompts_sample.json
autopatch/autopatch_bench.json
autopatch/autopatch_lite.json
autopatch/autopatch_samples.json
autopatch/autopatch_arvo_examples.json""".split()
for f in files:
    p=os.path.join(base,f)
    try:
        d=json.load(open(p,encoding='utf-8'))
    except Exception as e:
        print(f,"ERR",e);continue
    if isinstance(d,list):
        k=collections.Counter(tuple(sorted(x.keys())) if isinstance(x,dict) else type(x).__name__ for x in d)
        print(f,"list",len(d),list(k.items())[:2])
    else:
        print(f,"dict",list(d.keys())[:10])
