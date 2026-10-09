# v2 Summary preview — changed or new Summary rows only

(Unchanged summaries omitted. Full text: two_level_v2.md; change log: v2_changes.md)

## Input-level jailbreak detection

| Row | Before | After |
|---|---|---|
| R4 | **Depends on the selected detector.** NeMo offers a perplexity-based heuristic check or an embedding classifier served by an NVIDIA model service. The heuristic check runs only on the LLMRails engine. If the detector is unreachable, requests are let through. **[Documented]** | **Depends on the selected detector.** A perplexity-based heuristic check (LLMRails only) or an embedding classifier served by an NVIDIA model service. If the detector is unreachable, requests are let through. Several third-party guards also offer jailbreak or prompt-injection detection. **[Documented]** |
| R8 | **Key open questions.** How a jailbreak is defined (not documented), which detector and engine will be used, and the fact that output is only blocked or allowed, with no score. | **Key open questions.** How a jailbreak is defined (not documented), which detector will be used, the NIM decision threshold and training data, and how a detector outage behaves. |
| R9 | NVIDIA docs (Jailbreak protection guide, NemoGuard JailbreakDetect deployment tutorial, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. | NVIDIA docs (Jailbreak protection guide, NemoGuard JailbreakDetect deployment tutorial, Rail engine support, third-party vendor pages), the NemoGuard JailbreakDetect model card on Hugging Face, and NeMo Guardrails v0.24.1 source code on GitHub. |

## Input-level content-safety moderation

| Row | Before | After |
|---|---|---|
| R2 | **Harmful or policy-violating user content.** Covers unsafe requests such as violence, crime, hate speech or sexual content, with categories set by the chosen model and prompt. **[Documented: example prompt in repo]** The authoritative category list is unconfirmed because two NVIDIA examples number it differently. **[To be verified]** | **Harmful or policy-violating user content.** Covers unsafe requests such as violence, crime, hate speech or sexual content, with categories set by the chosen model and prompt. **[Documented: example prompt in repo]** The category count depends on the model: 23 for Safety Guard v3, 22 for Reasoning-4B. **[Documented: vendor site]** |
| R4 | **A classifier LLM judges the message.** Options include Nemotron safety models, Llama Guard, ShieldGemma, or the main LLM itself; both runtime engines support the main checks. **[Documented]** One Nemotron model is not named on the docs page, and optional third-party services are listed. **[To be verified]** | **A classifier LLM judges the message.** Options include Nemotron safety models, Llama Guard, ShieldGemma, or the main LLM itself; both runtime engines support the main checks. **[Documented]** Optional third-party services are listed; most are commercial vendors per their vendor sites, and some licences remain open. **[Documented: vendor site]** **[To be verified]** |
| R8 | **Key open questions.** Production licence terms for the NVIDIA safety models and services, which of the two category lists is authoritative, and false-positive and false-negative rates. | **Key open questions.** Whether NIM production use requires AI Enterprise, the licensing of a few third-party vendors, the NemoGuard 8B language coverage, and false-positive and false-negative rates. |
| R9 | NVIDIA docs (Content safety, Self check, Third-party guides, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. | NVIDIA docs (Content safety, Self check, Third-party guides, Rail engine support), NVIDIA model cards and vendor sites, and NeMo Guardrails v0.24.1 source code on GitHub. |

## Output-level content-safety moderation

| Row | Before | After |
|---|---|---|
| R4 | **A classifier LLM judges the response.** It offers the same model options as the input check, and both runtime engines support the main checks. **[Documented]** When streaming, checks run on chunks of tokens. **[Documented]** Optional third-party services are listed, one of them input-only. **[To be verified]** | **A classifier LLM judges the response.** Same model options as the input check, on both runtime engines. **[Documented]** Streaming checks run on chunks of tokens. **[Documented]** Third-party services are listed, one input-only; most are commercial vendors per vendor sites, some licences open. **[Documented: vendor site]** **[To be verified]** |
| R8 | **Key open questions.** Whether unsafe text leaks before a block at different chunk sizes, how violations spanning chunk boundaries are handled, and exact streaming support on each engine. | **Key open questions.** Whether unsafe text leaks before a block at different chunk sizes, how violations spanning chunk boundaries are handled, and whether every self check variant works with streaming. |
| R9 | NVIDIA docs (Content safety, Self check, Third-party guides, configuration reference v0.22.0, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. | NVIDIA docs (Content safety, Self check, Third-party guides, configuration reference v0.22.0, Rail engine support, Engine feature support), vendor sites, and NeMo Guardrails v0.24.1 source code on GitHub. |

## Input-level topic control

| Row | Before | After |
|---|---|---|
| R4 | **A topic-control model classifies the message.** An NVIDIA topic-control model judges the message as on-topic or off-topic against a policy in the system prompt, and off-topic is blocked. Both runtime engines support it. **[Documented]** No third-party backends are documented. **[To be verified]** | **A topic-control model classifies the message.** An NVIDIA topic-control model judges the message as on-topic or off-topic against a policy in the system prompt, and off-topic is blocked. Both runtime engines support it. **[Documented]** No third-party backends are documented. **[Documented]** |
| R8 | **Key open questions.** Licence and AI Enterprise requirements, performance and false-positive rates (not published), and how multi-turn conversations are handled. | **Key open questions.** Whether production use needs AI Enterprise, performance and false-positive rates (not published), and how multi-turn conversations are handled. |
| R9 | NVIDIA docs (Topic control guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. | NVIDIA docs (Topic control guide, Third-party index, Rail engine support), NVIDIA model card and NIM pages, and NeMo Guardrails v0.24.1 source code on GitHub. |

## Dialog-level conversational flow control

| Row | Before | After |
|---|---|---|
| R1 | **Dialog-level conversational flow control.** Steers multi-turn conversations by mapping user messages to intents and enforcing the bot's next step through Colang flows. **[Documented]** | **Dialog-level conversational flow control.** Steers multi-turn conversations by mapping user messages to intents and enforcing the bot's next step through conversation flows. The flows are written by the developer; NeMo provides the engine that runs them, not a ready-made detector. **[Documented]** |
| R4 | **Intent matching by embeddings and/or LLM.** It matches similar example messages, then asks the LLM for the intent, or uses the closest match alone. **[Documented]** The engine support table does not cover dialog rails. **[Not disclosed]** No third-party backends are documented. **[To be verified]** | **Intent matching by embeddings and/or LLM over developer-written flows.** Similar example messages are matched, then the LLM picks the intent, or the closest match is used alone. **[Documented]** LLMRails only, not IORails. **[Documented]** Coverage is only as broad as the flows written. **[Inferred]** No third-party backends are documented. **[Inferred]** |
| R6 | **Conversation history, Colang definitions and an embeddings model.** Needs example utterances in Colang files, a main LLM unless matching by embeddings only, and an embedding index. Optional similarity threshold and fallback intent. **[Documented]** | **Conversation history, Colang definitions and an embeddings model.** Needs example utterances in Colang files, a main LLM unless embeddings-only, and an embedding index; similarity threshold and fallback intent are optional. **[Documented]** The test bench needs a reference Colang configuration that we author. **[Inferred]** |
| R7 | **Minimum setup:** harness, Colang configuration with at least one off-topic user intent and refusal flow, main LLM, embedding model, paraphrase and multi-turn test sets, and a recorder. Content-safety and topic-control model services are not needed. **[Inferred from the documented rail position]** | **Minimum setup:** harness, a reference Colang configuration that we author with example user intents, refusal flows and multi-turn flows, the LLMRails engine, main LLM, embedding model, paraphrase and multi-turn test sets, and a recorder. Content-safety and topic-control model services are not needed. **[Inferred]** |
| R8 | **Key open questions.** How robust intent matching is to paraphrase and adversarial phrasing, whether IORails supports dialog rails, and the latency and extra LLM calls. | **Key open questions.** How robust intent matching is to paraphrase and adversarial phrasing, which Colang version the test bench will use, and the latency and extra LLM calls. |
| R9 | NVIDIA docs (Colang topical rails tutorial, Rail types and Configuration reference for v0.22.0, Rail engine support). | NVIDIA docs (Colang topical rails tutorial, Colang overview and What's Changed, Rail types and Configuration reference for v0.22.0, Engine feature support, Rail engine support, Third-party index) and one NeMo Guardrails v0.24.1 documentation page on GitHub. |

## Input-level PII detection & masking

| Row | Before | After |
|---|---|---|
| R8 | **Key open questions.** The Presidio masking text is unverified, the mask path ignores the configured score threshold, backend licensing is unclear, and behaviour when a backend is unreachable is mostly unchecked. | **Key open questions.** The Presidio replacement text is not stated in the docs, GLiNER container terms and Polygraf licensing are unclear, and behaviour when a backend is unreachable is mostly unchecked. |
| R9 | NVIDIA docs (PII detection guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. | NVIDIA docs (PII detection guide, Presidio guide, Rail engine support), vendor and model pages for licensing, and NeMo Guardrails v0.24.1 source code and documentation on GitHub. |

## Output-level PII detection & masking

| Row | Before | After |
|---|---|---|
| R8 | **Key open questions.** Whether personal data is released during streaming before masking, how well it catches model-generated personal data, and backend licensing and pricing. | **Key open questions.** Whether personal data is released during streaming before masking, how well it catches model-generated personal data, and GLiNER container terms and Polygraf licensing. |
| R9 | NVIDIA docs (PII detection guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. | NVIDIA docs (PII detection guide, Presidio guide, Rail engine support), vendor and model pages for licensing, and NeMo Guardrails v0.24.1 source code and documentation on GitHub. |

## Retrieval-level chunk filtering

| Row | Before | After |
|---|---|---|
| R8 | **Key open questions.** Whether blanking removes one chunk or all of them (the code blanks everything), how custom retrievers behave, and whether chunks are checked one by one or joined. | **Key open questions.** The regex docs say one chunk is removed while the code blanks all of them, how custom retrievers behave, and the remaining backend licensing. |
| R9 | NVIDIA docs (Rail engine support, PII detection, Regex and Agentic security guides) and NeMo Guardrails v0.24.1 source code on GitHub. | NVIDIA docs (Rail engine support, PII detection, Regex and Agentic security guides), vendor and model pages for licensing, and NeMo Guardrails v0.24.1 source code and documentation on GitHub. |

## Regex pattern blocklist (input/output)

| Row | Before | After |
|---|---|---|
| R4 | **Pattern matching, no model.** Each pattern is tested against the text and all matching patterns are reported. **[Documented: repo v0.24.1]** It is built into NeMo, needs no extra package and runs on both engines for input and output. **[Documented]** No third-party backends are documented. **[To be verified]** | **Pattern matching, no model.** Each pattern is tested against the text and all matching patterns are reported. **[Documented: repo v0.24.1]** It is built into NeMo, needs no extra package and runs on both engines for input and output. **[Documented]** No third-party backends are documented. **[Documented]** |
| R8 | **Key open questions.** How the docs describe the matching method, how slow or unsafe patterns are handled, and how Unicode and other regex flags are treated. | **Key open questions.** How slow or unsafe patterns are handled (ReDoS), how Unicode is normalised, and that the docs do not name the matching method. |
| R9 | NVIDIA docs (Regex guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. | NVIDIA docs (Regex guide, Rail engine support), NeMo Guardrails v0.24.1 source code on GitHub, and one develop-branch source file. |

## Output-level injection detection

| Row | Before | After |
|---|---|---|
| R4 | **YARA rule matching.** Built-in rules cover code, SQL, template and cross-site scripting, with optional custom rules. The reject option blocks; the omit option strips matched text. **[Documented]** It runs on both engines. **[Documented]** YARA being open-source is unverified. **[To be verified]** | **YARA rule matching.** Built-in rules cover code, SQL, template and cross-site scripting, with optional custom rules. The reject option blocks; the omit option strips matched text. **[Documented]** It runs on both engines. **[Documented]** YARA is open-source (BSD-3-Clause). **[Documented: vendor site]** The licence of its Python package is unchecked. **[To be verified]** |
| R8 | **Key open questions.** The code accepts a third action that fails, how well the omit option really removes payloads, and false positives on legitimate code answers. | **Key open questions.** Which default action applies, how well the omit option really removes payloads, false positives on legitimate code answers, and the licence of the YARA Python package. |
| R9 | NVIDIA docs (Agentic security guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. | NVIDIA docs (Agentic security guide, Rail engine support), the YARA repository, and NeMo Guardrails v0.24.1 source code on GitHub. |

## Context-bloat detection (input)

| Row | Before | After |
|---|---|---|
| R4 | **Statistical checks, no model.** Checks message size, randomness, repeated characters and repeated phrases, in that order. **[Documented: repo v0.24.1]** The action can reject, truncate or warn. **[Documented]** The input check runs on both engines. **[Documented]** No third-party backends. **[To be verified]** | **Statistical checks, no model.** Checks message size, randomness, repeated characters and repeated phrases, in that order. **[Documented: repo v0.24.1]** The action can reject, truncate or warn. **[Documented]** The input check runs on both engines. **[Documented]** No third-party backends. **[Documented]** |
| R5 | **Block, truncated message or allow.** Reject blocks, truncate shortens the message, and warn lets it through with the findings recorded. **[Documented: repo v0.24.1]** | **Block, truncated message or allow.** Reject blocks, truncate shortens the message, and warn lets it through with only a log entry. **[Documented: repo v0.24.1]** |
| R6 | **User message text plus thresholds.** Needs size, randomness and repetition thresholds, a chosen action, and the input check enabled. **[Documented]** The code also reads two further settings. **[Documented: repo v0.24.1]** | **User message text plus thresholds.** Needs size, randomness and repetition thresholds, a chosen action, and the input check enabled. **[Documented]** Minimum length and n-gram size are two further settings with documented defaults. **[Documented]** |
| R8 | **Key open questions.** In the code, truncate only shortens for the size limit and rejects other findings, which the docs do not say. Also unclear are false positives on legitimate long pastes and whether warnings are visible to the caller. | **Key open questions.** False positives on legitimate long pastes such as logs or code, and how the entropy check behaves on non-English text. |
| R9 | NVIDIA docs (Agentic security guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. | NVIDIA docs (Agentic security guide, Rail engine support, Third-party index) and NeMo Guardrails v0.24.1 source code on GitHub. |

## Tool-call validation

| Row | Before | After |
|---|---|---|
| R4 | **Structural allowlist and JSON Schema check.** It supports only the OpenAI-style format. **[Documented]** NVIDIA's pages disagree on which engines run it. **[Documented]** A model-based tool safety check exists only in a development branch. **[Not disclosed in v0.24.1 docs]** **[To be verified]** | **Structural allowlist and JSON Schema check.** It supports only the OpenAI-style format. **[Documented]** The built-in validators run on IORails only; LLMRails needs custom flows. **[Documented]** A model-based tool safety check exists only in the development branch, not in any release. **[Documented: develop branch]** |
| R8 | **Key open questions.** Which engine actually runs the tool checks in v0.24.1, since the docs conflict, and whether the model-based tool safety check and per-tool pattern checks reach a release. | **Key open questions.** Whether the built-in validator behaves as documented on LLMRails at runtime, whether plain output rails see tool-call arguments on LLMRails, and which JSON Schema draft applies. |
| R9 | NVIDIA docs (Tool calling guide, Rail engine support) and NeMo Guardrails v0.24.1 docs and source code on GitHub. | NVIDIA docs (Tool calling guide, Rail engine support, Engine feature support), NeMo Guardrails v0.24.1 docs and source code on GitHub, and develop-branch source files for unreleased features. |

## Tool-result validation

| Row | Before | After |
|---|---|---|
| R4 | **Structural linkage check only.** It does not enforce a response schema or check content safety, and checks consistency within one request only. **[Documented]** NVIDIA's pages disagree on which engines run it. **[Documented]** A model-based tool safety check exists only in a development branch. **[Not disclosed in v0.24.1 docs]** **[To be verified]** | **Structural linkage check only.** No response schema or content-safety check; consistency is checked within one request only. **[Documented]** The built-in validators run on IORails only; LLMRails needs custom flows. **[Documented]** A model-based tool safety check exists only in the development branch. **[Documented: develop branch]** |
| R8 | **Key open questions.** Which engine runs the tool checks in v0.24.1, since the docs conflict, and that result text itself is not checked, so injection via tool results is unaddressed. | **Key open questions.** Whether the built-in tool-result validator behaves as documented on LLMRails at runtime. |
| R9 | NVIDIA docs (Tool calling guide, Rail engine support) and NeMo Guardrails v0.24.1 docs on GitHub. | NVIDIA docs (Tool calling guide, Rail engine support, Engine feature support), NeMo Guardrails v0.24.1 docs and source code on GitHub, and develop-branch source files for unreleased features. |

## Grounded fact-checking (output)

| Row | Before | After |
|---|---|---|
| R4 | **Entailment judgement against evidence.** The LLM scores support, an AlignScore server judges it, or a Patronus Lynx model detects hallucination. **[Documented]** These run on the LLMRails engine only; IORails does not support them. **[Documented]** Several paid and open third-party options are listed. **[To be verified]** | **Entailment judgement against evidence.** The LLM scores support, an AlignScore server judges it, or a Patronus Lynx model detects hallucination. **[Documented]** These run on the LLMRails engine only; IORails does not support them. **[Documented]** Several commercial and open third-party options are listed, with some licences still unverified. **[Documented: vendor site]** **[To be verified]** |
| R5 | **Score and block decision.** The self-check option returns a 0 to 1 score and blocks below a threshold. **[Documented]** Other backends return their own results, and the exact output shape for each vendor is unconfirmed. **[Documented]** **[To be verified]** | **Score and block decision.** The self-check option returns a 0 to 1 score and blocks below a threshold. **[Documented]** Other backends return their own results; the output shape is confirmed for most vendors but not for AutoAlign or Fiddler. **[Documented: repo v0.24.1]** **[To be verified]** |
| R8 | **Key open questions.** Thresholds for non-LLM backends, whether the IORails exclusion list holds for v0.24.1, and vendor licensing and cost. | **Key open questions.** Thresholds and output shapes for a few vendors, and the licensing and cost of Patronus API, AutoAlign and Cleanlab. |
| R9 | NVIDIA docs (Fact-checking guide, Rail engine support) and the NeMo Guardrails v0.24.1 engine-support page on GitHub. | NVIDIA docs (Fact-checking guide, Rail engine support), the NeMo Guardrails v0.24.1 engine-support page and source code on GitHub, and vendor sites and model cards for licensing. |

## Self-consistency hallucination detection (output)

| Row | Before | After |
|---|---|---|
| R9 | NVIDIA docs (Fact-checking guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub. | NVIDIA docs (Fact-checking guide, Rail engine support, Third-party index) and NeMo Guardrails v0.24.1 source code and documentation on GitHub. |

## Execution-level custom action rails **(NEW COLUMN)**

| Row | Before | After |
|---|---|---|
| R1 | — | **Execution-level custom action rails.** Developer-written checks around the custom actions an app or the model triggers, validating what goes into an action and what comes out. **[Documented]** NeMo supplies the hook, not a ready-made detector. **[Inferred]** |
| R2 | — | **Unsafe or invalid use of custom actions.** Addresses actions called with bad arguments or returning untrusted results; the docs name agentic security as the main use. **[Documented]** What is caught depends entirely on the checks written. **[Inferred]** |
| R3 | — | **Around a custom action call, inside the conversation flow.** A developer-written flow calls an action and then branches on its result, for example refusing and stopping. The configuration reference says execution rails act before and after action execution. **[Documented: repo v0.24.1]** |
| R4 | — | **Developer-written Python and Colang, no model of its own.** NeMo provides the action decorator, the flow runtime and action execution. **[Documented: repo v0.24.1]** The check logic comes from the developer. **[Inferred]** Execution rails run on LLMRails only, because IORails does not run custom actions. **[Documented]** |
| R5 | — | **Whatever the developer's flow returns.** Typically a refusal message and a stopped response, but the format is not fixed by NeMo. **[Documented: repo v0.24.1]** An action may return a structured allow, block or transform decision. **[Documented: repo v0.24.1]** |
| R6 | — | **Action name, arguments and result, plus a reference configuration we author.** The test bench cannot reuse a ready-made check, so it needs a custom-action configuration with test actions that we write. **[Inferred]** Actions can read conversation context such as the last user message. **[Documented: repo v0.24.1]** |
| R7 | — | **Minimum setup:** harness, a configuration with a few test actions and flows that we write, a main LLM or scripted calls that trigger them, test cases with allowed and blocked inputs, the LLMRails engine and a recorder of action calls and blocks. No external model service is required by NeMo for this function. **[Inferred]** |
| R8 | — | **Key open questions.** Whether the documented execution rails key is silently accepted by the configuration, what exactly they wrap, and how they differ in practice from tool rails. |
| R9 | — | NVIDIA docs (Engine Feature Support, Rail types for v0.22.0 and latest, Tools Integration) and NeMo Guardrails v0.24.1 documentation and source on GitHub. |
