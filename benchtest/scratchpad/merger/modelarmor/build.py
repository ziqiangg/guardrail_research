"""Build modelarmor_two_level.md and modelarmor_inventory_final.md from the drafts + resolutions (run from the repo root)."""
import re
import sys
import json
from collections import OrderedDict

sys.path.insert(0, "benchtest/scratchpad/merger/modelarmor")
import lib
import edits_a
import edits_b
import edits_inv

DR = "benchtest/drafts/"
FULLSHA = "37f936ac9d69e173da0ba4123e382c52b2dd741f"
TAG = "modelarmor/v1.3.0"


def norm(s):
    s = s.replace(FULLSHA, TAG).replace("37f936ac", TAG)
    s = re.sub(r"\bread (2026-10-09)", r"\1", s)
    return s


def main():
    A, notes_a = lib.parse_cols(DR + "modelarmor_cols_a.md")
    B, notes_b = lib.parse_cols(DR + "modelarmor_cols_b.md")
    C = OrderedDict()
    allc = {}
    allc.update(A)
    allc.update(B)
    for i in range(1, 11):
        C[f"MA{i}"] = allc[f"MA{i}"]
    # normalise pins and hint style first, so every edit anchors on the normalised text
    for d in C.values():
        d["head"] = norm(d["head"])
        for r in d["rows"].values():
            r["summary"] = norm(r["summary"])
            r["detail"] = [norm(x) for x in r["detail"]]
    before = {c: {n: (r["summary"], list(r["detail"])) for n, r in d["rows"].items()} for c, d in C.items()}

    edits_a.apply(C)
    edits_b.apply(C)
    open(DR + "modelarmor_two_level.md", "w", encoding="utf-8").write(lib.serialise_cols(C))

    pre, blocks, notes_i = lib.parse_inv(DR + "modelarmor_inventory.md")
    pre = [norm(x) for x in pre]
    for b in blocks:
        b["head"] = norm(b["head"])
        b["intro"] = [norm(x) for x in b["intro"]]
        b["hdr"] = [norm(x) for x in b["hdr"]]
        b["rows"] = [[norm(c) for c in r] for r in b["rows"]]
    pre[0] = "# Model Armor inventory (final, sheet 3x; the sheet letter is assigned at P8)"
    pre = edits_inv.apply(pre, blocks)
    open(DR + "modelarmor_inventory_final.md", "w", encoding="utf-8").write(lib.serialise_inv(pre, blocks))

    json.dump(dict(ops=lib.OPS, iops=lib.IOPS, notes_a=notes_a, notes_b=notes_b, notes_i=notes_i,
                   counts=[len(b["rows"]) for b in blocks]),
              open("benchtest/scratchpad/merger/modelarmor/ops.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("ops", len(lib.OPS), "iops", len(lib.IOPS), "block rows", [len(b["rows"]) for b in blocks])


if __name__ == "__main__":
    main()
