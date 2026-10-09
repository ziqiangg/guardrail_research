"""Quote sweep: every "..." fragment in sdp_two_level.md Detail bullets and sdp_inventory_final.md cells
is searched in the union of the fetched official pages (pages/) and the client code at the tag (code/).
Whitespace, curly quotes and the ellipsis are normalised; '…' splits a quote into parts."""
import re, glob, sys
base = "benchtest/scratchpad/verifier/sdp/"
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip().lower()
corpus = ""
for f in glob.glob(base + "pages/*.txt") + glob.glob(base + "code/*"):
    t = open(f, encoding="utf-8", errors="replace").read()
    corpus += "\n" + norm(t)
    # code: also strip leading '#' docstring indentation joins
corpus_nosp = re.sub(r"[^a-z0-9]", "", corpus)
miss, n = [], 0
for path in ["benchtest/drafts/sdp_two_level.md", "benchtest/drafts/sdp_inventory_final.md"]:
    cur = ""
    for ln, line in enumerate(open(path, encoding="utf-8"), 1):
        if line.startswith("## Column"):
            cur = line.split(":")[0][10:]
        if not (line.startswith("•") or line.startswith("  –") or line.startswith("|")):
            continue
        for q in re.findall(r'"([^"]{12,})"', line):
            for part in re.split(r"…|\.\.\.", q):
                part = part.strip(" .,;:")
                if len(part) < 12:
                    continue
                n += 1
                p = norm(part)
                if p in corpus:
                    continue
                if re.sub(r"[^a-z0-9]", "", p) in corpus_nosp:
                    continue
                miss.append(f"{path.split('/')[-1]}:{ln} [{cur}] {part[:150]}")
print("quote fragments checked:", n, "misses:", len(miss))
for m in miss:
    print("  ", m)
