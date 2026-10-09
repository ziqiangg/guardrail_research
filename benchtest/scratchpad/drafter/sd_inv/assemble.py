import sys,re
sys.path.insert(0,'.')
from gen_common import *
import blk_a,blk_b,blk_c,blk_d,blk_e,blk_f
def tbl(hdr, rows):
    out=["| "+" | ".join(hdr)+" |","|"+"|".join(["---"]*len(hdr))+"|"]
    for r in rows:
        assert len(r)==len(hdr),(r[0],len(r),len(hdr))
        for c in r:
            assert "|" not in c and "`" not in c and "**" not in c,(r[0],c[:60])
        out.append("| "+" | ".join(r)+" |")
    return "\n".join(out)
FIX=[("DOCS overview","DOCS sensitive-data-protection-overview"),("DOCS limits","LIM"),("DOCS pricing","PRC"),("DOCS roles-permissions","DOCS access-control/roles-permissions")]
def fix(t):
    for a,b in FIX: t=t.replace(a,b)
    return t
HEAD = """# Sensitive Data Protection inventory (final, sheet 3x)

Scope: Google Cloud Sensitive Data Protection (SDP, formerly Cloud DLP; the API is still named the Cloud Data Loss Prevention API), covering the content methods that can sit on the AI data path and the storage, discovery and policy components around them. Rows that only process data unrelated to the AI conversation are kept as inventory and use the marker — (inventory only, not in Table 3). Covered-by cells use the six provisional SDP column headers. Labels use the sheet's allowed forms; docs facts are read pages with no public docs repo to pin, read on 2026-10-09; code facts are pinned to googleapis/google-cloud-python at tag google-cloud-dlp-v3.40.0 (commit 69401247a72c0f0786741ac937c3c5aa2afc8ead). Short names: DOCS slug = https://docs.cloud.google.com/sensitive-data-protection/docs/slug; REST name = DOCS/reference/rest/v2 page for that resource (REST root = DOCS/reference/rest); LIM = https://docs.cloud.google.com/sensitive-data-protection/limits; PRC = https://cloud.google.com/sensitive-data-protection/pricing; SLA = https://cloud.google.com/sensitive-data-protection/sla; Model Armor docs and Gemini Enterprise docs are cross-reference pages and are marked not SDP docs. Counts that are mine are labelled Inferred with the counting rule.
"""
INTRO = {
"a":"Components of the DLP API grouped by what they do. Only the synchronous content methods return results to the caller; none of them blocks anything by itself. The content policy is the only ALLOW or BLOCK output, and its evaluation call is not exposed in the REST resource or the Python client.",
"b":"Built-in infoTypes grouped, not one row per infoType, because the reference lists 261 and changes periodically. The page says to call infoTypes.list for the latest list [Documented] (DOCS infotypes-reference). Group boundaries are my own; counts come from the infoType categories table on the same page.",
"c":"The docs transformation table has exactly these 12 objects. Reversible and Referential integrity are read from the table columns (a mark or an empty cell).",
"d":"Ways to reach SDP and places SDP is wrapped. Model Armor rows are integration paths only; the Model Armor columns own their internals.",
"e":"Values are quoted from the limits, pricing and SLA pages. The limits page says its values are subject to change.",
"f":"Where SDP processes and stores things, and which locations support which features.",
}
parts=[HEAD]
for key,title,hdr,rows in [
 ("a","(a) Method and component catalogue",blk_a.HA,blk_a.ROWS_A),
 ("b","(b) InfoType group catalogue",blk_b.HB,blk_b.ROWS_B),
 ("c","(c) De-identification transformation catalogue",blk_c.HC,blk_c.ROWS_C),
 ("d","(d) Integration and access paths",blk_d.HDD,blk_d.ROWS_D),
 ("e","(e) Limits, quotas and pricing",blk_e.HE,blk_e.ROWS_E),
 ("f","(f) Region and availability",blk_f.HF,blk_f.ROWS_F)]:
    parts.append("## "+title+"\n"+fix(INTRO[key])+"\n\n"+fix(tbl(hdr,rows))+"\n")
open("body.md","w",encoding="utf-8").write("\n".join(parts))
print(sum(len(x) for x in [blk_a.ROWS_A,blk_b.ROWS_B,blk_c.ROWS_C,blk_d.ROWS_D,blk_e.ROWS_E,blk_f.ROWS_F]))
