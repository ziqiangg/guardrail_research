# R021 — Verbatim read when fetch_text.py returns an empty body
- Date: 2026-10-09   Product: global (first use: modelarmor T21)   Asked by: gr-verifier (modelarmor P7, Q1)
- Ruling: A plain `curl` GET of the official page, parsed with the Python standard-library HTML parser, counts as a verbatim read (it is raw page text, not a summary; CLAUDE.md hard rule 4). Record the method in the scratchpad. An absence found this way is `[Not disclosed]` with what was checked.
- decided_by: main (CLAUDE.md hard rules 2 and 4)
