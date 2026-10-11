# Final run summary (2026-10-11)

Branch `claude/kind-keller-fv5ae4`. All ten products are done, sheet 4 is regrouped, and the workbook rebuilds with 0 diffs against HEAD.

## 1. Deliverables
| Product | Sheet 3 columns | Inventory / eval sheets | Explainer page | Key rulings |
|---|---|---|---|---|
| NeMo Guardrails (baseline) | F–U (16) | 3b, 3c eval | nemo-rails-explained.html | R001 |
| Llama Guard (baseline) | V–Z (5) | 3d | llama-guard-explained.html | — |
| GovTech Sentinel (baseline) | AA–AG (7) | 3e | sentinel-explained.html | — |
| Presidio | AH–AM (6) | 3f | presidio-explained.html | R016, R022, R029 |
| Sensitive Data Protection | AN–AS (6) | 3g. SDP Inventory | sdp-explained.html | R018, R023, R029 |
| Model Armor | AT–BC (10) | 3h | modelarmor-explained.html | R017, R024, R025, R029 |
| LionGuard | BD (1) | 3i | lionguard-explained.html | R031, R033, R035 |
| Purple Llama | BE–BK (7) | 3j, 3k CyberSecEval eval | purplellama-explained.html | R004, R030, R034, R036 |
| Cloak | BL–BN (3) | 3l | cloak-explained.html | R037, R039, R041 |
| Litmus | — (R003) | 3m, 3n eval | litmus-explained.html | R038, R040, R041 |
| Sheet 4 | — | 34 groups (14 multi-product, 20 single) | — | R006, R042 |

Checks: every product's apply verify passed at P8; final full rebuild exit 0 (only the known F16 non-failure), every inventory sheet and sheet 4 PASS, compare vs HEAD 0 diffs; all per-product URL checks 0 broken; every page passed a fresh diagram review and user approval; all pages share one CSS block (R028 phone fix). LibreOffice was not available on this machine, so panel formulas carry no cached values; Excel computes them on open.

## 2. Suggested first comparison group (proposal, R032)
**C1 — input-level PII and sensitive-data detection and masking.** Widest membership (Bedrock, NeMo, Sentinel, Presidio, SDP, Model Armor, Cloak) on three documented independent engines (AWS, Presidio, SDP; Cloak reuse of Presidio is undisclosed); objective ground truth (entity type and span) once entity lists are harmonised; Presidio-backed members run locally with no account; its labelled data could seed C2, C5, C6, C7 and C14. Alternative: **C10 jailbreak / prompt-attack detection** (six functions; CyberSecEval prompt-injection cases are a possible input source; Meta published no harmless look-alike negatives, so false-alarm data would have to be found or built). Minimum v1 architecture for C1: a text-in / findings-out harness calling each engine on the same labelled set, plus an entity mapping table.

## 3. Open items for the user (recorded, not decided)
- **Testing terms before any bench run:** Google Cloud AUP testing clause (Model Armor, SDP; R025 ruling 1) and Preview features synthetic data only (R025 ruling 2, decided); Cloak Terms 3.4.7 "benchmarking tests or analyses", 3.3 written consent, 3.4.9/3.4.11, Schedule 2.2; Llama 4 AUP item 1.h and the 700M-MAU clause; Together terms §4 ("competitive analysis or benchmarking", sensitive personal data, default retention) for AlignmentCheck/PIICheck; OpenAI / Gemini embedder terms for harmful test text (LionGuard 2 / 2.1; OpenAI policy pages unreadable, HTTP 403); Gemma terms for LionGuard Lite; LionGuard licence (MIT + Singapore law vs paper's "research and public interest purposes only"); Semgrep LGPL 2.1; CyberSOCEval data CC BY-ND / CC BY-SA.
- **Access:** Cloak and Litmus are gated (government / approved users; API docs behind login); testing them would need onboarding.

## 4. Follow-ups (not blocking)
- NeMo columns E/F still say the Presidio default replacement string is "not verified"; Presidio PD2 now documents it (NeMo frozen, R001).
- Together removed Llama Guard 4 12B (2026-08-25) and Llama 4 Maverick, AlignmentCheck's default judge (2026-03-31), from serverless inference.
- Sentinel sheet 3e pins the playbook at staging; a production-vs-staging note like Litmus's could be added.
- Diagram legend: the "your app's job" swatch is blue while those boxes are grey on several pages.
- SDP dates: MEDICAL_ID legacy window ended ~2026-10-11; PERSON_NAME stable ~2026-11-02.
- Rule slips (all unauthenticated, no data used): sdp P5 dlp.googleapis.com GETs; purplellama P5 api.together.xyz/v1/models (401); one huggingface.co/api/datasets listing GET.
- Repo hygiene: some scratch copies and duplicate PDFs were pushed before ignore rules were added (lessons 17, 19); history was not rewritten.

## 5. Next steps
1. Open a pull request from `claude/kind-keller-fv5ae4` to `main` on claude.ai/code and merge when ready.
2. Decide the section-3 terms items before any bench testing.
3. If a bench is built, start with C1 (or C10), using the per-product R7/R8 suggestions.
