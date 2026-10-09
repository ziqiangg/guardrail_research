# R007 — Evidence and labelling precedents (from NeMo, Llama Guard, Sentinel)
- Date: 2026-10-09 (collected)   Product: global   Asked by: main
- Ruling (apply without asking):
  1. **Official sources** are the vendor's docs, the vendor's GitHub, Hugging Face or blog domains, and vendor-authored papers. For AWS-wrapped checks (Sentinel), AWS's own docs were used for AWS semantics, attributed in plain text.
  2. **Archived official pages** (Wayback) count as `[Documented]` with the plain text "(archived official page, <date>)". Current availability stays `[To be verified]`.
  3. **Legacy versions** (e.g. Llama Guard 1/2, LionGuard 1) appear in inventory and crosswalk tables only, never as Table 3 columns.
  4. **Two official sources that conflict** are written as two bullets, each labelled and attributed, and the conflict is logged in the change log. Prefer code at a pinned ref over docs for behaviour.
  5. **Absence claims** are `[Not disclosed]` with "checked X, Y". Never write `[Documented]` for "the docs don't say".
  6. **Closed or beta government services:** say "not public for a closed-beta service" in R8 and never speculate.
  7. **Pins:** GitHub repos use a tag or short SHA; HF repos use the revision sha; a deployed docs site uses its source repo commit when it can be matched (the Sentinel playbook precedent: staging @45908b48).
  8. **Comparator models** (e.g. a predecessor in a paper's table) may appear in Detail, never in Summaries.
- Decided by: user (accepted at past checkpoints)
- Applies to: all products
- Supersedes: none
