# -*- coding: utf-8 -*-
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def rd(f): return open(f, encoding="utf-8").read()
def wr(f, s): open(f, "w", encoding="utf-8").write(s)
def sub(s, a, b, cnt=1):
    assert s.count(a) == cnt, (a, s.count(a))
    return s.replace(a, b)
g = rd("gen_v3.py")
g = sub(g, 'MARKER = "Single-product: no comparator among NeMo / Llama Guard / Sentinel yet"', 'MARKER = "Single-product: no comparator among the ten products yet"')
g = sub(g, 'CARRY = {"C12": "C6", "C16": "C7", "C17": "C8", "C18": "C11", "C19": "C13",', 'CARRY = {"C12": "C6", "C15": "C7", "C16": "C8", "C17": "C11", "C18": "C12", "C19": "C13",')
g = sub(g, 'ORDER = [f"C{i}" for i in range(1, 34)]\nNMULTI = 15', 'ORDER = [f"C{i}" for i in range(1, 35)]\nNMULTI = 14')
g = sub(g, '        b = [x for x in b if not x.startswith("Single-product:") and x != ALSO]\n        d["diffs"] = ([MARKER, ALSO] + b, r)', '        b = [x for x in b if not x.startswith("Single-product:")]\n        d["diffs"] = ([MARKER] + b, r)')
g = sub(g, '''    L.append("Regrouped once across all ten products (R006), from the sheet 3 columns E to BN. Bench content in columns C to G is "
             "worded as proposals (R032); nothing here decides the bench design. Evaluation tools''', '''    L.append("Regrouped once across all ten products (R006), from the sheet 3 columns E to BN. Bench content in new and changed rows (columns C to G) is "
             "worded as proposals (R032); rows carried from v2 keep their v2 wording (see D2). Nothing here decides the bench design. Evaluation tools''')
wr("gen_v3.py", g)
print("ok")
