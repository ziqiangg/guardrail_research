# R012 — Model Armor sensitive-data columns vs the SDP product
- Date: 2026-10-09   Product: modelarmor, sdp   Asked by: gr-explorer (modelarmor P0, Q02)
- Question: Should MA5/MA6 (sensitive data via Sensitive Data Protection) stay as Model Armor columns when SDP gets its own columns?
- Options considered: (a) keep MA5/MA6, limited to how Model Armor invokes SDP (basic vs advanced, templates, limits, result fields), cross-referencing SDP for infoTypes and transformations; (b) drop them and point to SDP only.
- Ruling: (a). Precedents: NeMo PII columns wrap Presidio and Sentinel SN6 wraps AWS PII; each wrapper keeps its own column and cross-references the wrapped engine, never duplicating its internals. SDP columns describe the SDP API itself and list Model Armor as an integration path in the SDP inventory. Column split itself (MA1–MA10 vs fewer) remains a CP1 question (modelarmor q01).
- decided_by: main (precedent: NeMo E/F ↔ Presidio; SN6 ↔ AWS; CLAUDE.md "cross-reference, never duplicate")
