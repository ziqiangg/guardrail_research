# Triage of open evidence items (DRAFT)

Source: `drafts/two_level.md` (15 columns). No research done beyond suggesting sources; source suggestions are taken from each column's own R9 list plus the obvious NVIDIA/vendor page. Nothing here is verified.

Legend
- Cell notation `column:row`. The first column (Input-level jailbreak detection, no letter in the file) is written `0`. Columns A to N as in the file.
- DOCS = https://docs.nvidia.com/nemo/guardrails
- REPO = https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1
- Current label: TBV = [To be verified]; ND = [Not disclosed]; R8 = unlabelled R8 open question. Where an item sits in several cells with different labels, the labels are joined with a slash.
- Class: a = doc-answerable, b = needs testing, c = licensing/paid.
- Splitting rule: mixed items were split into separate ids where clean (e.g. "documented limitation" vs "measured false-positive rate").

## Class (a) doc-answerable

| id | statement (short) | applies to | current label | class | suggested official source |
|---|---|---|---|---|---|
| a1 | Do dialog rails run on IORails? PRE-RESOLVED: Engine Feature Support page says dialog rails LLMRails yes, IORails no ("Require the Colang runtime"); execution rails LLMRails only; tool rails both | D:R4, D:R8 | ND (D:R4), R8 (D:R8) | a (status: pre-resolved) | https://docs.nvidia.com/nemo/guardrails/reference/engine-feature-support |
| a2 | Which rails run on LLMRails vs IORails per v0.24.1 matrix (jailbreak flows, topic control IORails parity, fact-check IORails exclusion list) | 0:R8, C:R8, M:R8 | R8 | a | DOCS/reference/rail-engine-support ; REPO/docs/reference/rail-engine-support.mdx |
| a3 | Tool-call and tool-result rails: which engine runs them on v0.24.1 (tool-calling page says IORails only and Colang 1.0; support pages say both). Note: Engine Feature Support page already says both, so only the page conflict and a runtime smoke test remain | K:R4, K:R8, L:R4, L:R8 | R8 (K:R8, L:R8) | a | DOCS/latest/configure-guardrails/guardrail-catalog/tool-calling ; https://docs.nvidia.com/nemo/guardrails/reference/engine-feature-support ; REPO/docs/configure-rails/guardrail-catalog/tool-calling.mdx |
| a4 | Is the LLM-based `tool_safety_check` rail documented, and is it in any release (develop branch only?) | K:R4, K:R8, L:R4, L:R8 | ND / TBV | a | github.com/NVIDIA-NeMo/Guardrails develop branch docs and releases page; REPO/nemoguardrails/guardrails/actions/tool_call_action.py |
| a5 | Do per-tool regex checks (`regex check tool input/output`) reach a release | H:R8, K:R4, K:R8, L:R4, L:R8 | TBV: future release / R8 | a | github.com/NVIDIA-NeMo/Guardrails/releases and CHANGELOG; REPO/nemoguardrails/library/regex/flows.co |
| a6 | Authoritative content-safety category list (S1-S22 vs S1-S23) | A:R2, A:R8 | TBV / R8 | a | Model card for Nemotron safety models on huggingface.co/nvidia ; DOCS/configure-guardrails/guardrail-catalog/content-safety |
| a7 | Is Nemotron Safety Guard v3 named on the current content-safety page | A:R4, A:R8 | TBV / R8 | a | DOCS/configure-guardrails/guardrail-catalog/content-safety |
| a8 | Jailbreak definition / taxonomy and precise coverage of the model flow (NemoGuard JailbreakDetect) | 0:R2, 0:R8 | ND+TBV / R8 | a | NVIDIA model card for NemoGuard JailbreakDetect (huggingface.co/nvidia, build.nvidia.com) ; DOCS/configure-guardrails/guardrail-catalog/jailbreak-protection |
| a9 | JailbreakDetect NIM decision threshold | 0:R5 | ND | a | Model card / NIM docs for NemoGuard JailbreakDetect ; DOCS/get-started/tutorials/nemoguard-jailbreakdetect-deployment |
| a10 | JailbreakDetect NIM training data | 0:R4 | ND | a | Model card (huggingface.co/nvidia) |
| a11 | Heuristic thresholds: defaults and configurability | 0:R8 | R8 | a | DOCS/configure-guardrails/guardrail-catalog/jailbreak-protection ; REPO/nemoguardrails/library/jailbreak_detection/actions.py |
| a12 | JailbreakDetect NIM endpoint and API key settings | 0:R8 | R8 | a | DOCS/get-started/tutorials/nemoguard-jailbreakdetect-deployment |
| a13 | Which rails honour `enable_rails_exceptions` (jailbreak, PII flows; PII flows show no exception path) | 0:R8, E:R8, F:R8 | R8 | a | REPO/nemoguardrails/library/sensitive_data_detection/flows.co ; REPO/nemoguardrails/library/jailbreak_detection/flows.co |
| a14 | Jailbreak output format (blocked or allowed, no score) | 0:R8 | R8 | a | REPO/nemoguardrails/library/jailbreak_detection/actions.py |
| a15 | Heuristic English-only limitation (documented scope) | 0:R8 | R8 | a | DOCS/configure-guardrails/guardrail-catalog/jailbreak-protection (the measured false-positive effect is b2) |
| a16 | torch/transformers dependency for heuristics | 0:R8 | R8 | a | DOCS/configure-guardrails/guardrail-catalog/jailbreak-protection |
| a17 | Are Llama Guard `policy_violations` populated | A:R8, B:R8 | R8 | a | REPO/nemoguardrails/library/llama_guard/flows.co and actions.py |
| a18 | Content-safety model language coverage | A:R8 | R8 | a | Model cards for the Nemotron safety models (huggingface.co/nvidia) |
| a19 | GCP Text Moderation input-only | B:R4 | TBV | a | DOCS/configure-guardrails/guardrail-catalog/third-party |
| a20 | Streaming support per engine and per variant (output rails incl. `self check output`; hallucination check with streaming) | B:R8, N:R8 | R8 | a | DOCS/v0.22.0/configure-guardrails/configuration-reference ; DOCS/reference/rail-engine-support |
| a21 | Custom topic-control models | C:R8 | R8 | a | DOCS/configure-guardrails/guardrail-catalog/topic-control ; model card for llama-3.1-nemoguard-8b-topic-control |
| a22 | Colang 1.0 vs 2.x differences | D:R8 | R8 | a | DOCS/configure-guardrails/colang/colang-1/tutorials/6-topical-rails (and the Colang 2 docs) |
| a23 | Presidio masking text (`mask_token` marked unused; default replacement text) | E:R8, F:R8 | R8 | a | REPO/nemoguardrails/library/sensitive_data_detection/actions.py ; Presidio docs (microsoft.github.io/presidio) |
| a24 | Presidio mask path uses default threshold 0.4 instead of configured `score_threshold` | E:R8 | R8 | a | REPO/nemoguardrails/library/sensitive_data_detection/actions.py ; Presidio default threshold in Presidio docs |
| a25 | spaCy install steps on the PII docs page | E:R8 | R8 | a | DOCS/configure-guardrails/guardrail-catalog/pii-detection |
| a26 | Polygraf absent from the PII docs page (docs coverage) | E:R4, E:R8, F:R8 | TBV / R8 | a | DOCS/configure-guardrails/guardrail-catalog/pii-detection ; REPO/nemoguardrails/library/polygraf/flows.co |
| a27 | Is the HF retrieval flow documented on the PII or agentic pages | G:R8 | R8 | a | DOCS/configure-guardrails/guardrail-catalog/pii-detection ; .../agentic-security |
| a28 | Regex/HF retrieval empty-chunk behaviour: one chunk or all (code blanks whole string) | G:R8 | R8 | a | REPO/nemoguardrails/library/regex/flows.co ; REPO/nemoguardrails/library/hf_classifier/flows.co |
| a29 | Retrieval chunk size limits | G:R8 | R8 | a | DOCS (retrieval / knowledge-base config) ; REPO/nemoguardrails/library/context_bloat_detection/actions.py |
| a30 | Retrieval checks per chunk or on joined text | G:R8 | R8 | a | REPO/nemoguardrails/library/regex/flows.co and the other retrieval flows.co files |
| a31 | Does the regex docs page state the matching function (code uses `search`) | H:R8 | R8 | a | DOCS/configure-guardrails/guardrail-catalog/third-party/regex ; REPO/nemoguardrails/library/regex/actions.py |
| a32 | Regex flag handling beyond case; multiline flag | H:R8 | R8 | a | REPO/nemoguardrails/library/regex/actions.py |
| a33 | Regex behaviour on empty patterns or missing section | H:R8 | R8 | a | REPO/nemoguardrails/library/regex/actions.py |
| a34 | Are any third-party backends documented for this function (jailbreak none; topic, dialog, regex, injection, context-bloat, tool call, tool result, hallucination) | C:R4, D:R4, H:R4, I:R4, J:R4, K:R4, L:R4, N:R4 | TBV | a | DOCS/configure-guardrails/guardrail-catalog/third-party (index) |
| a35 | Injection `sanitize` action accepted by validation but raises NotImplementedError; docs list only reject and omit | I:R8 | R8 | a | REPO/nemoguardrails/library/injection_detection/actions.py |
| a36 | Injection detection default action value | I:R8 | R8 | a | DOCS/configure-guardrails/guardrail-catalog/agentic-security ; REPO/nemoguardrails/library/injection_detection/actions.py |
| a37 | YARA built-in rule coverage | I:R8 | R8 | a | REPO/nemoguardrails/library/injection_detection/ (yara_rules dir) |
| a38 | Does the `bot say` refusal text leak matched rule names | I:R8 | R8 | a | REPO/nemoguardrails/library/injection_detection/flows.co |
| a39 | Context-bloat `truncate` only cuts for size cap, rejects other findings (docs silent) | J:R8 | R8 | a | REPO/nemoguardrails/library/context_bloat_detection/actions.py ; DOCS agentic-security page |
| a40 | Context-bloat `min_chars` and `ngram_size` defaults | J:R8 | R8 | a | REPO/nemoguardrails/library/context_bloat_detection/actions.py |
| a41 | Is a `warn` result visible to the caller | J:R8 | R8 | a | REPO/nemoguardrails/library/context_bloat_detection/flows.co |
| a42 | Non-OpenAI tool wire formats (docs say OpenAI Chat Completions only) | K:R8, L:R8 | R8 | a | DOCS/latest/configure-guardrails/guardrail-catalog/tool-calling |
| a43 | Are tool-call arguments seen by plain output rails | K:R8 | R8 | a | DOCS/latest/configure-guardrails/guardrail-catalog/tool-calling |
| a44 | Silent fallback to LLMRails when a tool flow name is mistyped/redundant | K:R8, L:R8 | R8 | a | DOCS/latest/configure-guardrails/guardrail-catalog/tool-calling (already stated; confirm) |
| a45 | Which JSON Schema dialects validate | K:R8 | R8 | a | REPO/nemoguardrails/guardrails/actions/tool_call_action.py (validator class used) |
| a46 | Tool results: no content check / no cross-turn provenance (documented as not covered; note bench may want a compensating rail) | L:R8 | R8 | a | DOCS/latest/configure-guardrails/guardrail-catalog/tool-calling |
| a47 | Thresholds for non-LLM fact-check backends | M:R8 | R8 | a | DOCS/configure-guardrails/guardrail-catalog/fact-checking ; vendor docs |
| a48 | How `$check_facts` / `$check_hallucination` / `$hallucination_warning` flags are set in practice | M:R8, N:R8 | R8 | a | DOCS/configure-guardrails/guardrail-catalog/fact-checking |
| a49 | Exact output shape per fact-check vendor | M:R5 | TBV | a | Vendor docs (Patronus, Fiddler, AutoAlign, Cleanlab, AlignScore repo) ; DOCS third-party pages |
| a50 | Which main-LLM providers work with self-check hallucination | N:R4, N:R8 | TBV / R8 | a | DOCS/configure-guardrails/guardrail-catalog/fact-checking ; REPO/nemoguardrails/library/hallucination/actions.py |
| a51 | Hallucination check makes parallel separate calls rather than an `n` parameter | N:R4 | TBV | a | REPO/nemoguardrails/library/hallucination/actions.py |

## Class (b) needs testing (stays open for the test bench)

| id | statement (short) | applies to | current label | class | suggested official source |
|---|---|---|---|---|---|
| b1 | Behaviour when detector/backend is unreachable (jailbreak documented fail-open, Polygraf fails closed per code, others unchecked, hallucination extra-calls fail-open) | 0:R8, E:R8, N:R8 | R8 | b (note: partly code-readable; test confirms) | none; code hints in REPO/nemoguardrails/library/polygraf/flows.co |
| b2 | False-positive rate on non-English text and code (jailbreak benign set) | 0:R6 | TBV | b | none (docs give heuristic FPR only) |
| b3 | False-positive / false-negative rates (content safety, topic control, fact-check) | A:R8, C:R8, M:R8 | R8 | b | none (model cards give vendor numbers, not bench numbers) |
| b4 | Streaming leakage: unsafe text or unmasked PII released before block/rewrite | B:R8, F:R8 | R8 | b | none |
| b5 | Violation spanning chunk boundaries | B:R8 | R8 | b | none |
| b6 | Topic-control multi-turn behaviour | C:R8 | R8 | b | none |
| b7 | Topic-control policy-prompt sensitivity | C:R8 | R8 | b | none |
| b8 | Dialog intent-matching robustness to paraphrase and adversarial phrasing | D:R8 | R8 | b | none |
| b9 | Embeddings-only similarity threshold tuning | D:R8 | R8 | b | none |
| b10 | Does single-call mode change accuracy | D:R8 | R8 | b | none |
| b11 | Latency and extra LLM calls (dialog; hallucination 3+ calls) | D:R8, N:R8 | R8 | b | none |
| b12 | PII recall and precision per entity type and language, incl. model-generated PII | E:R8, F:R8 | R8 | b | none |
| b13 | Behaviour with custom retrievers | G:R8 | R8 | b | none |
| b14 | ReDoS / regex timeout handling | H:R8 | R8 | b | none (docs unlikely to cover) |
| b15 | Unicode normalisation in regex matching | H:R8 | R8 | b | none |
| b16 | Injection `omit` effectiveness | I:R8 | R8 | b | none |
| b17 | False positives on legitimate code answers (injection) | I:R8 | R8 | b | none |
| b18 | False positives on legitimate long pastes (context bloat) | J:R8 | R8 | b | none |
| b19 | Multilingual entropy behaviour | J:R8 | R8 | b | none |
| b20 | Fact-check behaviour with long or multiple chunks | M:R8 | R8 | b | none |
| b21 | Accuracy of the self-consistency agreement judge | N:R8 | R8 | b | none |
| b22 | Selected jailbreak flow (heuristics vs model); bench design decision, not a research fact | 0:R8 | R8 | b (note: decision item, closes when the bench picks) | none |

## Class (c) licensing / paid

| id | statement (short) | applies to | current label | class | suggested official source |
|---|---|---|---|---|---|
| c1 | NIM production licence terms (AI Enterprise needed or not): content-safety, topic-control NIMs (also applies to the JailbreakDetect NIM, which the file does not label) | A:R8, B:R8, C:R8 | R8 | c | https://www.nvidia.com/en-us/data-center/products/ai-enterprise/ ; NVIDIA AI Enterprise / NIM licence terms; build.nvidia.com model pages |
| c2 | Licence terms for Nemotron Safety Guard v3 and Reasoning-4B | A:R8 | R8 | c | Model cards on huggingface.co/nvidia (licence field) |
| c3 | Paid status of listed content-safety vendors (ActiveFence, Cisco AI Defense, Prompt Security, Fiddler, CrowdStrike AIDR, Trend Micro, GCP Text Moderation) | A:R4, A:R8, B:R4, B:R8 | TBV / R8 | c | Each vendor's official pricing page; DOCS/configure-guardrails/guardrail-catalog/third-party |
| c4 | Licensing of Clavata and PolicyAI | A:R4, B:R4 | TBV | c | Vendor official sites |
| c5 | Guardrails AI and HF classifier confirmed open-source | A:R4, B:R4, G:R4 | TBV | c | github.com/guardrails-ai/guardrails licence file; model card of the chosen HF classifier |
| c6 | GLiNER-PII NIM: paid status / licence, and whether it is open | E:R4, E:R8, F:R4, F:R8, G:R4, G:R8 | TBV / R8 | c | build.nvidia.com GLiNER-PII model page; Hugging Face model card |
| c7 | Private AI pricing / paid status | E:R4, E:R8, F:R4, F:R8, G:R4, G:R8 | TBV / R8 | c | https://www.private-ai.com (pricing page) |
| c8 | Polygraf licensing and pricing | E:R4, E:R8, F:R4, F:R8, G:R4, G:R8 | TBV / R8 | c | Polygraf official site; REPO/nemoguardrails/library/polygraf/ |
| c9 | Presidio open-source confirmation | E:R4, F:R4, G:R4 | TBV | c | github.com/microsoft/presidio licence file |
| c10 | YARA open-source confirmation | I:R4 | TBV | c | github.com/VirusTotal/yara and yara-python licence files |
| c11 | Paid status / cost of fact-check vendors (Patronus API, Fiddler faithfulness, AutoAlign, Cleanlab) | M:R4, M:R8 | TBV / R8 | c | Each vendor's official pricing page |
| c12 | AlignScore licence (open-source self-hosted; model licence) | M:R4, M:R8 | TBV / R8 | c | github.com/yuh-zha/AlignScore licence; model card |
| c13 | Patronus Lynx open-weight licence | M:R4 | TBV | c | Patronus Lynx model card on huggingface.co/PatronusAI |

## Counts per class

| class | count |
|---|---|
| (a) doc-answerable | 51 (of which 1 pre-resolved: a1) |
| (b) needs testing | 22 |
| (c) licensing/paid | 13 |
| total ids | 86 |

Notes
- Splits made: jailbreak English-only (a15 documented scope vs b2 measured false positives); jailbreak outage (documented fail-open stays inside b1 with a note).
- a3 is partly covered by the Engine Feature Support page (tool rails supported on both engines); only the conflict with the tool-calling page remains. It was not marked pre-resolved because the brief named only the dialog item.
- Items with a mixed nature and the dominant class chosen: b1 (b, partly code-readable), b22 (b, decision), a46 (a, already documented as a gap).

## Recommended research order for (a) and (c)

Highest decision value for the test bench first.

1. a3, a2, then a1 closeout (engine support): decides which engine every config, and therefore every test, runs on.
2. a4, a5: decides whether tool_safety_check and per-tool regex are in scope or out of scope for v0.24.1.
3. c1, c2: NIM and Nemotron model licence terms gate whether the NVIDIA safety/topic/jailbreak models can be used at all.
4. c6, c7, c8 (then c3, c4, c11): PII and third-party backend paid status decides which backends enter the bench.
5. a50, a17, a13: provider support, Llama Guard violation metadata and exception behaviour shape the test harness and its assertions.
6. a8, a9, a6, a7: taxonomy, thresholds and model naming fix the labels for the content-safety and jailbreak datasets.
7. a48, a47, a49: how fact-check flags and non-LLM thresholds are set, needed before building those tests.
8. a23-a26 (Presidio masking/threshold, Polygraf docs coverage), a35-a41 (injection and context-bloat code behaviour).
9. Remaining (a) items and (c) open-source confirmations (c5, c9, c10, c12, c13), which are quick lookups.
