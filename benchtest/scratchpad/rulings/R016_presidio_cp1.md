# R016 — presidio CP1
- Date: 2026-10-09   Product: presidio   Asked by: main (CP1; triage T1–T7, Q01/Q02)
- Ruling:
  1. Official sources: data-privacy-stack docs, GitHub org and GHCR, plus Microsoft-authored pages (transition page, microsoft.github.io stub). Header prefix `Presidio:` is frozen. CLAUDE.md product row to read "Presidio (data-privacy-stack; formerly Microsoft)".
  2. Six columns PD1–PD6 as drafted (no fold of PD3→PD2 or PD6→PD1; PD5 presidio-structured stays a column).
  3. Inventory at recognizer-family level (31 rows), not per-entity.
  4. Research stays read-only (R019): no local pip/spaCy/GHCR runs; T17/T18/T25/T31/T33/T39 stay open as needs-testing for the bench.
  5. Third-party component licences (spaCy models, Tesseract, GLiNER, Medical-NER, …) are listed in the inventory, each citing its owner's page and marked "not Presidio docs" (R019).
- decided_by: user (AskUserQuestion, 2026-10-09)
