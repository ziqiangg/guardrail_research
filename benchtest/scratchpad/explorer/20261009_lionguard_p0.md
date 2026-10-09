# LionGuard P0 note (2026-10-09, gr-explorer)

## 1. Header
- **Product:** GovTech LionGuard (open models, self-hosted). Scope per R005: LionGuard 2, 2.1, 2 Lite as columns; LionGuard 1 inventory only. Hosted Sentinel behaviour stays under Sentinel (AA, sheet 3e).
- **Canonical repos (Hugging Face, org `govtech`, not gated; all re-checked 2026-10-09 via `https://huggingface.co/api/models/govtech/<repo>`; no revision has moved since the seeds):**
  - `govtech/lionguard-2` @ `be4e38c9` (full `be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591`, lastModified 2025-11-18)
  - `govtech/lionguard-2.1` @ `1c3a9ea7` (full `1c3a9ea7718f81ea32e6688c0ff18ac8866525e8`)
  - `govtech/lionguard-2-lite` @ `d56c17a0` (full `d56c17a08a937f2591a906fb5c8ec699a844c422`)
  - `govtech/lionguard-v1` @ `92cc0491` (full `92cc0491764602c97031693a7f1a2bcc82c6aaf9`, legacy)
  - Demo Space `govtech/lionguard-demo` @ `4ade46d1` (docker; unchanged since 2025-11-19).
- **GitHub:** no LionGuard inference or training repo found. The `govtech-responsibleai` org lists 12 repos (playbook, RabakBench, KnowOrNot, meta-evaluator, guardopt and others); `govtech-responsibleai/lionguard` and `/lionguard-demo` return "Repository not found" (git ls-remote). Playbook `staging` is still `45908b48c0a8b6d3855a154c0e41a12958a99205`; `main` is `97338569`. The inference code lives inside the HF repos (`inference.py`, `lionguard2.py`).
- **Official domains used:** huggingface.co/govtech, arxiv.org (GovTech-authored papers), blog.ai.gov.sg, govtech-responsibleai.github.io/playbook and its repo via raw.githubusercontent.com (pin 45908b48), huggingface.co/google (only to record the Lite embedder's gating; Google's page, not GovTech's). `www.aiguardian.gov.sg` returned 403 to fetch_text.py and `aiguardian.gov.sg` did not resolve, so Sentinel-service facts were not re-checked here (they stay in the Sentinel drafts).
- **Ownership or redirect findings:** none.
- **Playbook match:** the deployed page text matches `website/docs/tools/lionguard.md` at 45908b48 (checked: "can be fully retrained within two minutes", "we recommend **LionGuard 2.1**", the `embeddinggemma-300m` row).

## 2. Function list (proposed)
| ID | Header | Function | Direction (R002) | Evidence |
|---|---|---|---|---|
| LN1 | `LionGuard: Localised harmful-content classification` | Scores one text string for overall harm plus six Singapore-contextualised harm categories (11 scores). Three variants differ only in the embedding model. | One undifferentiated check: the model takes an embedding of a string, no direction flag. Single column per the R002 library definition (as Sentinel AA, Presidio Analyzer). R3 and R6 must say it applies to prompts and responses. | E02-E12, E15-E25 |

No second function is proposed: the models expose only this classifier. Off-topic, system-prompt-leakage and refusal models belong to Sentinel/playbook (sheet 3e), not LionGuard. If CP1 prefers one column per variant: LN1 `... (LionGuard 2, OpenAI embeddings)`, LN2 `... (LionGuard 2.1, Gemini embeddings)`, LN3 `... (LionGuard 2 Lite, local EmbeddingGemma)` (see Q01). Recommended: one column, variants as inventory rows and R4/R6/R7 bullets.

Prefix proposal: `LionGuard:` (the owner writes "LionGuard"; GovTech is not part of the brand; Sentinel keeps `GovTech Sentinel:`). See Q02.

## 3. Proposed inventory blocks (next sheet letter; slug lionguard, IDs LN)
| Block | Columns | Rows (approx) |
|---|---|---|
| (a) Variant table | Variant / Status / Embedding model and dimension / Serving needs / Classifier size / HF repo and revision / Licence / Covered by Table 3 column | 4 (LionGuard 1 legacy, 2, 2.1, 2 Lite) |
| (b) Output keys and taxonomy | Output key / Category / Level / Description / LionGuard 1 key (crosswalk to sheet 3e (c)) / Source | 11 (+ LionGuard 1 note) |
| (c) Dependencies and access | Component / Role / Who hosts / Access terms / Needed by variant / Source. Rows: OpenAI embeddings API, Gemini API, google/embeddinggemma-300m (gated, Gemma licence), BAAI/bge-large-en-v1.5 (v1), transformers and torch pins, sentence-transformers | 6-7 |
| (d) Artefacts and references | Artefact / Type / Owner / Revision or date / Licence or access / Covered by. Rows: 4 model repos, lionguard-2-synthetic-instruct, RabakBench (open) and RabakBench-full (manual gate), demo Space, playbook page, 2 papers, 3 blogs | 10-12 |
| (e) Cross-reference to Sentinel | Item / Sentinel column or sheet 3e block / Note (hosted ids lionguard-2-*, token limits, default-version question stay under Sentinel) | 3-4 |

Covered-by values: variants 2, 2.1, Lite -> the LN1 header; LionGuard 1 -> `— (legacy, not in Table 3)`; datasets, Space, papers, blogs -> `— (inventory only, not in Table 3)` (R011).

## 4. Sources table
All HF files were read raw at the revision (`/resolve/<sha8>/`) on 2026-10-09; copies are in `benchtest/scratchpad/explorer/lionguard/`.

| ID | URL | Verbatim quote | Label | R rows |
|---|---|---|---|---|
| E01 | https://huggingface.co/api/models/govtech/lionguard-2 (also -2.1, -2-lite, -v1) | sha `be4e38c988d3...`; tags `en, ms, ta, zh`, `text-classification`, `custom_code`; `gated: false`; files `model.safetensors`, `inference.py`, `lionguard2.py`, `requirements.txt`, `LICENSE`; safetensors total 848,942 params (2, 2.1) and 259,118 (Lite); model.safetensors 3,398,496 bytes (2, 2.1), 1,039,200 bytes (Lite) | [Documented: repo govtech/lionguard-2@be4e38c9] (parallel for each repo) | R4, R6, R7 |
| E02 | https://huggingface.co/govtech/lionguard-2/blob/be4e38c9/README.md | "It leverages OpenAI's `text-embedding-3-large` with a multi-head classifier to return fine-grained scores for the following categories" | [Documented: repo govtech/lionguard-2@be4e38c9] | R1, R2, R4 |
| E03 | same, Usage section | "Get OpenAI embeddings (users to input their own OpenAI API key)" | [Documented: repo govtech/lionguard-2@be4e38c9] | R4, R7 |
| E04 | https://huggingface.co/govtech/lionguard-2/blob/be4e38c9/lionguard2.py | predict: "If L2 category exists, and P(L2) > P(L1), Set both P(L1) and P(L2) to their average to maintain ordinal consistency"; returns "A dictionary of probabilities." | [Documented: repo govtech/lionguard-2@be4e38c9] | R4, R5 |
| E05 | same file, class docstring versus code | docstring: "encoded with OpenAI's `text-embedding-3-small` model"; README, inference.py and config use `text-embedding-3-large`, 3072 dims | [Documented: repo govtech/lionguard-2@be4e38c9] (internal conflict, section 6) | R4, R8 |
| E06 | .../lionguard-2/blob/be4e38c9/inference.py | `response = client.embeddings.create(input=texts, model="text-embedding-3-large")`; `model = AutoModel.from_pretrained("govtech/lionguard-2", trust_remote_code=True)` | [Documented: repo govtech/lionguard-2@be4e38c9] | R6, R7 |
| E07 | .../lionguard-2/blob/be4e38c9/config.json and requirements.txt | `"input_dim": 3072`; `numpy==2.3.1 openai==1.93.0 transformers==4.50.3 torch==2.3.1` | [Documented: repo govtech/lionguard-2@be4e38c9] | R4, R6, R7 |
| E08 | .../lionguard-2.1/blob/1c3a9ea7/README.md | "It leverages Gemini's `gemini-embedding-001` with a multi-head classifier"; "users to input their own Gemini API key" | [Documented: repo govtech/lionguard-2.1@1c3a9ea7] | R4, R7 |
| E09 | .../lionguard-2.1/blob/1c3a9ea7/requirements.txt | `numpy==2.3.1 transformers==4.50.3 torch==2.3.1 google-genai==1.50.1` | [Documented: repo govtech/lionguard-2.1@1c3a9ea7] | R7 |
| E10 | .../lionguard-2-lite/blob/d56c17a0/README.md | "This `lite` version leverages Google's `embeddinggemma-300m` (768-dimensional embeddings)"; "LionGuard 2 Lite runs fully locally, with no external API calls." | [Documented: repo govtech/lionguard-2-lite@d56c17a0] | R4, R7 |
| E11 | .../lionguard-2-lite/blob/d56c17a0/inference.py, README, requirements.txt | `return [f"task: classification | query: {c}" for c in texts]`; "NOTE: use encode() instead of encode_documents()"; `sentence-transformers==5.1.2` | [Documented: repo govtech/lionguard-2-lite@d56c17a0] | R6, R7 |
| E12 | .../lionguard-2-lite/blob/d56c17a0/config.json | `"input_dim": 768`, `"model_type": "lionguard2lite"` | [Documented: repo govtech/lionguard-2-lite@d56c17a0] | R4 |
| E13 | https://huggingface.co/google/embeddinggemma-300m (API `gated: "manual"`) | "This repository is publicly accessible, but you have to accept the conditions to access its files and content." Licence: gemma | [Documented] (Google page, not GovTech; fetched 2026-10-09) | R7, R8 |
| E14 | .../lionguard-2/blob/be4e38c9/LICENSE (md5 01aeb061... identical in 2.1 and Lite) | "the contents of this repository are provided under the MIT License SUBJECT FURTHER TO THE FOLLOWING: (1) The MIT License and the terms herein ... shall be governed by the laws of Singapore." (SIAC arbitration follows) | [Documented: repo govtech/lionguard-2@be4e38c9] | R7, R8 |
| E15 | https://govtech-responsibleai.github.io/playbook/tools/lionguard/ = website/docs/tools/lionguard.md @45908b48 | "Support for English, Singlish, Chinese, Malay, and partial Tamil."; "If a Level 2 instance is detected, Level 1 is also flagged by design."; "For best performance, we recommend LionGuard 2.1. For local deployment, we recommend LionGuard 2 Lite."; "All three versions are open-sourced for self-hosting via Hugging Face and accessible through the Sentinel API." | [Documented: repo govtech-responsibleai/playbook@45908b48] | R2, R4, R7 |
| E16 | https://arxiv.org/abs/2507.15339 (html v2), abstract and section 4 | "Built on pre-trained OpenAI embeddings and a multi-head ordinal classifier, LionGuard 2 outperforms several commercial and open-source systems across 17 benchmarks"; "The resulting classifier contains 0.85M parameters and occupies only 3.2 MB on disk." | [Documented] | R4, R5 |
| E17 | same, section 3 | "Running synchronously on a single CPU, the embedding call handles ≈250 tokens/s, while the classifier head itself processes ≈1.5×10^4 tokens/s, giving an end-to-end throughput of ≈300 tokens/s." | [Documented] | R6, R7 |
| E18 | same, section 5.1 | "we report binary F1 at a 0.5 threshold. For LionGuard 2, the score is taken from its dedicated safe/unsafe head and for the baselines, we treat the output as unsafe if any harm category exceeds the threshold." | [Documented] | R5 |
| E19 | same, Table 1 (LionGuard 2 row, text-embedding-3-large) | Test 77.0 / RabakBench 88.1 / SS 87.8 / ZH 78.4 / MS 66.6 (header order in the fetched HTML: Embeddings, Test, RabakBench, SS, ZH, MS, TA; row shows five values, Tamil cell is separated in the extract; see Sentinel changes for the Table 1 and Table 3 label question) | [Documented] | R5, R8 |
| E20 | same, section 5 and Limitations | "LionGuard 2 obtains the highest scores on Singlish, Chinese, and Malay, with margins of 8-25% over the next-best model, and is comparable to much larger LLM-based systems on the four English datasets."; "its Tamil performance remains moderate" | [Documented] | R2, R5 |
| E21 | same, section 7.1 | "LionGuard 2 inherits its representations from OpenAI's text-embedding-3-large. Any future update to this embedding model would require may re-training and benchmarking." | [Documented] | R4, R8 |
| E22 | same, ethics statement | "Our model weights are published on Hugging Face exclusively for research and public interest purposes only, with clear usage guidelines that prohibit deployment for harmful applications." | [Documented] (see conflict 2) | R7, R8 |
| E23 | https://blog.ai.gov.sg/introducing-lionguard-2-multilingual-llm-guardrail-for-singapore/ (29 Jul 2025) | "LionGuard 2 is open-sourced, including model weights and part of the training data."; "Performance remains robust for Chinese (88%) and Malay (78%), though slightly behind popular solutions like LlamaGuard 4 for Tamil."; section "LionGuard 2 as an input and output guardrail" | [Documented] | R3, R4, R5 |
| E24 | https://blog.ai.gov.sg/decision-models-for-guardrails-exploring-jev-and-kev-for-moderation/ | "LionGuard requires both embedding generation, which can be run locally or through an API depending on the variant, and classifier inference on the selected hardware."; "using the same 0.5 threshold"; table row Original test: LionGuard 2.1 0.7318 | [Documented] (only published 2.1 number found; private split) | R5, R6 |
| E25 | https://blog.ai.gov.sg/guardrails-in-the-wild-closing-the-retraining-loop-for-lionguard-2/ | "Architecturally, LionGuard 2 uses a shared representation feeding into 11 classification heads."; "users have manually reported more than 200 false positives and false negatives" | [Documented] | R4, R8 |
| E26 | https://huggingface.co/govtech/lionguard-v1 README and config.json @92cc0491 | "It uses pre-trained BAAI English embeddings and performs classification with a trained Ridge Classification model."; config `"model": "BAAI/bge-large-en-v1.5"`, `"max_length": 512`, binary thresholds high_recall 0.2, balanced 0.5, high_precision 0.8 | [Documented: repo govtech/lionguard-v1@92cc0491] | inventory (a) |
| E27 | https://arxiv.org/abs/2407.10995 (html) | "LionGuard scored lower than Moderation API on precision (0.63 vs 0.74) but significantly higher on recall (0.81 vs 0.56) when using 0.5 as the prediction threshold." | [Documented] (LionGuard 1) | inventory (a) |
| E28 | https://huggingface.co/api/datasets?author=govtech | `govtech/lionguard-2-synthetic-instruct` (gated false), `govtech/RabakBench` (false), `govtech/RabakBench-full` (manual) | [Documented] | inventory (d) |
| E29 | https://huggingface.co/api/spaces/govtech/lionguard-demo | sha `4ade46d19acee9c9088c711533a7c47fe24a8e3b`, sdk docker | [Documented: repo govtech/lionguard-demo@4ade46d1] | inventory (d) |

LN1 coverage per R-row: R1 E02, E15; R2 E02, E15, E20; R3 E06, E10, E11, E23 (string in, no direction flag; blog shows input and output use); R4 E02, E04, E07, E08, E10, E12, E16, E21, E25; R5 E04, E16, E18, E19, E20, E23, E24; R6 E06, E07, E11, E17, E24; R7 E03, E06, E08-E14; R8 sections 5-6; R9 these sources.

Facts re-checked from code and config at the pins (`[Documented: repo govtech/lionguard-2@be4e38c9]`, same for 2.1 and Lite at their pins): output keys are `binary, hateful_l1, hateful_l2, insults, sexual_l1, sexual_l2, physical_violence, self_harm_l1, self_harm_l2, all_other_misconduct_l1, all_other_misconduct_l2` (11); `predict` takes an array of embeddings (N x input_dim) and returns a dict of lists of floats with no threshold and no text handling; shared layers 3072 to 256 to 128 with dropout 0.2, seven heads each 128 to 32 to 2 with sigmoid; 2.1 has the same head (3072 in), Lite 768 in; all three need `trust_remote_code=True`.

## 5. Gaps (checked, not stated)
1. **Thresholds for 2, 2.1, Lite:** no operating threshold or calibration guidance on the HF cards, playbook, paper (only the 0.5 evaluation point, E18) or blogs. `[Not disclosed]`.
2. **Evaluation of 2.1 and Lite:** only one 2.1 number (0.7318, private split, E24). Nothing for Lite in the cards, playbook, paper or three blogs.
3. **Maximum input length of the self-hosted models:** the classifier takes a fixed vector, so the limit is the embedder's; the HF cards state no limit or truncation behaviour. Sentinel's per-version token limits (in the Sentinel draft) were not re-checked (aiguardian 403 / unreachable).
4. **Latency and hardware for 2.1 and Lite:** only the LionGuard 2 CPU figure (E17), which includes the OpenAI call. Lite memory and GPU needs not stated.
5. **Jailbreak and prompt-injection coverage:** not stated in cards, playbook, papers or blogs; the taxonomy is content harms only.
6. **Training and inference code on GitHub:** no LionGuard repo in `govtech-responsibleai` (12 repos listed; ls-remote not found); no training code; the dataset `lionguard-2-synthetic-instruct` is only "part of the training data".
7. **Third-party embedder terms** (OpenAI API, Gemini API, Gemma licence) not read; out of vendor scope, may be cited in inventory (c) per R019 once read.
8. **Retrained LionGuard 2 (blog 21 Aug 2026):** HF revisions have not changed since 2025-11-18, so no retrained model is public on the pinned repos. Whether it will be released: `[Not disclosed]` (blog checked).
9. **Per-language numbers for 2.1 and Lite:** HF language tags are the same four, but no per-language figures.

## 6. Conflicts
1. **Embedder in `lionguard2.py`:** docstring says `text-embedding-3-small`; README, inference.py and config say `text-embedding-3-large` at 3072 dims (E05). Code and card agree with the paper; the docstring is stale.
2. **Licence wording:** repo LICENSE is MIT plus Singapore law and SIAC (E14); the paper says the weights are published "exclusively for research and public interest purposes only" (E22). Keep as two bullets; licensing item (Q04).
3. **Paper table column labels:** Table 1 reads SS, ZH, MS, TA; Table 3 reportedly reads SS, MS, ZH, TA with identical LionGuard 2 values (carried from the Sentinel work, not re-verified in Table 3 here). The blog's Chinese 88 and Malay 78 fit Table 1's order (87.8 and 78.4).
4. **Benchmark count:** blog 29 Jul 2025 says 16 benchmarks; abstract (v2) and playbook say 17 (E16, E15, E23). Keep both.

## 7. URLs visited (HTTP status)
- 200: huggingface.co/api/models/govtech/{lionguard-v1, lionguard-2, lionguard-2.1, lionguard-2-lite} (also with `?blobs=true`); /api/models?author=govtech; /api/datasets?author=govtech; /api/spaces?author=govtech; /api/spaces/govtech/lionguard-demo; huggingface.co/govtech/{lionguard-2, lionguard-2.1, lionguard-2-lite, lionguard-v1}/resolve/<sha8>/{README.md, inference.py, lionguard2.py, lionguard2lite.py, config.json, requirements.txt, LICENSE}; huggingface.co/api/models/google/embeddinggemma-300m; huggingface.co/google/embeddinggemma-300m; govtech-responsibleai.github.io/playbook/tools/lionguard/; raw.githubusercontent.com/govtech-responsibleai/playbook/45908b48.../website/docs/tools/lionguard.md; arxiv.org/abs/2507.15339, /abs/2407.10995, /html/2507.15339, /html/2407.10995; the three blog.ai.gov.sg posts (E23-E25); api.github.com/orgs/govtech-responsibleai/repos and git/trees/45908b48 (anonymous, read-only listing).
- 404: raw.githubusercontent.com playbook guessed paths docs/tools/lionguard.md and three more (real path is website/docs/tools/lionguard.md).
- Not found: git ls-remote govtech-responsibleai/lionguard and /lionguard-demo.
- 403: www.aiguardian.gov.sg/docs/sentinel/sentinel-guardrails (fetch_text.py); aiguardian.gov.sg did not resolve (DNS).
- Not done: a shallow clone of the playbook was denied by the permission system (R020 raw route used instead); no weights downloaded (safetensors metadata from the HF API only); no hosted API called; no *.googleapis.com.
- Tools: HF REST and raw URLs by curl and fetch_text.py (verbatim); GitHub MCP, WebSearch, WebFetch and Context7 not needed.

## 8. QUESTIONS
See `20261009_lionguard_q01.md` to `_q04.md`: Q01 one column or one per variant (CP1); Q02 prefix `LionGuard:` or `GovTech LionGuard:`; Q03 what counts as self-hosted given embedder dependencies (OpenAI and Gemini APIs, gated EmbeddingGemma); Q04 licence wording conflict routed to the resolver.
