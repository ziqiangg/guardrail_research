import sys, os
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import merge_lib as L, ops_cols, ops_inv
D = "benchtest/drafts/"
def run():
    C = L.Cols([D + "lionguard_cols_a.md"])
    V = L.Inv(D + "lionguard_inventory.md")
    ops_cols.apply(C)
    ops_inv.apply(V)
    return C, V
if __name__ == "__main__":
    C, V = run()
    open(D + "lionguard_two_level.md", "w", encoding="utf-8").write(C.render(C.order))
    open(D + "lionguard_inventory_final.md", "w", encoding="utf-8").write(V.render())
    print("ops:", len(L.LOG), L.COUNTS)
