import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s=open("check_v3.py",encoding="utf-8").read()
def sub(s,a,b):
    assert s.count(a)==1,a
    return s.replace(a,b)
s=sub(s,'MARKER = "\u2022 Single-product: no comparator among NeMo / Llama Guard / Sentinel yet"','MARKER = "\u2022 Single-product: no comparator among the ten products yet"')
s=sub(s,'''    if not single and len(letters) < 2:
        err(f"{cid}: marked multi-product but has {len(letters)} function(s)")''','''    PROD = {"LlamaFirewall": "Purple Llama", "Code Shield": "Purple Llama", "Prompt Guard 2": "Purple Llama"}
    prods = {PROD.get(HDR[L].split(":")[0], HDR[L].split(":")[0]) for L in letters}
    if not single and len(prods) < 2:
        err(f"{cid}: marked multi-product but spans only {prods}")
    if single and len(prods) != 1:
        err(f"{cid}: single-product row spans {prods}")''')
open("check_v3.py","w",encoding="utf-8").write(s)
