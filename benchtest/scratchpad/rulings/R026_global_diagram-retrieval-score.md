# R026 — Diagram scorecard: Retrieval "Partly" vs "No"
- Date: 2026-10-09   Product: all diagrams   Asked by: gr-verifier (sdp P10 review Q1)
- Question: Sentinel scores Retrieval "No" and SDP "Partly", though both accept any text and neither documents retrieval use. Which rule keeps pages consistent?
- Ruling: On explainer-page scorecards, Retrieval is **Partly** only when the vendor documents a document, file or attachment input (or a retrieval integration) that a retrieved passage could go through; otherwise **No** (or Yes when a retrieval rail is documented, as for NeMo). "Accepts any text" alone is not enough. Existing pages already comply (Sentinel No; SDP and Presidio Partly on documented file/structured inputs), so no change to done products.
- decided_by: main (consistency convention; diagrams README scorecard rules; no change to user rulings)
- Applies to: all P10 diagrams from B1 on
- Supersedes: none
