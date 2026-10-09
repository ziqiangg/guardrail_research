# GovTech Sentinel research brief (shared by all drafting agents)

## Scope (user-decided)
- **GovTech Sentinel** is Singapore GovTech's hosted "Guardrails as a Service" API, together with the GovTech models behind it.
- Table 3 gets **7 columns**. Model variants and version differences go in Detail bullets.
- **LionGuard:** LionGuard 2, 2.1 and 2 Lite are covered in column 1. LionGuard 1 (`govtech/lionguard-v1`) is legacy and appears only in the sheet 3e inventory and the category crosswalk.
- **Planned guardrails:** `hallucination` and `meta-llama/prompt-guard-jailbreak` (Prompt-Guard-86M) are planned, not available. Mention them only in R8 and in the 3e catalogue.
- **Out of scope:**
  - Litmus, GovTech's AI testing product. You may mention in R4 or R7 that GovTech recommends pairing Sentinel with Litmus.
  - Meta Prompt Guard internals.
  - AWS Bedrock Guardrails internals beyond what the Sentinel docs and AWS's official Bedrock Guardrails docs state about the wrapped checks.
- **Honesty rule.** Sentinel is a closed-beta government asset, so much is not public. Say `[Not disclosed]` and name the sources you checked. Never fill a gap by guessing.

## The 7 Table 3 columns (exact headers)
1. `GovTech Sentinel: Localised harmful-content classification (LionGuard 2)`
2. `GovTech Sentinel: Prompt-attack detection`
3. `GovTech Sentinel: Off-topic prompt detection against the system prompt`
4. `GovTech Sentinel: System-prompt leakage detection`
5. `GovTech Sentinel: Refusal detection`
6. `GovTech Sentinel: PII detection and masking (AWS Bedrock)`
7. `GovTech Sentinel: Generic content moderation via AWS Bedrock Guardrails`

## Official sources only
- **Sentinel docs (aiguardian.gov.sg):**
  - https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Overview
  - https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails
  - https://www.aiguardian.gov.sg/docs/sentinel/sentinel-getting-started
  - https://www.aiguardian.gov.sg/docs/wiki/Sentinel-APIs-%E2%80%90-User-Guide
  - https://www.aiguardian.gov.sg/docs/sentinel/sentinel-demo
  - Known dead link: /docs/wiki/Sentinel-Onboarding-Guide returns 403.
- **GovTech Responsible AI playbook:**
  - https://govtech-responsibleai.github.io/playbook/tools/sentinel/
  - …/tools/lionguard/
  - …/tools/off-topic-guardrail/
  - …/improving-ai-systems/guardrails/ (guardrail-architecture, production-integration, threshold tuning)
  - GitHub source of the playbook: govtech-responsibleai/playbook. Pin it to the commit you read.
- **GovTech developer portal:** https://www.developer.tech.gov.sg/products/categories/cybersecurity/sentinel (also /overview, /features-roadmap, /resources, /getting-started).
- **GovTech AI blog:** blog.ai.gov.sg, for example the LionGuard 2 post at https://blog.ai.gov.sg/introducing-lionguard-2-multilingual-llm-guardrail-for-singapore/.
- **Hugging Face, org `govtech`:**
  - Models: `lionguard-v1`, `lionguard-2`, `lionguard-2.1`, `lionguard-2-lite`, `jina-embeddings-v2-small-en-off-topic`, `stsb-roberta-base-off-topic`.
  - Spaces: `lionguard-demo`, `system-prompt-leakage`, `off-topic-demo`.
  - Datasets: `lionguard-2-synthetic-instruct` and RabakBench.
  - Pin each repo to the revision sha you read. `hub_repo_details` or the HF API gives the sha.
- **GovTech-authored arXiv papers:** read the /html/ version for verbatim tables.
  - LionGuard 1: 2407.10995
  - LionGuard 2: 2507.15339
  - Off-topic guardrail: 2411.12946
  - RabakBench: check its arXiv id if you cite it.
- **AWS official docs:** only for column 6 and column 7 facts about what each wrapped Bedrock check means (docs.aws.amazon.com/bedrock/…guardrails…). Label these [Documented] and state in plain text that they are AWS docs, not Sentinel docs.
- **Tools:**
  - Load via ToolSearch: "select:WebFetch,WebSearch,mcp__github__get_file_contents,mcp__github__search_code,mcp__github__list_commits".
  - The HF MCP tools: ToolSearch "+hf" or "select:mcp__9b0f51f6-b49a-4ee4-bc86-568dfa66da25__hf_fs,mcp__9b0f51f6-b49a-4ee4-bc86-568dfa66da25__hub_repo_details". These read model cards, configs and code, and the HF repos are not gated.
  - curl via Bash works for aiguardian.gov.sg, the playbook and arxiv.org/html. raw.githubusercontent.com may reset the connection, so use github.com blob pages instead.
  - WebFetch summarises. For any number or quote you rely on, ask for VERBATIM text, or read the raw HTML with curl.
  - Context7 has no Sentinel or LionGuard entry. That is already known; don't retry it.

## Exploration findings to RE-VERIFY (do not copy blindly)
- **Service:**
  - A multi-tenant SaaS API, "Guardrails as a Service".
  - Endpoints: `POST https://sentinel.aiguardian.gov.sg/api/v1/validate`, and staging at `https://sentinel.stg.aiguardian.gov.sg/api/v1/validate`.
  - Auth: header `x-api-key`.
  - Request: `text`, plus `guardrails` (a dict of guardrail id → params). Optional shared top-level params such as `messages` can be overridden per guardrail. A suite key (`lionguard-2`, `aws`) expands to all its members. There is no input/output flag; the caller chooses which text to send.
  - Response: `request_id`, `status` (completed or failed), `results` keyed by guardrail with `{score, time_taken, …}`, `errors` (per guardrail, or "_" for global errors), and a top-level `time_taken`. Partial results are possible.
- **Scores:**
  - Every guardrail returns a `score` from 0 to 1.
  - No threshold is applied server-side. The guidance is "typically a score above 0.95 indicates high likelihood".
  - The playground defaults are Failure Threshold 0.95 and Warning Threshold 0.80.
- **Access:**
  - Closed beta, "available only to Singapore Government public officers".
  - "Not suitable for integration with production systems"; a production-grade service is to come separately.
  - Singapore IP addresses only. Sign-up is through a form.gov.sg interest form, which issues an API key.
  - Rate limits, SLA, pricing, data retention and hosting region: not documented.
- **Missing artefacts:**
  - No SDK, no Sentinel GitHub repo, and no changelog or versioning beyond `/api/v1`.
  - Benchmarking report: "planned for a future release".
  - The Dashboard is mentioned but not documented.
- **Guardrails:**
  - **LionGuard 2 suite** (Input/Output): `lionguard-2-binary`, `-hateful_l1`, `-hateful_l2`, `-insults`, `-sexual_l1`, `-sexual_l2`, `-physical_violence`, `-self_harm_l1`, `-self_harm_l2`, `-all_other_misconduct_l1`, `-all_other_misconduct_l2`.
    - Variants: `lionguard-2` (OpenAI text-embedding-3-large, 8192-token limit), `lionguard-2-1` (gemini-embedding-001, 2048 tokens) and `lionguard-2-lite` (embeddinggemma-300m, 2048 tokens, "low-latency").
    - "If a Level 2 instance is detected, Level 1 is also flagged by design."
  - **`prompt-attack`:**
    - Detects prompt attacks that "manipulate the language model, bypass system constraints, or inject malicious instructions".
    - Input/Output in the detail table but Input-only in the summary table (a conflict).
    - Returns `score` plus `confidence`.
    - Model not disclosed, and absent from the playbook's Sentinel page.
  - **`off-topic`:**
    - Input; needs `messages` including a system message. The playbook calls the parameter `system_prompt` instead.
    - Detects "requests that are irrelevant with respective to the system prompt".
  - **`system-prompt-leakage`:** Output; needs a system message. Detects whether the output "directly or indirectly leaks the system prompt".
  - **`refusal`:**
    - Output; needs `user_prompt`. Returns `score`, `classification` (e.g. "Reject") and `reasoning`.
    - "Useful for analytics."
    - Model not disclosed.
  - **`aws/*`:**
    - Input only: `aws/hate`, `aws/insults`, `aws/misconduct`, `aws/sexual`, `aws/violence` and `aws/prompt_attack`.
    - Input/Output: `aws/pii`. Optional `entity_types`, default ["SG_NRIC","EMAIL"]. Returns `masked_text` and `pii_entities[{match,type}]`.
    - "aws guardrails have a character limit of 25,000".
  - **Planned:** `hallucination` (Output, param `context`) and `meta-llama/prompt-guard-jailbreak` (Input, Prompt-Guard-86M).
  - **"Relevance"** appears in the types table, but no ID implements it.
- **Playbook vs aiguardian conflicts:**
  - The playbook uses the `govtech/` prefix and the suite key `lionguard2`; aiguardian uses unprefixed ids and `lionguard-2`.
  - The playbook uses param `system_prompt`; aiguardian uses `messages`.
  - The playbook shows refusal with no params; aiguardian requires `user_prompt`.
- **LionGuard 2 model:**
  - Ordinal MLP head: shared 256→128, then 7 heads, about 0.85M params.
  - Embedder: OpenAI text-embedding-3-large, 3072-dim, so the user's own OpenAI key is needed. The `lionguard2.py` docstring wrongly says 3-small.
  - Output: per-key probabilities, with no thresholds shipped. The paper reports F1 at 0.5. The HF demo uses binary <0.4 pass, 0.4–0.7 warn, ≥0.7 fail.
  - Languages: English, Singlish, Chinese, Malay, partial Tamil. HF tags: en, ms, ta, zh.
- **LionGuard 2 paper 2507.15339, binary F1:**
  - Own test set: 77.0.
  - RabakBench, SGHateCheck and SGToxicGuard per language. Table 1 and Table 3 order the ZH and MS columns differently, so verify against the html.
  - English benchmarks: BeaverTails 73.7, SORRY-Bench 73.7, OpenAI Mod 70.5, SimpleSafetyTests 100.0.
  - Comparators: OpenAI Moderation on the test set 54.7; LlamaGuard 4 12B on the test set 26.5.
  - About 300 tokens/s on 1 CPU.
  - Limitations: closed-source embedder dependency, about 4% binary/category disagreement, weaker on Tamil.
  - Deployed on AI Guardian, where it "replaces its predecessor".
- **LionGuard 2.1 and Lite:** no paper and no evaluation. The playbook recommends 2.1 "for best performance, especially multilingual". Lite runs fully locally, with the input prefix "task: classification | query: {text}".
- **LionGuard 1:**
  - BAAI/bge-large-en-v1.5 plus ridge classifiers, shipped as ONNX.
  - Keys: binary, hateful, harassment, public_harm, self_harm, sexual, toxic, violent. No levels.
  - English/Singlish only.
  - Three threshold sets (high_recall / balanced / high_precision); the binary set is 0.2 / 0.5 / 0.8.
  - Paper 2407.10995, Table 4, PR-AUC; binary 0.819 vs OpenAI Moderation 0.675.
- **Off-topic models (paper 2411.12946):**
  - Two variants:
    - Bi-encoder (`govtech/jina-embeddings-v2-small-en-off-topic`): synthetic-set ROC-AUC 0.99 / F1 0.97, JailbreakBench F1 0.83, 2216 pairs/min on a T4.
    - Cross-encoder (`govtech/stsb-roberta-base-off-topic`): F1 0.99 on the synthetic set, JailbreakBench F1 0.72.
  - English only. Typical thresholds of 0.4–0.6 from internal studies. Internal deployment since September 2024.
  - Which variant Sentinel serves: not stated.
- **System-prompt leakage:** the only artefact is HF Space `govtech/system-prompt-leakage` `app.py`: logistic regression on concatenated Azure OpenAI text-embedding-3-small embeddings of the system prompt and the output, with a 0.5 cutoff in the demo. No paper and no evaluation. Whether Sentinel uses the same model is not stated.
- **Licence:** GovTech HF models use `license_name: govtech-singapore`, i.e. MIT plus a Singapore-law / SIAC arbitration clause, with GovTech marks excluded. Sentinel service terms: check the aiguardian pages and the developer portal.

## Labels
- **[Documented]:** an official GovTech or Singapore Government page (aiguardian.gov.sg, the playbook, developer.tech.gov.sg, blog.ai.gov.sg), a govtech HF model card, a GovTech-authored arXiv paper, or official AWS docs for the AWS wrapper semantics.
- **[Documented: repo <repo>@<sha>]:** official code or files, e.g. `govtech/lionguard-2@<sha>` on HF, a Space at its sha, or `govtech-responsibleai/playbook@<sha>`.
- **[Inferred]**, **[To be verified]**, **[Not disclosed]**.
- Never label something [Documented] unless you read it in that source. When two GovTech sources disagree, give both, each with its label, and list the conflict in Reviewer notes.

## Format: exactly like drafts/two_level_v2.md and drafts/lg_two_level.md
```
## Column SNn: GovTech Sentinel: <exact header>
### R1
Summary: **Bold lead.** 1–3 plain sentences. **[Label]**
Detail:
• one fact … **[Label]**
  – sub-item
### R2 … ### R9
```
- **Rows:**
  - R1 function.
  - R2 threat or condition.
  - R3 what it inspects and where it operates (input, output, or needs the system prompt or user prompt as context).
  - R4 mechanism. It must state the backing model or variant (or [Not disclosed]) and the access/serving route: Sentinel API, or self-hosting the HF model where one exists.
  - R5 output (score fields, extra fields such as masked_text or reasoning, and the threshold guidance).
  - R6 input and context required, including API parameters.
  - R7 minimum test setup: "**Minimum setup:** …" with **[Inferred]**. Note that it needs Sentinel beta access from a Singapore IP, or self-hosting of the HF model where one exists.
  - R8 open items: no labels; a comma or bullet list.
  - R9 sources: one URL per bullet. The Summary is a plain line with no bold lead and no label.
- **Summary:**
  - ≤45 words (R7 ≤60).
  - No code identifiers, underscores, backticks or `$`. Write "LionGuard 2", not `lionguard-2-binary`.
  - Each label must match the facts the summary draws on.
  - The R8 Summary is "**Key open questions.** …" with no label.
- **Detail:**
  - One fact per `• ` bullet, each ending with its bold label.
  - Guardrail ids, param names and model ids go inline in backticks.
- Add a `## Reviewer notes` section at the end: contradictions between sources, anything you were unsure of, and which facts came from summarised fetches.
