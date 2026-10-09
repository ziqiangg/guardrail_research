import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import merge_lib as L, ops_cols, ops_inv
D = "/home/user/guardrail_research/benchtest/drafts/"
C = L.Cols([D + "presidio_cols_a.md", D + "presidio_cols_b.md"])
V = L.Inv(D + "presidio_inventory.md")
ops_cols.apply(C)
ops_inv.apply(V)
ids = C.order
open(D + "presidio_two_level.md", "w", encoding="utf-8").write(C.render(ids))
open(D + "presidio_inventory_final.md", "w", encoding="utf-8").write(V.render())
print("ops:", len(L.LOG), L.COUNTS)
