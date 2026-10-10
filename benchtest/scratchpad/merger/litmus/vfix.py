"""P7 verifier fixes: applied to the finals after build.py; logged to log.json key 'vfix'."""
import json
D = "benchtest/drafts/"
EVP, INVP = D + "litmus_eval_tooling_final.md", D + "litmus_inventory_final.md"
ev = open(EVP, encoding="utf-8").read()
inv = open(INVP, encoding="utf-8").read()
LOG = []


def short(s, n=120):
    s = s.replace("**", "").replace("|", "/").replace("`", "")
    return s if len(s) <= n else s[:n - 1] + "…"


def fx(which, old, new, loc, kind, why, count=1):
    global ev, inv
    t = ev if which == "EV" else inv
    assert t.count(old) == count, (which, old[:70], t.count(old))
    t = t.replace(old, new)
    if which == "EV":
        ev = t
    else:
        inv = t
    LOG.append(dict(file=which, loc=loc, kind=kind, before=short(old), after=short(new), why=why))


# ---- required fixes
fx("EV", "and the `govtech-responsibleai` organisation (11 repositories) has none (checked 2026-10-10)",
   "and the `govtech-responsibleai` organisation (12 public repositories, listed 2026-10-10) has none (checked 2026-10-10)",
   "Overview, 'No open-source Litmus server or client' bullet (line 40)", "replace",
   "Required fix 1: GitHub's organisation listing shows 12 public repositories, not 11 (the 11 came from an MCP search result); main ruling: absence checks that quote an organisation size cite the organisation listing")
fx("EV", "pages); do not read \"built on Moonshot\" into it **[Not disclosed]**",
   "pages); no source states that the hosted service is built on Moonshot **[Not disclosed]**",
   "Engine coverage, 'Litmus engine' bullet (line 137)", "replace", "Required fix 2: instruction to the reader removed (README section 4; R032)")
fx("INV", "All rows are inventory only: Litmus tests an application, it is not a guardrail.",
   "All rows are inventory only: Litmus tests an application; it does not defend one at runtime [Documented: repo govtech-responsibleai/playbook@45908b48] (PB tools/litmus.md@45908b48:46).",
   "Block (a) intro (line 9)", "replace", "Required fix 3: unlabelled classification replaced by the quoted playbook sentence (T20 precedent)")
fx("INV", "The sample Action inserts the value, unquoted, into a JSON array named endpoints, so it expects a JSON string or object [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1].",
   "The sample Action inserts the value, unquoted, into a JSON array named endpoints [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1] (action.yml@190600937062:34-36). The value must therefore already be valid JSON, such as a quoted string [Inferred] (premise: it is placed unquoted inside a JSON array).",
   "(c) endpoint row, Conflict or note cell (line 38)", "replace", "Required fix 4: file fact and drafter's reading split into two labelled facts (README section 3 rule 5)")

# ---- optional suggestions (all accepted by main)
loc_fixes = [
    ("EV", "tools/litmus.md line 53. The sample GitHub Action", "tools/litmus.md@45908b48:53. The sample GitHub Action", "Version scope (line 3)"),
    ("INV", "tools/litmus.md line 53)", "tools/litmus.md@45908b48:53)", "Short-name legend, PB (line 5)"),
    ("EV", "(PB tools/litmus.md line 57)", "(PB tools/litmus.md@45908b48:57)", "Overview, TechPass bullet (line 19)"),
    ("EV", "(PB tools/litmus.md line 46 and the Where it fits section)", "(PB tools/litmus.md@45908b48:46 and the Where it fits section)", "Overview, Sentinel relation bullet (line 24)"),
    ("EV", "(PB tools/litmus.md line 9)", "(PB tools/litmus.md@45908b48:9)", "Red-teaming, curated prompts bullet (line 105)"),
    ("EV", "safety.mdx, line 17)", "safety.mdx@45908b48:17)", "Red-teaming, safety-testing bullet (line 111)"),
    ("EV", "(PB tools/kaleidoscope.md line 22 ", "(PB tools/kaleidoscope.md@45908b48:22 ", "Red-teaming, Kaleidoscope bullet (line 112)"),
    ("EV", "(PB tools/litmus.md line 52)", "(PB tools/litmus.md@45908b48:52)", "Engine coverage, playbook caution bullet (line 124)"),
    ("EV", "(PB tools/litmus.md line 46) **[Documented", "(PB tools/litmus.md@45908b48:46) **[Documented", "Engine coverage, pairing bullet (line 125)"),
    ("EV", "(PB tools/litmus.md line 57; not visited)", "(PB tools/litmus.md@45908b48:57; not visited)", "Engine coverage, host bullet playbook (line 139)"),
    ("EV", "(line 46) and a body of", "(action.yml@190600937062:46) and a body of", "Engine coverage, sample Action bullet (line 130)"),
]
for w, o, n, l in loc_fixes:
    fx(w, o, n, l, "style", "Optional 1: uniform file@ref:line locator (changes section 1 said all locators use this form)")
fx("EV", "• No archived copy of either address: the Internet Archive availability API returned no snapshot and its CDX index no rows (checked 2026-10-10; control: one capture of Litmus-Getting-Started on 2026-05-13) **[Documented]**",
   "• The Internet Archive availability API returned no snapshot for either address and its CDX index no rows (checked 2026-10-10; control: one capture of Litmus-Getting-Started on 2026-05-13) **[Documented]**",
   "Overview, archive bullet (line 45)", "replace", "Optional 2: observation form instead of an absence opening under [Documented]")
fx("EV", "• Pass conditions in the test page depend on the application (for example \"unless it is a medical chatbot\"), so a bench could record the application's purpose with each case. **[Inferred]**",
   "• Some test descriptions depend on the application (Medical: \"unless it is a medical chatbot\"; Financial: \"unless it is a financial services specific chatbot\"), so a bench could record the application's purpose with each case. **[Inferred]**",
   "Reuse, application-dependence bullet (line 151)", "replace", "Optional 3: the quoted words are in the Description column, not the Outcome (pass condition) column")
fx("EV", "functional evaluation module within Litmus\". |", "functional evaluation module within Litmus\" [Documented: repo govtech-responsibleai/playbook@45908b48]. |",
   "Tools row 6, Evaluates cell (line 58)", "edit", "Optional 4: the closing sentence gets its own label, as the inventory Kaleidoscope row does")
fx("EV", "• Relation to Sentinel (sheet 3e, columns AA to AG, plain-text cross-reference):",
   "• Relation to Sentinel (sheet 3 columns AA to AG and inventory sheet 3e, plain-text cross-reference):",
   "Overview, Sentinel relation bullet (line 24)", "replace", "Optional 5: columns AA to AG are on sheet 3; 3e is the Sentinel inventory sheet")
fx("INV", "(file name dated 2025-09-16)", "(created 2025-09-16 per the PDF metadata)",
   "(a) Onboarding and access request / Needs (line 16)", "edit", "Optional 6: same provenance wording as the eval sheet (T10)")
fx("EV", "No list of supported models or guardrails,", "No list of supported models or providers,",
   "Engine coverage Summary", "summary", "Optional 7: 'providers' is backed by the Detail bullet on supported models and providers; 'guardrails' was only indirectly backed; still 43 words excluding the label")
fx("EV", "(2024-12-10): the same DTO", "(2024-12-10; AI Verify Foundation repo, not a GovTech source): the same DTO",
   "Engine coverage, Moonshot 0.5.0 bullet (line 132)", "edit", "Optional 8: the bullet carries its own 'not a GovTech source' note")
fx("EV", "(latest tag, 2026-02-05): the route takes", "(latest tag, 2026-02-05; AI Verify Foundation repo, not a GovTech source): the route takes",
   "Engine coverage, Moonshot 0.7.6 bullet (line 133)", "edit", "Optional 8")
fx("EV", "that the portal links to? The portal says \"To begin, refer to this onboarding guide.\" and links",
   "that the portal links to (the portal says \"To begin, refer to this onboarding guide.\" and links",
   "Open questions, onboarding guide (line 173)", "style", "Optional 9: one question mark")
fx("EV", "guide\" (no capture of the guide found)? **[To be verified]**", "guide\"; no capture of the guide found)? **[To be verified]**",
   "Open questions, onboarding guide (line 173)", "style", "Optional 9: closes the bracket")
fx("EV", "Kaleidoscope is recorded as one row and its repository was not researched.", "Kaleidoscope is one row, from GovTech pages only.",
   "Tools note (line 49)", "style", "Optional 10: process wording removed")

open(EVP, "w", encoding="utf-8", newline="\n").write(ev)
open(INVP, "w", encoding="utf-8", newline="\n").write(inv)
lg = json.load(open("benchtest/scratchpad/merger/litmus/log.json", encoding="utf-8"))
lg["vfix"] = LOG
json.dump(lg, open("benchtest/scratchpad/merger/litmus/log.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("vfix", len(LOG))
