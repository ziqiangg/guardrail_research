"""P7 verifier pass 2: explain every changed column line by (a) the merger's global gsub patterns
or (b) a full 'after' text in merger/sdp/log.json; then check each log.json entry is in sdp_changes.md.
Also reports removed original lines not accounted for by any log 'before'."""
import re, json, sys
sys.path.insert(0, "benchtest/scratchpad/verifier/sdp")
from diff_cols import parse, norm  # noqa  (re-runs pass 1; harmless)

G = [
    (r"the detection column", "the sensitive-data detection in text column"),
    (r"the reversible-tokenisation column", "the reversible tokenisation and re-identification column"),
    (r"they are covered in the image columns", "they are covered in the image detection and redaction and the image safety classification columns"),
    (r"the SD1 and SD2 columns", "the sensitive-data detection in text and custom detector columns"),
    (r"the SD5 column", "the image detection and redaction column"),
    (r"the SD6 column", "the image safety classification column"),
    (r"the SD3 column", "the masking and de-identification in text column"),
    (r"packages/google-cloud-dlp/(google/cloud/dlp/gapic_version\.py@|README\.rst@|setup\.py@)", r"\1"),
    (r"(?<![/\w])dlp_v2/", "google/cloud/dlp_v2/"),
    (r"(?<![/\w])dlp/gapic_version\.py@", "google/cloud/dlp/gapic_version.py@"),
]
def g(s):
    for p, r in G:
        s = re.sub(p, r, s)
    return s

D = "benchtest/drafts/"
orig = {}
orig.update(parse(D + "sdp_cols_a.md")); orig.update(parse(D + "sdp_cols_b.md"))
fin = parse(D + "sdp_two_level.md")
log = json.load(open("benchtest/scratchpad/merger/sdp/log.json", encoding="utf-8"))
cols_log = [e for e in log if e["file"] == "cols"]
afters = "\n".join(e["after"] for e in cols_log)
befores = "\n".join(e["before"] for e in cols_log)
chg = norm(open(D + "sdp_changes.md", encoding="utf-8").read())

unexpl, removed_unexpl = [], []
for c in sorted(fin):
    for r in range(1, 10):
        o = orig[c][r]; f = fin[c][r]
        og = [g(x) for x in o["lines"]]
        for x in f["lines"]:
            if x in og:
                continue
            if x.strip() in afters or g(x).strip() in afters:
                continue
            # an 'after' may itself have been later gsubbed
            if any(x.strip() in g(e["after"]) for e in cols_log):
                continue
            unexpl.append(f"{c} R{r}: {x[:220]}")
        fl = set(f["lines"])
        for x, xg in zip(o["lines"], og):
            if xg in fl or x in fl:
                continue
            if x.strip() in befores or x.strip()[:80] in befores:
                continue
            removed_unexpl.append(f"{c} R{r}: {x[:220]}")

print("final lines not explained by gsub or log.json:", len(unexpl))
for u in unexpl: print("  +", u)
print("removed original lines not in any log.json before:", len(removed_unexpl))
for u in removed_unexpl: print("  -", u)

# log.json -> changes.md
miss = []
for e in log:
    b = norm(e["before"])[:50]
    a = norm(e["after"])[:50]
    if (b and b in chg) or (a and a in chg):
        continue
    miss.append((e["file"], e["loc"], e["tid"], e["before"][:80], e["after"][:80]))
print("log.json entries not findable in sdp_changes.md:", len(miss))
for m in miss: print("  ", m)
