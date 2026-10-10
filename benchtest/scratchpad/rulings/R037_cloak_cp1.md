# R037 — cloak CP1
- Date: 2026-10-10   Product: cloak   Asked by: main (CP1, after P4 triage: 75 items, H 13)
- Ruling:
  - **Columns:** three, CK1 `Cloak: Free-text PII detection and anonymisation`, CK2 `Cloak: Custom entity detection in free text (lists, regex and LLM)`, CK3 `Cloak: Reversible anonymisation and decryption (encrypt and restore)`. Tabular anonymisation, mock data generation, the offline Anonymiser package and Mirage stay inventory only; enCRYPT legacy.
  - **CK3 direction (R002):** one column; anonymise and restore sides stay separate bullets; revisit only if the gated API later shows a direction setting.
  - Prefix `Cloak:` and header wording as ruled by main (queue.md). Terms clauses (3.3, 3.4.7, 3.4.9, 3.4.11, Schedules 2.2/4.6) recorded verbatim, permitted use decided before any bench testing (R025 pattern, R032 wording).
- decided_by: user (AskUserQuestion, 2026-10-10)
