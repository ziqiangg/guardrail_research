# Summary-row preview (human layer) — full detail in two_level.md


## Input-level jailbreak detection (expanded)

| Row | Summary |
|---|---|
| R1 | **Input-level jailbreak detection.** Checks whether a user input may be attempting to bypass the application's safeguards. NeMo offers two options: a perplexity-based heuristic check and an embedding-based classifier model. **[Documented]** |
| R2 | **Jailbreak attempts in user inputs.** The heuristic option targets unusually long inputs and adversarial prefix or suffix strings, and is intended for English only. **[Documented]** No attack taxonomy is published, so the classifier option's coverage is unclear. **[Not disclosed]** **[To be verified]** |
| R3 | **User messages before the main model.** It operates as an input rail before normal LLM processing continues. **[Documented]** Both options read only the current user message. **[Documented: repo v0.24.1 actions.py]** |
| R4 | **Depends on the selected detector.** NeMo offers a perplexity-based heuristic check or an embedding classifier served by an NVIDIA model service. The heuristic check runs only on the LLMRails engine. If the detector is unreachable, requests are let through. **[Documented]** |
| R5 | **Block or allow outcome.** A blocked input gets a refusal message and the response stops, or an exception if exceptions are enabled. **[Documented]** No score is exposed. **[Documented: repo v0.24.1]** The decision threshold of the NVIDIA model service is not specified. **[Documented]** **[Not disclosed]** |
| R6 | **Jailbreak and benign user prompts.** Single-turn prompts suffice because only the current user message is checked. **[Documented: repo v0.24.1]** Benign test sets should include non-English text and code, which raise false positives. **[Inferred]** **[To be verified]** |
| R7 | **Minimum setup:** test-data loader, configured NeMo input rail, selected detector, product adapter, result recorder and evaluator. The classifier option needs a reachable hosted or local model service and API key; the heuristic option needs a service for production-like runs, or torch and transformers for testing. A basic prompt-submission harness is sufficient. RAG, tool execution and multi-agent components are not required. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** How a jailbreak is defined (not documented), which detector and engine will be used, and the fact that output is only blocked or allowed, with no score. |
| R9 | NVIDIA docs (Jailbreak protection guide, NemoGuard JailbreakDetect deployment tutorial, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. |

## Input-level content-safety moderation

| Row | Summary |
|---|---|
| R1 | **Input-level content-safety moderation.** Checks each user message against a safety policy before the main model runs, and blocks unsafe input. **[Documented]** |
| R2 | **Harmful or policy-violating user content.** Covers unsafe requests such as violence, crime, hate speech or sexual content, with categories set by the chosen model and prompt. **[Documented: example prompt in repo]** The authoritative category list is unconfirmed because two NVIDIA examples number it differently. **[To be verified]** |
| R3 | **User message, before the main model.** Runs as an input check using one of three flows. A blocked message gets a refusal and the response stops, or an exception is raised if exceptions are enabled. **[Documented]** |
| R4 | **A classifier LLM judges the message.** Options include Nemotron safety models, Llama Guard, ShieldGemma, or the main LLM itself; both runtime engines support the main checks. **[Documented]** One Nemotron model is not named on the docs page, and optional third-party services are listed. **[To be verified]** |
| R5 | **Allow or block decision.** The check reports whether the message is blocked, plus any policy violations found. Nemotron-style models return a safe or unsafe verdict with categories. **[Documented]** |
| R6 | **User message text and a configured safety model.** Needs a model entry, a safety prompt and a reachable model endpoint. Reasoning models need a generous output token limit. **[Documented]** |
| R7 | **Minimum setup:** prompt-submission harness, labelled benign and harmful inputs, NeMo configuration with the chosen safety model and prompt, a reachable model endpoint, a stub or real main LLM, and a logger. Output-side, RAG and tool components are not required. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** Production licence terms for the NVIDIA safety models and services, which of the two category lists is authoritative, and false-positive and false-negative rates. |
| R9 | NVIDIA docs (Content safety, Self check, Third-party guides, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. |

## Output-level content-safety moderation

| Row | Summary |
|---|---|
| R1 | **Output-level content-safety moderation.** Checks the model's generated response against a safety policy before it reaches the user. For Nemotron prompts the user turn is checked with it. **[Documented]** |
| R2 | **Unsafe or off-policy generated content.** Addresses harmful model responses that input checks missed. The categories depend on the chosen model and prompt. **[Documented]** |
| R3 | **Bot response, after the main model.** Runs as an output check using one of three flows. A block gives a refusal and stops the response, or raises an exception if exceptions are enabled. **[Documented]** |
| R4 | **A classifier LLM judges the response.** It offers the same model options as the input check, and both runtime engines support the main checks. **[Documented]** When streaming, checks run on chunks of tokens. **[Documented]** Optional third-party services are listed, one of them input-only. **[To be verified]** |
| R5 | **Allow or block decision.** The check reports whether the response is blocked, plus any policy violations. With streaming, a block can end the stream after some text has already been sent, unless checks are set to run before release. **[Documented]** |
| R6 | **Bot response text, usually with the user input.** Needs a model entry, a safety prompt and an endpoint. Streaming needs extra configuration and has default chunk settings. **[Documented]** |
| R7 | **Minimum setup:** prompt harness with a main LLM or scripted unsafe responses, prompts known to elicit unsafe output, output-rail configuration with the safety model, an endpoint and a logger. Streaming tests also need a client that records released and blocked chunks. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** Whether unsafe text leaks before a block at different chunk sizes, how violations spanning chunk boundaries are handled, and exact streaming support on each engine. |
| R9 | NVIDIA docs (Content safety, Self check, Third-party guides, configuration reference v0.22.0, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. |

## Input-level topic control

| Row | Summary |
|---|---|
| R1 | **Input-level topic control.** Checks whether a user message stays within the topics the application allows, and blocks off-topic messages. **[Documented]** |
| R2 | **Off-topic or out-of-scope requests.** Addresses conversations drifting outside the policy written in the system prompt. It is not a general harm detector. **[Inferred]** |
| R3 | **User message, before the main model.** A single input check. A blocked message gets a refusal and the response stops, or a specific exception if exceptions are enabled. **[Documented]** |
| R4 | **A topic-control model classifies the message.** An NVIDIA topic-control model judges the message as on-topic or off-topic against a policy in the system prompt, and off-topic is blocked. Both runtime engines support it. **[Documented]** No third-party backends are documented. **[To be verified]** |
| R5 | **Allow or block decision.** The check returns a blocked flag, and the flow records whether the message was on topic before refusing or raising the exception. **[Documented]** |
| R6 | **User message plus an allowed-topic policy.** Needs a topic-control model entry, a running model endpoint and a prompt holding the policy. Whether conversation history is used is not stated. **[Documented]** |
| R7 | **Minimum setup:** harness, on-topic and off-topic test sets including borderline cases, NeMo configuration with a topic-control model and policy prompt, a model endpoint and a result recorder. A stub main LLM is sufficient. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** Licence and AI Enterprise requirements, performance and false-positive rates (not published), and how multi-turn conversations are handled. |
| R9 | NVIDIA docs (Topic control guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. |

## Dialog-level conversational flow control

| Row | Summary |
|---|---|
| R1 | **Dialog-level conversational flow control.** Steers multi-turn conversations by mapping user messages to intents and enforcing the bot's next step through Colang flows. **[Documented]** |
| R2 | **Off-topic or disallowed conversation paths.** Addresses topics or dialog paths the designer defines, for example refusing cooking questions. It covers only what has been defined. **[Documented]** |
| R3 | **Conversation stage, after input rails.** Designer-written rules bind a user intent to a canned bot response. The pipeline runs intent generation, next step, then bot message. **[Documented]** |
| R4 | **Intent matching by embeddings and/or LLM.** It matches similar example messages, then asks the LLM for the intent, or uses the closest match alone. **[Documented]** The engine support table does not cover dialog rails. **[Not disclosed]** No third-party backends are documented. **[To be verified]** |
| R5 | **Intent, next step and bot message.** The output is the canned or generated bot reply, such as a polite refusal. It is not a pass or fail result like the other rails. **[Documented]** |
| R6 | **Conversation history, Colang definitions and an embeddings model.** Needs example utterances in Colang files, a main LLM unless matching by embeddings only, and an embedding index. Optional similarity threshold and fallback intent. **[Documented]** |
| R7 | **Minimum setup:** harness, Colang configuration with at least one off-topic user intent and refusal flow, main LLM, embedding model, paraphrase and multi-turn test sets, and a recorder. Content-safety and topic-control model services are not needed. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** How robust intent matching is to paraphrase and adversarial phrasing, whether IORails supports dialog rails, and the latency and extra LLM calls. |
| R9 | NVIDIA docs (Colang topical rails tutorial, Rail types and Configuration reference for v0.22.0, Rail engine support). |

## Input-level PII detection & masking

| Row | Summary |
|---|---|
| R1 | **Input-level PII detection and masking.** Scans each user message for personal or sensitive details before the main model runs. Detect options block the message; mask options rewrite it. **[Documented]** |
| R2 | **Personal data in user prompts.** Addresses users pasting names, emails, card or ID numbers and similar details that would otherwise reach the LLM, logs or tools. Coverage depends on the backend and configured entity list. **[Inferred]** |
| R3 | **User message, before the main model.** Four families of checks (Presidio, GLiNER, Private AI, Polygraf) each have a detect version and a mask version. **[Documented]** Detect stops the response with a refusal-style reply; mask rewrites the message. **[Documented: repo v0.24.1]** |
| R4 | **Entity recognition by a local library or remote service.** Presidio runs locally; GLiNER, Private AI and Polygraf call a configured service. Masking replaces the matched text. **[Documented: repo v0.24.1]** All input flows run on both engines. **[Documented]** Backend licensing is partly unverified. **[To be verified]** |
| R5 | **Block decision or rewritten message.** Detect checks report a blocked result; mask checks return the rewritten message along with the original and masked text. If nothing changes, the message is allowed. **[Documented: repo v0.24.1]** |
| R6 | **User message text plus backend settings.** Each backend needs its own configuration: entity lists and Python packages for Presidio, or a running endpoint and, for some, an API key for the others. **[Documented]** |
| R7 | **Minimum setup:** prompt harness, test prompts with synthetic PII of known types and clean controls, NeMo configuration with one backend and entity list, any service or model that backend needs, a stub main LLM, and a recorder of blocked, masked and forwarded text. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** The Presidio masking text is unverified, the mask path ignores the configured score threshold, backend licensing is unclear, and behaviour when a backend is unreachable is mostly unchecked. |
| R9 | NVIDIA docs (PII detection guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. |

## Output-level PII detection & masking

| Row | Summary |
|---|---|
| R1 | **Output-level PII detection and masking.** Scans the model's response for personal or sensitive details before it reaches the user. Detect options block the response; mask options rewrite it. **[Documented]** |
| R2 | **Personal data leaking in generated text.** Addresses the LLM repeating personal data from the prompt, context or training data. Coverage depends on the backend and entity list. **[Inferred]** |
| R3 | **Bot response, after the main model.** Four families of checks (Presidio, GLiNER, Private AI, Polygraf) each have a detect and a mask version. **[Documented]** Detect stops the response with a refusal-style reply; mask rewrites it. **[Documented: repo v0.24.1]** |
| R4 | **Same recognisers as input, applied to the bot message.** The four backends are reused with output-specific entity lists. **[Documented]** All output flows run on both engines. **[Documented]** Backend licensing is partly unverified. **[To be verified]** |
| R5 | **Block decision or rewritten response.** Detect checks report a blocked result; mask checks return the rewritten response with source, original and masked text. Otherwise the response is allowed. **[Documented: repo v0.24.1]** |
| R6 | **Bot response text plus backend settings.** Each backend has its own output entity list, plus the endpoint and API key settings used for input. **[Documented]** |
| R7 | **Minimum setup:** harness, a main LLM or scripted responses containing synthetic PII, clean controls, output-rail configuration with one backend, that backend's service or model, and a recorder of the final user-visible text. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** Whether personal data is released during streaming before masking, how well it catches model-generated personal data, and backend licensing and pricing. |
| R9 | NVIDIA docs (PII detection guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. |

## Retrieval-level chunk filtering

| Row | Summary |
|---|---|
| R1 | **Retrieval-level chunk filtering.** Checks or rewrites the knowledge-base chunks retrieved for a turn before they reach the prompt. **[Documented]** |
| R2 | **Poisoned, sensitive or padded retrieved content.** Addresses personal data in chunks, forbidden patterns, padding that bloats the context, and text flagged by a classifier in retrieval sources. **[Inferred]** |
| R3 | **Retrieved chunks, after retrieval and before generation.** Configured as a list of retrieval checks, with seven kinds of check found in the v0.24.1 code. **[Documented: repo v0.24.1]** |
| R4 | **Depends on the flow.** Options are a personal-data backend, a pattern match, size statistics or a Hugging Face classifier. Detect options stop the response; pattern and classifier options blank the chunks. **[Documented: repo v0.24.1]** Runs on the LLMRails engine only. **[Documented]** Backend licensing is partly unverified. **[To be verified]** |
| R5 | **Chunks kept, rewritten, emptied or turn blocked.** Block options answer with an "answer unknown" style reply, or a retrieval-bloated message for padding. **[Documented: repo v0.24.1]** |
| R6 | **Retrieved chunks plus a knowledge base.** Needs a knowledge base or custom retrieval step that fills the retrieved chunks, the retrieval checks list, and the settings of the chosen check. **[Inferred]** |
| R7 | **Minimum setup:** small knowledge base with clean chunks and seeded bad chunks (personal data, forbidden pattern, padding), configuration with retrieval checks, the LLMRails engine, a stub or real LLM, and a log of the chunks passed to the prompt. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** Whether blanking removes one chunk or all of them (the code blanks everything), how custom retrievers behave, and whether chunks are checked one by one or joined. |
| R9 | NVIDIA docs (Rail engine support, PII detection, Regex and Agentic security guides) and NeMo Guardrails v0.24.1 source code on GitHub. |

## Regex pattern blocklist (input/output)

| Row | Summary |
|---|---|
| R1 | **Regex pattern blocklist.** Blocks a user message or bot response that matches any configured regular expression. **[Documented]** |
| R2 | **Known forbidden strings or formats.** Addresses fixed patterns such as banned phrases, secret formats or identifiers. It cannot catch paraphrases. **[Inferred]** |
| R3 | **User message or bot response.** Separate input and output checks. **[Documented]** A match gives a refusal and stops the response. A retrieval variant also exists and blanks matching chunks. **[Documented: repo v0.24.1]** |
| R4 | **Pattern matching, no model.** Each pattern is tested against the text and all matching patterns are reported. **[Documented: repo v0.24.1]** It is built into NeMo, needs no extra package and runs on both engines for input and output. **[Documented]** No third-party backends are documented. **[To be verified]** |
| R5 | **Block decision.** The result says whether the text was blocked and lists the matched patterns. The flow does not switch to an exception when exceptions are enabled. **[Documented: repo v0.24.1]** |
| R6 | **Text plus pattern list.** Needs a list of regular-expression patterns for each position and an optional case-insensitive flag. No models or keys are needed. **[Documented]** |
| R7 | **Minimum setup:** harness, strings that match and do not match each pattern, a configuration with patterns for input and output, a stub LLM that returns scripted text, and a result recorder. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** How the docs describe the matching method, how slow or unsafe patterns are handled, and how Unicode and other regex flags are treated. |
| R9 | NVIDIA docs (Regex guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. |

## Output-level injection detection

| Row | Summary |
|---|---|
| R1 | **Output-level injection detection.** Scans the bot's output for code, SQL, template or cross-site scripting payloads before it is passed on. **[Documented]** |
| R2 | **Exploit strings in generated output.** Addresses model output that could run as code or queries in downstream systems, mainly in agentic setups. The docs call it defence-in-depth, not a standalone control. **[Documented]** |
| R3 | **Bot message, after the main model.** A single output-only check. **[Documented]** |
| R4 | **YARA rule matching.** Built-in rules cover code, SQL, template and cross-site scripting, with optional custom rules. The reject option blocks; the omit option strips matched text. **[Documented]** It runs on both engines. **[Documented]** YARA being open-source is unverified. **[To be verified]** |
| R5 | **Block, stripped text or allow.** On reject, the bot says the output triggered a rule and stops, or raises an exception if exceptions are enabled. **[Documented: repo v0.24.1]** |
| R6 | **Bot message text plus configuration.** Needs injection settings, the output check enabled, and the YARA Python package. **[Documented]** |
| R7 | **Minimum setup:** harness, scripted bot outputs containing code, SQL, template and XSS payloads plus benign controls, configuration with chosen injection types and action, the YARA package, and a recorder. No retrieval or input checks are needed. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** The code accepts a third action that fails, how well the omit option really removes payloads, and false positives on legitimate code answers. |
| R9 | NVIDIA docs (Agentic security guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. |

## Context-bloat detection (input)

| Row | Summary |
|---|---|
| R1 | **Input-level context-bloat detection.** Flags oversized, padded or repetitive user messages before they reach the main LLM. **[Documented]** |
| R2 | **Context-manipulation padding.** Addresses long or repetitive input meant to bury instructions, make the model forget its system prompt, or burn the token budget. **[Documented]** |
| R3 | **User message, before the main model.** A reject says the message appears oversized or padded and stops the response. A retrieval variant also exists. **[Documented: repo v0.24.1]** |
| R4 | **Statistical checks, no model.** Checks message size, randomness, repeated characters and repeated phrases, in that order. **[Documented: repo v0.24.1]** The action can reject, truncate or warn. **[Documented]** The input check runs on both engines. **[Documented]** No third-party backends. **[To be verified]** |
| R5 | **Block, truncated message or allow.** Reject blocks, truncate shortens the message, and warn lets it through with the findings recorded. **[Documented: repo v0.24.1]** |
| R6 | **User message text plus thresholds.** Needs size, randomness and repetition thresholds, a chosen action, and the input check enabled. **[Documented]** The code also reads two further settings. **[Documented: repo v0.24.1]** |
| R7 | **Minimum setup:** harness, test inputs of normal text, text over 5000 characters, a repeated single character, repeated phrases and low-randomness filler, configuration trying each action in turn, and a recorder of outcome and metrics. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** In the code, truncate only shortens for the size limit and rejects other findings, which the docs do not say. Also unclear are false positives on legitimate long pastes and whether warnings are visible to the caller. |
| R9 | NVIDIA docs (Agentic security guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. |

## Tool-call validation

| Row | Summary |
|---|---|
| R1 | **Tool-call validation (output side).** Checks each tool call the model emits against the tools the application declared, before the call reaches the application. It is a local structural check with no LLM call. **[Documented]** |
| R2 | **Unknown tools, malformed arguments and invalid tool schemas.** Catches calls to undeclared tools, arguments that break the tool's schema, arguments given to a no-parameter tool, and invalid declared schemas. **[Documented]** It does not judge whether an allowed call is harmful. **[Inferred]** |
| R3 | **Model response, after the main LLM.** A response containing only tool calls skips the text output checks. A block returns a fixed refusal, and a provider failure returns an internal-error message. The check does not run tools. **[Documented]** |
| R4 | **Structural allowlist and JSON Schema check.** It supports only the OpenAI-style format. **[Documented]** NVIDIA's pages disagree on which engines run it. **[Documented]** A model-based tool safety check exists only in a development branch. **[Not disclosed in v0.24.1 docs]** **[To be verified]** |
| R5 | **Allow or block outcome.** A block gives a fixed refusal text, or an error payload when streaming, with a reason such as "not an allowed tool". A provider outage gives an internal-error message instead. **[Documented]** |
| R6 | **Declared tools plus the model's tool calls.** Needs tool definitions in the configuration and a model that emits tool calls. Hosted tools identified only by type are allowed by type and their arguments are not checked. **[Documented]** |
| R7 | **Minimum setup:** harness sending requests with declared tools, a model or scripted responses emitting valid, unknown-name, bad-argument and no-parameter-with-arguments calls, configuration with the tool-call check on IORails, and a recorder. No tool execution is needed. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** Which engine actually runs the tool checks in v0.24.1, since the docs conflict, and whether the model-based tool safety check and per-tool pattern checks reach a release. |
| R9 | NVIDIA docs (Tool calling guide, Rail engine support) and NeMo Guardrails v0.24.1 docs and source code on GitHub. |

## Tool-result validation

| Row | Summary |
|---|---|
| R1 | **Tool-result validation (input side).** Checks tool-result messages in the request before the model sees them. It is a local structural check with no LLM call. **[Documented]** |
| R2 | **Malformed or inconsistent tool results.** Catches missing or unlinked call IDs, duplicate IDs, mismatched tool names and invalid content types. **[Documented]** It is not a content-safety or prompt-injection check on the result text. **[Documented]** |
| R3 | **Request input, before the main model.** Runs alongside the input checks, with the same refusal and error behaviour as the tool-call check. **[Documented]** Plain input and output checks see only message content, so tool results bypass input checks. **[Documented]** |
| R4 | **Structural linkage check only.** It does not enforce a response schema or check content safety, and checks consistency within one request only. **[Documented]** NVIDIA's pages disagree on which engines run it. **[Documented]** A model-based tool safety check exists only in a development branch. **[Not disclosed in v0.24.1 docs]** **[To be verified]** |
| R5 | **Allow or block outcome.** A block gives a fixed refusal text, or an error payload when streaming. A provider failure gives an internal-error message. **[Documented]** |
| R6 | **Conversation history with tool messages.** Needs the assistant turn containing the tool calls and one tool message per call ID, resent on each request. Declared tools are needed for name checks. **[Documented]** |
| R7 | **Minimum setup:** harness sending conversations with tool messages (valid, missing ID, duplicate ID, wrong name, non-string content), configuration with the tool-result check on IORails, a stub main LLM, and a recorder. No real tool execution is needed. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** Which engine runs the tool checks in v0.24.1, since the docs conflict, and that result text itself is not checked, so injection via tool results is unaddressed. |
| R9 | NVIDIA docs (Tool calling guide, Rail engine support) and NeMo Guardrails v0.24.1 docs on GitHub. |

## Grounded fact-checking (output)

| Row | Summary |
|---|---|
| R1 | **Grounded fact-checking (output).** Checks whether the bot reply is supported by the retrieved evidence before it reaches the user. **[Documented]** |
| R2 | **Unsupported claims in RAG answers.** Addresses replies that contradict or go beyond the knowledge-base chunks. It does not help without retrieved evidence. **[Documented]** |
| R3 | **Bot response, after the main model.** Three output checks are available, and the self-check one runs only when a fact-checking flag is set. **[Documented]** |
| R4 | **Entailment judgement against evidence.** The LLM scores support, an AlignScore server judges it, or a Patronus Lynx model detects hallucination. **[Documented]** These run on the LLMRails engine only; IORails does not support them. **[Documented]** Several paid and open third-party options are listed. **[To be verified]** |
| R5 | **Score and block decision.** The self-check option returns a 0 to 1 score and blocks below a threshold. **[Documented]** Other backends return their own results, and the exact output shape for each vendor is unconfirmed. **[Documented]** **[To be verified]** |
| R6 | **Reply plus retrieved chunks.** Needs retrieved evidence, the fact-checking flag set, and for self-check a prompt and the main LLM. AlignScore needs a running server; vendors need accounts or keys. **[Documented]** |
| R7 | **Minimum setup:** harness, a small knowledge base or injected retrieved chunks, supported and unsupported answer pairs, a configuration on the LLMRails engine with the chosen check, a judge LLM or AlignScore server, and a recorder. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** Thresholds for non-LLM backends, whether the IORails exclusion list holds for v0.24.1, and vendor licensing and cost. |
| R9 | NVIDIA docs (Fact-checking guide, Rail engine support) and the NeMo Guardrails v0.24.1 engine-support page on GitHub. |

## Self-consistency hallucination detection (output)

| Row | Summary |
|---|---|
| R1 | **Self-consistency hallucination detection (output).** Samples extra generations and checks whether they agree with the original reply; disagreement suggests a hallucination. No grounding documents are needed. **[Documented]** |
| R2 | **Fabricated facts without retrieval.** Addresses unstable answers drawn from the model's own knowledge. It cannot catch a consistent but wrong answer. **[Inferred]** |
| R3 | **Bot response, after the main model.** One flow blocks and another appends a warning, each running only when its flag is set. **[Documented]** |
| R4 | **Resampling plus an LLM agreement check.** By default two extra responses are generated and the LLM judges whether they agree with the original. **[Documented: repo v0.24.1]** It runs on the LLMRails engine only. **[Documented]** If all extra generations fail, the reply is allowed. **[Documented: repo v0.24.1]** Supported providers are unclear. **[To be verified]** |
| R5 | **Block or warning.** The outcome is allow or block, and the warning option appends text instead of blocking. **[Documented: repo v0.24.1]** |
| R6 | **Bot reply and the prompt that produced it.** Needs the last bot prompt, a main LLM, a self-check prompt and the flag set. **[Documented]** |
| R7 | **Minimum setup:** harness, prompts with stable answers and prompts the model tends to invent answers for, a configuration on the LLMRails engine with the check and flag, a main LLM allowing temperature 1.0, and a recorder. **[Inferred from the documented rail position]** |
| R8 | **Key open questions.** Which main-LLM providers work (unconfirmed), the added latency and cost of three or more LLM calls, and that a failure of the extra calls lets the reply through. |
| R9 | NVIDIA docs (Fact-checking guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. |