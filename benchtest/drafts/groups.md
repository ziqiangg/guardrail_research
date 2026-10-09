# Sheet 4 — Candidate Comparison Groups (draft)

Group IDs C1 to C24 are used only in this draft for cross-reference (they are not sheet-3 columns). References such as "AB R4" mean sheet 3, column AB, row 4 (Summary or Detail).

## A. Group table

| Candidate group | Guardrail functions included | Common test inputs | Ground truth | Outputs to capture | Common metrics | Minimum architecture | Material differences or limitations |
|---|---|---|---|---|---|---|---|
| C1 PII detection and masking in input text | E: Amazon Bedrock Guardrails: PII detection and masking (template example column); K: NeMo Guardrails: Input-level PII detection & masking; AF: GovTech Sentinel: PII detection and masking (AWS Bedrock) | Single user messages with synthetic, labelled PII of known types, ambiguous strings, custom-format identifiers and non-PII controls (E R6, K R7, AF R7). NeMo ships no PII dataset, so seed data must be built (3c Reuse). | Per text: PII type and character span of each item, expected action (block, mask or allow) and expected masked text. Entity lists differ, so score a harmonised common subset (name, email, phone, address, national ID, card number) and report other types separately. | Decision (blocked, masked, allowed); detected types and matches where exposed (K R5, AF R5); masked text; score where present (AF only, observed 0.0 and 1.0, AF R4); latency; error. | Detection rate (recall), false-positive rate and false-negative rate per entity type and per text; masking correctness (masked text equals expected, no residual PII); latency. No score-based curves: AF score looks like a flag (AF R4); E and K expose none (E R5, K R5). | Shared harness: loader, adapters, common result format, recorder, evaluator. E: Bedrock account with a sensitive-information policy. K: NeMo config with one backend, e.g. Presidio with spaCy (K R6, K R7). AF: Sentinel beta key from a Singapore IP (3e (d) access paths). NeMo eval run could drive K only, on LLMRails, at reply level (3c Tools: nemoguardrails eval run). | Entity lists differ: E uses AWS types plus regex (E R4); K depends on the backend (K R2, K R4); AF defaults to SG_NRIC and EMAIL, origin undisclosed (AF R2, AF R8). AF wraps AWS Bedrock Guardrails (AF R4), so it shares the backend with E and is not an independent product (3e (b) catalogue: aws/pii). Mask styles differ (E R5, K R4, AF R5); IORails masks only user and bot messages (3b rail types). AF returns raw matches (AF R3). Sentinel is closed beta (3e (d) access paths). E has summary-level research only. Output side is C2. |
| C2 PII detection and masking in output text | E: Amazon Bedrock Guardrails: PII detection and masking (template example column); L: NeMo Guardrails: Output-level PII detection & masking; AF: GovTech Sentinel: PII detection and masking (AWS Bedrock) | Model responses (scripted or generated) containing synthetic, labelled PII, plus clean controls and borderline strings (L R7, E R6, AF R7). No NeMo-provided dataset (3c Reuse). | Per response: PII type and span of each item, expected action (block, mask or allow) and expected final user-visible text. Score the harmonised common entity subset; report other types separately. | Decision (blocked, masked, allowed); detected types and matches where exposed (L R5, AF R5); final user-visible text; score where present (AF only, AF R4); latency; error. | Detection rate, false-positive rate and false-negative rate per entity type; masking correctness on the final text; latency. No score-based curves (AF R4, E R5, L R5). | Shared harness with scripted or real main LLM responses, adapters, common result format, recorder, evaluator. E: Bedrock account with a sensitive-information policy. L: NeMo output rail config with one backend and its service (L R7). AF: Sentinel beta key from a Singapore IP (3e (d) access paths). NeMo eval run could drive L only, on LLMRails (3c Tools: nemoguardrails eval run). | Same entity-list and mask-style differences as C1 (E R4, L R4, AF R2, AF R5). AF wraps AWS Bedrock Guardrails (AF R4), so it shares the backend with E and is not independent. L may release PII during streaming before the rewrite (L R8); rewrites under streaming need stream_first false (L R4); NeMo evaluation tooling has no streaming (3c Engine coverage), so test non-streaming first. Input side is C1. |
| C3 Harmful-content classification of input (user prompts) | G: NeMo Guardrails: Input-level content-safety moderation; V: Llama Guard: Input-level prompt content-safety classification; AA: GovTech Sentinel: Localised harmful-content classification (LionGuard 2); AG: GovTech Sentinel: Generic content moderation via AWS Bedrock Guardrails | Single-turn user prompts, harmful and benign, with benign near-misses (G R7, V R7, AA R7, AG R7). NeMo-provided seeds: Anthropic red-team-attempts and helpful-base prompts (3c Datasets), usable for the binary label only (no categories, 3c Reuse). OpenAI Moderation set and ToxicChat are not in the repo (3c Datasets). | Per prompt: binary harmful or benign label plus a category label mapped to a common taxonomy. Taxonomies differ: Nemotron S1 to S23 or S1 to S22 (G R2), Llama Guard S1 to S14 (V R2), LionGuard six categories with levels (AA R2), AWS five categories (AG R2). Compare per category only where a mapping exists. | Decision; category codes or per-category scores (G R5, V R5, AA R5, AG R5); first-token probability for V only if extracted (V R5); latency; error. | True-positive, false-positive and false-negative rates on the binary harmful label at each product's own decision point; precision and F1 as NeMo reports them (3c Published results). AUPRC and sweeps only for AA (and V if probabilities are extracted); AG shows only 0.0 or 1.0 (AG R5). | Shared harness: loader, adapters, common result format, recorder, evaluator. G: NeMo input rail, safety model endpoint, prompt (G R6). V: GPU-served Llama Guard with template and verdict parser (3d (c) integration paths). AA, AG: Sentinel beta key from a Singapore IP, or self-hosted LionGuard for AA (3e (d) access paths). NeMo eval run could drive G only, on LLMRails; eval rail moderation tests just the self-check prompt (3c Tools). | Taxonomies differ; AG has no self-harm category (AG R2). AA is tuned to Singapore languages (AA R2). G and V give verdicts without a score (G R5, V R5); AA gives scores with no server threshold (AA R5). G can call Llama Guard (G R4), so G and V may share a model. AG wraps AWS Bedrock Guardrails (3e (b) catalogue: aws/*), so it shares the backend with E and is not independent. V is not built for jailbreaks (V R2). NVIDIA's Llama Guard versus self-check figures are NeMo-reported with an old main LLM, not cross-product comparable (3c Published results). Sentinel is closed beta (3e (d) access paths). |
| C4 Harmful-content classification of output (model responses) | H: NeMo Guardrails: Output-level content-safety moderation; W: Llama Guard: Output-level response content-safety classification; AA: GovTech Sentinel: Localised harmful-content classification (LionGuard 2) | Model responses to benign and harmful prompts, scripted or generated, including safe refusals of unsafe prompts and benign near-misses (H R7, W R7, AA R7). H and W need the prompt as context; AA needs only the response (AA R3). NeMo moderation sample prompts can elicit responses (3c Datasets), but no labelled responses are provided. | Per response: binary unsafe or safe label judged on the response itself, plus a category label mapped to a common taxonomy (Nemotron codes H R2, Llama Guard S1 to S14 W R2, LionGuard AA R2). Compare per category only where a mapping exists. | Decision; category codes or per-category scores (H R5, W R5, AA R5); first-token probability for W only if extracted (W R5); latency; error. | True-positive, false-positive and false-negative rates on the binary unsafe label at each product's decision point. AUPRC and sweeps only for AA (and W if probabilities are extracted). Non-streaming runs only. | Shared harness with scripted responses or a stub main LLM, adapters, common result format, recorder, evaluator. H: NeMo output rail with a safety model endpoint (H R7). W: GPU-served Llama Guard with response template and verdict parser (3d (c) integration paths). AA: Sentinel beta key or self-hosted LionGuard (3e (d) access paths). NeMo eval rail moderation notes it cannot judge outputs accurately (3c Tools). | H with Nemotron prompts checks the user turn with the response (H R1), W judges the response (W R3), AA reads the response alone (AA R3), so a harmful prompt can change the result. Taxonomies differ (H R2, W R2, AA R2). W reports no threshold and LG3 and LG4 figures are not comparable (W R5). H blocks can follow streamed tokens (H R5). AG is excluded: Sentinel lists it input only (3e (b) catalogue: aws/*; AG R3). Sentinel is closed beta (3e (d) access paths). |
| C5 Input-level jailbreak and prompt-attack detection | F: NeMo Guardrails: Input-level jailbreak detection; AB: GovTech Sentinel: Prompt-attack detection; AG: GovTech Sentinel: Generic content moderation via AWS Bedrock Guardrails | Single-turn jailbreak, injection and benign prompts, including benign prompts that mention instructions or code and non-English text (F R6, AB R7, AG R7). Garak probe families dan, encoding, goodside, promptinject and gcg can seed attacks, but need benign controls added (3c Red-teaming, 3c Reuse). Heuristic-threshold datasets are not in the repo (3c Datasets). | Per prompt: binary attack or benign label under one agreed definition, optionally with an attack style. Definitions differ: F undefined (F R2), AB three intents (AB R2), AG jailbreak, injection and possibly leakage (AG R2). Garak labels come from its own detectors, some model-based (3c Tools: garak). | Decision; score where present (AB score and confidence AB R5; AG score AG R5; F none F R5); latency; error, including detector-unreachable cases (F R4). | True-positive, false-positive and false-negative rates at each product's decision point; latency. AUPRC and sweeps only for AB (AG shows 0.0 and 1.0, AG R5; F has no score). Garak reports protection rates per probe and does not measure false positives (3c Red-teaming). | Shared harness: loader, adapters, common result format, recorder, evaluator. F: NeMo input rail with a detector; heuristics need torch and transformers or a server_endpoint, the model flow a NemoGuard endpoint (F R7). AB, AG: Sentinel beta key (3e (d) access paths). Garak NeMoGuardrails generator could drive F only, on LLMRails or a server (3c Red-teaming, 3c Engine coverage). | F returns block or allow only and fails open if its detector is down (F R4, F R5); heuristics are English-only, run on LLMRails only (3b surface table) and misfire on code (F R2). AB model undisclosed, confidence undefined (AB R4, AB R5); its scope is disputed (3e (b) catalogue: prompt-attack). AG is the aws/prompt_attack id, input-only, sharing the Bedrock backend with E. A Prompt-Guard id is planned, not available (3e (b) catalogue). NVIDIA garak and heuristic results are NeMo-reported and not comparable (3c Published results). |
| C6 Input-level off-topic detection against a policy or system prompt | I: NeMo Guardrails: Input-level topic control; AC: GovTech Sentinel: Off-topic prompt detection against the system prompt | Pairs of (allowed-topic policy or system prompt, user message): on-topic, off-topic and borderline messages under several policies of different breadth (I R7, AC R7). English baseline (AC R6). NeMo example policies in the sample_abc eval config can seed one policy (3c Datasets). | Per pair: on-topic or off-topic label relative to the stated policy, written by the test author per policy. The same policy text must be rendered into each product's format. | Decision (blocked or on-topic flag, I R5); score for AC (AC R5); latency; error. | True-positive rate (off-topic caught), false-positive rate (on-topic blocked) and false-negative rate at each decision point; latency. AUPRC and sweeps only for AC; I returns a verdict (I R5). NeMo reports no topic-control accuracy (3c Published results). | Shared harness that injects the policy per case, adapters, common result format, recorder, evaluator. I: NeMo input rail, topic_control model entry, NemoGuard Topic Control endpoint, policy prompt (I R6, I R7). AC: Sentinel beta key, or self-hosted bi-encoder or cross-encoder (3e (d) access paths). NeMo eval run could drive I on LLMRails; eval rail topical tests dialog, not topic control (3c Tools). | I takes an explicit allowed-topics policy (I R4, I R6); AC infers relevance from the system prompt (AC R1). AC is English only (AC R6); I language coverage is not stated. Multi-turn use is unknown for I (I R8) and unclear for AC (AC R3). AC served variant undisclosed (AC R4); parameter name conflicts (AC R6); scope conflicts (3e (b) catalogue: off-topic). I has no published accuracy (3c Published results). Sentinel is closed beta. |
| C7 Dialog-level conversational flow control | J: NeMo Guardrails: Dialog-level conversational flow control | Multi-turn conversations and paraphrased user messages around a reference Colang configuration we author (J R6, J R7). NeMo seeds: chit-chat (76 intents, 226 test samples) and banking77 (77 intents, 231 test samples) with conversion scripts (3c Datasets). | Expected user intent, next step and bot reply per turn under the authored flows. | Matched intent, next step, bot message, latency, number of LLM calls, error (J R5, J R8). | Intent-matching accuracy, bot-intent and bot-message accuracy as NeMo reports them (3c Tools: nemoguardrails eval rail topical), false-refusal rate on on-path messages, latency, LLM calls. | Harness, authored Colang configuration, LLMRails engine (not IORails), main LLM, embedding model, recorder (J R7). NeMo eval rail topical can be reused as is for J (3c Tools); it runs on LLMRails only (3b rail types). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Evaluates NeMo intent matching over our own configuration, not a vendor detector (J R6). Output is a reply, not pass or fail (J R5). LLMRails only (J R4). Colang 1.0 versus 2.x unresolved (J R8). Published accuracies are NeMo-reported on older models (3c Published results). |
| C8 Retrieval-level chunk filtering | M: NeMo Guardrails: Retrieval-level chunk filtering | A small knowledge base with clean chunks and seeded bad chunks: PII, forbidden pattern, padding (M R7). NeMo provides no retrieval test data (3c Reuse). | Per chunk and per configured check: kept, rewritten, blanked or turn blocked. | Chunks passed to the prompt, block outcome, rewritten text, latency, error (M R5, M R7). | Detection rate and false-positive rate on seeded chunks per check type; chunk-removal correctness; latency. | Harness, knowledge base or custom retrieval step, NeMo config with rails.retrieval.flows, LLMRails engine, stub LLM, log of chunks sent to the prompt (M R7). NeMo eval run does not model retrieval (3c Tools). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Checks the joined chunk text and blanks all chunks, while docs say one chunk (M R4, M R8). LLMRails only (3b rail types). Reuses PII, regex, bloat and HF classifier backends on retrieved text (M R3). NeMo publishes no retrieval results (3c Published results). |
| C9 Regex pattern blocklist on input | N: NeMo Guardrails: Regex pattern blocklist (input/output) | User messages that match and do not match each configured pattern (N R7). No NeMo dataset (3c Reuse). | Per message and pattern list: expected block or allow, derived from the patterns we author, so ground truth is deterministic. | Block decision, matched patterns (detections), latency, error (N R5). | Exact agreement with expected outcome, false-positive and false-negative rates against the authored patterns; latency, including slow-pattern cases. | Harness, NeMo config with input patterns, stub LLM, recorder; both engines (3b surface table: regex check input). NeMo eval run could drive it on LLMRails at reply level (3c Tools). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Deterministic matching with no model: tests configuration and engine, not learned detection (N R4, N R2). No paraphrase coverage (N R2). Matching method undocumented (N R8). No exception path (N R5). No NeMo results published (3c Published results). Output side is C10; retrieval variant is C8 (N R3). |
| C10 Regex pattern blocklist on output | N: NeMo Guardrails: Regex pattern blocklist (input/output) | Bot responses (scripted by a stub LLM) that match and do not match each configured output pattern (N R7). No NeMo dataset (3c Reuse). | Per response and pattern list: expected block or allow, derived from the authored patterns. | Block decision, matched patterns (detections), latency, error (N R5). | Exact agreement with expected outcome, false-positive and false-negative rates against the authored patterns; latency. | Harness, NeMo config with output patterns, stub LLM returning scripted text, recorder; both engines (3b surface table: regex check output). NeMo eval run could drive it on LLMRails (3c Tools). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Same limits as C9: deterministic, no paraphrase coverage, undocumented matching method, no exception path (N R2, N R5, N R8); no NeMo results published (3c Published results). Input side is C9. |
| C11 Context-bloat detection on input | P: NeMo Guardrails: Context-bloat detection (input) | Normal text, text over the size cap, repeated characters, repeated phrases, low-entropy filler and legitimate long pastes such as logs or code (P R7, P R8). No NeMo dataset (3c Reuse). | Per input and configured thresholds: expected outcome (block, truncate or allow), authored from the thresholds, plus a legitimate or abusive label for long pastes. | Outcome (block, truncated message, allow), reported metrics, latency, error (P R5). | Detection rate on padded inputs and false-positive rate on legitimate long inputs; truncation correctness; latency. | Harness, NeMo input rail config with each action tried in turn, stub LLM, recorder; both engines (P R4, P R7). NeMo eval run could drive it on LLMRails (3c Tools). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Statistical checks with no model and thresholds we set (P R4). The warn action hides detections from the caller (P R5). Non-English behaviour unverified (P R8). No NeMo results published (3c Published results). |
| C12 Output-level injection detection | O: NeMo Guardrails: Output-level injection detection | Scripted bot outputs containing code, SQL, template and cross-site scripting payloads, plus benign code answers (O R7). Garak xss and malwaregen probe families may seed payloads (3c Red-teaming); NeMo has no injection dataset (3c Reuse). | Per output: payload class (code, SQL injection, template, XSS) or benign, with expected action (block or strip). | Outcome (block, stripped text, allow), matched rule names, latency, error (O R5). | Detection rate per payload class, false-positive rate on benign code answers, stripping correctness for omit; latency. | Harness, scripted outputs, NeMo output rail with injection config and yara-python, recorder; both engines (3b surface table: injection detection). NeMo eval run could drive it on LLMRails (3c Tools). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Fixed YARA rule set, defence-in-depth, not a standalone control (O R2, O R4). Docs and code disagree on the default action (O R6, O R8). Possible false positives on legitimate code (O R8). No NeMo results published beyond garak (3c Published results). |
| C13 Tool-call validation | Q: NeMo Guardrails: Tool-call validation | Declared tool definitions plus scripted model responses with valid calls, unknown tool names, bad arguments, arguments to a no-parameter tool and invalid schemas (Q R7). No NeMo dataset (3c Reuse). | Per call: structurally valid or invalid, with expected reason; deterministic from the declared schema. | Allow or block, refusal text or error payload, block reason, latency, error (Q R5). | Block accuracy (true-positive and false-positive rates against schema validity), reason correctness, latency. | Harness sending OpenAI-format requests with tools, scripted or real model emitting tool calls, NeMo IORails config with tool call validation, recorder; no tool execution (Q R6, Q R7). NeMo eval runners cannot be reused: no tool fields, IORails untested (3c Engine coverage). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Structural allowlist and JSON Schema check only; does not judge whether an allowed call is harmful (Q R2). Built-in validator is IORails only, OpenAI format only; LLMRails needs custom flows (3b surface table). Model-based tool safety exists on develop only (Q R4). No NeMo results published (3c Published results). |
| C14 Tool-result validation | R: NeMo Guardrails: Tool-result validation | Conversations with an assistant turn carrying tool calls and tool messages: valid, missing ID, duplicate ID, wrong name, non-string content (R R7). No NeMo dataset (3c Reuse). | Per conversation: structurally consistent or not, with expected reason; deterministic. | Allow or block, refusal text or error payload, latency, error (R R5). | Block accuracy (true-positive and false-positive rates against structural validity), latency. | Harness sending conversations with tool messages, NeMo IORails config with tool result validation, stub main LLM, recorder; no tool execution (R R6, R R7). NeMo eval runners cannot be reused: IORails untested, no tool fields (3c Engine coverage). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Structural linkage only: no response schema, no content-safety or injection check on result text (R R2, R R4). Plain input rails do not see tool results (R R3). IORails only for built-ins (3b surface table). Model-based result judge on develop only (R R4). No NeMo results published (3c Published results). |
| C15 Execution-level custom action rails | U: NeMo Guardrails: Execution-level custom action rails | Action calls with allowed and blocked arguments and trusted and untrusted results, triggered through flows we author (U R6, U R7). No NeMo dataset (3c Reuse). | Per case: expected allow, block or transform decision defined by our own test logic. | Action call log, rail decision (allow, block, transform), final reply, latency, error (U R5, U R7). | Agreement of the decision with the authored expectation; false-positive and false-negative rates of the authored checks; latency. | Harness, NeMo configuration with test actions and flows we write, scripted calls or a main LLM, LLMRails engine, recorder (U R7). NeMo eval run can observe execution rails only through the final reply (3c Tools: nemoguardrails eval run). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. No built-in detector, so only the wrapper mechanism and our test logic are evaluated (U R1, U R4). Output format not fixed (U R5). Documented rails.execution key has no backing field in v0.24.1 (U R4). LLMRails only (3b rail types). No NeMo results published (3c Published results). |
| C16 Grounded fact-checking of output | S: NeMo Guardrails: Grounded fact-checking (output) | Triples of question, retrieved evidence and reply, supported and unsupported (S R7). NeMo seeds: MS MARCO triples with LLM-made negatives and a 1-item sample (3c Datasets: MS MARCO; factchecking/sample.json); negatives depend on the generating LLM (3c Reuse). | Per reply: supported or unsupported by the supplied evidence. | Decision, 0 to 1 support score for self-check and AlignScore, latency, error (S R5). | True-positive, false-positive and false-negative rates at the decision point; positive, negative and overall accuracy and ms per fact as NeMo reports (3c Tools: nemoguardrails eval rail fact-checking); AUPRC from scores for self-check and AlignScore only. | Harness, small knowledge base or injected chunks, NeMo config on LLMRails with check_facts set by a custom Colang flow, judge LLM or AlignScore server, recorder (S R6, S R7). NeMo eval rail fact-checking bypasses the rail pipeline and tests the self-check prompt only (3c Tools). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Needs retrieved evidence (S R2). Fixed 0.5 threshold for self-check and AlignScore (S R5). LLMRails only (3b surface table). Vendor backends return different output shapes (S R5). NeMo published accuracies use retired models and 100 triples (3c Published results). Sentinel hallucination id is Planned, not available (3e (b) catalogue). |
| C17 Self-consistency hallucination detection of output | T: NeMo Guardrails: Self-consistency hallucination detection (output) | Prompts with stable answers and prompts the main LLM tends to invent answers for, run through a live main LLM so resampling is possible (T R7). NeMo seed: 15 false-premise questions, unlabelled, smoke test only (3c Datasets: hallucination/sample.txt; 3c Reuse). | Per prompt and reply: hallucinated or not, from reference answers or human review. Consistent but wrong answers cannot be caught (T R2). | Allow or block, is_hallucination flag, warning text, latency, number of LLM calls, error (T R5, T R8). | True-positive, false-positive and false-negative rates at the decision point; added latency and calls. No score, so no AUPRC. NeMo reports only the percentage flagged (3c Tools: nemoguardrails eval rail hallucination). | Harness, NeMo config on LLMRails with the hallucination flag set by a custom Colang flow, main LLM allowing temperature 1.0, recorder (T R6, T R7). NeMo eval rail hallucination exists but has no ground truth and bypasses the pipeline (3c Tools). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Results depend on random resampling. If every extra generation fails the reply is allowed (T R4, T R8). LLMRails only (3b surface table). Supported providers unclear (T R4). Adds at least two LLM calls (T R8). NeMo runner flags any "no" in the judge text (3c Tools). |
| C18 Multimodal content-safety classification of input (image and text prompts) | X: Llama Guard: Multimodal (image + text) content-safety classification | Image-plus-text user prompts, single and multi-image, benign and harmful, run as prompt checks (X R7). | Per prompt: safe or unsafe plus category S1 to S13 (X R2, X R7). | First-line verdict, category codes, latency, error (X R5). | True-positive, false-positive and false-negative rates, precision and F1 at the verdict; per-category recall; no score or threshold documented, so no AUPRC (X R5). | One GPU host serving Llama Guard 4 and Llama Guard 3-11B-Vision via transformers with a processor, harness, verdict parser, logger (X R4, X R7; 3d (a) variant table). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Only 3-11B-Vision (one image) and Llama Guard 4 (several) take images (3d (a) variant table; X R4). Not for image-only or text-only classification (X R3). Prompt checks are weaker than response checks (X R3). Language rules conflict (X R8). EU licence clause may apply (X R4, X R8). Response side is C19. |
| C19 Multimodal content-safety classification of output (image and text prompt with text response) | X: Llama Guard: Multimodal (image + text) content-safety classification | Image-plus-text prompts with a canned or generated text response, benign and harmful, run as response checks (X R7, X R6). | Per pair: response safe or unsafe plus category S1 to S13 (X R2, X R7). | First-line verdict, category codes, latency, error (X R5). | True-positive, false-positive and false-negative rates, precision and F1; per-category recall; no score or threshold documented (X R5). | One GPU host serving Llama Guard 4 and Llama Guard 3-11B-Vision with processor, response template, verdict parser, logger (X R4, X R7; 3d (a) variant table). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Same limits as C18. Response checks are stronger than prompt checks (X R3). LG4 does not say whether image content in a response is classified (X R6). 3-11B-Vision response F1 and LG4 figures come from different sets (X R5). Input side is C18. |
| C20 Code-interpreter abuse classification (S14) | Y: Llama Guard: Code-interpreter and tool-use abuse classification | Agent turns containing code or search-result text with the preceding user turn: S14 abuse cases, near-boundary benign code, benign code (Y R7). | Per item: S14 unsafe or safe label, with the expected S14 code. | Verdict, category codes (whether S14 appears), latency, error (Y R5). | S14 true-positive, false-positive and false-negative rates on the verdict; compare serialisation variants; no documented threshold (Y R4). | Harness, GPU serving of Llama Guard 3-8B and Llama Guard 4 (3-1B as negative control), response template with S14, verdict parser, logger (Y R7; 3d (a) variant table). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. S14 exists only in LG3-8B, its INT8 build and LG4 (3d (a) variant table; Y R1). Tool-call and tool-output serialisation is undefined by Meta (Y R3, Y R6). LG4 has no S14 metric and OGX omits S14 for LG4 (Y R4; 3d (c) integration paths). Llama Guard does not detect injection (Y R2). |
| C21 Custom-policy classification of input (prompts) | Z: Llama Guard: Custom-policy classification | User prompts labelled under a small custom taxonomy (for example three categories with positives, negatives and near-boundary items), run with names only, with descriptions, few-shot and excluded-category variants (Z R7). | Per prompt: category label under the author-defined taxonomy, plus expected flip when a default category is excluded. | Verdict, codes keyed to the supplied categories, latency, error (Z R5). | Per-category true-positive and false-positive rates; rate of verdict change under exclusion or replacement; no score or threshold documented. | Harness, taxonomy builder, GPU serving of Llama Guard 3-1B, 3-11B-Vision and 4 (templates take categories) and 3-8B via the cookbook builder, verdict parser (Z R4, Z R7; 3d (a) variant table). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. 3-8B template ignores categories (Z R4; 3d (a) variant table). No Meta page shows LG4 custom usage (Z R4, Z R8). No published quality results beyond the LG1 paper (Z R2). Custom key formats untested (Z R5). Response side is C22. |
| C22 Custom-policy classification of output (responses) | Z: Llama Guard: Custom-policy classification | Prompt-response pairs labelled under the custom taxonomy, with the same names-only, description, few-shot and exclusion variants (Z R7). | Per response: category label under the author-defined taxonomy, plus expected flip when a default category is excluded. | Verdict, codes keyed to the supplied categories, latency, error (Z R5). | Per-category true-positive and false-positive rates; rate of verdict change under exclusion or replacement; no score or threshold documented. | Harness, taxonomy builder, GPU serving of Llama Guard 3-1B, 3-11B-Vision and 4 and 3-8B via the cookbook builder, response template, verdict parser (Z R4, Z R7; 3d (a) variant table). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Same limits as C21 (Z R4, Z R8). Response classification needs both turns (Z R3). Compare only within Llama Guard (Z R2). Input side is C21. |
| C23 System-prompt leakage detection | AD: GovTech Sentinel: System-prompt leakage detection | Pairs of system prompt and model output: leaking outputs (verbatim, word-substituted, paraphrased, reordered, obfuscated, partial) and non-leaking outputs that share vocabulary (AD R7). | Per pair: leak or no leak. | Score from 0 to 1, latency, error (AD R5). | True-positive, false-positive and false-negative rates at a stated threshold; threshold sweep and AUPRC from the score; latency. | Harness, Sentinel beta key from a Singapore IP, script calling /validate with the system prompt in messages, labelled pairs (AD R6, AD R7; 3e (d) access paths). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Model undisclosed (AD R4); no published evaluation (AD R2). The 0.95 guidance would miss a documented 0.909 clear leak (AD R5). messages versus system_prompt conflict (AD R6). Only a demo Space exists, needing an Azure OpenAI key (3e (d) access paths). Closed beta. |
| C24 Refusal detection | AE: GovTech Sentinel: Refusal detection | Pairs of user prompt and model reply: hard refusal, soft refusal with alternative, refusal wrapped in help, safe completion of a risky request, full answer, benign decline (AE R7). | Per pair: human-labelled refusal class (refused, partial, answered). | Score, class label, reasoning text, latency, error (AE R5). | Agreement with human labels (accuracy, refusal precision and recall), over-refusal detection rate, repeat-run stability, latency. | Harness, Sentinel beta key from a Singapore IP, script calling /validate with user_prompt, human-labelled pairs (AE R6, AE R7; 3e (d) access paths). | Single-product: no comparator among NeMo / Llama Guard / Sentinel yet. Positioned as analytics, not a block control (AE R1). Model, rubric and label set undisclosed (AE R2, AE R4). user_prompt required or not is a docs conflict (AE R6; 3e (b) catalogue: refusal). No accuracy figures published (AE R8). |

## B. Rationale per group

Criteria from docx Section 4: (1) same type of test inputs, (2) same ground truth, (3) same or comparable metrics, (4) common minimum architecture. For single-product rows the criteria are assessed against the closest candidate comparator. Evidence from the inventories is cited as 3b (NeMo rail inventory), 3c (NeMo evaluation tooling), 3d (Llama Guard inventory) and 3e (Sentinel inventory), each with the section name.

### C1 PII detection and masking in input text (E, K, AF)

- (1) Inputs ✓ Yes. Text prompts carrying PII with controls: E R6, K R7, AF R7. No NeMo-provided PII dataset exists (3c Reuse: gaps), so no seed data is inherited.
- (2) Ground truth ✓ Yes, with harmonisation. PII type and location: E R6, K R5, AF R5; supported types differ: E R2, K R2, AF R2.
- (3) Metrics ✓ Yes. Detection, false-positive and masking correctness fit all three outcomes: E R5, K R5, AF R5. NVIDIA publishes no PII results (3c Published results).
- (4) Architecture ✓ Yes. Text-level harness plus one adapter per product; no RAG, tools or agent: E R7, K R7, AF R7. 3c Tools: eval run weakens reuse: it judges the final reply only and runs on the classic engine (3c Engine coverage).
- Note: E and AF are in both C1 and C2 because both inspect prompts and replies (E R3, AF R3; 3e (b) catalogue lists aws/pii as Input/Output); K is input-only and L output-only (K R3, L R3).
- Note: N (regex) is not included: no PII taxonomy or spans, block-only outcome (N R5), so ground truth would be our own patterns. M (retrieval PII flows) inspects chunks (M R1, M R3), so it is C8.
- Note: AF is included although its default entity list is narrower (AF R2); the common-subset rule handles this.

### C2 PII detection and masking in output text (E, L, AF)

- (1) Inputs ✓ Yes. Responses carrying PII with controls: L R7, E R6, AF R7.
- (2) Ground truth ✓ Yes, with harmonisation. Same type and span labels: L R5, E R5, AF R5.
- (3) Metrics ✓ Yes. Same metrics as C1 on the response text: L R5, E R5, AF R5.
- (4) Architecture ✓ Yes. Scripted-response harness plus one adapter each: L R7, E R7, AF R7. NeMo tooling cannot test streaming leaks (3c Engine coverage; 3c Reuse: gaps).
- Note: Separate from C1 by user decision; the inspected text, test data and streaming behaviour differ (L R4, L R8).
- Note: E R3 and AF R3 mark both sides, so they appear here and in C1.

### C3 Harmful-content classification of input (user prompts) (G, V, AA, AG)

- (1) Inputs ✓ Yes. Prompt-only harmful and benign text: G R7, V R7, AA R7, AG R7. NeMo datasets (3c Datasets) can seed it if labels are compatible.
- (2) Ground truth ✓ Partly. Binary harmful label is shared; categories need a mapping: G R2, V R2, AA R2, AG R2. Anthropic prompts carry a 0 to 4 rating, not categories (3c Reuse).
- (3) Metrics ✓ Yes at the binary decision point: G R5, V R5, AA R5, AG R5. Score metrics only for AA. NeMo reports accuracy, precision, recall, F1 (3c Published results).
- (4) Architecture ✓ Yes. Prompt-submission harness with one adapter each: G R7, V R7, AA R7, AG R7. NeMo runners reach only G (3c Tools), so the cross-product harness is still needed.
- Note: AG is in C3 for its five harm filters only; its prompt_attack id is in C5 (AG R1, AG R2). The ids detect different things and the AWS prompt attack filter is input-only (AG R3; 3e (b) catalogue: aws/* Input).
- Note: Z (custom policy) is excluded: ground truth is a tester-defined taxonomy (Z R2, Z R7); see C21 and C22.
- Note: X (multimodal) is excluded: it needs images (X R3), which not every member can consume; see C18.
- Note: Y (S14) is excluded: different threat, response-side (Y R2, Y R3); see C20.
- Note: AA and AG are comparable only at the binary level: AA R2 and AG R2 category sets overlap but are not equal.

### C4 Harmful-content classification of output (model responses) (H, W, AA)

- (1) Inputs ✓ Yes. Response text with optional prompt context: H R7, W R7, AA R7.
- (2) Ground truth ✓ Partly. Binary unsafe label is shared; categories need a mapping: H R2, W R2, AA R2.
- (3) Metrics ✓ Yes at the binary decision point: H R5, W R5, AA R5.
- (4) Architecture ✓ Yes. Scripted-response harness, one adapter each: H R7, W R7, AA R7. NeMo moderation runner is weak for outputs (3c Tools: nemoguardrails eval rail moderation).
- Note: Separate from C3 by user decision; test data (responses plus context) and judged unit differ (W R3).
- Note: AG is not here: Sentinel marks all six AWS ids input only (3e (b) catalogue; AG R3). AG R8 lists output use as a test question; add AG if confirmed.
- Note: AA appears in C3 and C4 because Sentinel lists LionGuard as Input/Output (3e (b) catalogue: lionguard-2-*; AA R3).
- Note: Y (S14) judges agent output but is a single-category code-abuse test (Y R3); see C20.

### C5 Input-level jailbreak and prompt-attack detection (F, AB, AG)

- (1) Inputs ✓ Yes. Jailbreak and benign prompts: F R6, AB R7, AG R7. Garak probes are NeMo-adjacent seeds but have no benign counterpart (3c Red-teaming).
- (2) Ground truth ✓ Yes, with caveat: binary attack label shared, definitions differ: F R2, AB R2, AG R2.
- (3) Metrics ✓ Yes at the decision point: F R5, AB R5, AG R5. Score metrics only for AB. Garak protection rates are not FPR (3c Red-teaming).
- (4) Architecture ✓ Yes. Prompt-submission harness, one adapter each: F R7, AB R7, AG R7. Garak and NeMo runners reach F only (3c Engine coverage).
- Note: AG appears in C3 (harm filters) and C5 (prompt_attack id): one column, one suite call (AG R1), split by id.
- Note: V and W are excluded: Llama Guard is not designed to detect jailbreak or injection (V R2, W R2). The Sentinel Prompt-Guard id is Planned (3e (b) catalogue).
- Note: AC (off-topic) catches many jailbreaks as a side effect but is not built for them (AC R2); it stays in C6.
- Note: P (context bloat) targets padding (P R2); AD is output-side leakage (AD R3).

### C6 Input-level off-topic detection against a policy or system prompt (I, AC)

- (1) Inputs ✓ Yes. System-prompt or policy plus user message: I R6, AC R6.
- (2) Ground truth ✓ Yes. On-topic label relative to the policy: I R4, AC R2.
- (3) Metrics ✓ Yes at the decision point: I R5, AC R5. Score metrics only for AC.
- (4) Architecture ✓ Yes. Harness with policy injection and one adapter each: I R7, AC R7. 3c Tools shows NeMo has no topic-control runner, so none is reusable.
- Note: J (dialog flow control) is excluded although it can refuse off-topic messages (J R2): output is a canned reply (J R5), ground truth is intents we author (J R6), it needs Colang and LLMRails (J R7; 3b rail types). See C7. NeMo does ship a topical runner for J, not for I (3c Tools).
- Note: Neither product is a general harm detector (I R2, AC R2); harmful prompts belong in C3.

### C7 Dialog-level conversational flow control (J)

- (1) Inputs ✗ (partial) vs closest candidate. Both take user messages, but J needs multi-turn history and authored intents (J R6).
- (2) Ground truth ✗ vs closest candidate. Intents defined by our own Colang file (J R6).
- (3) Metrics ✗ vs closest candidate. Reply correctness is not a binary verdict (J R5).
- (4) Architecture ✗ vs closest candidate. Needs Colang, embeddings and LLMRails (J R7).
- Note: Closest candidate is C6 (off-topic): J can refuse off-topic messages (J R2) but fails on ground truth and decision (J R5, J R6).
- Note: 3c strengthens a single-product row: NeMo provides datasets and a runner for J (3c Datasets, 3c Tools), which no other group has.

### C8 Retrieval-level chunk filtering (M)

- (1) Inputs ✗ vs closest candidate. Chunks from a knowledge base (M R6).
- (2) Ground truth ✗ vs closest candidate. Chunk-level keep or remove labels (M R5).
- (3) Metrics ✗ (partial) vs closest candidate. Detection rates apply, chunk-removal correctness does not exist elsewhere.
- (4) Architecture ✗ vs closest candidate. Needs a knowledge base and LLMRails (M R7).
- Note: Closest candidates are C1 and C2 (PII) and C9 and C10 (regex): the retrieval flows reuse those backends (M R3) but inspect retrieved chunks at a different position (M R1).

### C9 Regex pattern blocklist on input (N)

- (1) Inputs ✗ vs closest candidate. Strings keyed to authored patterns (N R7).
- (2) Ground truth ✗ vs closest candidate. Defined by the pattern list (N R6).
- (3) Metrics ✗ (partial) vs closest candidate. Block rates apply but carry no semantic meaning (N R4).
- (4) Architecture ✓ vs closest candidate in principle, no model to compare (N R7).
- Note: Closest candidates are C1 (PII, via custom regex) and C5 (attack strings): a regex can be written for either, but ground truth is then our own pattern (N R2).

### C10 Regex pattern blocklist on output (N)

- (1) Inputs ✗ vs closest candidate. Responses keyed to authored patterns (N R7).
- (2) Ground truth ✗ vs closest candidate. Defined by the pattern list (N R6).
- (3) Metrics ✗ (partial) vs closest candidate. Same as C9 (N R4).
- (4) Architecture ✓ vs closest candidate in principle, no model to compare (N R7).
- Note: Closest candidates are C2 (PII output) and C12 (injection output): both can be approximated by regex, but ground truth is then our own pattern (N R2).
- Note: Input and output are separate groups by user decision; N R3 lists separate input and output flows.

### C11 Context-bloat detection on input (P)

- (1) Inputs ✗ vs closest candidate. Oversized or repetitive text, not attack prompts (P R7).
- (2) Ground truth ✗ vs closest candidate. Threshold-derived (P R4).
- (3) Metrics ✗ (partial) vs closest candidate. Detection and false-positive rates apply (P R8).
- (4) Architecture ✓ vs closest candidate (input rail plus harness, P R7), but nothing to compare against.
- Note: Closest candidate is C5 (jailbreak): both target input manipulation, but padding is detected by size and entropy, a different threat and test set (P R2).

### C12 Output-level injection detection (O)

- (1) Inputs ✗ (partial) vs closest candidate. Both consume code in model output (O R7, Y R7).
- (2) Ground truth ✗ vs closest candidate. Payload classes (O R4) versus S14 abuse (Y R2).
- (3) Metrics ✗ (partial) vs closest candidate. Detection and false-positive rates apply to both.
- (4) Architecture ✗ vs closest candidate. YARA package, no GPU (O R7), versus GPU-served classifier (Y R7).
- Note: Closest candidates are C20 (Y, code-interpreter abuse) and C10 (regex output). Y judges abuse of an interpreter (Y R2), O finds exploit strings for downstream systems (O R2): different threat and labels.

### C13 Tool-call validation (Q)

- (1) Inputs ✗ vs closest candidate. Model-emitted calls versus request-side tool messages (Q R3, R R3).
- (2) Ground truth ✗ vs closest candidate. Schema validity versus ID linkage (Q R2, R R2).
- (3) Metrics ✗ (partial) vs closest candidate. Both are block-decision accuracy.
- (4) Architecture ✓ vs closest candidate, shared IORails config. User decision keeps output-side and input-side rows apart.
- Note: Closest candidate is C14 (tool-result validation), same engine and format: fails on position and object, a model call versus a tool message (Q R3, R R3).
- Note: Y (tool-use abuse) and U (custom actions) are not tool-call authorisation controls: Y classifies content (Y R3), U is developer logic (U R4).
- Note: 3c Engine coverage: NeMo evaluation has no tool-call expectation type, so 3c weakens architecture reuse for C13 to C15.

### C14 Tool-result validation (R)

- (1) Inputs ✗ vs closest candidate. Request-side tool messages (R R6).
- (2) Ground truth ✗ vs closest candidate. Linkage consistency (R R2).
- (3) Metrics ✗ (partial) vs closest candidate. Block accuracy.
- (4) Architecture ✓ vs closest candidate, shared IORails config.
- Note: Closest candidate is C13: same engine, different object and position (R R3, Q R3).
- Note: Injection through result text is unaddressed by this rail (R R4).

### C15 Execution-level custom action rails (U)

- (1) Inputs ✗ vs closest candidate. Authored action calls, not tool-call or tool-message formats (U R6).
- (2) Ground truth ✗ vs closest candidate. Our own logic.
- (3) Metrics ✗ (partial) vs closest candidate. Decision agreement.
- (4) Architecture ✗ vs closest candidate. LLMRails with Colang, not IORails (U R4).
- Note: Closest candidates are C13 and C14 (tool rails): separate rows in NeMo documentation (U R1; 3b rail types) with different engines and authorship (U R4, Q R4).

### C16 Grounded fact-checking of output (S)

- (1) Inputs ✗ vs closest candidate. Evidence chunks (S R6) versus prompt and live resampling (T R6).
- (2) Ground truth ✗ vs closest candidate. Support by evidence versus instability (S R2, T R2).
- (3) Metrics ✗ (partial) vs closest candidate. Decisions comparable, score only for S (S R5, T R5).
- (4) Architecture ✗ (partial) vs closest candidate. Both need LLMRails, a judge LLM and a custom flag flow (S R6, T R6); T also needs temperature-1.0 sampling (T R7).
- Note: Closest candidate is C17: also output-side hallucination detection, but it needs evidence while C17 needs resampling (S R2, T R1).
- Note: 3e (b) catalogue lists a Sentinel hallucination guardrail as Planned (not available, takes a context parameter); add it to C16 if it becomes available.

### C17 Self-consistency hallucination detection of output (T)

- (1) Inputs ✗ vs closest candidate. No evidence needed (T R1).
- (2) Ground truth ✗ vs closest candidate. Instability, not unsupportedness (T R2); NeMo sample has no labels (3c Datasets).
- (3) Metrics ✗ (partial) vs closest candidate. Binary metrics only (T R5).
- (4) Architecture ✗ (partial) vs closest candidate. Shares LLMRails and judge LLM with C16 but needs live sampling (T R7).
- Note: Closest candidate is C16: fails on inputs and ground truth (S R2, T R2).

### C18 Multimodal content-safety classification of input (image and text prompts) (X)

- (1) Inputs ✗ vs closest candidate. Images required (X R3).
- (2) Ground truth ✗ (partial) vs closest candidate. Same S-code taxonomy (X R2) with multimodal labels.
- (3) Metrics ✓ vs closest candidate. Same verdict metrics.
- (4) Architecture ✗ (partial) vs closest candidate. Same Llama Guard serving plus image processing (X R4).
- Note: Closest candidate is C3: Llama Guard 4 handles its text-only items (V R1), but X needs images that no other member can consume (X R3).
- Note: Split from C19 by user decision (input and output are separate groups); 3c is not used: no NeMo evaluation tool targets Llama Guard.

### C19 Multimodal content-safety classification of output (image and text prompt with text response) (X)

- (1) Inputs ✗ vs closest candidate. Image in the prompt (X R3).
- (2) Ground truth ✗ (partial) vs closest candidate. Same S-codes, multimodal pairs (X R2).
- (3) Metrics ✓ vs closest candidate. Same verdict metrics.
- (4) Architecture ✗ (partial) vs closest candidate. Same serving as C4 W plus image processing (X R4).
- Note: Closest candidate is C4: Llama Guard text responses are covered there (W R1), but C19 needs an image in the prompt (X R3).
- Note: Split from C18 by user decision.

### C20 Code-interpreter abuse classification (S14) (Y)

- (1) Inputs ✗ (partial) vs closest candidate. Agent code turns (Y R6) rather than general responses.
- (2) Ground truth ✗ vs closest candidate. S14 only.
- (3) Metrics ✓ vs closest candidate. Verdict metrics.
- (4) Architecture ✓ vs closest candidate, same serving as C4 member W.
- Note: Closest candidates are C4 (response harm) and C12 (injection in output): Y is one category of the Llama Guard taxonomy (Y R4), an abuse-of-interpreter label, not general harm or payload (Y R2).
- Note: Y could be folded into C4 as an S14 slice of W; kept separate because C4 members have no comparable abuse category (H R2, AA R2).

### C21 Custom-policy classification of input (prompts) (Z)

- (1) Inputs ✗ (partial) vs closest candidate. Same text prompts (Z R6).
- (2) Ground truth ✗ vs closest candidate. Author-defined categories.
- (3) Metrics ✗ (partial) vs closest candidate. Per-category rates plus exclusion flips unique to Z.
- (4) Architecture ✓ vs closest candidate, same serving as C3 member V.
- Note: Closest candidate is C3: same classifier, but ground truth is a tester-defined taxonomy, so scores are not comparable with fixed-taxonomy members (Z R2, Z R7).
- Note: Split from C22 by user decision; 3c is not used.

### C22 Custom-policy classification of output (responses) (Z)

- (1) Inputs ✗ (partial) vs closest candidate. Same response pairs (Z R3).
- (2) Ground truth ✗ vs closest candidate. Author-defined categories.
- (3) Metrics ✗ (partial) vs closest candidate. Per-category rates plus exclusion flips.
- (4) Architecture ✓ vs closest candidate, same serving as C4 member W.
- Note: Closest candidate is C4: same classifier, but ground truth is tester-defined, so scores are not comparable with fixed-taxonomy members (Z R2, Z R7).

### C23 System-prompt leakage detection (AD)

- (1) Inputs ✗ vs closest candidate. System prompt as context with the output (AD R3).
- (2) Ground truth ✗ vs closest candidate. Leak label (AD R2).
- (3) Metrics ✗ (partial) vs closest candidate.
- (4) Architecture ✓ vs closest candidate, Sentinel access only (AD R7).
- Note: Closest candidates are C5 (AG prompt_attack with leakage) and C4 (output safety): AD judges output similarity to a system prompt, not attack input or harmful content (AD R3).
- Note: AG may include prompt-leakage detection in the Standard tier (AG R2) but it is input-side and undisclosed, so it is not a comparator.

### C24 Refusal detection (AE)

- (1) Inputs ✗ (partial) vs closest candidate. Model replies with prompt (AE R3).
- (2) Ground truth ✗ vs closest candidate. Refusal labels, not harm labels (AE R2).
- (3) Metrics ✗ vs closest candidate. Agreement with human labels (AE R7).
- (4) Architecture ✗ (partial) vs closest candidate. Sentinel access only.
- Note: Closest candidates are C4 (response safety) and C6 (off-topic): AE detects declines of any reason, not unsafe content or topic drift (AE R2).

## C. Accounting

| Column | Header | Group(s) |
|---|---|---|
| E | Amazon Bedrock Guardrails: PII detection and masking | C1, C2 |
| F | NeMo Guardrails: Input-level jailbreak detection | C5 |
| G | NeMo Guardrails: Input-level content-safety moderation | C3 |
| H | NeMo Guardrails: Output-level content-safety moderation | C4 |
| I | NeMo Guardrails: Input-level topic control | C6 |
| J | NeMo Guardrails: Dialog-level conversational flow control | C7 |
| K | NeMo Guardrails: Input-level PII detection & masking | C1 |
| L | NeMo Guardrails: Output-level PII detection & masking | C2 |
| M | NeMo Guardrails: Retrieval-level chunk filtering | C8 |
| N | NeMo Guardrails: Regex pattern blocklist (input/output) | C9, C10 |
| O | NeMo Guardrails: Output-level injection detection | C12 |
| P | NeMo Guardrails: Context-bloat detection (input) | C11 |
| Q | NeMo Guardrails: Tool-call validation | C13 |
| R | NeMo Guardrails: Tool-result validation | C14 |
| S | NeMo Guardrails: Grounded fact-checking (output) | C16 |
| T | NeMo Guardrails: Self-consistency hallucination detection (output) | C17 |
| U | NeMo Guardrails: Execution-level custom action rails | C15 |
| V | Llama Guard: Input-level prompt content-safety classification | C3 |
| W | Llama Guard: Output-level response content-safety classification | C4 |
| X | Llama Guard: Multimodal (image + text) content-safety classification | C18, C19 |
| Y | Llama Guard: Code-interpreter and tool-use abuse classification | C20 |
| Z | Llama Guard: Custom-policy classification | C21, C22 |
| AA | GovTech Sentinel: Localised harmful-content classification (LionGuard 2) | C3, C4 |
| AB | GovTech Sentinel: Prompt-attack detection | C5 |
| AC | GovTech Sentinel: Off-topic prompt detection against the system prompt | C6 |
| AD | GovTech Sentinel: System-prompt leakage detection | C23 |
| AE | GovTech Sentinel: Refusal detection | C24 |
| AF | GovTech Sentinel: PII detection and masking (AWS Bedrock) | C1, C2 |
| AG | GovTech Sentinel: Generic content moderation via AWS Bedrock Guardrails | C3, C5 |

### 3c usage

Groups citing sheet 3c in their table cells: C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17.
Why: C1 to C6 and C8 to C17 are NeMo-related; they cite 3c for NeMo seed datasets (3c Datasets: C3, C4, C6, C7, C16, C17), garak probe families (3c Red-teaming: C5, C12), NeMo runners (3c Tools: C1, C2, C3, C4, C6, C7, C9 to C11, C12, C15 to C17), engine limits (3c Engine coverage: C2, C5, C13, C14) or the documented absence of any NeMo evaluation for the function (3c Reuse, 3c Published results: C1 to C3, C5, C8 to C15).
Groups not citing 3c: C18, C19, C20, C21, C22, C23, C24. These are Llama Guard (C18 to C22) and Sentinel (C23, C24) functions: 3c covers NeMo evaluation only and no 3c tool drives a non-NeMo product.
Reusable pieces across groups, with 3c caveats: the policy-and-interaction schema as a harness shape and the run record (calls, tokens, latency) as a result template (3c Reuse); the benchmark folder for latency testing of NeMo servers (3c Tools: benchmark). Runners are written for the classic engine, IORails is untested, there is no streaming and only three expected-output types exist (3c Engine coverage). They drive NeMo members only, so the cross-product harness is still needed.


All 29 columns E to AG appear in at least one group: yes.

Functions in more than one group: E (C1, C2); N (C9, C10); X (C18, C19); Z (C21, C22); AA (C3, C4); AF (C1, C2); AG (C3, C5).

## D. Open comparability questions

- Verdict versus score. F returns block or allow only with no score (F R5); G, H, I, V, W, Q and R return verdicts (G R5, H R5, I R5, V R5, W R5, Q R5, R R5). AA, AB, AC, AD, AE, AF and AG return 0 to 1 scores with no server threshold (AA R5, AB R5, AC R5, AD R5, AE R5, AF R5, AG R5). Groups C3 to C6 can therefore be compared only at a binary decision point; AUPRC applies to a subset of members.
- Sentinel scores may not be probabilities. AG examples show only 0.0 and 1.0 (AG R5) and AF behaves like a flag (AF R4), while the docs call the score a probability (AA R5). Threshold guidance differs: 0.95 generic, playground 0.95 and 0.80, paper 0.5, demos 0.4 and 0.7 (AA R5, AC R5, AD R5). A single threshold policy for the bench is undecided.
- Closed beta and access. Sentinel is limited to Singapore Government public officers and Singapore IP addresses, labelled proof of concept and unsuitable for production (AA R6, AB R6, AC R6, AD R6, AE R6, AF R4, AG R4). Only LionGuard and the off-topic models have self-hosting routes (3e (d) access paths; AA R4, AC R4); AB, AE, AF and AG have none (AB R4, AE R4, AF R4, AG R4), and AD has only a demo Space that needs an Azure OpenAI key (AD R4).
- Undisclosed models. AB, AE, AF and AG internals are not disclosed (AB R4, AE R4, AF R4, AG R4); AD service model is unconfirmed (AD R4); AC served variant is unconfirmed (AC R4); F classifier threshold and coverage are undisclosed (F R5, F R8); AWS models are not named (AG R4). Results cannot be attributed to a model.
- Shared AWS backend. E, AF and AG all use AWS Bedrock Guardrails (E R4, AF R4, AG R4). Results from E and AF in C1 and C2, and from AG in C3 and C5, are not independent product comparisons. Whether Sentinel configures the same tier, strengths and region as a native Bedrock policy is not stated (AF R4, AG R8). E has summary-level research only (E R1).
- Input or output scope conflicts. AB is Input in one table and Input/Output in another (AB R3); AC types and guardrail tables disagree (AC R3); AG ids are Input only although AWS filters support output (AG R3, AG R8). Whether AB, AC and AG can be added to output-side groups needs live testing.
- Taxonomy mapping. Nemotron S1 to S23 or S1 to S22 (G R2), Llama Guard S1 to S14 with S14 only in some versions (V R2, Y R1), LionGuard six categories with levels (AA R2), AWS five categories with no self-harm (AG R2). Llama Guard category and version coverage is in 3d (a) variant table and LionGuard in 3e (c) crosswalk. A mapping table must be written and agreed before any per-category result is reported.
- Model and version choice inside a function. V and W cover LG4, LG3-8B, LG3-8B-INT8, LG3-1B and 3-11B-Vision (V R1, W R1) with different language and S14 support (V R6, Y R1); G lists Llama Guard, Nemotron, ShieldGemma or self-check as backends (G R4); AA has three LionGuard versions and the Sentinel default is unclear (AA R4, AA R8). The bench must fix which version represents each function (3d (a) variant table).
- Engines and flags in NeMo. Several functions run on LLMRails only (J R4, M R4, S R4, T R4, U R4), tool rails on IORails only (Q R4, R R4), and S and T need a custom Colang flow to set a flag (S R6, T R6). A single NeMo harness may need both engines. Detector outages fail open for F and T (F R4, T R4).
- Languages. AA targets Singlish, Chinese, Malay and Tamil (AA R2); AC is English only (AC R6); F heuristics are English only (F R2); LG language coverage is contested for LG4 (V R8); AWS tier and language support under Sentinel are not stated (AG R6, AF R6). Multilingual subsets cannot be run for every member.
- Documentation conflicts affecting adapters. Sentinel parameters and ids differ between the portal and the playbook (AA R6, AC R6, AD R6, AE R6, AF R6); NeMo documented keys not matching v0.24.1 (U R4, O R6, M R4). Adapters should be validated with smoke tests before measurement.
- NeMo evaluation tooling covers NeMo only. Its runners are written for the classic engine, IORails is untested, there is no streaming and only three expected-output types exist (3c Engine coverage); the moderation, fact-checking and hallucination tasks bypass the rail pipeline and test the self-check prompts only (3c Tools). Garak drives a NeMo config or server only (3c Red-teaming). No NeMo tool or garak path drives Llama Guard, Bedrock or Sentinel.
- NVIDIA published results are NeMo-reported, mostly 2023 to early 2024 on retired models, with small samples and no false-positive measurement for garak (3c Published results, 3c Reuse). They must not be used as baselines or compared with other products. Datasets in the repo are mostly 1 to 15 item placeholders; the real ones must be downloaded, and ToxicChat is non-commercial (3c Datasets).
- Seed-data label compatibility. NeMo datasets give binary harmful or benign prompts (Anthropic ratings, 3c Datasets), intent labels (chit-chat, banking77) or constructed fact-check negatives. Only the binary prompt labels transfer, and only to C3 members; other groups need purpose-built data (3c Reuse: gaps).
- Sentinel planned guardrails. A hallucination id and a Prompt-Guard jailbreak id are listed as Planned and not available (3e (b) catalogue); C5 and C16 can gain Sentinel members later.
- Latency is not like for like. Sentinel latency includes network round trips from Singapore (AA R4, AB R4), NeMo and Llama Guard latency depends on our own hosting (F R7, V R4), NeMo benchmark tooling tests server capacity with mock LLMs only (3c Tools: benchmark), and Sentinel AWS-suite latency is a single docs sample (AG R4). Latency should be reported per deployment, not ranked across products.
