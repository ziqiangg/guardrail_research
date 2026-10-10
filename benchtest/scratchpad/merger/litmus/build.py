import json, re, sys, os
sys.path.insert(0, "benchtest/scratchpad/merger/litmus")
import ev_ops, inv_ops

ev, inv = ev_ops.ev, inv_ops.inv
evt = ev.result()
invt = inv.result()

# ---- brief conflict ids (C1..C21 exist only in the brief and triage) -> plain wording; ordered, specific first
CONF = []
def cs(old, new):
    global evt
    c = evt.count(old)
    assert c >= 1, old
    evt = evt.replace(old, new)
    CONF.append((old, new, c))

cs(" per test case (conflict C8).", " per test case.")
cs("(conflict C4, not resolved)", "(the sources conflict; not resolved)")
cs("(conflict C8 with the docs' pass/fail per test case)", "(this conflicts with the docs' pass/fail per test case)")
cs("(conflict C11; DOCS Test-Information-Documentation)", "(the page mixes both words; DOCS Test-Information-Documentation)")
cs("(no test_suites line, conflict C3)", "(no test_suites line, although the parameter table marks it required)")
cs("(conflict C2) [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1]", "(the two Actions differ) [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1]")
cs("with different inputs (conflict C2); and does the Getting Started example need `test_suites` (conflict C3)?",
   "with different inputs; and does the Getting Started example need `test_suites`, which the parameter table marks required?")
cs("(conflict C18)", "(the step heading and the text differ)")
cs("Wording (conflict C5):", "Wording:")
cs("\"wog-baseline-v1\", conflict C7)", "\"wog-baseline-v1\", which differs from the id above)")
cs("(conflict C7 on the suite name `wog-baseline-v1` against `aiguardian-baseline-tests`)", "(the suite name `wog-baseline-v1` differs from `aiguardian-baseline-tests`)")
cs("Description, conflict C13:", "Description (the two texts differ):")
cs("Conflict C14:", "Conflict:")
cs("(conflict C20)", "(the two descriptions differ)")
cs("(conflict C6: staging login link", "(the hosts differ: staging login link")
cs("(conflict C4: portal", "(the sources differ: portal")
cs("since the docs describe prompt testing only (conflict C10)?", "since the docs describe prompt testing only?")
cs("playbook example), conflict C8?", "playbook example)?")
cs("Alignment, conflict C9 first side:", "Alignment, first side of a minor difference:")
cs("Alignment, conflict C9 second side:", "Alignment, second side:")
cs("Host conflict C6, ", "Host conflict, ")
cs("Taxonomy, conflict C1, developer portal:", "Taxonomy, developer portal (differs from the docs test page):")
cs("Taxonomy, conflict C1, one-pager:", "Taxonomy, one-pager (differs from both pages):")
cs("Kaleidoscope, conflict C12, playbook Kaleidoscope page:", "Kaleidoscope, playbook Kaleidoscope page (it differs from the Litmus page):")
left = re.findall(r"[Cc]onflict C\d+", evt)
assert not left, left

# parse checks later in separate script
OUT = "benchtest/drafts/"
open(OUT + "litmus_eval_tooling_final.md", "w", encoding="utf-8", newline="\n").write(evt.rstrip("\n") + "\n")
open(OUT + "litmus_inventory_final.md", "w", encoding="utf-8", newline="\n").write(invt.rstrip("\n") + "\n")
json.dump(dict(ev=ev.log, inv=inv.log, conf=CONF), open("benchtest/scratchpad/merger/litmus/log.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("EV ops", len(ev.log), "INV ops", len(inv.log), "conf replacements", sum(c for _, _, c in CONF))
