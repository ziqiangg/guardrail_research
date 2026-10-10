import re, os, sys, html
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
DIAG = os.path.join(ROOT, "benchtest", "diagrams")
OUT = os.path.join(DIAG, "cloak-explained.html")

def rd(p):
    with open(p, "rb") as f:
        return f.read().decode("utf-8")

# base CSS: sentinel lines 6-110 verbatim
sent = rd(os.path.join(DIAG, "sentinel-explained.html")).split("\n")
base = "\n".join(sent[5:110]) + "\n"

head = rd(os.path.join(HERE, "head.html"))
adds = rd(os.path.join(HERE, "additions.css"))
body = rd(os.path.join(HERE, "body.html"))

def marker(i, cls):
    return '<marker id="%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="%s"/></marker>' % (i, cls)

def defs_n(m):
    n, kinds = m.group(1), m.group(2)
    ind = " " * 10
    lines = [marker("a" + n, "ah")]
    mp = {"o": ("ahok", "o"), "n": ("ahno", "n"), "e": ("ahed", "e")}
    for k in kinds:
        cls, suf = mp[k]
        lines.append(marker("a" + n + suf, cls))
    return "<defs>\n" + "\n".join(ind + "  " + l for l in lines) + "\n" + ind + "</defs>"

body = re.sub(r"@@DEFS:(\d+)([one]*)@@", defs_n, body)
body = re.sub(r"@@MK:([a-z0-9-]+)@@", lambda m: marker(m.group(1), "ah"), body)

# positioning table: copy sibling cells word for word from presidio-explained.html (R027)
pres = rd(os.path.join(DIAG, "presidio-explained.html"))
tbl = re.search(r"<thead><tr><th></th><th>NeMo Guardrails</th>.*?</table>", pres, re.S).group(0)
rows = re.findall(r"<tr><td>.*?</tr>", tbl, re.S)
assert len(rows) == 8, len(rows)
cloak_cells = {
 "What it is": "A hosted service that finds personal data in text, documents and tables and rewrites it (free text is covered here)",
 "Who runs it": "GovTech, on the Government Commercial Cloud. No way to run free-text anonymisation yourself is documented.",
 "What it hands back": "Rewritten text or files, and in the Web UI (the Cloak website you sign in to) a findings table with a type and score for each match. No safe or unsafe verdict is described.",
 "Decides where checks run": "No. Your app chooses what to send; no input or output setting was found, and the API details are behind a login.",
 "Your own rules and fixed replies": "Your own entity types: word lists, patterns and, in beta, AI-model examples. You choose the replacement text.",
 "Edits text": "Yes: replace, redact, mask, alias, pseudonymise or encrypt",
 "Singapore languages": "Tuned for Singapore (NRICs, local phone numbers, UENs (business registration numbers), addresses, postal codes); names in roman characters. Other languages are not stated.",
 "Who can use it": "Government users, and select non-government entities that Cloak approves; the Terms limit others to a purpose GovTech agrees in writing. Free for approved users in FY26.",
}
out_rows = []
for r in rows:
    label = re.match(r"<tr><td>(.*?)</td>", r).group(1)
    new = r.replace("</tr>", "<td>%s</td></tr>" % cloak_cells[label])
    out_rows.append("          " + new)
body = body.replace("@@POSROWS@@", "\n".join(out_rows))

links = [
 ("Cloak Guide home", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/home.md"),
 ("Cloak Guide FAQs", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/faqs.md"),
 ("Free-text intro", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/intro-to-fta.md"),
 ("Usage guide", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/usage-guide.md"),
 ("Entity types", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/intro.md"),
 ("Confidence level", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/advanced-features/confidence-level.md"),
 ("Encrypt", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/encrypt.md"),
 ("Pseudonymisation", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/pseudonymisation.md"),
 ("Replace (Unique)", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/replace-unique.md"),
 ("Custom entities: fixed list", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-fixed-list.md"),
 ("Custom entities: regex", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-structured.md"),
 ("Custom entities: AI model (beta)", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/intro.md"),
 ("Free-text decryption", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/decryption/free-text-decryption.md"),
 ("Secrets Manager", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/decryption/secrets-manager.md"),
 ("Registration guide", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/registration-guide.md"),
 ("Release notes", "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/release-notes.md"),
 ("API guide (login required)", "https://docs.developer.tech.gov.sg/docs/cloak-api-guide/"),
 ("Cloak site", "https://www.cloak.gov.sg"),
 ("Portal: overview", "https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/overview"),
 ("Portal: features and roadmap", "https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/features-roadmap"),
 ("Portal: use cases", "https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/use-cases"),
 ("Portal: FAQs", "https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/faqs"),
 ("Terms of Use", "https://file.go.gov.sg/cloak-terms.pdf"),
 ("Privacy Statement", "https://go.gov.sg/cloak-privacy"),
 ("2023 USENIX PEPR slides", "https://www.usenix.org/system/files/pepr23_slides-tang.pdf"),
 ("Playbook: privacy improvements", "https://govtech-responsibleai.github.io/playbook/improving-ai-systems/privacy-improvements/"),
 ("Sentinel guardrails (checked, no mention of Cloak)", "https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails"),
]
body = body.replace("@@LINKS@@", " · ".join('<a href="%s">%s</a>' % (u, l) for l, u in links))

assert "@@" not in body, re.findall(r"@@.*?@@", body)
page = head + base + adds + "\n" + body
with open(OUT, "wb") as f:
    f.write(page.encode("utf-8"))
print("wrote", OUT, len(page))
