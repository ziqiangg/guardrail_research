import json, sys
sys.path.insert(0, "/home/user/guardrail_research/benchtest/scratchpad/merger/sdp")
from engine import Doc, ROOT, LOG
from cols_edits import apply_cols
from inv_edits import apply_inv

A = open(ROOT + "sdp_cols_a.md", encoding="utf-8").read().rstrip("\n").split("\n")
B = open(ROOT + "sdp_cols_b.md", encoding="utf-8").read().rstrip("\n").split("\n")
cols = Doc("cols", A + B, "col")
apply_cols(cols)

inv_src = open(ROOT + "sdp_inventory.md", encoding="utf-8").read().rstrip("\n").split("\n")
inv = Doc("inv", inv_src, "inv")
# split off the Reviewer notes (moved to the change log)
rn_start = next(i for i, l in enumerate(inv.lines) if l.startswith("## Reviewer notes"))
rn_text = "\n".join(inv.lines[rn_start:])
inv.lines = inv.lines[:rn_start]
while inv.lines and inv.lines[-1] == "":
    inv.lines.pop()
apply_inv(inv)

open(ROOT + "sdp_two_level.md", "w", encoding="utf-8").write("\n".join(cols.lines) + "\n")
open(ROOT + "sdp_inventory_final.md", "w", encoding="utf-8").write("\n".join(inv.lines) + "\n")
json.dump(LOG, open("/home/user/guardrail_research/benchtest/scratchpad/merger/sdp/log.json", "w"), indent=1, ensure_ascii=False)
open("/home/user/guardrail_research/benchtest/scratchpad/merger/sdp/inventory_reviewer_notes.md", "w", encoding="utf-8").write(rn_text + "\n")
print("edits logged:", len(LOG))
