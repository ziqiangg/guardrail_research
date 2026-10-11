# Sheet 4 — Candidate Comparison Groups (draft v3, bulleted)

Regrouped once across all ten products (R006), from the sheet 3 columns E to BN. Bench content in new and changed rows (columns C to G) is worded as proposals (R032); rows carried from v2 keep their v2 wording (see D2). Nothing here decides the bench design. Evaluation tools CyberSecEval (3k) and Litmus (3n) have no sheet 3 columns and are cited only as possible sources of test inputs or ground truth.

## A. Group table

Bands applied by the builder: C1 to C14 are comparison groups (2+ products); C15 to C34 are single-product functions (no comparator yet).

| Candidate group | Guardrail functions included | Common test inputs | Ground truth | Outputs to capture | Common metrics | Minimum architecture | Material differences or limitations |
|---|---|---|---|---|---|---|---|
| C1 Input-level PII and sensitive-data detection and masking in text | E: Amazon Bedrock Guardrails: PII detection and masking (template example column); K: NeMo Guardrails: Input-level PII detection & masking; AF: GovTech Sentinel: PII detection and masking (AWS Bedrock); AH: Presidio: PII detection in text (Analyzer); AI: Presidio: PII anonymisation and masking in text (Anonymizer); AN: Sensitive Data Protection: Sensitive-data detection in text (infoType inspection); AP: Sensitive Data Protection: Sensitive-data masking and de-identification in text; AX: Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection); BL: Cloak: Free-text PII detection and anonymisation | • Suggested: single user messages with synthetic, labelled PII of known types<br>• Add ambiguous strings, custom-format identifiers, Singapore-style IDs, non-PII controls<br>• NeMo ships no PII dataset; seed data would be built<br>• presidio-research is a possible scorer for span results<br>Refs: E R6, K R7, AF R7, AH R7, AN R7, BL R7, 3c Reuse | • Suggested: per text, PII type and character span of each item<br>• Expected action (block, mask or allow) and expected masked text<br>• Entity lists differ: a harmonised common subset could be scored<br>• Possible subset: name, email, phone, address, national ID, card number<br>• Other types reported separately, such as NRIC or FIN where supported<br>Refs: E R2, K R2, AF R2, AH R2, AN R2, AX R2, BL R2 | • Decision where exposed: blocked, masked or allowed (E, K, AF)<br>• Findings with type and span where exposed (AH, AN, AX, AF)<br>• Score: AH 0 to 1; AN five levels; AF 0 to 1<br>• AF scores seen so far were 0.0 or 1.0<br>• Masked text or change list (AI, AP, AX, BL)<br>• Latency; error<br>Refs: K R5, AF R5, AH R5, AI R5, AN R5, AP R5, AX R5, BL R5 | • Detection rate (recall) per entity type; precision where spans are returned<br>• False-positive and false-negative rates, same breakdown<br>• Masking correctness: masked text equals expected, no residual PII<br>• Threshold sweeps only for score or likelihood outputs (AH, AN)<br>• Latency per call<br>• E and K expose no score; AF score looks like a flag<br>Refs: AH R5, AN R5, AF R4, E R5, K R5, AP R5 | • Suggested harness: loader, adapters, common result format, recorder, evaluator<br>• AH, AI: pip install plus spaCy model, or GHCR image<br>• E: Bedrock sensitive-information policy; AF: Sentinel beta key, Singapore IP<br>• AN, AP, AX: Google Cloud project; AX adds a Model Armor template<br>• BL: approved Cloak account for Web UI or API<br>• K: NeMo config with one backend; eval run could drive K only<br>Refs: AH R7, AI R7, AN R7, AP R7, AX R7, BL R7, K R7, 3e (d) access paths, 3f (d) integration paths, 3g (d) integration and access paths, 3h (b) integration paths, 3l (b) access and integration paths, 3c Tools | • Entity lists differ: AWS types, Presidio recognizers, SDP infoTypes, Cloak groups<br>• Shared backends, not independent: K-AH, AF-E, AX-AN<br>• BL may reuse Presidio recognisers; GovTech does not say<br>• AH, AN return findings only; AI masks only supplied spans<br>• AX basic mode uses a short, US-leaning fixed list<br>• BL needs approved access; Terms clause 3.4.7 benchmarking question open<br>• Google AUP testing clause not recorded in AN, AP or AX columns<br>• AF returns raw matches; Sentinel is closed beta; E has summary-level research<br>• BI regex scanner covers four PII shapes: see C3<br>• Output side is C2<br>Refs: E R4, K R4, AF R4, AH R5, AI R3, AX R2, AX R8, BL R4, BL R8, AN R8, 3g (d) integration and access paths, 3l (e) limits and terms |
| C2 Output-level PII and sensitive-data detection and masking in text | E: Amazon Bedrock Guardrails: PII detection and masking (template example column); L: NeMo Guardrails: Output-level PII detection & masking; AF: GovTech Sentinel: PII detection and masking (AWS Bedrock); AH: Presidio: PII detection in text (Analyzer); AI: Presidio: PII anonymisation and masking in text (Anonymizer); AN: Sensitive Data Protection: Sensitive-data detection in text (infoType inspection); AP: Sensitive Data Protection: Sensitive-data masking and de-identification in text; AY: Model Armor: Output-level sensitive data detection and de-identification (Sensitive Data Protection); BL: Cloak: Free-text PII detection and anonymisation | • Suggested: model responses, scripted or generated, with synthetic labelled PII<br>• Add clean responses, borderline strings and responses repeating prompt PII<br>• No product ships labelled response data; seed data would be built<br>Refs: L R7, E R6, AF R7, AH R3, AY R7, 3c Reuse | • Suggested: per response, PII type and span of each item<br>• Expected action (block, mask or allow) and final user-visible text<br>• Score the harmonised common entity subset, as in C1<br>• Other types reported separately<br>Refs: L R5, E R2, AF R3, AY R2 | • Decision where exposed: blocked, masked or allowed (E, L, AF)<br>• Findings with type, span, score or likelihood (AH, AN, AY, AF)<br>• Final text or de-identified copy (AI, AP, AY, BL)<br>• Latency; error<br>Refs: L R5, AF R5, AH R5, AI R5, AN R5, AP R5, AY R5, BL R5 | • Detection rate, false-positive and false-negative rates per entity type<br>• Masking correctness on the final text<br>• Threshold sweeps only for score or likelihood outputs (AH, AN)<br>• Latency per call; non-streaming runs first<br>Refs: AH R5, AN R5, E R5, L R5, L R8 | • Suggested harness feeding scripted or real main LLM responses<br>• Adapters, result format, recorder, evaluator as in C1<br>• L: NeMo output rail with one backend and its service<br>• AY: Model Armor response method, regional template, SDP basic or advanced<br>• nemoguardrails eval run could drive L only, on LLMRails<br>Refs: L R7, AY R7, 3h (b) integration paths, 3e (d) access paths, 3c Tools | • Same entity-list, backend-sharing and access limits as C1<br>• L may release PII during streaming before the rewrite<br>• Rewrites under streaming need stream_first false<br>• AY basic list may not apply to responses; result shape unshown<br>• AF wraps AWS Bedrock Guardrails: backend shared with E, not independent<br>• NeMo evaluation tooling has no streaming: test non-streaming first<br>• Input side is C1<br>Refs: L R4, L R8, AY R2, AY R3, AF R4, 3c Engine coverage |
| C3 Input-level rule-based pattern matching in text (regex, word lists, fixed rules) | E: Amazon Bedrock Guardrails: PII detection and masking (template example column); N: NeMo Guardrails: Regex pattern blocklist (input/output); AM: Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers); AO: Sensitive Data Protection: Custom detectors and inspection rules (custom infoTypes); BI: LlamaFirewall: Regex pattern blocking and custom scanners (Regex scanner); BK: LlamaFirewall: Hidden Unicode tag-character detection (Hidden ASCII scanner); BM: Cloak: Custom entity detection in free text (lists, regex and LLM) | • Suggested: user messages that match and do not match the same rules<br>• Authored regex and word lists loaded into each product's own format<br>• BI, BK: strings built around their fixed documented rules<br>• No product dataset; strings would be written for the test<br>Refs: N R7, AM R7, AO R7, BI R7, BK R7, BM R7, E R6 | • Suggested: per string and rule set, expected match or no match<br>• Derived from the rule definitions, so the label is deterministic<br>• Expected spans where the product returns them<br>• BI, BK: expected outcome follows their fixed documented rules<br>Refs: N R2, AM R2, AO R2, BI R2, BK R2, BM R2, E R4 | • Block or mask decision (E, N, BI, BK)<br>• Matched pattern or span, with score or likelihood (N, AM, AO, BI)<br>• Transformed text per match (BM, E); decoded hidden text (BK)<br>• Latency; error<br>Refs: N R5, AM R5, AO R5, BI R5, BK R5, BM R5, E R5 | • Exact agreement with the expected match outcome per string<br>• False-positive and false-negative rates against the rules<br>• Span overlap where spans are returned (AM, AO)<br>• Latency, including slow-pattern cases<br>• No score curves: AM and AO scores are author-set<br>Refs: N R5, AM R5, AO R5, BI R5, BM R4 | • Suggested harness: rule loader, adapters, result format, recorder, evaluator<br>• N: NeMo config with input patterns and a stub LLM<br>• AM: local Analyzer with spaCy model; BI, BK: llamafirewall, no key<br>• AO: Google Cloud project, DLP User role; E: Bedrock policy<br>• BM: approved Cloak account; custom entities set per project<br>Refs: N R7, AM R7, AO R7, BI R7, BK R7, BM R7, E R7, 3c Tools | • Authored patterns for N, AM, AO, BM, E; BI, BK rules fixed<br>• BI, BK rules could be re-expressed as regex for the other products<br>• Regex dialects, limits and matching methods differ; AO caps regex at 1000<br>• AM, AO and BM (API only) add context or hotword rules<br>• BK compares only if the others get the tag-block regex<br>• BM LLM entity is Beta and not pattern matching: test apart<br>• BM Terms clause 3.4.7 benchmarking question is an open item<br>• Output side is C4; the N retrieval variant is C16<br>Refs: AO R6, BI R6, BK R2, BM R4, BM R6, BM R8, N R3, N R8, AM R4 |
| C4 Output-level rule-based pattern matching in text (regex, word lists, fixed rules) | E: Amazon Bedrock Guardrails: PII detection and masking (template example column); N: NeMo Guardrails: Regex pattern blocklist (input/output); AM: Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers); AO: Sensitive Data Protection: Custom detectors and inspection rules (custom infoTypes); BI: LlamaFirewall: Regex pattern blocking and custom scanners (Regex scanner); BK: LlamaFirewall: Hidden Unicode tag-character detection (Hidden ASCII scanner); BM: Cloak: Custom entity detection in free text (lists, regex and LLM) | • Suggested: bot responses scripted by a stub LLM<br>• Responses that match and do not match each rule<br>• Same rule lists as C3; no product dataset<br>Refs: N R7, AM R3, AO R3, BI R3, BK R3, 3c Reuse | • Suggested: per response and rule set, expected match or no match<br>• Derived from the rule definitions, so deterministic<br>• Expected final text where a product transforms matches<br>Refs: N R2, AM R2, AO R2, BK R2, BM R5, E R5 | • Block or mask decision (E, N, BI, BK)<br>• Matched pattern or span, with score or likelihood (N, AM, AO, BI)<br>• Transformed text per match (BM, E)<br>• Latency; error<br>Refs: N R5, AM R5, AO R5, BI R5, BK R5, BM R5 | • Exact agreement with the expected match outcome per response<br>• False-positive and false-negative rates against the rules<br>• Span overlap where spans are returned (AM, AO)<br>• Latency<br>Refs: N R5, AM R5, AO R5, BI R5 | • Suggested harness with a stub LLM returning scripted text<br>• N: NeMo config with output patterns, both engines<br>• Other adapters as in C3: AM, AO, BI, BK, BM, E<br>• nemoguardrails eval run could drive N on LLMRails<br>Refs: N R7, 3b surface table, 3c Tools, E R7 | • Same limits as C3: authored patterns, BI and BK fixed, dialects differ<br>• N has a separate output check; the others take any string<br>• N output check has no exception path<br>• BI and BK are outside the default role map<br>• Input side is C3<br>Refs: N R3, N R8, BI R3, BK R3, AM R3, AO R3 |
| C5 Reversible tokenisation of text before the model (encrypt side) | AJ: Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt); AQ: Sensitive Data Protection: Reversible tokenisation and re-identification (AES-SIV and FPE); BN: Cloak: Reversible anonymisation and decryption (encrypt and restore) | • Suggested: user messages with synthetic labelled entities to tokenise<br>• Repeated values, so token consistency can be observed<br>• Same entity set across the three products<br>• No product dataset; strings would be written for the test<br>Refs: AJ R7, AQ R7, BN R7 | • Suggested: per entity, original value and span in the outgoing text<br>• Expected: no original value survives in the tokenised text<br>• Expected token properties per product: format, length, alphabet<br>Refs: AJ R4, AQ R4, BN R4 | • Tokenised text with item list (AJ) or change summary (AQ)<br>• Ciphertext strings in the text (BN)<br>• Token format, length and alphabet<br>• Latency; error<br>Refs: AJ R5, AQ R5, BN R5 | • Residual-PII rate: original values left in the tokenised text<br>• Token format conformity: length, alphabet, base64<br>• Token consistency for repeated values, observed per product<br>• Latency per call; round-trip exactness is scored in C6<br>Refs: AJ R4, AQ R4, BN R2 | • Suggested harness: loader, adapters, key setup, recorder, evaluator<br>• AJ: Anonymizer with a caller-held AES key; local, no account<br>• AQ: Google Cloud project, DLP and KMS APIs, wrapped key in region<br>• BN: approved Cloak account and a Secrets Manager secret<br>Refs: AJ R7, AQ R7, BN R7, 3f (d) integration paths, 3g (d) integration and access paths, 3l (b) access and integration paths | • Keys differ: caller-held (AJ), Cloud KMS wrapped (AQ), Secrets Manager (BN)<br>• BN Encrypt may be Presidio's encrypt operator; GovTech does not say<br>• AJ uses a random vector per entity; AQ repeats tokens per key<br>• AQ docs disagree on whether AES-SIV keeps length<br>• BN needs approved access; Terms clause 3.4.7 benchmarking question open<br>• Entity detection differs: AJ uses the Analyzer, AQ and BN their own<br>• Restore side is C6<br>Refs: AJ R4, AQ R4, BN R4, BN R8, AJ R3, AQ R2, 3l (e) limits and terms |
| C6 Restoring tokens in model output (decrypt side) | AJ: Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt); AQ: Sensitive Data Protection: Reversible tokenisation and re-identification (AES-SIV and FPE); BN: Cloak: Reversible anonymisation and decryption (encrypt and restore) | • Suggested: mock model replies that echo, edit, drop or reorder tokens<br>• Replies with several tokens, and replies with none<br>• Wrong key or secret, and damaged-token cases<br>• Tokens produced by C5 runs<br>Refs: AJ R7, AQ R7, BN R7, AJ R3 | • Suggested: per reply, expected restored text with original values<br>• Echoed tokens restore exactly; dropped tokens stay absent<br>• Wrong-key and damaged-token expectations are open: observe and record<br>Refs: AJ R1, AQ R1, BN R1, AJ R8, AQ R8 | • Restored text and item list (AJ)<br>• Re-identified item and change summary (AQ)<br>• Decrypted value per pasted token (BN Web UI)<br>• Error or silent wrong text; latency<br>Refs: AJ R5, AQ R5, BN R5, BN R8 | • Restore exactness per token<br>• Partial-restore rate for edited or reordered tokens<br>• Failure handling: clear error versus silently wrong text<br>• Latency per call<br>Refs: AJ R7, AQ R7, BN R7 | • Suggested harness replaying mock replies, with key handling<br>• AJ: Deanonymize with the same key, token spans and types<br>• AQ: re-identify with the same wrapped key and surrogate name<br>• BN: Web UI decrypts one pasted token; API takes rows<br>Refs: AJ R6, AQ R6, BN R6, 3f (d) integration paths, 3g (d) integration and access paths | • AJ needs token offsets; model edits can move them<br>• BN restores one value at a time in the UI<br>• AQ re-identify may not accept conversation or batch items<br>• BN Terms clause 3.4.7 benchmarking question is an open item<br>• Long encrypted tokens may be altered by a real model<br>• Encrypt side is C5<br>Refs: AJ R3, AJ R8, BN R3, BN R8, AQ R8 |
| C7 PII and sensitive-text detection and redaction in images | AK: Presidio: PII detection and redaction in images (Image Redactor); AR: Sensitive Data Protection: Sensitive-data detection and redaction in images; BC: Model Armor: Image screening with OCR and visual scanning | • Suggested: images of known text carrying labelled synthetic PII, plus clean images<br>• Screenshots, scans and photos; varied fonts, sizes and layouts<br>• AR also: images with ID-type objects for its object detectors<br>• Preview features (AR faces, BC) with synthetic data only<br>Refs: AK R7, AR R7, BC R7, AR R2, 3h (d) locations and feature availability | • Suggested: per image, PII text items with entity type and box<br>• Expected redacted regions; clean images expect none<br>• Hand-drawn box coordinates; box origin conventions differ<br>• Entity lists differ: score a harmonised subset<br>Refs: AK R2, AR R2, BC R2, AR R8, BC R8 | • Redacted image (AK, AR, BC)<br>• Findings with type, score or likelihood and box<br>• Extracted text (BC)<br>• Latency; error<br>Refs: AK R5, AR R5, BC R5 | • Per-entity detection rate on text read from the image<br>• Box overlap with hand-drawn ground truth<br>• Residual readable PII after redaction, checked by re-running OCR<br>• False-positive rate on clean images; latency<br>Refs: AK R5, AR R5, BC R5 | • Suggested harness: image loader, adapters, box scorer, recorder, evaluator<br>• AK: Image Redactor with Tesseract and spaCy model, or Docker image<br>• AR: Google Cloud project, DLP API, regional endpoint such as Singapore<br>• BC: Model Armor template in us or eu with image modality<br>• BC also needs an advanced SDP template; redaction a de-identify template<br>Refs: AK R7, AR R7, BC R7, 3f (d) integration paths, 3g (f) region and availability, 3h (d) locations and feature availability | • AK is beta; BC is Preview, us and eu only<br>• AR adds object detectors beyond text<br>• BC wraps SDP image handling: backend shared with AR, not independent<br>• OCR engines differ; AK thresholds differ between Python and REST<br>• Format and size limits are stated for AR and BC only<br>• No direction flag: one group kept; BC response-side images not shown<br>• Google AUP testing clause is recorded for BC as an open item<br>Refs: AK R1, AK R4, AK R5, AR R6, BC R3, BC R4, BC R8, AK R3 |
| C8 Harmful-content classification of input (user prompts) | G: NeMo Guardrails: Input-level content-safety moderation; V: Llama Guard: Input-level prompt content-safety classification; AA: GovTech Sentinel: Localised harmful-content classification (LionGuard 2); AG: GovTech Sentinel: Generic content moderation via AWS Bedrock Guardrails; AT: Model Armor: Input-level responsible AI safety filtering; BD: LionGuard: Localised harmful-content classification | • Suggested: single-turn user prompts, harmful and benign, plus benign near-misses<br>• NeMo seeds: Anthropic red-team-attempts and helpful-base prompts, binary label only<br>• Litmus Undesirable Content themes could guide cases; it publishes no prompts<br>• Multilingual cases: Singlish, Chinese, Malay, Tamil (AA, BD); AT nine languages<br>Refs: G R7, V R7, AA R7, AG R7, AT R7, BD R2, 3c Datasets, 3n Reuse | • Suggested: per prompt, binary harmful or benign label<br>• Plus category label mapped to a common taxonomy<br>• Taxonomies differ: G Nemotron codes; V S1 to S14; AA, BD six<br>• AG five categories; AT four plus CSAM<br>• Compare per category only where a mapping exists<br>Refs: G R2, V R2, AA R2, AG R2, AT R2, BD R2 | • Decision where exposed (G, V, AG, AT overall match state)<br>• Category codes, per-category scores or probabilities (AA, BD, AT)<br>• First-token probability for V only if extracted<br>• Latency; error<br>Refs: G R5, V R5, AA R5, AG R5, AT R5, BD R5 | • True-positive, false-positive, false-negative rates on binary harmful label<br>• Measured at each product's own decision point<br>• AUPRC and sweeps only where probabilities exist: AA, BD, V if extracted<br>• AG shows 0.0 or 1.0; AT gives match states and levels<br>• BD ships no cut-off; AA scores have no server threshold<br>Refs: 3c Published results, AG R5, AT R5, BD R5, AA R5 | • Suggested harness: loader, adapters, common result format, recorder, evaluator<br>• G: NeMo input rail, safety model endpoint, prompt<br>• V: GPU-served Llama Guard with template and verdict parser<br>• AA, AG: Sentinel beta key, Singapore IP; BD: local Transformers<br>• AT: Google Cloud project, Model Armor template, regional endpoint<br>Refs: G R6, 3d (c) integration paths, 3e (d) access paths, 3i (c) dependencies and access, 3h (b) integration paths, 3c Tools | • AA and BD share LionGuard models: not independent<br>• G can call Llama Guard: G and V may share a model<br>• AG wraps AWS Bedrock Guardrails and has no self-harm category<br>• AT model undisclosed; default confidence unclear; Google AUP clause open item<br>• BD embedder terms (OpenAI, Gemini, Gemma) are open items<br>• Taxonomies and thresholds differ; Sentinel is closed beta<br>Refs: AG R2, AA R2, G R5, V R5, AT R4, AT R8, BD R8, 3i (c) dependencies and access, 3e (b) catalogue |
| C9 Harmful-content classification of output (model responses) | H: NeMo Guardrails: Output-level content-safety moderation; W: Llama Guard: Output-level response content-safety classification; AA: GovTech Sentinel: Localised harmful-content classification (LionGuard 2); AU: Model Armor: Output-level responsible AI safety filtering; BD: LionGuard: Localised harmful-content classification | • Suggested: model responses to benign and harmful prompts, scripted or generated<br>• Include safe refusals of unsafe prompts and benign near-misses<br>• H, W need the prompt; AA, BD, AU read the response alone<br>• NeMo moderation sample prompts can elicit responses; none are labelled<br>• Litmus Undesirable Content themes could guide cases; it publishes no prompts<br>Refs: H R7, W R7, AA R3, AU R3, BD R3, 3c Datasets, 3n Reuse | • Suggested: per response, binary unsafe or safe label on the response itself<br>• Plus category label mapped to a common taxonomy<br>• Taxonomies: Nemotron codes, Llama Guard S1 to S14, LionGuard six, AU four<br>• Compare per category only where a mapping exists<br>Refs: H R2, W R2, AA R2, AU R2, BD R2 | • Decision where exposed (H, W, AU overall match state)<br>• Category codes, per-category scores or probabilities (AA, BD, AU)<br>• First-token probability for W only if extracted<br>• Latency; error<br>Refs: H R5, W R5, AA R5, AU R5, BD R5 | • True-positive, false-positive, false-negative rates on binary unsafe label<br>• Measured at each product's decision point<br>• AUPRC and sweeps: AA, BD, and W if probabilities extracted<br>• AU gives match states with confidence levels, no score<br>• Non-streaming runs only<br>Refs: H R5, W R5, AU R5, BD R5, AA R5 | • Suggested harness with scripted responses or a stub main LLM<br>• Also adapters, common result format, recorder, evaluator<br>• H: NeMo output rail with a safety model endpoint<br>• W: GPU-served Llama Guard with response template, verdict parser<br>• AA: Sentinel key; BD: local models; AU: regional response method<br>Refs: H R7, 3d (c) integration paths, 3e (d) access paths, 3i (c) dependencies and access, 3h (b) integration paths, 3c Tools | • H with Nemotron prompts checks the user turn with the response<br>• W judges the response; AA, BD, AU read it alone<br>• So a harmful prompt can change the result<br>• Taxonomies differ; W reports no threshold: LG3, LG4 figures not comparable<br>• AA and BD share LionGuard models: not independent<br>• H blocks can follow streamed tokens<br>• AG excluded: Sentinel lists it input only<br>• AU docs examples send no prompt; Google AUP clause open item<br>• Sentinel is closed beta<br>Refs: H R1, W R3, AA R3, AU R3, AU R8, H R2, W R5, 3e (b) catalogue, AG R3, 3e (d) access paths |
| C10 Input-level jailbreak and prompt-attack detection | F: NeMo Guardrails: Input-level jailbreak detection; AB: GovTech Sentinel: Prompt-attack detection; AG: GovTech Sentinel: Generic content moderation via AWS Bedrock Guardrails; AV: Model Armor: Input-level prompt injection and jailbreak detection; BE: Prompt Guard 2: Input-level prompt-attack detection (jailbreak and injection); BF: LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner) | • Suggested: single-turn jailbreak, injection and benign prompts<br>• Benign prompts that mention instructions or code; also non-English text<br>• Possible attack sources: Garak families; CyberSecEval injection cases, 251 English<br>• Benign look-alikes would be needed; Meta publishes none<br>• Litmus DoAnythingNow theme could guide jailbreak cases; no prompts published<br>Refs: F R6, AB R7, AG R7, AV R7, BE R7, BF R7, 3c Red-teaming, 3k Datasets, 3k Reuse, 3n Reuse | • Suggested: per prompt, binary attack or benign label under one agreed definition<br>• Optionally with an attack style; CyberSecEval technique labels could help<br>• Definitions differ: F undefined; AB three intents; AV override and jailbreak<br>• BE flags explicit override only; AG jailbreak, injection, possibly leakage<br>• Garak labels come from its own detectors, some model-based<br>Refs: F R2, AB R2, AG R2, AV R2, BE R2, 3k Reuse, 3c Tools | • Decision: F block or allow; BE label; BF allow or block<br>• Scores: AB with confidence; AG, BE, BF; AV level; F none<br>• Latency; error, including detector-unreachable cases<br>Refs: AB R5, AG R5, AV R5, BE R5, BF R5, F R5, F R4 | • True-positive, false-positive, false-negative rates at each product's decision point<br>• Recall at a fixed false-positive rate, as Meta reports for BE<br>• AUPRC and sweeps only for scored outputs: AB, BE, BF<br>• AG shows 0.0 and 1.0; AV gives levels; F has no score<br>• Latency; Garak reports protection rates per probe, not false positives<br>Refs: AG R5, AV R5, BE R5, 3c Red-teaming | • Suggested harness: loader, adapters, common result format, recorder, evaluator<br>• F: NeMo input rail with a detector (heuristics, or NemoGuard endpoint)<br>• BE: gated Hugging Face weights, Transformers; BF: llamafirewall PromptGuard scanner<br>• AB, AG: Sentinel beta key; AV: Google Cloud template, regional endpoint<br>• Garak NeMoGuardrails generator could drive F only<br>Refs: F R7, BE R7, BF R7, AV R7, 3e (d) access paths, 3j (e) integration and access paths, 3h (b) integration paths, 3c Red-teaming, 3c Engine coverage | • BF runs the BE model: not independent<br>• Both need the Llama 4 licence gate<br>• Whether the Llama 4 policy allows attack-prompt testing is an open item<br>• AG is the aws/prompt_attack id, sharing the Bedrock backend with E<br>• AB model undisclosed; AV Google AUP clause open item<br>• F returns block or allow only, fails open, English-only heuristics<br>• BE has a 512-token limit and eight evaluated languages<br>• BI regex scanner holds two injection phrases: see C3<br>• NVIDIA garak, heuristic and Meta results are vendor-reported, not comparable<br>Refs: BF R4, BE R8, BF R8, AG R2, AV R8, F R5, BE R6, BE R2, BI R2, 3c Published results, 3j (f) licences, gating and terms |
| C11 Prompt-injection detection in model output, tool output and retrieved text | AW: Model Armor: Output-level prompt injection and jailbreak detection; BE: Prompt Guard 2: Input-level prompt-attack detection (jailbreak and injection); BF: LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner) | • Suggested: tool results and retrieved passages, with and without injected instructions<br>• Scripted model replies carrying instructions or jailbreak text<br>• CyberSecEval has 55 indirect cases that could seed injected passages<br>• Benign tool text such as logs, JSON, web pages needed<br>Refs: AW R7, BE R7, BF R7, BF R3, 3k Datasets, 3k Reuse | • Suggested: per text, injected or clean, under one agreed definition<br>• Direct or indirect label where seeded from CyberSecEval<br>• Definitions differ: AW names MCP tool errors; BE flags explicit override only<br>Refs: AW R2, BE R2, BF R2 | • Match flag with confidence level (AW)<br>• Label with score (BE); allow or block with reason (BF)<br>• Latency; error<br>Refs: AW R5, BE R5, BF R5 | • True-positive, false-positive, false-negative rates at each decision point<br>• AUPRC and sweeps only for scored outputs: BE, BF<br>• AW gives a confidence level, not a score<br>• Latency; BE and BF truncate beyond 512 tokens<br>Refs: AW R5, BE R5, BF R5, BF R6 | • Suggested harness submitting text on the tool, retrieval or response path<br>• AW: regional response method with a template, or gateway setting<br>• BF: llamafirewall with the TOOL role and PromptGuard scanner<br>• BE: gated weights loaded with Transformers; no service<br>Refs: AW R7, BF R7, BE R7, 3h (b) integration paths, 3j (c) roles, use cases and default scanner map | • AW scope conflicts: overview says responses, templates page says prompts only<br>• BF runs the BE model: not independent<br>• BE behaviour on tool and retrieved text is untested by Meta<br>• BE, BF on model replies: undocumented; Meta names user and tool text<br>• AW three-word rule for responses unknown; Google AUP clause open item<br>• Llama 4 licence gate and testing question open for BE, BF<br>• Hidden-character check is in C3; NeMo chunk filtering is C16<br>Refs: AW R1, BF R4, BE R3, BF R3, BE R8, AW R8, BF R8, 3j (f) licences, gating and terms |
| C12 Input-level off-topic detection against a policy or system prompt | I: NeMo Guardrails: Input-level topic control; AC: GovTech Sentinel: Off-topic prompt detection against the system prompt | • Pairs of (allowed-topic policy or system prompt, user message)<br>• On-topic, off-topic and borderline messages under several policies of different breadth<br>• English baseline<br>• NeMo example policies in sample_abc eval config can seed one policy<br>Refs: I R7, AC R7, AC R6, 3c Datasets | • Per pair: on-topic or off-topic label relative to stated policy<br>• Written by the test author per policy<br>• Same policy text must be rendered into each product's format<br>Refs: I R2, AC R2, AC R6 | • Decision (blocked or on-topic flag)<br>• Score for AC<br>• Latency; error<br>Refs: I R5, AC R5 | • True-positive rate (off-topic caught), false-positive rate (on-topic blocked)<br>• False-negative rate at each decision point; latency<br>• AUPRC and sweeps only for AC<br>• I returns a verdict<br>• NeMo reports no topic-control accuracy<br>Refs: I R5, 3c Published results | • Shared harness injecting policy per case; adapters, result format, recorder, evaluator<br>• I: NeMo input rail, topic_control model entry, policy prompt<br>• I: NemoGuard Topic Control endpoint<br>• AC: Sentinel beta key, or self-hosted bi-encoder or cross-encoder<br>• NeMo eval run could drive I on LLMRails<br>• Eval rail topical tests dialog, not topic control<br>Refs: I R6, I R7, 3e (d) access paths, 3c Tools | • I takes explicit allowed-topics policy; AC infers relevance from system prompt<br>• AC is English only; I language coverage not stated<br>• Multi-turn use unknown for I, unclear for AC<br>• AC served variant undisclosed; parameter name conflicts<br>• Scope conflicts (off-topic); I has no published accuracy<br>• Sentinel is closed beta<br>Refs: I R4, I R6, AC R1, AC R6, I R8, AC R3, AC R4, 3e (b) catalogue, 3c Published results |
| C13 Image content-safety classification of input (user-supplied images) | X: Llama Guard: Multimodal (image + text) content-safety classification; AS: Sensitive Data Protection: Image safety classification (sexual and violent content) | • Suggested: lawful, approved images labelled by category, with a fixed neutral text<br>• Real and AI-generated images; benign near-misses<br>• X needs a text part; AS takes image bytes only<br>Refs: X R7, AS R7, X R6, AS R6 | • Suggested: per image, safe or unsafe label from human review<br>• Harmonised subset: sexual content and violence; other categories reported apart<br>• Categories differ: X S1 to S13; AS three image categories<br>Refs: X R2, AS R2, AS R7 | • First-line verdict and category codes (X)<br>• Likelihood bucket per finding (AS)<br>• Latency; error<br>Refs: X R5, AS R5 | • True-positive, false-positive, false-negative rates at each decision point<br>• Per-category recall on the harmonised subset<br>• AS sweep over likelihood buckets; X has no score or threshold<br>• Latency per call<br>Refs: X R5, AS R5, AS R7 | • Suggested harness: image loader, adapters, label store, recorder, evaluator<br>• X: GPU host serving Llama Guard 4 or 3-11B-Vision, with processor<br>• AS: Google Cloud project, DLP API, image-scanning location such as Singapore<br>• AS request names the three image context detectors<br>Refs: X R4, X R7, AS R7, AS R6, 3d (a) variant table, 3g (f) region and availability | • X is not for image-only input; fixed neutral text is needed<br>• AS judges the whole image; X judges image and text together<br>• X judges request hazard; AS judges what the image shows<br>• Categories differ; AS models trained mainly on real-world images<br>• EU licence clause may apply to X<br>• AS on generated images has no comparator: X response side is C24<br>• Google AUP limits on explicit test images apply to AS<br>• AS accuracy and thresholds are open questions<br>Refs: X R3, X R4, X R7, AS R1, AS R3, AS R4, AS R7, AS R8, X R8 |
| C14 Sensitive-data detection and masking in tables and records | AL: Presidio: PII detection and anonymisation in structured data (tables and JSON); AN: Sensitive Data Protection: Sensitive-data detection in text (infoType inspection); AP: Sensitive Data Protection: Sensitive-data masking and de-identification in text | • Suggested: small tables with known PII columns and clean columns<br>• Cells with mixed content, odd column names and empty values<br>• JSON objects with known PII keys (AL only)<br>• Records could stand for retrieved rows or parsed tool output<br>Refs: AL R7, AN R6, AP R6, AL R3 | • Suggested: per cell, PII entity type or none<br>• Per table, expected column-to-entity map (AL; derived for AN)<br>• Expected masked table: PII cells changed, clean cells untouched<br>• Harmonised entity subset scored; other types reported apart<br>Refs: AL R2, AL R5, AN R2, AP R5 | • Transformed table or object (AL, AP)<br>• AL column-to-entity map, no per-cell findings or scores<br>• AN findings with likelihood and position<br>• AP change summary; latency; error<br>Refs: AL R5, AN R5, AP R5 | • Cell-level detection rate and false-positive rate on clean cells<br>• Column-map accuracy where a map exists (AL; derived for AN)<br>• Masking correctness per cell: PII changed, clean unchanged<br>• Latency and throughput on larger tables<br>Refs: AL R7, AL R8, AN R5, AP R5 | • Suggested harness: table loader, adapters, cell scorer, recorder, evaluator<br>• AL: presidio-structured package with the English spaCy model; no account<br>• AN, AP: Google Cloud project, DLP User role, table content item<br>• SDP request caps: 0.5 MB and 50,000 table values<br>Refs: AL R7, AN R7, AP R7, 3f (d) integration paths, 3g (a) method and component catalogue, 3g (e) limits, quotas and pricing | • AL maps columns by sampling; AN, AP read each cell<br>• AL is alpha (0.0.8); SDP is a managed API<br>• No SDP column documents JSON input; AL does<br>• Table use is a content-item mode of AN, AP<br>• Free text inside cells is future work for AL<br>• AL shares Analyzer and Anonymizer backends with C1<br>Refs: AL R1, AL R4, AL R2, AN R1, AP R1, AL R8, AN R3 |
| C15 Dialog-level conversational flow control | J: NeMo Guardrails: Dialog-level conversational flow control | • Multi-turn conversations and paraphrased user messages<br>• Around a reference Colang configuration we author<br>• NeMo seeds: chit-chat (76 intents, 226 test samples)<br>• Also banking77 (77 intents, 231 test samples)<br>• Both come with conversion scripts<br>Refs: J R6, J R7, 3c Datasets | • Expected user intent, next step and bot reply per turn<br>• Under the authored flows<br>Refs: J R2, J R5, 3c Datasets | • Matched intent, next step, bot message<br>• Latency, number of LLM calls, error<br>Refs: J R5, J R8 | • Intent-matching accuracy<br>• Bot-intent and bot-message accuracy as NeMo reports them (nemoguardrails eval rail topical)<br>• False-refusal rate on on-path messages<br>• Latency, LLM calls<br>Refs: 3c Tools | • Harness, authored Colang configuration, LLMRails engine (not IORails)<br>• Main LLM, embedding model, recorder<br>• NeMo eval rail topical can be reused as is for J<br>• Runs on LLMRails only<br>Refs: J R7, 3c Tools, 3b rail types | • Single-product: no comparator among the ten products yet<br>• Evaluates NeMo intent matching over our own configuration<br>• Not a vendor detector<br>• Output is a reply, not pass or fail<br>• LLMRails only<br>• Colang 1.0 versus 2.x unresolved<br>• Published accuracies NeMo-reported on older models<br>Refs: J R6, J R5, J R4, J R8, 3c Published results |
| C16 Retrieval-level chunk filtering | M: NeMo Guardrails: Retrieval-level chunk filtering | • Small knowledge base with clean chunks<br>• Seeded bad chunks: PII, forbidden pattern, padding<br>• NeMo provides no retrieval test data<br>Refs: M R7, 3c Reuse | • Per chunk and per configured check<br>• Outcome: kept, rewritten, blanked or turn blocked<br>Refs: M R2, M R5 | • Chunks passed to the prompt, block outcome<br>• Rewritten text, latency, error<br>Refs: M R5, M R7 | • Detection rate and false-positive rate on seeded chunks, per check type<br>• Chunk-removal correctness; latency<br>Refs: M R5, 3c Tools | • Harness, knowledge base or custom retrieval step<br>• NeMo config with rails.retrieval.flows, LLMRails engine<br>• Stub LLM; log of chunks sent to the prompt<br>• NeMo eval run does not model retrieval<br>Refs: M R7, 3c Tools | • Single-product: no comparator among the ten products yet<br>• Checks joined chunk text and blanks all chunks<br>• Docs say one chunk<br>• LLMRails only<br>• Reuses PII, regex, bloat and HF classifier backends on retrieved text<br>• NeMo publishes no retrieval results<br>Refs: M R4, M R8, 3b rail types, M R3, 3c Published results |
| C17 Context-bloat detection on input | P: NeMo Guardrails: Context-bloat detection (input) | • Normal text, text over the size cap, repeated characters<br>• Repeated phrases, low-entropy filler<br>• Legitimate long pastes such as logs or code<br>• No NeMo dataset<br>Refs: P R7, P R8, 3c Reuse | • Per input and configured thresholds: expected outcome<br>• Outcome: block, truncate or allow, authored from thresholds<br>• Plus legitimate or abusive label for long pastes<br>Refs: P R2, P R5 | • Outcome: block, truncated message, allow<br>• Reported metrics, latency, error<br>Refs: P R5 | • Detection rate on padded inputs<br>• False-positive rate on legitimate long inputs<br>• Truncation correctness; latency<br>Refs: P R5, 3c Published results | • Harness, NeMo input rail config, stub LLM, recorder<br>• Each action tried in turn; both engines<br>• NeMo eval run could drive it on LLMRails<br>Refs: P R4, P R7, 3c Tools | • Single-product: no comparator among the ten products yet<br>• Statistical checks with no model<br>• Thresholds we set<br>• Warn action hides detections from the caller<br>• Non-English behaviour unverified<br>• No NeMo results published<br>Refs: P R4, P R5, P R8, 3c Published results |
| C18 Output-level injection detection | O: NeMo Guardrails: Output-level injection detection | • Scripted bot outputs with code, SQL, template and cross-site scripting payloads<br>• Plus benign code answers<br>• Garak xss and malwaregen probe families may seed payloads<br>• NeMo has no injection dataset<br>Refs: O R7, 3c Red-teaming, 3c Reuse | • Per output: payload class (code, SQL injection, template, XSS) or benign<br>• Expected action: block or strip<br>Refs: O R2, O R5 | • Outcome: block, stripped text, allow<br>• Matched rule names, latency, error<br>Refs: O R5 | • Detection rate per payload class<br>• False-positive rate on benign code answers<br>• Stripping correctness for omit; latency<br>Refs: O R5, 3c Published results | • Harness, scripted outputs<br>• NeMo output rail with injection config and yara-python, recorder<br>• Both engines (injection detection)<br>• NeMo eval run could drive it on LLMRails<br>Refs: 3b surface table, 3c Tools | • Single-product: no comparator among the ten products yet<br>• Fixed YARA rule set; defence-in-depth, not a standalone control<br>• Docs and code disagree on the default action<br>• Possible false positives on legitimate code<br>• No NeMo results published beyond garak<br>Refs: O R2, O R4, O R6, O R8, 3c Published results |
| C19 Tool-call validation | Q: NeMo Guardrails: Tool-call validation | • Declared tool definitions plus scripted model responses<br>• Cases: valid calls, unknown tool names, bad arguments<br>• Arguments to a no-parameter tool, invalid schemas<br>• No NeMo dataset<br>Refs: Q R7, 3c Reuse | • Per call: structurally valid or invalid, with expected reason<br>• Deterministic from the declared schema<br>Refs: Q R2, Q R5 | • Allow or block; refusal text or error payload<br>• Block reason, latency, error<br>Refs: Q R5 | • Block accuracy: true-positive and false-positive rates against schema validity<br>• Reason correctness<br>• Latency<br>Refs: Q R5, 3c Published results | • Harness sending OpenAI-format requests with tools<br>• Scripted or real model emitting tool calls<br>• NeMo IORails config with tool call validation, recorder<br>• No tool execution<br>• NeMo eval runners cannot be reused: no tool fields, IORails untested<br>Refs: Q R6, Q R7, 3c Engine coverage | • Single-product: no comparator among the ten products yet<br>• Structural allowlist and JSON Schema check only<br>• Does not judge whether an allowed call is harmful<br>• Built-in validator is IORails only, OpenAI format only<br>• LLMRails needs custom flows<br>• Model-based tool safety exists on develop only<br>• No NeMo results published<br>Refs: Q R2, 3b surface table, Q R4, 3c Published results |
| C20 Tool-result validation | R: NeMo Guardrails: Tool-result validation | • Conversations with an assistant turn carrying tool calls and tool messages<br>• Cases: valid, missing ID, duplicate ID, wrong name, non-string content<br>• No NeMo dataset<br>Refs: R R7, 3c Reuse | • Per conversation: structurally consistent or not, with expected reason<br>• Deterministic<br>Refs: R R2, R R5 | • Allow or block; refusal text or error payload<br>• Latency, error<br>Refs: R R5 | • Block accuracy: true-positive and false-positive rates against structural validity<br>• Latency<br>Refs: R R5, 3c Published results | • Harness sending conversations with tool messages<br>• NeMo IORails config with tool result validation<br>• Stub main LLM, recorder; no tool execution<br>• NeMo eval runners cannot be reused: IORails untested, no tool fields<br>Refs: R R6, R R7, 3c Engine coverage | • Single-product: no comparator among the ten products yet<br>• Structural linkage only: no response schema<br>• No content-safety or injection check on result text<br>• Plain input rails do not see tool results<br>• IORails only for built-ins<br>• Model-based result judge on develop only<br>• No NeMo results published<br>Refs: R R2, R R4, R R3, 3b surface table, 3c Published results |
| C21 Execution-level custom action rails | U: NeMo Guardrails: Execution-level custom action rails | • Action calls with allowed and blocked arguments<br>• Trusted and untrusted results<br>• Triggered through flows we author<br>• No NeMo dataset<br>Refs: U R6, U R7, 3c Reuse | • Per case: expected allow, block or transform decision<br>• Defined by our own test logic<br>Refs: U R2, U R5 | • Action call log, rail decision (allow, block, transform)<br>• Final reply, latency, error<br>Refs: U R5, U R7 | • Agreement of decision with authored expectation<br>• False-positive and false-negative rates of authored checks<br>• Latency<br>Refs: U R5, 3c Tools | • Harness, NeMo configuration with test actions and flows we write<br>• Scripted calls or a main LLM<br>• LLMRails engine, recorder<br>• nemoguardrails eval run can observe execution rails only through final reply<br>Refs: U R7, 3c Tools | • Single-product: no comparator among the ten products yet<br>• No built-in detector<br>• Only wrapper mechanism and our test logic are evaluated<br>• Output format not fixed<br>• Documented rails.execution key has no backing field in v0.24.1<br>• LLMRails only<br>• No NeMo results published<br>Refs: U R1, U R4, U R5, 3b rail types, 3c Published results |
| C22 Grounded fact-checking of output | S: NeMo Guardrails: Grounded fact-checking (output) | • Triples of question, retrieved evidence and reply<br>• Supported and unsupported<br>• NeMo seeds: MS MARCO triples with LLM-made negatives<br>• Also a 1-item sample (factchecking/sample.json)<br>• Negatives depend on the generating LLM<br>Refs: S R7, 3c Datasets, 3c Reuse | • Per reply: supported or unsupported<br>• Judged against the supplied evidence<br>Refs: S R2, S R5 | • Decision<br>• 0 to 1 support score for self-check and AlignScore<br>• Latency, error<br>Refs: S R5 | • True-positive, false-positive, false-negative rates at the decision point<br>• Positive, negative, overall accuracy, ms per fact as NeMo reports<br>• Tool: nemoguardrails eval rail fact-checking<br>• AUPRC from scores for self-check and AlignScore only<br>Refs: 3c Tools | • Harness, small knowledge base or injected chunks<br>• NeMo config on LLMRails, check_facts set by custom Colang flow<br>• Judge LLM or AlignScore server, recorder<br>• NeMo eval rail fact-checking bypasses the rail pipeline<br>• Tests the self-check prompt only<br>Refs: S R6, S R7, 3c Tools | • Single-product: no comparator among the ten products yet<br>• Needs retrieved evidence<br>• Fixed 0.5 threshold for self-check and AlignScore<br>• LLMRails only<br>• Vendor backends return different output shapes<br>• NeMo published accuracies use retired models and 100 triples<br>• Sentinel hallucination id is Planned, not available<br>Refs: S R2, S R5, 3b surface table, 3c Published results, 3e (b) catalogue |
| C23 Self-consistency hallucination detection of output | T: NeMo Guardrails: Self-consistency hallucination detection (output) | • Prompts with stable answers<br>• Prompts the main LLM tends to invent answers for<br>• Run through a live main LLM so resampling is possible<br>• NeMo seed: 15 false-premise questions, unlabelled, smoke test only (hallucination/sample.txt)<br>Refs: T R7, 3c Datasets, 3c Reuse | • Per prompt and reply: hallucinated or not<br>• From reference answers or human review<br>• Consistent but wrong answers cannot be caught<br>Refs: T R2 | • Allow or block; is_hallucination flag; warning text<br>• Latency, number of LLM calls, error<br>Refs: T R5, T R8 | • True-positive, false-positive, false-negative rates at the decision point<br>• Added latency and calls<br>• No score, so no AUPRC<br>• NeMo reports only the percentage flagged (nemoguardrails eval rail hallucination)<br>Refs: 3c Tools | • Harness, NeMo config on LLMRails<br>• Hallucination flag set by custom Colang flow<br>• Main LLM allowing temperature 1.0, recorder<br>• nemoguardrails eval rail hallucination: no ground truth, bypasses pipeline<br>Refs: T R6, T R7, 3c Tools | • Single-product: no comparator among the ten products yet<br>• Results depend on random resampling<br>• If every extra generation fails, reply is allowed<br>• LLMRails only<br>• Supported providers unclear<br>• Adds at least two LLM calls<br>• NeMo runner flags any "no" in judge text<br>Refs: T R4, T R8, 3b surface table, 3c Tools |
| C24 Multimodal content-safety classification of output (image and text prompt with text response) | X: Llama Guard: Multimodal (image + text) content-safety classification | • Image-plus-text prompts with canned or generated text response<br>• Benign and harmful, run as response checks<br>Refs: X R7, X R6 | • Per pair: response safe or unsafe<br>• Plus category S1 to S13<br>Refs: X R2, X R7 | • First-line verdict, category codes<br>• Latency, error<br>Refs: X R5 | • True-positive, false-positive, false-negative rates, precision and F1<br>• Per-category recall<br>• No score or threshold documented<br>Refs: X R5 | • One GPU host serving Llama Guard 4 and Llama Guard 3-11B-Vision<br>• With processor, response template, verdict parser, logger<br>Refs: X R4, X R7, 3d (a) variant table | • Single-product: no comparator among the ten products yet<br>• Same limits as C13<br>• Response checks are stronger than prompt checks<br>• LG4 does not say whether image content in a response is classified<br>• 3-11B-Vision response F1 and LG4 figures come from different sets<br>• Input side is C13 (with AS)<br>Refs: X R3, X R6, X R5 |
| C25 Code-interpreter abuse classification (S14) | Y: Llama Guard: Code-interpreter and tool-use abuse classification | • Agent turns containing code or search-result text<br>• With the preceding user turn<br>• Cases: S14 abuse, near-boundary benign code, benign code<br>• Possible seed: CyberSecEval interpreter set, 500 prompts in five attack types<br>Refs: Y R7, 3k Datasets | • Per item: S14 unsafe or safe label<br>• With the expected S14 code<br>Refs: Y R2, Y R5 | • Verdict, category codes (whether S14 appears)<br>• Latency, error<br>Refs: Y R5 | • S14 true-positive, false-positive, false-negative rates on the verdict<br>• Compare serialisation variants<br>• No documented threshold<br>Refs: Y R4 | • Harness, GPU serving of Llama Guard 3-8B and Llama Guard 4<br>• 3-1B as negative control<br>• Response template with S14, verdict parser, logger<br>Refs: Y R7, 3d (a) variant table | • Single-product: no comparator among the ten products yet<br>• S14 exists only in LG3-8B, its INT8 build and LG4<br>• Tool-call and tool-output serialisation undefined by Meta<br>• LG4 has no S14 metric<br>• OGX omits S14 for LG4<br>• Llama Guard does not detect injection<br>Refs: 3d (a) variant table, Y R1, Y R3, Y R6, Y R4, 3d (c) integration paths, Y R2 |
| C26 Custom-policy classification of input (prompts) | Z: Llama Guard: Custom-policy classification | • User prompts labelled under a small custom taxonomy<br>• E.g. three categories: positives, negatives, near-boundary items<br>• Variants: names only, descriptions, few-shot, excluded-category<br>Refs: Z R7 | • Per prompt: category label under author-defined taxonomy<br>• Plus expected flip when a default category is excluded<br>Refs: Z R2, Z R5 | • Verdict; codes keyed to the supplied categories<br>• Latency, error<br>Refs: Z R5 | • Per-category true-positive and false-positive rates<br>• Rate of verdict change under exclusion or replacement<br>• No score or threshold documented<br>Refs: Z R5, Z R8 | • Harness, taxonomy builder, verdict parser<br>• GPU serving of Llama Guard 3-1B, 3-11B-Vision and 4 (templates take categories)<br>• 3-8B via the cookbook builder<br>Refs: Z R4, Z R7, 3d (a) variant table | • Single-product: no comparator among the ten products yet<br>• 3-8B template ignores categories<br>• No Meta page shows LG4 custom usage<br>• No published quality results beyond the LG1 paper<br>• Custom key formats untested<br>• Response side is C27<br>Refs: Z R4, 3d (a) variant table, Z R8, Z R2, Z R5 |
| C27 Custom-policy classification of output (responses) | Z: Llama Guard: Custom-policy classification | • Prompt-response pairs labelled under the custom taxonomy<br>• Same variants: names-only, description, few-shot, exclusion<br>Refs: Z R7 | • Per response: category label under author-defined taxonomy<br>• Plus expected flip when a default category is excluded<br>Refs: Z R2, Z R3 | • Verdict; codes keyed to the supplied categories<br>• Latency, error<br>Refs: Z R5 | • Per-category true-positive and false-positive rates<br>• Rate of verdict change under exclusion or replacement<br>• No score or threshold documented<br>Refs: Z R5, Z R8 | • Harness, taxonomy builder, response template, verdict parser<br>• GPU serving of Llama Guard 3-1B, 3-11B-Vision and 4<br>• 3-8B via the cookbook builder<br>Refs: Z R4, Z R7, 3d (a) variant table | • Single-product: no comparator among the ten products yet<br>• Same limits as C26<br>• Response classification needs both turns<br>• Compare only within Llama Guard<br>• Input side is C26<br>Refs: Z R4, Z R8, Z R3, Z R2 |
| C28 System-prompt leakage detection | AD: GovTech Sentinel: System-prompt leakage detection | • Pairs of system prompt and model output<br>• Leaking outputs: verbatim, word-substituted, paraphrased, reordered, obfuscated, partial<br>• Non-leaking outputs that share vocabulary<br>Refs: AD R7 | • Per pair: leak or no leak<br>Refs: AD R2, AD R5 | • Score from 0 to 1<br>• Latency, error<br>Refs: AD R5 | • True-positive, false-positive, false-negative rates at a stated threshold<br>• Threshold sweep and AUPRC from the score<br>• Latency<br>Refs: AD R5, AD R8 | • Harness, labelled pairs<br>• Sentinel beta key from a Singapore IP<br>• Script calling /validate with system prompt in messages<br>Refs: AD R6, AD R7, 3e (d) access paths | • Single-product: no comparator among the ten products yet<br>• Model undisclosed; no published evaluation<br>• 0.95 guidance would miss a documented 0.909 clear leak<br>• messages versus system_prompt conflict<br>• Only a demo Space exists, needing an Azure OpenAI key<br>• Closed beta<br>Refs: AD R4, AD R2, AD R5, AD R6, 3e (d) access paths |
| C29 Refusal detection | AE: GovTech Sentinel: Refusal detection | • Pairs of user prompt and model reply<br>• Cases: hard refusal, soft refusal with alternative, refusal wrapped in help<br>• Safe completion of risky request, full answer, benign decline<br>• Litmus refusal-based tests could suggest themes; it publishes no prompts<br>Refs: AE R7, 3n Reuse | • Per pair: human-labelled refusal class<br>• Classes: refused, partial, answered<br>Refs: AE R2, AE R5 | • Score, class label, reasoning text<br>• Latency, error<br>Refs: AE R5 | • Agreement with human labels (accuracy, refusal precision and recall)<br>• Over-refusal detection rate<br>• Repeat-run stability; latency<br>Refs: AE R5, AE R8 | • Harness, human-labelled pairs<br>• Sentinel beta key from a Singapore IP<br>• Script calling /validate with user_prompt<br>Refs: AE R6, AE R7, 3e (d) access paths | • Single-product: no comparator among the ten products yet<br>• Positioned as analytics, not a block control<br>• Model, rubric and label set undisclosed<br>• user_prompt required or not is a docs conflict (refusal)<br>• No accuracy figures published<br>Refs: AE R1, AE R2, AE R4, AE R6, 3e (b) catalogue, AE R8 |
| C30 Document screening of uploaded files | BB: Model Armor: Document screening (PDF, CSV, text and Office files) | • Suggested: PDF, CSV, text, Office files with planted injection, fake data, URLs<br>• One file per type, from 69 bytes to 4 MB<br>• Clean files as controls; synthetic content only<br>Refs: BB R7, BB R6 | • Suggested: per file, expected match for each enabled filter<br>• Planted items are known, so labels are deterministic<br>• Expected outcome for oversize or tiny files: skipped or rejected<br>Refs: BB R2, BB R5 | • Per-filter result: execution state and match state<br>• URL positions only for plain text<br>• Skipped or rejected status; latency; error<br>Refs: BB R5 | • Detection rate per filter and file type<br>• False-positive rate on clean files<br>• Skip and reject behaviour at the size limits<br>• Latency by file size<br>Refs: BB R5, BB R6 | • Suggested harness: file generator, base64 encoder, adapter, recorder, evaluator<br>• Model Armor template in a full-support region with the wanted filters<br>• Direct API prompt method, with the file type set by hand<br>• Model Armor user role<br>Refs: BB R6, BB R7, 3h (b) integration paths | • Single-product: no comparator among the ten products yet<br>• Text extractor undisclosed; scans and layout handling unknown<br>• Embedded images in files are not screened, though one page says otherwise<br>• Only the direct API and Gemini Enterprise accept documents<br>• Response-side documents are undocumented<br>• Cloak (BL) and SDP (AN) also take files: not compared here<br>• Google AUP testing clause not recorded for BB: open item<br>Refs: BB R2, BB R3, BB R4, BB R8, 3h (b) integration paths |
| C31 Input-level malicious URL detection | AZ: Model Armor: Input-level malicious URL detection | • Suggested: user prompts with known-bad and benign URLs<br>• Shortened, obfuscated, redirecting and URL-encoded links<br>• Prompts with more than 256 URLs; benign look-alike domains<br>Refs: AZ R7, AZ R2 | • Suggested: per URL, malicious or benign label<br>• Labels would need an independent URL reputation source: not chosen<br>Refs: AZ R7, AZ R4 | • Match flag and matched URLs, with ranges for plain text<br>• Execution state; latency; error<br>Refs: AZ R5 | • True-positive and false-positive rates per URL<br>• Behaviour past the 256-URL scan limit<br>• Latency per call<br>Refs: AZ R5, AZ R2 | • Suggested harness: prompt loader, adapter, recorder, evaluator<br>• Model Armor template with the URL filter on, in a full-support region<br>• Regional sanitize-user-prompt endpoint; no confidence setting exists<br>Refs: AZ R7, AZ R6, 3h (d) locations and feature availability | • Single-product: no comparator among the ten products yet<br>• Reputation source and method are not disclosed<br>• On or off only; no confidence level<br>• Unavailable in limited-support regions with data residency enforced<br>• Only the first 256 URLs are scanned; encoded URLs not decoded<br>• Google AUP testing clause is an open item<br>• Response side is C32<br>Refs: AZ R4, AZ R5, AZ R2, AZ R8, 3h (d) locations and feature availability |
| C32 Output-level malicious URL detection | BA: Model Armor: Output-level malicious URL detection | • Suggested: model responses with known-bad and benign URLs, scripted<br>• Shortened, obfuscated and URL-encoded links; streamed chunks<br>• Responses with more than 256 URLs<br>Refs: BA R7, BA R8 | • Suggested: per URL, malicious or benign label<br>• Labels would need an independent URL reputation source: not chosen<br>Refs: BA R7, BA R4 | • Match flag and matched URLs, with ranges for plain text<br>• Execution state; latency; error<br>Refs: BA R5 | • True-positive and false-positive rates per URL<br>• Behaviour past the 256-URL scan limit and across chunks<br>• Latency per call<br>Refs: BA R5, BA R8 | • Suggested harness: scripted responses, adapter, recorder, evaluator<br>• Model Armor template with the URL filter on, in a full-support region<br>• Regional sanitize-model-response endpoint<br>Refs: BA R7, BA R6, 3h (d) locations and feature availability | • Single-product: no comparator among the ten products yet<br>• Same limits as C31: method undisclosed, on or off only<br>• Unavailable in limited-support regions with data residency enforced<br>• Docs examples send no user prompt<br>• Google AUP testing clause is an open item<br>• Input side is C31<br>Refs: BA R4, BA R3, BA R8, 3h (d) locations and feature availability |
| C33 Trace-level agent goal-hijacking detection | BG: LlamaFirewall: Trace-level agent goal-hijacking detection (AlignmentCheck) | • Suggested: traces of one user request plus agent actions, half hijacked<br>• Indirect injection inside tool results that pushes the agent off-goal<br>• Legitimate but unusual actions as benign controls<br>• Synthetic traces suggested, since traces leave the machine<br>Refs: BG R7, BG R2, BG R3 | • Suggested: per action, aligned or hijacked relative to the user request<br>• Labels authored together with each trace<br>Refs: BG R2, BG R7 | • Score 1.0 or 0.0; decision human-in-the-loop required or allow<br>• Never a block decision<br>• Latency; error; judge model reachability<br>Refs: BG R5 | • True-positive and false-positive rates at the decision<br>• Judge stability across repeat runs<br>• Latency, context limits and Together cost per trace<br>Refs: BG R5, BG R8 | • Suggested harness building traces, with an assistant-role scanner<br>• llamafirewall on Python 3.10 or later<br>• Together API key and a judge model Together serves<br>Refs: BG R6, BG R7, 3j (b) LlamaFirewall scanner catalogue, 3j (c) roles, use cases and default scanner map | • Single-product: no comparator among the ten products yet<br>• Meta labels it experimental; figures are from Meta's own benchmark<br>• Code default model is listed as removed from Together serverless<br>• Model and endpoint cannot be set through the constructor<br>• Traces go to a third-party API; Together terms are an open item<br>• Not a content filter; treats doubtful actions as aligned<br>Refs: BG R1, BG R4, BG R5, BG R6, BG R8, 3j (f) licences, gating and terms |
| C34 Output-level insecure-code detection in model responses | BH: LlamaFirewall: Output-level insecure-code detection (CodeShield scanner); BJ: Code Shield: Output-level insecure-code detection (LLM-generated code) | • Suggested: scripted model outputs with insecure and benign code answers<br>• Possible seeds: CyberSecEval code prompts<br>• Benign code answers would be needed to test false positives<br>Refs: BH R7, BJ R7, 3k Reuse | • Suggested: per output, insecure or benign, with CWE class<br>• Independent labels would be needed; CyberSecEval ground truth is Code Shield itself<br>Refs: BH R2, BJ R2, 3k Reuse | • BH: block or allow, score 1.0 or 0.0, issue list in reason<br>• BJ: insecure flag, issue list, block, warn or ignore<br>• Matched rule, CWE and line where given<br>• Latency; error<br>Refs: BH R5, BJ R5 | • Detection rate per CWE class; false-positive rate on benign code<br>• Agreement between the scanner and the library on the same text<br>• Latency by language<br>Refs: BH R5, BJ R5 | • Suggested harness: scripted outputs, adapters, recorder, evaluator<br>• BH: llamafirewall with codeshield and Semgrep; BJ: pip codeshield and Semgrep<br>• No key, model or gated access for BH or BJ<br>Refs: BH R7, BJ R7, 3j (d) Code Shield language and analyzer matrix | • Single-product: no comparator among the ten products yet<br>• BH runs the BJ engine: one engine through two surfaces<br>• BH scans whole messages; BJ takes a code string<br>• BH and BJ language lists conflict: seven or eight<br>• Code Shield is not a taint-flow analyser; Semgrep licence recorded<br>• NeMo O checked: it flags payloads, not coding practice<br>Refs: BH R4, BH R3, BJ R3, BJ R2, BJ R8, O R2, 3j (f) licences, gating and terms |

## B. Rationale per group

Criteria are the docx section 4 tests: same type of test inputs, same ground truth, same or comparable metrics, common minimum architecture. A tick means the members meet it; a cross marks the criterion that keeps a candidate out. Input and output are separate groups (R002); a function that takes any string is listed in each side it applies to. References are sheet 3 column and row (for example AH R5) or inventory/evaluation sheet sections.

### C1 Input-level PII and sensitive-data detection and masking in text

Functions: E, K, AF, AH, AI, AN, AP, AX, BL (9 functions)

- Test inputs ✓: Single user messages carrying labelled PII; every member accepts a string (E R3, K R3, AF R3, AH R3, AI R3, AN R3, AP R3, AX R3, BL R3).
- Ground truth ✓: Entity type and span per text, plus expected masked text; entity lists differ, so a harmonised subset is scored (E R2, K R2, AF R2, AH R2, AN R2, AX R2, BL R2).
- Comparable metrics ✓: Detection and false-positive rates per entity type, and masking correctness, are computable from every output shape (AH R5, AN R5, AP R5, AX R5, BL R5, E R5, K R5, AF R5).
- Minimum architecture ✓: A text harness with one adapter per product; no RAG, agent or tool execution is needed (E R7, K R7, AH R7, AN R7, AX R7, BL R7).
- Checked and left out: AO, AM, BM: authored detectors, so the ground truth is the author's rule set, not PII types (see C3). BI: fixed regex shapes, no entity spans (see C3). AJ, AQ, BN: ground truth is a restored value, not a masked one (see C5 and C6). AK, AR, BC: test inputs are images (see C7). AL: test inputs are tables (see C14; AN and AP also appear there). M: retrieval-level chunk checks, a different object and rail (see C16).
- Recorded open items (listed, not decided): Cloak Terms clause 3.4.7 (benchmarking) for BL: open (BL R8). Google AUP testing clause (R025) is recorded in Model Armor columns AT to AW, AZ, BA and BC, not in AN, AP or AX: whether it bears here is open. Sentinel (AF) is closed beta with Singapore-IP access (AF R7).

### C2 Output-level PII and sensitive-data detection and masking in text

Functions: E, L, AF, AH, AI, AN, AP, AY, BL (9 functions)

- Test inputs ✓: Model responses carrying labelled PII, scripted or generated; each member accepts a response string (E R3, L R3, AF R3, AH R3, AI R3, AN R3, AP R3, AY R3, BL R3).
- Ground truth ✓: Same entity and span labels as C1, plus the final user-visible text (L R5, AY R2, AF R3).
- Comparable metrics ✓: Same detection, false-positive and masking measures as C1 (AH R5, AN R5, AY R5, L R5).
- Minimum architecture ✓: Scripted or stub-LLM responses into the same adapters; AY uses the response method (AY R7, L R7).
- Checked and left out: AG: generic Bedrock moderation, not a PII function (C8, C10). Reversible and image functions follow C5, C6 and C7.
- Recorded open items (listed, not decided): Cloak Terms clause 3.4.7 for BL: open (BL R8). Google AUP testing clause not recorded in AN, AP or AY: open.

### C3 Input-level rule-based pattern matching in text (regex, word lists, fixed rules)

Functions: E, N, AM, AO, BI, BK, BM (7 functions)

- Test inputs ✓: Strings that match or miss a defined rule; every member runs on any string (N R3, AM R3, AO R3, BI R3, BK R3, BM R3, E R3).
- Ground truth ✓: Expected match comes from the rule definition, so it is deterministic; BI and BK use their documented fixed rules (N R2, AM R2, AO R2, BI R2, BK R2, BM R2, E R4).
- Comparable metrics ✓: Exact agreement, false-positive and false-negative rates against the rules, and latency (N R5, AM R5, AO R5, BI R5, BK R5, BM R5).
- Minimum architecture ✓: A rule loader plus one adapter per product; no detection model is needed for N, BI or BK, and AM loads a spaCy model with its Analyzer (N R7, AM R7, BI R7, BK R7, AO R7).
- Checked and left out: AH: built-in recognizers whose truth is a PII type, not an authored rule (C1). BM LLM entity: a Beta few-shot model, not rule matching (BM R4). M: matches on chunks, a retrieval-level rail (C16).
- Recorded open items (listed, not decided): Cloak Terms clause 3.4.7 for BM: open (BM R8).

### C4 Output-level rule-based pattern matching in text (regex, word lists, fixed rules)

Functions: E, N, AM, AO, BI, BK, BM (7 functions)

- Test inputs ✓: Scripted responses that match or miss a rule; N has a separate output check, the others take any string (N R3, AM R3, AO R3, BI R3, BK R3).
- Ground truth ✓: Deterministic from the rule definitions (N R2, AM R2, AO R2, BK R2).
- Comparable metrics ✓: Exact agreement, false-positive and false-negative rates, latency (N R5, AM R5, AO R5, BI R5, BK R5).
- Minimum architecture ✓: Stub LLM with scripted text and the C3 adapters (N R7, 3c Tools).
- Checked and left out: Output-level PII masking is C2; payload scanning of output is C18 and code scanning is C34.
- Recorded open items (listed, not decided): Cloak Terms clause 3.4.7 for BM: open (BM R8).

### C5 Reversible tokenisation of text before the model (encrypt side)

Functions: AJ, AQ, BN (3 functions)

- Test inputs ✓: User messages with synthetic entities to tokenise before the model (AJ R3, AQ R3, BN R3).
- Ground truth ✓: Original value and span per entity; expected: no raw value left in the outgoing text (AJ R1, AQ R1, BN R1).
- Comparable metrics ✓: Residual-PII rate and token format conformity apply to all three (AJ R5, AQ R5, BN R5).
- Minimum architecture ✓: Harness plus key setup per product: caller key, KMS wrapped key, Secrets Manager secret (AJ R7, AQ R7, BN R7).
- Checked and left out: AI, AP, BL: one-way operators; there is nothing to restore (C1). AJ with AH: the Analyzer finds entities for AJ, so detection is C1.
- Recorded open items (listed, not decided): Cloak Terms clause 3.4.7 for BN: open (BN R8).

### C6 Restoring tokens in model output (decrypt side)

Functions: AJ, AQ, BN (3 functions)

- Test inputs ✓: Mock model replies that echo, edit or drop tokens, plus wrong-key cases (AJ R3, AQ R3, BN R3).
- Ground truth ✓: Expected restored text with original values; failure expectations are open (AJ R8, AQ R8, BN R8).
- Comparable metrics ✓: Restore exactness, partial-restore rate and failure handling (AJ R5, AQ R5, BN R5).
- Minimum architecture ✓: Harness replaying replies, same key handling as C5 (AJ R6, AQ R6, BN R6).
- Checked and left out: The encrypt side is C5: inputs and ground truth differ (docx section 4), and each product exposes separate encrypt and restore operations (AJ R3, AQ R8, BN R3).
- Recorded open items (listed, not decided): Cloak Terms clause 3.4.7 for BN: open (BN R8).

### C7 PII and sensitive-text detection and redaction in images

Functions: AK, AR, BC (3 functions)

- Test inputs ✓: Images carrying known text with labelled PII, plus clean images (AK R3, AR R3, BC R3).
- Ground truth ✓: Entity type and box per text item; clean images expect none (AK R2, AR R2, BC R2).
- Comparable metrics ✓: Per-entity detection, box overlap, residual PII after redaction (AK R5, AR R5, BC R5).
- Minimum architecture ✓: Image loader and one adapter per product; all use OCR then an analyser (AK R4, AR R4, BC R4).
- Checked and left out: AS: judges whole-image safety, not sensitive text (see C13). BB: files, whose embedded images are not screened (see C30). AR object detectors (faces, passports) have no counterpart in AK or BC and are reported apart.
- Recorded open items (listed, not decided): Preview features (AR faces, BC): synthetic data only (R025 ruling 2). Google AUP testing clause recorded for BC (BC R8) and not for AR: open.

### C8 Harmful-content classification of input (user prompts)

Functions: G, V, AA, AG, AT, BD (6 functions)

- Test inputs ✓: Single-turn user prompts, harmful and benign (G R3, V R3, AA R3, AG R3, AT R3, BD R3).
- Ground truth ✓: Binary harmful label per prompt; category mapping only where taxonomies overlap (G R2, V R2, AA R2, AG R2, AT R2, BD R2).
- Comparable metrics ✓: True-positive, false-positive and false-negative rates at each decision point; sweeps only where probabilities exist (AA R5, BD R5, AT R5).
- Minimum architecture ✓: Prompt harness with adapters: NeMo rail, GPU Llama Guard, Sentinel key, Google template, local LionGuard (G R6, V R7, AA R7, AT R7, BD R7).
- Checked and left out: AB, AV, BE, BF: prompt attacks, a different threat and label (C10). X, AS: image inputs (C13). Z: author-defined taxonomy (C26). Y: S14 abuse labels (C25). Litmus (3n) is an evaluation tool, not a column: its Undesirable Content test names could be a theme list only.
- Recorded open items (listed, not decided): Google AUP testing clause for AT: open (AT R8). BD embedder terms (OpenAI, Gemini, Gemma) and licence texts: open (BD R8). Sentinel closed beta (AA R7, AG R7).

### C9 Harmful-content classification of output (model responses)

Functions: H, W, AA, AU, BD (5 functions)

- Test inputs ✓: Model responses to benign and harmful prompts; H and W also need the prompt (H R3, W R3, AA R3, AU R3, BD R3).
- Ground truth ✓: Binary unsafe label judged on the response; category mapping where taxonomies overlap (H R2, W R2, AA R2, AU R2, BD R2).
- Comparable metrics ✓: Same rates as C8 at each decision point (H R5, W R5, AA R5, AU R5, BD R5).
- Minimum architecture ✓: Scripted-response harness with the C8 adapters on the response path (H R7, W R7, AU R7, BD R7).
- Checked and left out: AG: Sentinel lists it input only (AG R3). X: image-plus-text responses (C24). Z: custom taxonomy (C27).
- Recorded open items (listed, not decided): Google AUP testing clause for AU: open (AU R8). BD embedder terms: open (BD R8).

### C10 Input-level jailbreak and prompt-attack detection

Functions: F, AB, AG, AV, BE, BF (6 functions)

- Test inputs ✓: Single-turn jailbreak, injection and benign prompts (F R3, AB R3, AG R3, AV R3, BE R3, BF R3).
- Ground truth ✓: Binary attack or benign label under one agreed definition, though definitions differ (F R2, AB R2, AG R2, AV R2, BE R2, BF R2).
- Comparable metrics ✓: Rates at each decision point; AUPRC for scored outputs only (AB R5, BE R5, BF R5, AV R5).
- Minimum architecture ✓: Prompt harness with adapters: NeMo rail, Sentinel key, Google template, local Prompt Guard 2 and LlamaFirewall (F R7, AB R7, AV R7, BE R7, BF R7).
- Checked and left out: AW: output and tool side (C11). BG: needs the whole agent trace (C33). O: output payloads (C18). BI: two injection phrases only, in a rule-matching group (C3). AC: off-topic is a different label (C12). CyberSecEval (3k) and Garak are possible sources of attack examples, not columns.
- Recorded open items (listed, not decided): Llama 4 licence gate and use policy for BE and BF: attack-prompt testing question open (BE R8, BF R8). Google AUP testing clause for AV: open (AV R8). Sentinel closed beta (AB R7, AG R7).

### C11 Prompt-injection detection in model output, tool output and retrieved text

Functions: AW, BE, BF (3 functions)

- Test inputs ✓: Untrusted text from tools, retrieval or model replies, with and without injected instructions; BE and BF on model replies is undocumented (BE R3), and BF defaults to user and tool roles (AW R3, BE R3, BF R3).
- Ground truth ✓: Injected or clean per text under one definition (AW R2, BE R2, BF R2).
- Comparable metrics ✓: Rates at each decision point; AUPRC for BE and BF only (AW R5, BE R5, BF R5).
- Minimum architecture ✓: Harness that places text on the tool or response path; three adapters (AW R7, BE R7, BF R7).
- Checked and left out: AV: user-prompt side (C10). BK: hidden characters, a rule match (C3). BB: files (C30). M: NeMo chunk checks for configured patterns and PII, not injection (C16).
- Recorded open items (listed, not decided): Llama 4 licence gate for BE and BF: open (BE R8, BF R8). Google AUP testing clause for AW: open (AW R8).

### C12 Input-level off-topic detection against a policy or system prompt

Functions: I, AC (2 functions)

- Test inputs ✓: Pairs of allowed-topic policy and user message (I R6, AC R6).
- Ground truth ✓: On-topic or off-topic label relative to the stated policy (I R2, AC R2).
- Comparable metrics ✓: Off-topic caught and on-topic blocked rates; AUPRC for AC only (I R5, AC R5).
- Minimum architecture ✓: Harness that injects the policy per case into each product's format (I R7, AC R7).
- Checked and left out: No later product offers topic control: Model Armor lists no topic filter (AT R8 asks about topic enforcement). Z (custom-policy classification, C26 and C27) could carry an off-topic category, but its ground truth is an author-defined taxonomy and it has no system-prompt input (Z R2, AC R6).
- Recorded open items (listed, not decided): Sentinel closed beta (AC R7).

### C13 Image content-safety classification of input (user-supplied images)

Functions: X, AS (2 functions)

- Test inputs ✓: User-supplied images, with a fixed neutral text for X (X R6, AS R6).
- Ground truth ✓: (approximate) Safe or unsafe per image on a harmonised subset, sexual content and violence; X labels the hazard of the image-plus-text request and expects harmful-looking images with benign text to be ambiguous (X R2, X R7), while AS labels what the image depicts (AS R1, AS R2), so agreement on the subset is measured, not assumed.
- Comparable metrics ✓: Rates at the verdict; AS sweep over likelihood buckets (X R5, AS R5).
- Minimum architecture ✓: Image loader with two adapters: GPU Llama Guard host and a Google DLP project (X R7, AS R7).
- Checked and left out: BC: sensitive-data screening of images (C7); image safety through an SDP template is inferred only (BC R2) [Inferred], so BC could become a C13 member if that is confirmed. X response side (C24) judges the response text, which AS cannot score. AS output side: AS R3 says the same call scores model-generated images; by the C7 reasoning (no direction flag, test inputs do not differ) it stays in C13 with no output-side row.
- Recorded open items (listed, not decided): EU licence clause for X (X R8). Google Cloud AUP limits on explicit or violent test images for AS: which images are acceptable is open (AS R7, AS R8).

### C14 Sensitive-data detection and masking in tables and records

Functions: AL, AN, AP (3 functions)

- Test inputs ✓: Small tables with known PII columns and clean columns (AL R3, AN R3, AP R3).
- Ground truth ✓: Cell-level PII labels; the column map follows from them (AL R2, AN R2).
- Comparable metrics ✓: Cell detection, masking correctness and latency (AL R5, AN R5, AP R5).
- Minimum architecture ✓: Table loader with two adapters: presidio-structured and an SDP table item (AL R7, AN R7, AP R7).
- Checked and left out: AH, AI: take one string, not a table; AL builds on them (C1). BB: file uploads are a different object (C30); BL file input is not studied in its columns.
- Recorded open items (listed, not decided): Google AUP testing clause not recorded in AN or AP: open.

### C15 Dialog-level conversational flow control

Functions: J (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 J R3, R5, R6, R7).
- Why it has no partner ✗: I (C12): ground truth is a topic label on single messages, not intent or flow on multi-turn dialogues (J R2, I R2); no later product has a flow engine.
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column J R8.

### C16 Retrieval-level chunk filtering

Functions: M (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 M R3, R5, R6, R7).
- Why it has no partner ✗: AH, AN, BE and BI accept retrieved text as a string but have no retrieval rail (AH R3, AN R3, BE R3); the rail position, not the detector, is what C16 tests.
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column M R8.

### C17 Context-bloat detection on input

Functions: P (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 P R3, R5, R6, R7).
- Why it has no partner ✗: N and BI (C3): ground truth is a pattern, not a size or entropy threshold (P R2).
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column P R8.

### C18 Output-level injection detection

Functions: O (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 O R3, R5, R6, R7).
- Why it has no partner ✗: BH and BJ: ground truth is insecure coding practice with CWE ids, not exploit payloads in output (O R2, BJ R2); Code Shield shows SQL injection only as a docs example (BH R3) and no XSS rule.
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column O R8.

### C19 Tool-call validation

Functions: Q (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 Q R3, R5, R6, R7).
- Why it has no partner ✗: Y and BG: ground truth is abuse or goal labels, not structural validity against a declared schema (Q R2, Y R2, BG R2).
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column Q R8.

### C20 Tool-result validation

Functions: R (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 R R3, R5, R6, R7).
- Why it has no partner ✗: AW, BE, BF and BK check tool-result text for injection or hidden characters; R checks message linkage only (R R2, AW R3, BF R3).
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column R R8.

### C21 Execution-level custom action rails

Functions: U (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 U R3, R5, R6, R7).
- Why it has no partner ✗: BI custom scanners are a similar extension route but BI is evaluated here as regex blocking (BI R1); neither has a built-in detector to compare (U R1).
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column U R8.

### C22 Grounded fact-checking of output

Functions: S (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 S R3, R5, R6, R7).
- Why it has no partner ✗: AD and AE: they compare against a system prompt or a user prompt, not retrieved evidence (S R2, AD R2, AE R2); no hallucination detector exists in later products.
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column S R8.

### C23 Self-consistency hallucination detection of output

Functions: T (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 T R3, R5, R6, R7).
- Why it has no partner ✗: S (C22): ground truth is support by evidence, not self-consistency across resamples (T R2, S R2).
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column T R8.

### C24 Multimodal content-safety classification of output (image and text prompt with text response)

Functions: X (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 X R3, R5, R6, R7).
- Why it has no partner ✗: W (C9): test inputs are text prompt-response pairs, not image-plus-text pairs (W R3, X R3). AS (C13) scores images, not response text (AS R3).
- Recorded open items (listed, not decided): EU licence clause may apply to the multimodal Llama Guard models (X R8).

### C25 Code-interpreter abuse classification (S14)

Functions: Y (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 Y R3, R5, R6, R7).
- Why it has no partner ✗: BH and BJ (C34): ground truth is insecure-code labels, not S14 abuse (BH R2, Y R2). G and V (C8): not S14 (V R2).
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column Y R8.

### C26 Custom-policy classification of input (prompts)

Functions: Z (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 Z R3, R5, R6, R7).
- Why it has no partner ✗: G, V, AT (C8): their taxonomies are fixed; the Z ground truth is an author-defined taxonomy (Z R2, V R2, AT R2).
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column Z R8.

### C27 Custom-policy classification of output (responses)

Functions: Z (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 Z R3, R5, R6, R7).
- Why it has no partner ✗: H, W, AU (C9): same reason as C26; Z response checks need both turns (Z R3, H R2).
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column Z R8.

### C28 System-prompt leakage detection

Functions: AD (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 AD R3, R5, R6, R7).
- Why it has no partner ✗: BG (C33): ground truth is goal alignment of an action, not leakage of a system prompt (AD R2, BG R2). AC (C12): off-topic, not leakage. AG: input-side leakage attempts, not leaked output (AG R2).
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column AD R8.

### C29 Refusal detection

Functions: AE (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 AE R3, R5, R6, R7).
- Why it has no partner ✗: No later column scores refusals (AE R2); Litmus (3n) test pass conditions are refusal-based but Litmus is not a column.
- Recorded open items (listed, not decided): none beyond those in the Material differences cell and column AE R8.

### C30 Document screening of uploaded files

Functions: BB (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 BB R3, R5, R6, R7).
- Why it has no partner ✗: BL and AN accept files (BL R3, AN R3) but their columns study text; BB is a screening call over file types (BB R2). C1 holds the text side.
- Recorded open items (listed, not decided): Google AUP testing clause is not recorded for BB: open (BB R8).

### C31 Input-level malicious URL detection

Functions: AZ (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 AZ R3, R5, R6, R7).
- Why it has no partner ✗: No other product's column checks link reputation (AZ R2); BB runs the same Model Armor URL filter on files (BB R2); C11 and C10 look at instruction text, not link reputation.
- Recorded open items (listed, not decided): Google AUP testing clause is recorded for AZ: whether it bears on bench testing is open (AZ R8).

### C32 Output-level malicious URL detection

Functions: BA (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 BA R3, R5, R6, R7).
- Why it has no partner ✗: No other column examines URLs in responses (BA R2); AW checks injection text, not link reputation.
- Recorded open items (listed, not decided): Google AUP testing clause is recorded for BA: whether it bears on bench testing is open (BA R8).

### C33 Trace-level agent goal-hijacking detection

Functions: BG (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 BG R3, R5, R6, R7).
- Why it has no partner ✗: BE and BF (C10, C11): one message, no trace (BE R3, BF R3). AC (C12): checks prompt relevance, not agent actions (AC R3).
- Recorded open items (listed, not decided): Together terms and trace retention are open (BG R8); Llama 4 licence terms: see 3j (f).

### C34 Output-level insecure-code detection in model responses

Functions: BH, BJ (single product)

- Test inputs ✓, ground truth ✓, metrics ✓, minimum architecture ✓: met within the function itself (sheet 3 BH R3, R5, R6, R7).
- Why it has no partner ✗: O: ground truth is exploit payloads, not insecure coding practice (O R2, BJ R2); BH and BJ are one engine through two Purple Llama surfaces (BH R4).
- Recorded open items (listed, not decided): Semgrep licence and Code Shield terms are recorded in 3j (f): open.

## C. Accounting of sheet 3 columns

| Sheet 3 column | Function (sheet 3 row 3) | Groups listing it |
|---|---|---|
| E | Amazon Bedrock Guardrails: PII detection and masking | C1, C2, C3, C4 |
| F | NeMo Guardrails: Input-level jailbreak detection | C10 |
| G | NeMo Guardrails: Input-level content-safety moderation | C8 |
| H | NeMo Guardrails: Output-level content-safety moderation | C9 |
| I | NeMo Guardrails: Input-level topic control | C12 |
| J | NeMo Guardrails: Dialog-level conversational flow control | C15 |
| K | NeMo Guardrails: Input-level PII detection & masking | C1 |
| L | NeMo Guardrails: Output-level PII detection & masking | C2 |
| M | NeMo Guardrails: Retrieval-level chunk filtering | C16 |
| N | NeMo Guardrails: Regex pattern blocklist (input/output) | C3, C4 |
| O | NeMo Guardrails: Output-level injection detection | C18 |
| P | NeMo Guardrails: Context-bloat detection (input) | C17 |
| Q | NeMo Guardrails: Tool-call validation | C19 |
| R | NeMo Guardrails: Tool-result validation | C20 |
| S | NeMo Guardrails: Grounded fact-checking (output) | C22 |
| T | NeMo Guardrails: Self-consistency hallucination detection (output) | C23 |
| U | NeMo Guardrails: Execution-level custom action rails | C21 |
| V | Llama Guard: Input-level prompt content-safety classification | C8 |
| W | Llama Guard: Output-level response content-safety classification | C9 |
| X | Llama Guard: Multimodal (image + text) content-safety classification | C13, C24 |
| Y | Llama Guard: Code-interpreter and tool-use abuse classification | C25 |
| Z | Llama Guard: Custom-policy classification | C26, C27 |
| AA | GovTech Sentinel: Localised harmful-content classification (LionGuard 2) | C8, C9 |
| AB | GovTech Sentinel: Prompt-attack detection | C10 |
| AC | GovTech Sentinel: Off-topic prompt detection against the system prompt | C12 |
| AD | GovTech Sentinel: System-prompt leakage detection | C28 |
| AE | GovTech Sentinel: Refusal detection | C29 |
| AF | GovTech Sentinel: PII detection and masking (AWS Bedrock) | C1, C2 |
| AG | GovTech Sentinel: Generic content moderation via AWS Bedrock Guardrails | C8, C10 |
| AH | Presidio: PII detection in text (Analyzer) | C1, C2 |
| AI | Presidio: PII anonymisation and masking in text (Anonymizer) | C1, C2 |
| AJ | Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt) | C5, C6 |
| AK | Presidio: PII detection and redaction in images (Image Redactor) | C7 |
| AL | Presidio: PII detection and anonymisation in structured data (tables and JSON) | C14 |
| AM | Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers) | C3, C4 |
| AN | Sensitive Data Protection: Sensitive-data detection in text (infoType inspection) | C1, C2, C14 |
| AO | Sensitive Data Protection: Custom detectors and inspection rules (custom infoTypes) | C3, C4 |
| AP | Sensitive Data Protection: Sensitive-data masking and de-identification in text | C1, C2, C14 |
| AQ | Sensitive Data Protection: Reversible tokenisation and re-identification (AES-SIV and FPE) | C5, C6 |
| AR | Sensitive Data Protection: Sensitive-data detection and redaction in images | C7 |
| AS | Sensitive Data Protection: Image safety classification (sexual and violent content) | C13 |
| AT | Model Armor: Input-level responsible AI safety filtering | C8 |
| AU | Model Armor: Output-level responsible AI safety filtering | C9 |
| AV | Model Armor: Input-level prompt injection and jailbreak detection | C10 |
| AW | Model Armor: Output-level prompt injection and jailbreak detection | C11 |
| AX | Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection) | C1 |
| AY | Model Armor: Output-level sensitive data detection and de-identification (Sensitive Data Protection) | C2 |
| AZ | Model Armor: Input-level malicious URL detection | C31 |
| BA | Model Armor: Output-level malicious URL detection | C32 |
| BB | Model Armor: Document screening (PDF, CSV, text and Office files) | C30 |
| BC | Model Armor: Image screening with OCR and visual scanning | C7 |
| BD | LionGuard: Localised harmful-content classification | C8, C9 |
| BE | Prompt Guard 2: Input-level prompt-attack detection (jailbreak and injection) | C10, C11 |
| BF | LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner) | C10, C11 |
| BG | LlamaFirewall: Trace-level agent goal-hijacking detection (AlignmentCheck) | C33 |
| BH | LlamaFirewall: Output-level insecure-code detection (CodeShield scanner) | C34 |
| BI | LlamaFirewall: Regex pattern blocking and custom scanners (Regex scanner) | C3, C4 |
| BJ | Code Shield: Output-level insecure-code detection (LLM-generated code) | C34 |
| BK | LlamaFirewall: Hidden Unicode tag-character detection (Hidden ASCII scanner) | C3, C4 |
| BL | Cloak: Free-text PII detection and anonymisation | C1, C2 |
| BM | Cloak: Custom entity detection in free text (lists, regex and LLM) | C3, C4 |
| BN | Cloak: Reversible anonymisation and decryption (encrypt and restore) | C5, C6 |

Totals: 62 functions (E to BN); 0 in no group; 23 in more than one group; 34 groups (14 multi-product, 20 single-product).

## D. Changes against v2

v2 had 24 groups (6 multi-product, 18 single-product). v3 has 34 groups (14 multi-product, 20 single-product). A multi-product group has members from two or more different products. Every sheet 3 column E to BN is in at least one group (section C).

**D1. v2 to v3 identifiers**

| v2 | v3 | What happened |
|---|---|---|
| C1 PII, input | C1 | Kept; members added: AH, AI, AN, AP, AX, BL (E, K, AF stay) |
| C2 PII, output | C2 | Kept; members added: AH, AI, AN, AP, AY, BL (E, L, AF stay) |
| C3 Harmful content, input | C8 | Kept; members added: AT, BD (G, V, AA, AG stay) |
| C4 Harmful content, output | C9 | Kept; members added: AU, BD (H, W, AA stay) |
| C5 Jailbreak and prompt attack, input | C10 | Kept; members added: AV, BE, BF (F, AB, AG stay) |
| C6 Off-topic | C12 | Kept as it was; no later product fits |
| C7 Dialog flow control (J) | C15 | Single; renumbered |
| C8 Retrieval chunk filtering (M) | C16 | Single; renumbered |
| C9 Regex blocklist, input (N) | C3 | Became multi-product: now with E, AM, AO, BI, BK, BM |
| C10 Regex blocklist, output (N) | C4 | Became multi-product: same members as C3, output side |
| C11 Context-bloat (P) | C17 | Single; renumbered |
| C12 Output injection (O) | C18 | Single; renumbered, cells as in v2. BH and BJ were checked and not grouped with O |
| C13 Tool-call validation (Q) | C19 | Single; unchanged number |
| C14 Tool-result validation (R) | C20 | Single; renumbered |
| C15 Execution-level custom action rails (U) | C21 | Single; renumbered |
| C16 Grounded fact-checking (S) | C22 | Single; renumbered |
| C17 Self-consistency hallucination (T) | C23 | Single; renumbered |
| C18 Multimodal input (X) | C13 | Became multi-product: now with AS (image content safety) |
| C19 Multimodal output (X) | C24 | Single; renumbered |
| C20 Code-interpreter abuse (Y) | C25 | Single; renumbered |
| C21 Custom policy, input (Z) | C26 | Single; renumbered |
| C22 Custom policy, output (Z) | C27 | Single; renumbered |
| C23 System-prompt leakage (AD) | C28 | Single; renumbered |
| C24 Refusal detection (AE) | C29 | Single; renumbered |
| new | C5, C6 | Reversible tokenisation (encrypt side) and token restore (decrypt side): AJ, AQ, BN |
| new | C7 | PII and sensitive-text detection and redaction in images: AK, AR, BC |
| new | C11 | Prompt-injection detection in model output, tool output and retrieved text: AW, BE, BF |
| new | C14 | Sensitive-data detection and masking in tables and records: AL, AN, AP |
| new | C30 to C34 | Single-product: BB documents, AZ and BA malicious URLs, BG goal hijacking, BH and BJ insecure code (one Purple Llama engine) |

**D2. Other changes**

- Merges and moves: BK (hidden Unicode characters) and BI (fixed regex scanner) join the rule-based pattern groups C3 and C4 because their ground truth is a deterministic rule; AI, AL, AN and AP are placed where their input object matches (text, tables).
- Input and output stay separate (docx criteria, R002) for text, tokenisation versus restore, harmful content, and URLs; images are one group (C7) because AK, AR and BC have no direction flag and the test inputs do not differ (left open for the user).
- The C7 reasoning (no direction flag, one group) also applies to AS: it appears only in C13, and its use on model-generated images has no comparator, so there is no output-side row.
- A column that takes any string (for example AH, AN, BD, BE) is listed in each side it applies to, as R002 requires.
- Marker bullet: reworded to Single-product: no comparator among the ten products yet (main ruling, queue.md groups_v3); the build matches only the prefix Single-product:, so the coverage panel is unaffected.
- Refs: v2 cells without a Refs line now have one (24 cells carried from v2); every text cell in v3 ends with a Refs line.
- Carried rows keep their v2 bullets; cross-references to renumbered groups were updated (C24, C26, C27) and two inputs bullets were added (C25 with CyberSecEval, C29 with Litmus).
- Bench content in new or changed rows is worded as proposals (R032): Suggested, Possible, could, would be needed. Rows carried from v2 keep their v2 wording.
- The v2 section Rewrite check is not carried: the word-count and format checks are run by a script kept in the grouper scratchpad.
- Licence and terms constraints (Google AUP, Cloak Terms 3.4.7, Llama 4 use policy, Together terms, OpenAI and Gemini embedder terms) are listed as open items where they bear on a group; none is decided.

## E. Suggested first group, open items and builder notes

**E1. Which group to test first (a suggestion, not a decision)**

- Suggestion: C1 (input-level PII and sensitive-data detection and masking), then C2, which reuses its data.
- Reasons for C1: it has the widest membership (9 functions, joint widest with C2, on three documented independent engines, AWS, Presidio and SDP; whether Cloak reuses Presidio is undisclosed, BL R4); the ground truth (entity type and span) needs a harmonised entity subset but less taxonomy judgement than the harmful-content groups; three members need no account (AH, AI, and K over the Presidio backend); the same labelled data could seed C2, C5, C6, C7 and C14.
- Cautions: the entity lists differ, so a harmonised subset is needed; AF, AX and K reuse the AF/E, AX/AN and K/AH backends; BL may reuse Presidio recognisers (BL R4, inferred); BL is gated and Cloak Terms clause 3.4.7 is open.
- Alternative: C10 (input-level jailbreak and prompt-attack detection) has six functions, scored outputs for AUPRC, and a possible attack source in CyberSecEval (3k) with 251 English and 1,004 translated cases. It needs harmless look-alike messages that Meta did not publish, and definitions differ across products.
- C8 (harmful content) has several members with probability outputs (AA, BD, V if extracted), but its taxonomies differ most; it could follow.

**E2. Recorded open items that bear on groups (listed, not decided)**

| Item | Where recorded | Groups it touches |
|---|---|---|
| Cloak Terms clause 3.4.7 (benchmarking), R039 | BL, BM, BN R8; 3l (e) | C1, C2, C3, C4, C5, C6 |
| Google AUP testing clause (R025), recorded in AT, AU, AV, AW, AZ, BA, BC; not in AN, AP, AX, AY, BB | AT R8 and the others named | C1, C2, C7, C8, C9, C10, C11, C14, C30, C31, C32 |
| Google Cloud AUP limits on explicit or violent test images (not the testing clause) | AS R7, AS R8 | C13 |
| Llama 4 use policy and licence gate, 700M MAU clause | BE R8, BF R8; 3j (f) | C10, C11 |
| Together terms and trace retention | BG R8; BI R8 (experimental scanners); 3j (f) | C33, C3, C4 |
| OpenAI, Gemini and Gemma embedder terms for test text | BD R8; 3i (c) | C8, C9 |
| EU licence clause for the multimodal Llama Guard models | X R8 | C13, C24 |
| Semgrep licence and Code Shield terms | BH R8, BJ R8; 3j (f) | C34 |

Recorded user rulings (decided, not open): R025 ruling 2, Preview features are tested with synthetic data only. It names Model Armor Preview features (BC); applying it to the AR face detector (AR R1) is a reading. It bears on C7.

**E3. Notes for the sheet 4 builder (not done here)**

- build_groups_sheet.py assumes 24 rows, six comparison groups, 29 function columns (E to AG) and reads groups_v2.md. For v3 it would need: 34 rows, 14 comparison groups, 62 function columns (E to BN), the new file name, and extra totals for the new product prefixes. verify_groups_apply.py would change likewise.
- The coverage panel counts a group row by the substring of each sheet 3 header in column B, so every header must stay a unique substring (checked by the script).

