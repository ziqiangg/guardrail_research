# R011 — Third Covered-by marker: inventory only
- Date: 2026-10-09   Product: global (first use: presidio)   Asked by: gr-drafter (presidio P1 report)
- Question: Inventory rows that are current and available but deliberately not Table 3 columns (e.g. presidio-research per R010, presidio-cli) fit neither `— (legacy, not in Table 3)` nor `— (planned, not in Table 3)`. Which marker?
- Options considered: (a) reuse "legacy" (false); (b) add a third marker; (c) leave the cell blank (fails checks).
- Ruling: (b). Marker `— (inventory only, not in Table 3)` (em dash). Allowed in `check_drafts.py` MARKERS and documented in `drafts/README.md`. A new product's inventory config adds it to its `markers` tuple (gr-xlsx-writer, P8). Existing sheets 3b–3e are unchanged.
- decided_by: main (rules: inventory sheet config `markers` is per product; formatting/naming default)
