import sys, os, re
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import merge_lib as L
import ops_pl12, ops_pl64, ops_pl357, ops_inv, ops_ev, ops_p7

D = "benchtest/drafts/"
IDS = ["PL1", "PL2", "PL3", "PL4", "PL5", "PL6", "PL7"]


def global_cols(K):
    # ruling ids and process wording that survive the targeted edits
    for c in IDS:
        for n in range(1, 9):
            s, e = K.row(c, n)
            Ls = K.cols[c]["lines"]
            for i in range(s, e):
                for old, new in (("Direction (R002):", "Direction:"), ("Direction under R002:", "Direction:")):
                    if old in Ls[i]:
                        before = Ls[i]
                        Ls[i] = Ls[i].replace(old, new)
                        L._log("cols", "%s R%d" % (c, n), "style", before, Ls[i], "style 3: ruling id removed from the cell text")


def global_cols2(K):
    pairs = [
        (7, "• Table 3 input type:", "• Possible Table 3 input type:", "R032: proposal wording"),
    ]
    for c in IDS:
        for n, old, new, why in pairs:
            s, e = K.row(c, n)
            Ls = K.cols[c]["lines"]
            for i in range(s, e):
                if old in Ls[i]:
                    b = Ls[i]; Ls[i] = Ls[i].replace(old, new)
                    L._log("cols", "%s R%d" % (c, n), "style", b, Ls[i], why)
        for n in range(1, 9):
            s, e = K.row(c, n)
            Ls = K.cols[c]["lines"]
            for i in range(s, e):
                for old, new in (("and the clone for a CHANGELOG file", "and the repository file list for a CHANGELOG file"),
                                 (", the clone for a CHANGELOG file", ", the repository file list for a CHANGELOG file")):
                    if old in Ls[i]:
                        b = Ls[i]; Ls[i] = Ls[i].replace(old, new)
                        L._log("cols", "%s R%d" % (c, n), "style", b, Ls[i], "style 3: 'the clone' is session wording; names what was checked")


def build():
    K = L.Cols([D + "purplellama_cols_a.md", D + "purplellama_cols_b.md"])
    ops_pl12.apply(K)
    ops_pl64.apply(K)
    ops_pl357.apply(K)
    ops_p7.apply_cols(K)
    ops_p7.apply_p8(K)
    global_cols(K)
    global_cols2(K)
    return K


def build_inv():
    V = L.Inv(D + "purplellama_inventory.md")
    ops_inv.apply(V)
    ops_p7.apply_inv(V)
    return V


if __name__ == "__main__":
    K = build()
    out = K.render(IDS)
    open(D + "purplellama_two_level.md", "w", encoding="utf-8").write(out)
    n1 = len(L.LOG)
    V = build_inv()
    open(D + "purplellama_inventory_final.md", "w", encoding="utf-8").write(V.render())
    n2 = len(L.LOG)
    E = L.Ev(D + "purplellama_eval_tooling.md")
    ops_ev.apply(E)
    ops_p7.apply_ev(E)
    open(D + "purplellama_eval_tooling_final.md", "w", encoding="utf-8").write(
        E.render("## Topic: Meta CyberSecEval 4 evaluation tooling (reuse assessment for the test bench)"))
    print("col ops:", n1, "inv ops:", n2 - n1, "eval ops:", len(L.LOG) - n2, L.COUNTS)
