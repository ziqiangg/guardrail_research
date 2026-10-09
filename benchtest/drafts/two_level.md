## Column: NeMo Guardrails: Input-level jailbreak detection (expanded)
### R1
Summary: **Input-level jailbreak detection.** Checks whether a user input may be attempting to bypass the application's safeguards. NeMo offers two options: a perplexity-based heuristic check and an embedding-based classifier model. **[Documented]**
Detail:
• Checks whether a user input may be attempting to bypass the application's safeguards **[Documented]**
• NeMo ships two flows: **[Documented]**
  – `jailbreak detection heuristics` (perplexity-based)
  – `jailbreak detection model` (embedding classifier, via the NemoGuard JailbreakDetect NIM)
### R2
Summary: **Jailbreak attempts in user inputs.** The heuristic option targets unusually long inputs and adversarial prefix or suffix strings, and is intended for English only. **[Documented]** No attack taxonomy is published, so the classifier option's coverage is unclear. **[Not disclosed]** **[To be verified]**
Detail:
• Addresses jailbreak attempts in user inputs **[Documented]**
• The heuristics target unusually long or high-perplexity inputs **[Documented]**
• The heuristics target GCG-style adversarial prefix/suffix strings **[Documented]**
• The model flow is described as a general jailbreak classifier **[Documented]**
• The heuristics are intended for English only **[Documented]**
• The heuristics give more false positives on non-English text, including code **[Documented]**
• No jailbreak taxonomy is published **[Not disclosed]** **[To be verified]**
• Precise coverage of the model flow is unclear **[Not disclosed]** **[To be verified]**
### R3
Summary: **User messages before the main model.** It operates as an input rail before normal LLM processing continues. **[Documented]** Both options read only the current user message. **[Documented: repo v0.24.1 actions.py]**
Detail:
• Position: user messages, before the main model **[Documented]**
• It operates as an input rail that evaluates the user message before normal LLM processing continues **[Documented]**
• Both flows read the current user message only **[Documented: repo v0.24.1 actions.py]**
### R4
Summary: **Depends on the selected detector.** NeMo offers a perplexity-based heuristic check or an embedding classifier served by an NVIDIA model service. The heuristic check runs only on the LLMRails engine. If the detector is unreachable, requests are let through. **[Documented]**
Detail:
• Depends on the selected flow **[Documented]**
• Heuristics check length-per-perplexity (threshold 89.79) **[Documented]**
• Heuristics check prefix/suffix perplexity (threshold 1845.65, inputs over 20 words) **[Documented]**
• Heuristics use GPT-2-large with torch and transformers **[Documented]**
• In-process mode is for testing only **[Documented]**
• Production should set `server_endpoint` **[Documented]**
• Model flow uses a random forest on Snowflake Arctic embeddings **[Documented]**
• Model flow is called through the NemoGuard JailbreakDetect NIM (`nim_base_url`, `nim_server_endpoint`, `api_key_env_var`) **[Documented]**
• Engine support: heuristics run on LLMRails only (IORails blocks it) **[Documented]**
• Engine support: model flow runs on both engines **[Documented]**
• If the detector is unreachable the rail allows the request (fails open) **[Documented]**
• NIM training data is not published **[Not disclosed]**
• The docs list no third-party jailbreak backends **[Documented: none listed]**
### R5
Summary: **Block or allow outcome.** A blocked input gets a refusal message and the response stops, or an exception if exceptions are enabled. **[Documented]** No score is exposed. **[Documented: repo v0.24.1]** The decision threshold of the NVIDIA model service is not specified. **[Documented]** **[Not disclosed]**
Detail:
• Outcome is block or allow **[Documented]**
• On a block the bot replies "I'm sorry, I can't respond to that." and aborts **[Documented]**
• With `enable_rails_exceptions` set it raises `JailbreakDetectionRailException` instead **[Documented]**
• The underlying actions return a `RailOutcome` (`is_blocked`) **[Documented: repo v0.24.1]**
• The underlying actions expose no score **[Documented: repo v0.24.1]**
• The NIM is described as returning a binary result **[Documented]**
• The NIM threshold is not specified **[Not disclosed]**
### R6
Summary: **Jailbreak and benign user prompts.** Single-turn prompts suffice because only the current user message is checked. **[Documented: repo v0.24.1]** Benign test sets should include non-English text and code, which raise false positives. **[Inferred]** **[To be verified]**
Detail:
• Input: jailbreak and benign user prompts **[Documented: repo v0.24.1]**
• Single-turn prompts suffice because only the current user message is checked **[Documented: repo v0.24.1]**
• Reported heuristic performance: length/perplexity detects 31.19% with 7.44% FPR **[Documented]**
• Reported heuristic performance: prefix/suffix catches 49/50 GCG attacks at 0.04% FPR **[Documented]**
• Benign sets should include non-English text and code, which raise false positives **[Inferred]** **[To be verified]**
### R7
Summary: **Minimum setup:** test-data loader, configured NeMo input rail, selected detector, product adapter, result recorder and evaluator. The classifier option needs a reachable hosted or local model service and API key; the heuristic option needs a service for production-like runs, or torch and transformers for testing. A basic prompt-submission harness is sufficient. RAG, tool execution and multi-agent components are not required. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – test-data loader
  – configured NeMo input rail
  – selected flow
  – product adapter
  – result recorder
  – evaluator
• For the model flow, a reachable NIM (hosted or local) and API key are needed **[Inferred from the documented rail position]**
• For heuristics, a `server_endpoint` service is needed for production-like runs **[Inferred from the documented rail position]**
• For heuristics, torch and transformers are needed for in-process testing **[Inferred from the documented rail position]**
• A basic prompt-submission harness is sufficient **[Inferred from the documented rail position]**
• RAG, tool execution and multi-agent components are not required **[Inferred from the documented rail position]**
### R8
Summary: **Key open questions.** How a jailbreak is defined (not documented), which detector and engine will be used, and the fact that output is only blocked or allowed, with no score.
Detail:
• Selected flow (heuristics or model)
• Jailbreak definition (not documented)
• Engine (LLMRails or IORails)
• Thresholds (heuristics)
• NIM endpoint and API key
• `enable_rails_exceptions`
• Fail-open behaviour on detector outage
• Output format (blocked or allowed only, no score)
• English-only limitation
• torch/transformers dependencies
### R9
Summary: NVIDIA docs (Jailbreak protection guide, NemoGuard JailbreakDetect deployment tutorial, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/jailbreak-protection
• https://docs.nvidia.com/nemo/guardrails/get-started/tutorials/nemoguard-jailbreakdetect-deployment
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/jailbreak_detection/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/jailbreak_detection/actions.py

## Column A: NeMo Guardrails: Input-level content-safety moderation
### R1
Summary: **Input-level content-safety moderation.** Checks each user message against a safety policy before the main model runs, and blocks unsafe input. **[Documented]**
Detail:
• Checks each user message against a safety policy or taxonomy before the main LLM runs **[Documented]**
• Blocks unsafe input **[Documented]**
### R2
Summary: **Harmful or policy-violating user content.** Covers unsafe requests such as violence, crime, hate speech or sexual content, with categories set by the chosen model and prompt. **[Documented: example prompt in repo]** The authoritative category list is unconfirmed because two NVIDIA examples number it differently. **[To be verified]**
Detail:
• Addresses harmful or policy-violating user content **[Documented: example prompt in repo]**
• Addresses unsafe requests such as violence, criminal activity, hate speech or sexual content **[Documented: example prompt in repo]**
• The categories depend on the model and prompt chosen **[Documented: example prompt in repo]**
• A Nemotron example prompt in the repo notebook lists S1–S23 **[Documented: example prompt in repo]**
• The reasoning-model tutorial lists S1–S22 with different numbering **[To be verified]**
• The authoritative taxonomy is unconfirmed **[To be verified]**
### R3
Summary: **User message, before the main model.** Runs as an input check using one of three flows. A blocked message gets a refusal and the response stops, or an exception is raised if exceptions are enabled. **[Documented]**
Detail:
• Position: user message, before the main model **[Documented]**
• Input rail flows: **[Documented]**
  – `content safety check input $model=<type>`
  – `llama guard check input`
  – `self check input`
• A blocked message gets `bot refuse to respond` and `abort` **[Documented]**
• When `enable_rails_exceptions` is true, a rail exception is raised instead **[Documented]**
### R4
Summary: **A classifier LLM judges the message.** Options include Nemotron safety models, Llama Guard, ShieldGemma, or the main LLM itself; both runtime engines support the main checks. **[Documented]** One Nemotron model is not named on the docs page, and optional third-party services are listed. **[To be verified]**
Detail:
• A classifier LLM judges the message **[Documented]**
• Options: **[Documented]**
  – Nemotron content safety NIM (llama-3.1-nemoguard-8b-content-safety)
  – Nemotron-Content-Safety-Reasoning-4B (optional reasoning mode)
  – Llama Guard
  – ShieldGemma
  – the main LLM via `self_check_input` (Yes blocks; empty output blocks)
• Nemotron Safety Guard v3 is not named on the content-safety page **[To be verified]**
• Content safety, llama guard and self check input are supported on both LLMRails and IORails **[Documented]**
• Optional third-party backends: **[To be verified]**
  – ActiveFence (paid / non-OSS service)
  – Cisco AI Defense (paid / non-OSS service)
  – Prompt Security (paid / non-OSS service)
  – Fiddler (paid / non-OSS service)
  – Clavata (licensing to be verified)
  – PolicyAI (licensing to be verified)
  – CrowdStrike AIDR (paid / non-OSS service)
  – Trend Micro (paid / non-OSS service)
  – GCP Text Moderation (paid / non-OSS service)
  – Guardrails AI (open-source)
  – HF classifier (open-source)
### R5
Summary: **Allow or block decision.** The check reports whether the message is blocked, plus any policy violations found. Nemotron-style models return a safe or unsafe verdict with categories. **[Documented]**
Detail:
• Output is an allow or block decision **[Documented]**
• The action returns `is_blocked` plus `metadata.policy_violations` **[Documented]**
• The flow stores `$allowed` and `$policy_violations` **[Documented]**
• Nemotron-style output is a JSON-like safe/unsafe verdict with categories **[Documented]**
• The refusal can be localised when multilingual is enabled **[Documented]**
### R6
Summary: **User message text and a configured safety model.** Needs a model entry, a safety prompt and a reachable model endpoint. Reasoning models need a generous output token limit. **[Documented]**
Detail:
• Input: user message text; models configured in `models` **[Documented]**
• Needs a model entry whose `type` matches `$model` **[Documented]**
• Needs a prompt `content_safety_check_input $model=...` in `prompts.yml` **[Documented]**
• Needs an endpoint (NIM or OpenAI-compatible server such as vLLM) **[Documented]**
• Reasoning models need enough `max_tokens` (about 2048 suggested) **[Documented]**
### R7
Summary: **Minimum setup:** prompt-submission harness, labelled benign and harmful inputs, NeMo configuration with the chosen safety model and prompt, a reachable model endpoint, a stub or real main LLM, and a logger. Output-side, RAG and tool components are not required. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – prompt-submission harness
  – labelled benign and harmful inputs
  – NeMo config with the selected safety model and prompt
  – a reachable model endpoint
  – a stub or real main LLM
  – a logger for block, refusal and `policy_violations`
• Output-side, RAG and tool components are not required **[Inferred from the documented rail position]**
### R8
Summary: **Key open questions.** Production licence terms for the NVIDIA safety models and services, which of the two category lists is authoritative, and false-positive and false-negative rates.
Detail:
• NIM licence terms for production (AI Enterprise needed or not)
• Safety Guard v3 and Reasoning-4B licence terms
• S1–S22 vs S1–S23 taxonomy mismatch
• Whether the Nemotron-Safety-Guard-v3 model name is on the current docs page
• Vendor licensing
• Whether Llama Guard policy violations are populated
• Language coverage
• False positive and false negative rates
### R9
Summary: NVIDIA docs (Content safety, Self check, Third-party guides, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/content-safety
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/self-check
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/third-party
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/content_safety/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/llama_guard/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/self_check/input_check/flows.co

## Column B: NeMo Guardrails: Output-level content-safety moderation
### R1
Summary: **Output-level content-safety moderation.** Checks the model's generated response against a safety policy before it reaches the user. For Nemotron prompts the user turn is checked with it. **[Documented]**
Detail:
• Checks the model's generated response against a safety policy before it reaches the user **[Documented]**
• For Nemotron prompts, the user turn is checked along with the response **[Documented]**
### R2
Summary: **Unsafe or off-policy generated content.** Addresses harmful model responses that input checks missed. The categories depend on the chosen model and prompt. **[Documented]**
Detail:
• Addresses unsafe or off-policy generated content **[Documented]**
• Addresses harmful model responses that input checks missed **[Documented]**
• The categories depend on the chosen model and prompt **[Documented]**
### R3
Summary: **Bot response, after the main model.** Runs as an output check using one of three flows. A block gives a refusal and stops the response, or raises an exception if exceptions are enabled. **[Documented]**
Detail:
• Position: bot response, after the main model **[Documented]**
• Output rail flows: **[Documented]**
  – `content safety check output $model=<type>`
  – `llama guard check output`
  – `self check output`
• A block gives `bot refuse to respond` and `abort` **[Documented]**
• A rail exception is raised instead when `enable_rails_exceptions` is true **[Documented]**
### R4
Summary: **A classifier LLM judges the response.** It offers the same model options as the input check, and both runtime engines support the main checks. **[Documented]** When streaming, checks run on chunks of tokens. **[Documented]** Optional third-party services are listed, one of them input-only. **[To be verified]**
Detail:
• A classifier LLM judges the response **[Documented]**
• Same model options as input: Nemotron, Llama Guard, ShieldGemma, main LLM via `self_check_output` **[Documented]**
• With `self_check_output`, Yes blocks **[Documented]**
• With `self_check_output`, empty output blocks **[Documented]**
• With streaming, rails run on chunks of `chunk_size` tokens plus `context_size` carried tokens **[Documented]**
• Content safety, llama guard and self check output are supported on both LLMRails and IORails **[Documented]**
• Optional third-party backends: **[To be verified]**
  – ActiveFence (paid / non-OSS service)
  – Cisco AI Defense (paid / non-OSS service)
  – Prompt Security (paid / non-OSS service)
  – Fiddler (paid / non-OSS service)
  – Clavata (licensing to be verified)
  – PolicyAI (licensing to be verified)
  – CrowdStrike AIDR (paid / non-OSS service)
  – Trend Micro (paid / non-OSS service)
  – Guardrails AI (open-source)
  – HF classifier (open-source)
• GCP Text Moderation is input only per the page **[To be verified]**
### R5
Summary: **Allow or block decision.** The check reports whether the response is blocked, plus any policy violations. With streaming, a block can end the stream after some text has already been sent, unless checks are set to run before release. **[Documented]**
Detail:
• Output is an allow or block decision **[Documented]**
• Result is `is_blocked` plus `metadata.policy_violations` **[Documented]**
• In streaming with `stream_first: true`, a block terminates the stream with a JSON error after tokens were already sent **[Documented]**
• With `stream_first: false` rails run before tokens are released **[Documented]**
### R6
Summary: **Bot response text, usually with the user input.** Needs a model entry, a safety prompt and an endpoint. Streaming needs extra configuration and has default chunk settings. **[Documented]**
Detail:
• Input: bot response text, usually with the user input **[Documented]**
• Needs a model entry **[Documented]**
• Needs prompt `content_safety_check_output $model=...` or `self_check_output` using `{{ bot_response }}` **[Documented]**
• Needs an endpoint **[Documented]**
• Streaming needs `rails.output.streaming.enabled: true` **[Documented]**
• Streaming needs `stream_async()` **[Documented]**
• Defaults: chunk_size 200 **[Documented]**
• Defaults: context_size 50 **[Documented]**
• Defaults: stream_first true **[Documented]**
### R7
Summary: **Minimum setup:** prompt harness with a main LLM or scripted unsafe responses, prompts known to elicit unsafe output, output-rail configuration with the safety model, an endpoint and a logger. Streaming tests also need a client that records released and blocked chunks. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – prompt harness with a main LLM (or scripted unsafe responses)
  – prompts known to elicit unsafe output
  – NeMo output rail config with the safety model
  – endpoint
  – logger
• Streaming tests also need a streaming client that records released and blocked chunks **[Inferred from the documented rail position]**
### R8
Summary: **Key open questions.** Whether unsafe text leaks before a block at different chunk sizes, how violations spanning chunk boundaries are handled, and exact streaming support on each engine.
Detail:
• Whether unsafe text leaks before blocking at various chunk sizes
• Behaviour when a violation spans chunk boundaries
• Exact streaming support per engine (LLMRails vs IORails)
• Whether `self check output` is supported in streaming with every variant
• NIM licence terms
• Vendor licensing
• Llama Guard policy violation metadata
### R9
Summary: NVIDIA docs (Content safety, Self check, Third-party guides, configuration reference v0.22.0, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/content-safety
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/self-check
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/third-party
• https://docs.nvidia.com/nemo/guardrails/v0.22.0/configure-guardrails/configuration-reference
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/content_safety/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/self_check/output_check/flows.co

## Column C: NeMo Guardrails: Input-level topic control
### R1
Summary: **Input-level topic control.** Checks whether a user message stays within the topics the application allows, and blocks off-topic messages. **[Documented]**
Detail:
• Checks whether a user message stays within the topics the application allows **[Documented]**
• Blocks off-topic messages **[Documented]**
### R2
Summary: **Off-topic or out-of-scope requests.** Addresses conversations drifting outside the policy written in the system prompt. It is not a general harm detector. **[Inferred]**
Detail:
• Addresses off-topic or out-of-scope requests **[Inferred]**
• Addresses conversations drifting outside the policy written in the system prompt **[Inferred]**
• It is not a general harm detector **[Inferred]**
### R3
Summary: **User message, before the main model.** A single input check. A blocked message gets a refusal and the response stops, or a specific exception if exceptions are enabled. **[Documented]**
Detail:
• Position: user message, before the main model **[Documented]**
• Input rail flow `topic safety check input $model=topic_control` **[Documented]**
• A block gives `bot refuse to respond` and `abort` **[Documented]**
• With `enable_rails_exceptions` true, `TopicSafetyCheckInputException` is raised instead **[Documented]**
• Sets `$on_topic` **[Documented]**
### R4
Summary: **A topic-control model classifies the message.** An NVIDIA topic-control model judges the message as on-topic or off-topic against a policy in the system prompt, and off-topic is blocked. Both runtime engines support it. **[Documented]** No third-party backends are documented. **[To be verified]**
Detail:
• A topic-control model classifies the message **[Documented]**
• NemoGuard Topic Control NIM (llama-3.1-nemoguard-8b-topic-control, engine `nim`) must answer `on-topic` or `off-topic` against a policy in the system prompt **[Documented]**
• The output restriction is appended automatically **[Documented]**
• Off-topic is blocked **[Documented]**
• Supported on both LLMRails and IORails **[Documented]**
• No third-party backends are documented for this function **[To be verified]**
### R5
Summary: **Allow or block decision.** The check returns a blocked flag, and the flow records whether the message was on topic before refusing or raising the exception. **[Documented]**
Detail:
• Output is an allow or block decision **[Documented]**
• The action returns `is_blocked` **[Documented]**
• The flow sets `$on_topic` **[Documented]**
• The flow either refuses or raises the exception **[Documented]**
### R6
Summary: **User message plus an allowed-topic policy.** Needs a topic-control model entry, a running model endpoint and a prompt holding the policy. Whether conversation history is used is not stated. **[Documented]**
Detail:
• Input: user message plus an allowed-topic policy **[Documented]**
• Needs a model entry `type: topic_control` **[Documented]**
• Needs a running NIM endpoint (example `http://localhost:8123/v1`) **[Documented]**
• Needs a topic-safety prompt in `prompts.yml` with the policy **[Documented]**
• Conversation history use is not stated **[Documented]**
### R7
Summary: **Minimum setup:** harness, on-topic and off-topic test sets including borderline cases, NeMo configuration with a topic-control model and policy prompt, a model endpoint and a result recorder. A stub main LLM is sufficient. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – harness
  – on-topic and off-topic test sets including borderline cases
  – NeMo config with topic-control model and policy prompt
  – NIM endpoint
  – result recorder
• A stub main LLM is sufficient **[Inferred from the documented rail position]**
### R8
Summary: **Key open questions.** Licence and AI Enterprise requirements, performance and false-positive rates (not published), and how multi-turn conversations are handled.
Detail:
• NIM licence and AI Enterprise requirement
• Performance and false-positive rates (not published on the page)
• Multi-turn behaviour
• Policy-prompt sensitivity
• Custom topic models
• IORails parity
### R9
Summary: NVIDIA docs (Topic control guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/topic-control
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/topic_safety/flows.co

## Column D: NeMo Guardrails: Dialog-level conversational flow control
### R1
Summary: **Dialog-level conversational flow control.** Steers multi-turn conversations by mapping user messages to intents and enforcing the bot's next step through Colang flows. **[Documented]**
Detail:
• Steers multi-turn conversations **[Documented]**
• Maps user messages to intents **[Documented]**
• Enforces the bot's next step through Colang flows **[Documented]**
### R2
Summary: **Off-topic or disallowed conversation paths.** Addresses topics or dialog paths the designer defines, for example refusing cooking questions. It covers only what has been defined. **[Documented]**
Detail:
• Addresses off-topic or disallowed conversation paths **[Documented]**
• Addresses topics or dialog paths the designer defines, for example refusing cooking questions **[Documented]**
• It covers only what has been defined **[Documented]**
### R3
Summary: **Conversation stage, after input rails.** Designer-written rules bind a user intent to a canned bot response. The pipeline runs intent generation, next step, then bot message. **[Documented]**
Detail:
• Position: conversation stage, after input rails **[Documented]**
• Colang `define user ...` and `define flow ...` bind an intent to a canned bot response (for example `bot refuse to respond about cooking`) **[Documented]**
• Pipeline: intent generation, next step, bot message **[Documented]**
### R4
Summary: **Intent matching by embeddings and/or LLM.** It matches similar example messages, then asks the LLM for the intent, or uses the closest match alone. **[Documented]** The engine support table does not cover dialog rails. **[Not disclosed]** No third-party backends are documented. **[To be verified]**
Detail:
• Intent matching by embeddings and/or LLM **[Documented]**
• `generate_user_intent` finds similar user examples in a vector store, then asks the LLM for the intent **[Documented]**
• With `rails.dialog.user_messages.embeddings_only: true` the closest embedding match is used without the LLM **[Documented]**
• `rails.dialog.single_call.enabled` merges intent and response into one call **[Documented]**
• The LLMRails vs IORails support matrix does not cover dialog rails **[Not disclosed]**
• No third-party backends are documented for this function **[To be verified]**
### R5
Summary: **Intent, next step and bot message.** The output is the canned or generated bot reply, such as a polite refusal. It is not a pass or fail result like the other rails. **[Documented]**
Detail:
• Output is intent, next step and bot message **[Documented]**
• Output is the canned or generated bot reply, such as "I'm sorry, I cannot respond to that." **[Documented]**
• It is not a pass/fail result object like the other rails **[Documented]**
### R6
Summary: **Conversation history, Colang definitions and an embeddings model.** Needs example utterances in Colang files, a main LLM unless matching by embeddings only, and an embedding index. Optional similarity threshold and fallback intent. **[Documented]**
Detail:
• Input: conversation history, Colang definitions and an embeddings model **[Documented]**
• Needs Colang files with example utterances **[Documented]**
• Needs a main LLM unless embeddings-only **[Documented]**
• Needs an embedding index **[Documented]**
• Defaults: single_call false **[Documented]**
• Defaults: embeddings_only false **[Documented]**
• Optional `embeddings_only_similarity_threshold` **[Documented]**
• Optional fallback intent **[Documented]**
### R7
Summary: **Minimum setup:** harness, Colang configuration with at least one off-topic user intent and refusal flow, main LLM, embedding model, paraphrase and multi-turn test sets, and a recorder. Content-safety and topic-control model services are not needed. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – harness
  – Colang config with at least one off-topic user intent and refusal flow
  – main LLM
  – embedding model
  – paraphrase and multi-turn test sets
  – recorder
• Content-safety and topic NIMs are not needed **[Inferred from the documented rail position]**
### R8
Summary: **Key open questions.** How robust intent matching is to paraphrase and adversarial phrasing, whether IORails supports dialog rails, and the latency and extra LLM calls.
Detail:
• Robustness to paraphrase and adversarial phrasing
• Embeddings-only threshold tuning
• Whether single-call mode changes accuracy
• Colang 1.0 vs 2.x differences
• Dialog-rail support in IORails (the support matrix lists only input, output and retrieval surfaces)
• Latency and extra LLM calls
### R9
Summary: NVIDIA docs (Colang topical rails tutorial, Rail types and Configuration reference for v0.22.0, Rail engine support).
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/colang/colang-1/tutorials/6-topical-rails
• https://docs.nvidia.com/nemo/guardrails/v0.22.0/about-nemo-guardrails-library/rail-types
• https://docs.nvidia.com/nemo/guardrails/v0.22.0/configure-guardrails/configuration-reference
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support

## Column E: NeMo Guardrails: Input-level PII detection & masking
### R1
Summary: **Input-level PII detection and masking.** Scans each user message for personal or sensitive details before the main model runs. Detect options block the message; mask options rewrite it. **[Documented]**
Detail:
• Scans each user message for personal or sensitive entities before the main LLM runs **[Documented]**
• Detect flows block the message **[Documented]**
• Mask flows rewrite the message **[Documented]**
### R2
Summary: **Personal data in user prompts.** Addresses users pasting names, emails, card or ID numbers and similar details that would otherwise reach the LLM, logs or tools. Coverage depends on the backend and configured entity list. **[Inferred]**
Detail:
• Addresses personal data in user prompts **[Inferred]**
• Addresses users pasting names, emails, card or ID numbers, or similar entities **[Inferred]**
• Such entities would otherwise reach the LLM, logs or tools **[Inferred]**
• Coverage depends on the backend and the configured entity list **[Inferred]**
### R3
Summary: **User message, before the main model.** Four families of checks (Presidio, GLiNER, Private AI, Polygraf) each have a detect version and a mask version. **[Documented]** Detect stops the response with a refusal-style reply; mask rewrites the message. **[Documented: repo v0.24.1]**
Detail:
• Position: user message, before the main model **[Documented]**
• Flows: **[Documented]**
  – `detect sensitive data on input` / `mask sensitive data on input` (Presidio)
  – `gliner detect pii on input` / `gliner mask pii on input`
  – `detect pii on input` / `mask pii on input` (Private AI)
  – `polygraf detect pii on input` / `polygraf mask pii on input`
• Detect: `bot inform answer unknown` (GLiNER: `bot refuse to respond`), then `abort` **[Documented: repo v0.24.1]**
• Mask: rewrites `$user_message` **[Documented: repo v0.24.1]**
### R4
Summary: **Entity recognition by a local library or remote service.** Presidio runs locally; GLiNER, Private AI and Polygraf call a configured service. Masking replaces the matched text. **[Documented: repo v0.24.1]** All input flows run on both engines. **[Documented]** Backend licensing is partly unverified. **[To be verified]**
Detail:
• Entity recognition by a local library or remote service **[Documented: repo v0.24.1]**
• Presidio analyses text with spaCy `en_core_web_lg` **[Documented: repo v0.24.1]**
• GLiNER-PII, Private AI and Polygraf are HTTP calls to a configured `server_endpoint` **[Documented: repo v0.24.1]**
• Masking replaces spans: **[Documented: repo v0.24.1]**
  – GLiNER uses `[LABEL]` such as `[FIRST_NAME]`
  – Polygraf uses `<TYPE>`
  – Presidio uses its default replace operator
• Engine support: all input flows run on LLMRails and IORails **[Documented]**
• Rewriting rails force sequential execution under IORails **[Documented]**
• Rewriting rails turn off speculative generation under IORails **[Documented]**
• Optional third-party backends: **[To be verified]**
  – Presidio (open-source)
  – GLiNER-PII NIM (NVIDIA-hosted API key or self-hosted; paid status to be verified)
  – Private AI (paid / non-OSS service)
  – Polygraf (licensing to be verified; not on the PII docs page)
### R5
Summary: **Block decision or rewritten message.** Detect checks report a blocked result; mask checks return the rewritten message along with the original and masked text. If nothing changes, the message is allowed. **[Documented: repo v0.24.1]**
Detail:
• Output is a block decision or a rewritten message **[Documented: repo v0.24.1]**
• Detect actions return `is_blocked` (metadata `has_sensitive_data` or `has_pii`) **[Documented: repo v0.24.1]**
• Mask actions return `is_transform` with `transform_text["user_message"]` **[Documented: repo v0.24.1]**
• Mask actions return `metadata` holding the original and masked text **[Documented: repo v0.24.1]**
• If nothing changes the result is allow **[Documented: repo v0.24.1]**
### R6
Summary: **User message text plus backend settings.** Each backend needs its own configuration: entity lists and Python packages for Presidio, or a running endpoint and, for some, an API key for the others. **[Documented]**
Detail:
• Input: user message text plus backend config **[Documented]**
• Presidio: `rails.config.sensitive_data_detection.input.{entities, mask_token, score_threshold}` **[Documented]**
• Presidio: needs `presidio-analyzer`, `presidio-anonymizer`, spaCy and `en_core_web_lg` **[Documented]**
• GLiNER: `rails.config.gliner` with `threshold` default 0.5 **[Documented]**
• GLiNER: needs a running endpoint **[Documented]**
• Private AI: `server_endpoint` and entities **[Documented]**
• Private AI: `PAI_API_KEY` for the cloud API **[Documented]**
• Polygraf: `server_endpoint` and `POLYGRAF_API_KEY` **[Documented]**
### R7
Summary: **Minimum setup:** prompt harness, test prompts with synthetic PII of known types and clean controls, NeMo configuration with one backend and entity list, any service or model that backend needs, a stub main LLM, and a recorder of blocked, masked and forwarded text. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – prompt harness
  – test prompts with synthetic PII of known types and clean controls
  – a NeMo config with one chosen backend and entity list
  – any backend service or model it needs
  – a stub main LLM
  – a recorder for blocked, masked and forwarded text
### R8
Summary: **Key open questions.** The Presidio masking text is unverified, the mask path ignores the configured score threshold, backend licensing is unclear, and behaviour when a backend is unreachable is mostly unchecked.
Detail:
• `mask_token` is marked unused in the code so the Presidio masking text is unverified
• The mask path builds the analyzer at default threshold 0.4 rather than the configured score_threshold
• spaCy install steps not seen on the docs page
• GLiNER-PII NIM licensing and whether it is open
• Private AI and Polygraf pricing
• Polygraf absent from the docs page
• Recall and precision per entity type and language
• Behaviour when a backend is unreachable (Polygraf fails closed per repo v0.24.1, others not checked)
• No `enable_rails_exceptions` path found in these flows
### R9
Summary: NVIDIA docs (PII detection guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/pii-detection
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/sensitive_data_detection/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/sensitive_data_detection/actions.py
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/gliner/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/privateai/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/polygraf/flows.co

## Column F: NeMo Guardrails: Output-level PII detection & masking
### R1
Summary: **Output-level PII detection and masking.** Scans the model's response for personal or sensitive details before it reaches the user. Detect options block the response; mask options rewrite it. **[Documented]**
Detail:
• Scans the model's response for personal or sensitive entities before it reaches the user **[Documented]**
• Detect flows block the response **[Documented]**
• Mask flows rewrite the response **[Documented]**
### R2
Summary: **Personal data leaking in generated text.** Addresses the LLM repeating personal data from the prompt, context or training data. Coverage depends on the backend and entity list. **[Inferred]**
Detail:
• Addresses personal data leaking in generated text **[Inferred]**
• Addresses the LLM repeating PII from the prompt, context or training data **[Inferred]**
• Coverage depends on the backend and entity list **[Inferred]**
### R3
Summary: **Bot response, after the main model.** Four families of checks (Presidio, GLiNER, Private AI, Polygraf) each have a detect and a mask version. **[Documented]** Detect stops the response with a refusal-style reply; mask rewrites it. **[Documented: repo v0.24.1]**
Detail:
• Position: bot response, after the main model **[Documented]**
• Flows: **[Documented]**
  – `detect sensitive data on output` / `mask sensitive data on output`
  – `gliner detect pii on output` / `gliner mask pii on output`
  – `detect pii on output` / `mask pii on output`
  – `polygraf detect pii on output` / `polygraf mask pii on output`
• Detect gives `bot inform answer unknown` (GLiNER: `bot refuse to respond`) and `abort` **[Documented: repo v0.24.1]**
• Mask rewrites `$bot_message` **[Documented: repo v0.24.1]**
### R4
Summary: **Same recognisers as input, applied to the bot message.** The four backends are reused with output-specific entity lists. **[Documented]** All output flows run on both engines. **[Documented]** Backend licensing is partly unverified. **[To be verified]**
Detail:
• Same recognisers as input, applied to `$bot_message` **[Documented]**
• Backends are Presidio (spaCy), GLiNER-PII, Private AI and Polygraf **[Documented]**
• Entities are set under `...output.entities` **[Documented]**
• Engine support: all output flows run on LLMRails and IORails **[Documented]**
• Under IORails a rewriting rail forces sequential execution **[Documented]**
• Output rewrites with streaming require `stream_first: false` **[Documented]**
• Optional third-party backends: **[To be verified]**
  – Presidio (open-source)
  – GLiNER-PII NIM (API key or self-hosted; paid status to be verified)
  – Private AI (paid / non-OSS service)
  – Polygraf (licensing to be verified)
### R5
Summary: **Block decision or rewritten response.** Detect checks report a blocked result; mask checks return the rewritten response with source, original and masked text. Otherwise the response is allowed. **[Documented: repo v0.24.1]**
Detail:
• Output is a block decision or a rewritten response **[Documented: repo v0.24.1]**
• Detect returns `is_blocked` **[Documented: repo v0.24.1]**
• Mask returns `is_transform` with `transform_text["bot_message"]` **[Documented: repo v0.24.1]**
• Mask returns `metadata` (source, original, masked text) **[Documented: repo v0.24.1]**
• Otherwise allow **[Documented: repo v0.24.1]**
### R6
Summary: **Bot response text plus backend settings.** Each backend has its own output entity list, plus the endpoint and API key settings used for input. **[Documented]**
Detail:
• Input: bot response text plus backend config **[Documented]**
• Presidio uses `rails.config.sensitive_data_detection.output.{entities, mask_token, score_threshold}` **[Documented]**
• GLiNER, Private AI and Polygraf use their own `output` entity lists **[Documented]**
• GLiNER, Private AI and Polygraf use the endpoint and API key settings described for input **[Documented]**
### R7
Summary: **Minimum setup:** harness, a main LLM or scripted responses containing synthetic PII, clean controls, output-rail configuration with one backend, that backend's service or model, and a recorder of the final user-visible text. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – harness
  – a main LLM or scripted responses containing synthetic PII
  – clean controls
  – a NeMo output rail config with one backend
  – the backend service or model
  – a recorder for the final user-visible text
### R8
Summary: **Key open questions.** Whether personal data is released during streaming before masking, how well it catches model-generated personal data, and backend licensing and pricing.
Detail:
• Streaming behaviour of mask rails (whether PII is released before rewrite)
• `mask_token` unused in code
• Presidio default replacement text
• Recall on model-generated PII
• Backend licensing and pricing
• Polygraf docs coverage
• No exception path seen in these flows
### R9
Summary: NVIDIA docs (PII detection guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/pii-detection
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/sensitive_data_detection/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/gliner/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/privateai/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/polygraf/flows.co

## Column G: NeMo Guardrails: Retrieval-level chunk filtering
### R1
Summary: **Retrieval-level chunk filtering.** Checks or rewrites the knowledge-base chunks retrieved for a turn before they reach the prompt. **[Documented]**
Detail:
• Checks or rewrites the knowledge-base chunks retrieved for a turn **[Documented]**
• This happens before the chunks reach the prompt **[Documented]**
### R2
Summary: **Poisoned, sensitive or padded retrieved content.** Addresses personal data in chunks, forbidden patterns, padding that bloats the context, and text flagged by a classifier in retrieval sources. **[Inferred]**
Detail:
• Addresses poisoned, sensitive or padded retrieved content **[Inferred]**
• Addresses PII in chunks **[Inferred]**
• Addresses forbidden patterns **[Inferred]**
• Addresses context-bloat padding **[Inferred]**
• Addresses classifier-flagged text in RAG sources **[Inferred]**
### R3
Summary: **Retrieved chunks, after retrieval and before generation.** Configured as a list of retrieval checks, with seven kinds of check found in the v0.24.1 code. **[Documented: repo v0.24.1]**
Detail:
• Position: `$relevant_chunks`, after retrieval and before generation **[Documented: repo v0.24.1]**
• Configured under `rails.retrieval.flows` **[Documented: repo v0.24.1]**
• Flows found in v0.24.1: **[Documented: repo v0.24.1]**
  – `detect/mask sensitive data on retrieval`
  – `gliner detect/mask pii on retrieval`
  – `detect/mask pii on retrieval`
  – `polygraf detect/mask pii on retrieval`
  – `regex check retrieval`
  – `context bloat detection on retrieval`
  – `hf classifier check retrieval $classifier`
### R4
Summary: **Depends on the flow.** Options are a personal-data backend, a pattern match, size statistics or a Hugging Face classifier. Detect options stop the response; pattern and classifier options blank the chunks. **[Documented: repo v0.24.1]** Runs on the LLMRails engine only. **[Documented]** Backend licensing is partly unverified. **[To be verified]**
Detail:
• Depends on the flow: PII backend, regex, bloat statistics or HF classifier **[Documented: repo v0.24.1]**
• Detect flows block and abort **[Documented: repo v0.24.1]**
• Regex and HF retrieval flows blank the chunks instead of blocking **[Documented: repo v0.24.1]**
• Engine support: LLMRails only **[Documented]**
• IORails does not accept a `rails.retrieval` section **[Documented]**
• A config declaring a `rails.retrieval` section routes to LLMRails by default **[Documented]**
• Optional third-party backends: **[To be verified]**
  – Presidio (open-source)
  – GLiNER-PII NIM (paid status to be verified)
  – Private AI (paid / non-OSS service)
  – Polygraf (licensing to be verified)
  – HF classifier (local or hosted engine; open-source locally)
### R5
Summary: **Chunks kept, rewritten, emptied or turn blocked.** Block options answer with an "answer unknown" style reply, or a retrieval-bloated message for padding. **[Documented: repo v0.24.1]**
Detail:
• Outcome: chunks kept, rewritten, emptied or turn blocked **[Documented: repo v0.24.1]**
• Actions expose `is_blocked`, `is_transform`, `transform_text["relevant_chunks"]` and `metadata` **[Documented: repo v0.24.1]**
• Block flows answer `bot inform answer unknown` **[Documented: repo v0.24.1]**
• For bloat, block flows answer `bot inform retrieval bloated` **[Documented: repo v0.24.1]**
### R6
Summary: **Retrieved chunks plus a knowledge base.** Needs a knowledge base or custom retrieval step that fills the retrieved chunks, the retrieval checks list, and the settings of the chosen check. **[Inferred]**
Detail:
• Input: retrieved chunks plus a knowledge base **[Inferred]**
• Needs a knowledge base or custom retrieval action filling `relevant_chunks` **[Inferred]**
• Needs `rails.retrieval.flows` **[Inferred]**
• Needs the per-flow config of the chosen rail **[Inferred]**
### R7
Summary: **Minimum setup:** small knowledge base with clean chunks and seeded bad chunks (personal data, forbidden pattern, padding), configuration with retrieval checks, the LLMRails engine, a stub or real LLM, and a log of the chunks passed to the prompt. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – small knowledge base with clean chunks and seeded bad chunks (PII, forbidden pattern, padding)
  – NeMo config with `rails.retrieval.flows`
  – LLMRails
  – a stub or real LLM
  – a log of the chunks passed to the prompt
### R8
Summary: **Key open questions.** Whether blanking removes one chunk or all of them (the code blanks everything), how custom retrievers behave, and whether chunks are checked one by one or joined.
Detail:
• Whether the HF retrieval flow is documented on the PII or agentic pages
• Whether regex or HF empty-chunk behaviour drops one chunk or all (code blanks the whole `relevant_chunks` string)
• Chunk size limits
• Backend licensing
• Behaviour with custom retrievers
• Per-chunk versus joined checking
### R9
Summary: NVIDIA docs (Rail engine support, PII detection, Regex and Agentic security guides) and NeMo Guardrails v0.24.1 source code on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/pii-detection
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/third-party/regex
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/agentic-security
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/regex/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/context_bloat_detection/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/hf_classifier/flows.co

## Column H: NeMo Guardrails: Regex pattern blocklist (input/output)
### R1
Summary: **Regex pattern blocklist.** Blocks a user message or bot response that matches any configured regular expression. **[Documented]**
Detail:
• Blocks a user message or bot response that matches any configured regular expression **[Documented]**
### R2
Summary: **Known forbidden strings or formats.** Addresses fixed patterns such as banned phrases, secret formats or identifiers. It cannot catch paraphrases. **[Inferred]**
Detail:
• Addresses known forbidden strings or formats **[Inferred]**
• Addresses fixed patterns such as banned phrases, secrets formats or identifiers **[Inferred]**
• It cannot catch paraphrases **[Inferred]**
### R3
Summary: **User message or bot response.** Separate input and output checks. **[Documented]** A match gives a refusal and stops the response. A retrieval variant also exists and blanks matching chunks. **[Documented: repo v0.24.1]**
Detail:
• Position: user message or bot response **[Documented]**
• Flows `regex check input` and `regex check output` **[Documented]**
• A match gives `bot refuse to respond` and `abort` **[Documented: repo v0.24.1]**
• `regex check retrieval` also exists **[Documented: repo v0.24.1]**
• `regex check retrieval` blanks matching chunks **[Documented: repo v0.24.1]**
### R4
Summary: **Pattern matching, no model.** Each pattern is tested against the text and all matching patterns are reported. **[Documented: repo v0.24.1]** It is built into NeMo, needs no extra package and runs on both engines for input and output. **[Documented]** No third-party backends are documented. **[To be verified]**
Detail:
• Pattern matching, no model **[Documented: repo v0.24.1]**
• Each pattern is compiled once and tested with `search` **[Documented: repo v0.24.1]**
• All matching patterns are listed in `detections` **[Documented: repo v0.24.1]**
• `case_insensitive` defaults to false **[Documented]**
• The feature is built into the NeMo Guardrails library and needs no extra package **[Documented]**
• It is not a third-party service **[Documented]**
• Engine support: input and output flows run on LLMRails and IORails **[Documented]**
• Engine support: retrieval is LLMRails only **[Documented]**
• No third-party backends are documented **[To be verified]**
### R5
Summary: **Block decision.** The result says whether the text was blocked and lists the matched patterns. The flow does not switch to an exception when exceptions are enabled. **[Documented: repo v0.24.1]**
Detail:
• Output is a block decision **[Documented: repo v0.24.1]**
• Result is `is_blocked` plus metadata `is_match`, `text`, `detections` (matching patterns) and `source` **[Documented: repo v0.24.1]**
• The flow does not branch on `enable_rails_exceptions` **[Documented: repo v0.24.1]**
### R6
Summary: **Text plus pattern list.** Needs a list of regular-expression patterns for each position and an optional case-insensitive flag. No models or keys are needed. **[Documented]**
Detail:
• Input: text plus pattern list **[Documented]**
• `rails.config.regex_detection.{input,output,retrieval}.patterns` (list of regex strings) **[Documented]**
• `case_insensitive` **[Documented]**
• No models or keys **[Documented]**
### R7
Summary: **Minimum setup:** harness, strings that match and do not match each pattern, a configuration with patterns for input and output, a stub LLM that returns scripted text, and a result recorder. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – harness
  – strings that match and do not match each pattern
  – a config with `patterns` for input and output
  – a stub LLM that returns scripted text
  – a result recorder
### R8
Summary: **Key open questions.** How the docs describe the matching method, how slow or unsafe patterns are handled, and how Unicode and other regex flags are treated.
Detail:
• Whether the docs page states the matching function (code uses `search`)
• ReDoS or regex timeout handling
• Flag handling beyond case
• Unicode normalisation
• Behaviour on empty patterns or missing section (code logs and allows)
• The multiline flag
• Per-tool regex on tool-call arguments and results (`regex check tool output`, `regex check tool input`) appears in develop-branch docs but not in v0.24.1 (the v0.24.1 manifest lists only the input, output and retrieval flows) and not on the live docs page
### R9
Summary: NVIDIA docs (Regex guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/third-party/regex
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/regex/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/regex/actions.py

## Column I: NeMo Guardrails: Output-level injection detection
### R1
Summary: **Output-level injection detection.** Scans the bot's output for code, SQL, template or cross-site scripting payloads before it is passed on. **[Documented]**
Detail:
• Scans the bot's output for code, SQL, template or XSS injection payloads **[Documented]**
• The scan happens before the output is passed on **[Documented]**
### R2
Summary: **Exploit strings in generated output.** Addresses model output that could run as code or queries in downstream systems, mainly in agentic setups. The docs call it defence-in-depth, not a standalone control. **[Documented]**
Detail:
• Addresses exploit strings in generated output **[Documented]**
• Addresses model output that could run as code or queries in downstream systems **[Documented]**
• Mainly relevant in agentic setups **[Documented]**
• The docs call it defense-in-depth, not a standalone control **[Documented]**
### R3
Summary: **Bot message, after the main model.** A single output-only check. **[Documented]**
Detail:
• Position: bot message, after the main model **[Documented]**
• Output rail flow `injection detection` **[Documented]**
• It is output only **[Documented]**
### R4
Summary: **YARA rule matching.** Built-in rules cover code, SQL, template and cross-site scripting, with optional custom rules. The reject option blocks; the omit option strips matched text. **[Documented]** It runs on both engines. **[Documented]** YARA being open-source is unverified. **[To be verified]**
Detail:
• YARA rule matching **[Documented]**
• Rules named `code`, `sqli`, `template`, `xss` ship with the library **[Documented]**
• Optional custom `yara_path` or inline `yara_rules` **[Documented]**
• `reject` blocks **[Documented]**
• `omit` strips the matched text **[Documented]**
• Engine support: runs on LLMRails and IORails **[Documented]**
• No third-party backends **[To be verified]**
• YARA is open-source **[To be verified]**
### R5
Summary: **Block, stripped text or allow.** On reject, the bot says the output triggered a rule and stops, or raises an exception if exceptions are enabled. **[Documented: repo v0.24.1]**
Detail:
• Outcome: block, stripped text or allow **[Documented: repo v0.24.1]**
• Metadata holds `is_injection`, `text`, `detections` and `action` **[Documented: repo v0.24.1]**
• On reject the flow says "I'm sorry, the desired output triggered rule(s)..." and aborts **[Documented: repo v0.24.1]**
• When `enable_rails_exceptions` is true, it sends `InjectionDetectionRailException` instead **[Documented: repo v0.24.1]**
### R6
Summary: **Bot message text plus configuration.** Needs injection settings, the output check enabled, and the YARA Python package. **[Documented]**
Detail:
• Input: bot message text plus config **[Documented]**
• `rails.config.injection_detection.{injections, action, yara_path, yara_rules}` **[Documented]**
• `rails.output.flows: [injection detection]` **[Documented]**
• Needs `yara-python` (docs: `pip install nemoguardrails[jailbreak]`) **[Documented]**
### R7
Summary: **Minimum setup:** harness, scripted bot outputs containing code, SQL, template and XSS payloads plus benign controls, configuration with chosen injection types and action, the YARA package, and a recorder. No retrieval or input checks are needed. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – harness
  – scripted bot outputs containing code, SQL, template and XSS payloads plus benign controls
  – config with the chosen injections and action
  – `yara-python`
  – a recorder
• No retrieval or input rails needed **[Inferred from the documented rail position]**
### R8
Summary: **Key open questions.** The code accepts a third action that fails, how well the omit option really removes payloads, and false positives on legitimate code answers.
Detail:
• A `sanitize` action is accepted by the code validation but raises NotImplementedError
• The docs list only reject and omit
• Default action value
• Omit effectiveness (code says it may not be fully effective)
• False positives on code answers
• YARA rule coverage
• Whether `bot say` text leaks the matched rule names
### R9
Summary: NVIDIA docs (Agentic security guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/agentic-security
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/injection_detection/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/injection_detection/actions.py

## Column J: NeMo Guardrails: Context-bloat detection (input)
### R1
Summary: **Input-level context-bloat detection.** Flags oversized, padded or repetitive user messages before they reach the main LLM. **[Documented]**
Detail:
• Flags oversized, padded or repetitive user messages **[Documented]**
• This happens before the messages reach the main LLM **[Documented]**
### R2
Summary: **Context-manipulation padding.** Addresses long or repetitive input meant to bury instructions, make the model forget its system prompt, or burn the token budget. **[Documented]**
Detail:
• Addresses context-manipulation padding **[Documented]**
• Addresses long or repetitive input meant to bury instructions **[Documented]**
• Addresses long or repetitive input meant to make the model forget its system prompt **[Documented]**
• Addresses long or repetitive input meant to burn the token budget **[Documented]**
### R3
Summary: **User message, before the main model.** A reject says the message appears oversized or padded and stops the response. A retrieval variant also exists. **[Documented: repo v0.24.1]**
Detail:
• Position: user message, before the main model **[Documented: repo v0.24.1]**
• Flow `context bloat detection on input` **[Documented: repo v0.24.1]**
• A retrieval variant exists **[Documented: repo v0.24.1]**
• A reject says the message "appears oversized or padded" and aborts **[Documented: repo v0.24.1]**
### R4
Summary: **Statistical checks, no model.** Checks message size, randomness, repeated characters and repeated phrases, in that order. **[Documented: repo v0.24.1]** The action can reject, truncate or warn. **[Documented]** The input check runs on both engines. **[Documented]** No third-party backends. **[To be verified]**
Detail:
• Statistical checks, no model **[Documented: repo v0.24.1]**
• Checks in order: size cap, Shannon entropy, longest single-character run, repeated n-grams **[Documented: repo v0.24.1]**
• Defaults: **[Documented]**
  – max_chars 5000
  – min_entropy 3.5
  – max_repetition_ratio 0.4
  – max_run_ratio 0.1
• `action` is `reject`, `truncate` or `warn` **[Documented]**
• Engine support: input flow runs on LLMRails and IORails **[Documented]**
• Engine support: the retrieval flow is LLMRails only **[Documented]**
• No third-party backends **[To be verified]**
### R5
Summary: **Block, truncated message or allow.** Reject blocks, truncate shortens the message, and warn lets it through with the findings recorded. **[Documented: repo v0.24.1]**
Detail:
• Outcome: block, truncated message or allow **[Documented: repo v0.24.1]**
• Metadata holds `is_bloat`, `action`, `detections`, `metrics` **[Documented: repo v0.24.1]**
• Reject blocks **[Documented: repo v0.24.1]**
• Truncate rewrites `$user_message` **[Documented: repo v0.24.1]**
• Warn allows with detections recorded **[Documented: repo v0.24.1]**
### R6
Summary: **User message text plus thresholds.** Needs size, randomness and repetition thresholds, a chosen action, and the input check enabled. **[Documented]** The code also reads two further settings. **[Documented: repo v0.24.1]**
Detail:
• Input: user message text plus thresholds **[Documented]**
• `rails.config.context_bloat_detection.{max_chars, min_entropy, max_repetition_ratio, max_run_ratio, action}` **[Documented]**
• `rails.input.flows` **[Documented]**
• The code also reads `min_chars` and `ngram_size` **[Documented: repo v0.24.1]**
### R7
Summary: **Minimum setup:** harness, test inputs of normal text, text over 5000 characters, a repeated single character, repeated phrases and low-randomness filler, configuration trying each action in turn, and a recorder of outcome and metrics. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – harness
  – test inputs of normal text
  – text over 5000 characters
  – repeated single character
  – repeated phrases
  – low-entropy filler
  – config with each action in turn
  – a recorder of outcome and metrics
### R8
Summary: **Key open questions.** In the code, truncate only shortens for the size limit and rejects other findings, which the docs do not say. Also unclear are false positives on legitimate long pastes and whether warnings are visible to the caller.
Detail:
• In code `truncate` only cuts for the size cap and rejects for entropy, run and repetition findings, which the docs do not say
• `min_chars` and `ngram_size` defaults not read
• False positives on legitimate long pastes (logs, code)
• Multilingual entropy
• Whether `warn` is visible to the caller
### R9
Summary: NVIDIA docs (Agentic security guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/agentic-security
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/context_bloat_detection/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/context_bloat_detection/actions.py

## Column K: NeMo Guardrails: Tool-call validation
### R1
Summary: **Tool-call validation (output side).** Checks each tool call the model emits against the tools the application declared, before the call reaches the application. It is a local structural check with no LLM call. **[Documented]**
Detail:
• Output side **[Documented]**
• Checks each tool call the model emits against the tools the application declared **[Documented]**
• The check happens before the call reaches the application **[Documented]**
• It is a local structural check with no LLM call **[Documented]**
### R2
Summary: **Unknown tools, malformed arguments and invalid tool schemas.** Catches calls to undeclared tools, arguments that break the tool's schema, arguments given to a no-parameter tool, and invalid declared schemas. **[Documented]** It does not judge whether an allowed call is harmful. **[Inferred]**
Detail:
• Addresses unknown tools, malformed arguments and invalid tool schemas **[Documented]**
• Addresses calls to a tool outside the allowlist **[Documented]**
• Addresses arguments that violate the tool's JSON Schema **[Documented]**
• Addresses arguments supplied to a no-parameter tool **[Documented]**
• Addresses a declared schema that is itself invalid **[Documented]**
• It does not judge whether an allowed call is harmful **[Inferred]**
### R3
Summary: **Model response, after the main LLM.** A response containing only tool calls skips the text output checks. A block returns a fixed refusal, and a provider failure returns an internal-error message. The check does not run tools. **[Documented]**
Detail:
• Position: model response, after the main LLM **[Documented]**
• Flow `tool call validation` under `rails.tool_output.flows` **[Documented]**
• A response with only tool calls skips the text output rails **[Documented]**
• A block returns "I'm sorry, I can't respond to that." **[Documented]**
• Streaming returns a `guardrails_violation` payload **[Documented]**
• A provider failure returns "I'm sorry, an internal error has occurred." **[Documented]**
• The rail does not execute tools **[Documented]**
### R4
Summary: **Structural allowlist and JSON Schema check.** It supports only the OpenAI-style format. **[Documented]** NVIDIA's pages disagree on which engines run it. **[Documented]** A model-based tool safety check exists only in a development branch. **[Not disclosed in v0.24.1 docs]** **[To be verified]**
Detail:
• Structural allowlist and JSON Schema check **[Documented]**
• Supports only the OpenAI Chat Completions format (`openai` and `nim` engines) **[Documented]**
• Engine support conflicts in the docs **[Documented]**
• The tool-calling page says these rails "run only on the IORails engine… not available on the default `LLMRails` engine" **[Documented]**
• The tool-calling page says these rails need Colang 1.0 **[Documented]**
• The rail-engine-support and engine-feature-support pages mark both tool rails as supported on LLMRails and IORails **[Documented]**
• A misdirected, unknown or duplicated flow name silently falls back to LLMRails with no tool rail **[Documented]**
• An LLM-based `tool_safety_check` rail exists on the develop branch only (not in v0.24.1) **[Not disclosed in v0.24.1 docs]** **[To be verified]**
  – allow/block/moderate
  – IORails
• Per-tool regex checks on tool-call arguments appear in develop-branch docs only (not in v0.24.1) **[To be verified: future release]**
• No third-party backends are documented for this function **[To be verified]**
### R5
Summary: **Allow or block outcome.** A block gives a fixed refusal text, or an error payload when streaming, with a reason such as "not an allowed tool". A provider outage gives an internal-error message instead. **[Documented]**
Detail:
• Outcome is allow or block **[Documented]**
• A block gives the fixed refusal text (non-streaming) **[Documented]**
• A block gives a `guardrails_violation` error payload (streaming) **[Documented]**
• Block reasons are strings such as "tool call 'x' is not an allowed tool" **[Documented]**
• A provider outage gives an internal-error message instead **[Documented]**
• The streamed tool-call chunk is suppressed after a block **[Documented]**
### R6
Summary: **Declared tools plus the model's tool calls.** Needs tool definitions in the configuration and a model that emits tool calls. Hosted tools identified only by type are allowed by type and their arguments are not checked. **[Documented]**
Detail:
• Input: declared tools plus the model's tool calls **[Documented]**
• Needs tool definitions in `options.llm_params.tools` or `models[].parameters.tools` **[Documented]**
• Needs a model that emits tool calls **[Documented]**
• Hosted tools identified only by `type` are allowlisted by type **[Documented]**
• Arguments of hosted tools identified only by `type` are not schema-validated **[Documented]**
### R7
Summary: **Minimum setup:** harness sending requests with declared tools, a model or scripted responses emitting valid, unknown-name, bad-argument and no-parameter-with-arguments calls, configuration with the tool-call check on IORails, and a recorder. No tool execution is needed. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – harness sending requests with declared tools
  – a model or scripted responses that emit valid, unknown-name, bad-argument and no-parameter-with-arguments calls
  – an IORails config with `tool call validation`
  – a recorder for refusals and payloads
• No tool execution is needed **[Inferred from the documented rail position]**
### R8
Summary: **Key open questions.** Which engine actually runs the tool checks in v0.24.1, since the docs conflict, and whether the model-based tool safety check and per-tool pattern checks reach a release.
Detail:
• Verify which engine runs tool rails on v0.24.1 (the docs conflict)
• Whether the `tool_safety_check` rail and per-tool regex checks reach a release
• Behaviour for non-OpenAI wire formats
• Tool-call arguments seen by plain output rails
• Silent fallback when a flow name is mistyped
• Whether JSON Schema dialect variants validate
### R9
Summary: NVIDIA docs (Tool calling guide, Rail engine support) and NeMo Guardrails v0.24.1 docs and source code on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/tool-calling
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/guardrail-catalog/tool-calling.mdx
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/guardrails/actions/tool_call_action.py
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/reference/rail-engine-support.mdx

## Column L: NeMo Guardrails: Tool-result validation
### R1
Summary: **Tool-result validation (input side).** Checks tool-result messages in the request before the model sees them. It is a local structural check with no LLM call. **[Documented]**
Detail:
• Input side **[Documented]**
• Checks `role: tool` messages in the request **[Documented]**
• The check happens before the model sees them **[Documented]**
• It is a local structural check with no LLM call **[Documented]**
### R2
Summary: **Malformed or inconsistent tool results.** Catches missing or unlinked call IDs, duplicate IDs, mismatched tool names and invalid content types. **[Documented]** It is not a content-safety or prompt-injection check on the result text. **[Documented]**
Detail:
• Addresses malformed or inconsistent tool results **[Documented]**
• Addresses a missing or unlinked `tool_call_id` **[Documented]**
• Addresses duplicate IDs within the turn **[Documented]**
• Addresses a name that differs from the linked call **[Documented]**
• Addresses content that is not a string or content-block list **[Documented]**
• It is not a content-safety or prompt-injection check on result text **[Documented]**
### R3
Summary: **Request input, before the main model.** Runs alongside the input checks, with the same refusal and error behaviour as the tool-call check. **[Documented]** Plain input and output checks see only message content, so tool results bypass input checks. **[Documented]**
Detail:
• Position: request input, before the main model **[Documented]**
• Flow `tool result validation` under `rails.tool_input.flows` **[Documented]**
• It runs alongside the input rails **[Documented]**
• Refusal and error behaviour matches the tool-call rail **[Documented]**
• Plain input/output rails see only the `content` field **[Documented]**
• Tool-call arguments are not inspected by plain input/output rails **[Documented]**
• Tool results bypass input rails **[Documented]**
### R4
Summary: **Structural linkage check only.** It does not enforce a response schema or check content safety, and checks consistency within one request only. **[Documented]** NVIDIA's pages disagree on which engines run it. **[Documented]** A model-based tool safety check exists only in a development branch. **[Not disclosed in v0.24.1 docs]** **[To be verified]**
Detail:
• Structural linkage check only **[Documented]**
• It does not enforce a response schema **[Documented]**
• It does not run a content-safety check **[Documented]**
• Consistency is checked within one request only **[Documented]**
• There is no cross-turn provenance **[Documented]**
• Engine support conflicts in the docs **[Documented]**
• The tool-calling page says IORails only (not on `LLMRails`, Colang 1.0 needed) **[Documented]**
• The rail-engine-support and engine-feature-support pages mark it supported on both engines **[Documented]**
• An LLM-based `tool_safety_check` rail exists in source and is undocumented in v0.24.1 **[Not disclosed in v0.24.1 docs]** **[To be verified]**
  – develop branch only, not in v0.24.1
  – judges the tool result
  – allow/block/moderate
  – IORails
• Per-tool regex checks on tool results appear in develop-branch docs only (not in v0.24.1) **[To be verified: future release]**
• No third-party backends are documented **[To be verified]**
### R5
Summary: **Allow or block outcome.** A block gives a fixed refusal text, or an error payload when streaming. A provider failure gives an internal-error message. **[Documented]**
Detail:
• Outcome is allow or block **[Documented]**
• A block gives "I'm sorry, I can't respond to that." (non-streaming) **[Documented]**
• A block gives a `guardrails_violation` payload (streaming) **[Documented]**
• A provider failure gives "I'm sorry, an internal error has occurred." **[Documented]**
### R6
Summary: **Conversation history with tool messages.** Needs the assistant turn containing the tool calls and one tool message per call ID, resent on each request. Declared tools are needed for name checks. **[Documented]**
Detail:
• Input: conversation history with tool messages **[Documented]**
• Needs the assistant turn containing the tool calls **[Documented]**
• Needs one `role: tool` message per `tool_call_id` **[Documented]**
• These must be resent on each request **[Documented]**
• Declared tools are needed for name checks **[Documented]**
### R7
Summary: **Minimum setup:** harness sending conversations with tool messages (valid, missing ID, duplicate ID, wrong name, non-string content), configuration with the tool-result check on IORails, a stub main LLM, and a recorder. No real tool execution is needed. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – harness sending conversations with tool messages (valid, missing id, duplicate id, wrong name, non-string content)
  – an IORails config with `tool result validation`
  – a stub main LLM
  – a recorder
• No real tool execution is needed **[Inferred from the documented rail position]**
### R8
Summary: **Key open questions.** Which engine runs the tool checks in v0.24.1, since the docs conflict, and that result text itself is not checked, so injection via tool results is unaddressed.
Detail:
• Verify which engine runs tool rails on v0.24.1 (the docs conflict)
• Whether `tool_safety_check` and per-tool regex checks reach a release
• No content check on tool results (injection via results unaddressed)
• Cross-turn provenance
• Non-OpenAI formats
• Redundant-flow fallback to LLMRails
### R9
Summary: NVIDIA docs (Tool calling guide, Rail engine support) and NeMo Guardrails v0.24.1 docs on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/tool-calling
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/guardrail-catalog/tool-calling.mdx
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/reference/rail-engine-support.mdx

## Column M: NeMo Guardrails: Grounded fact-checking (output)
### R1
Summary: **Grounded fact-checking (output).** Checks whether the bot reply is supported by the retrieved evidence before it reaches the user. **[Documented]**
Detail:
• Output side **[Documented]**
• Checks whether the bot reply is supported by the retrieved evidence (`relevant_chunks`) **[Documented]**
• The check happens before the reply reaches the user **[Documented]**
### R2
Summary: **Unsupported claims in RAG answers.** Addresses replies that contradict or go beyond the knowledge-base chunks. It does not help without retrieved evidence. **[Documented]**
Detail:
• Addresses unsupported claims in RAG answers **[Documented]**
• Addresses replies that contradict the knowledge-base chunks **[Documented]**
• Addresses replies that go beyond the knowledge-base chunks **[Documented]**
• It does not help without retrieved evidence **[Documented]**
### R3
Summary: **Bot response, after the main model.** Three output checks are available, and the self-check one runs only when a fact-checking flag is set. **[Documented]**
Detail:
• Position: bot response, after the main model **[Documented]**
• Output flows: **[Documented]**
  – `self check facts`
  – `alignscore check facts`
  – `patronus lynx check output hallucination`
• `self check facts` only runs when `$check_facts == True` **[Documented]**
### R4
Summary: **Entailment judgement against evidence.** The LLM scores support, an AlignScore server judges it, or a Patronus Lynx model detects hallucination. **[Documented]** These run on the LLMRails engine only; IORails does not support them. **[Documented]** Several paid and open third-party options are listed. **[To be verified]**
Detail:
• Entailment judgement against evidence **[Documented]**
• `self check facts` has the LLM score support from 0 to 1 **[Documented]**
  – the docs example blocks below 0.5
  – empty or truncated output fails closed with 0.0
• `alignscore check facts` calls an AlignScore server at `rails.config.fact_checking.parameters.endpoint` **[Documented]**
• Patronus Lynx is a hallucination model (8B and 70B) **[Documented]**
• The built-in flows run on LLMRails only **[Documented]**
• IORails does not support them because they read `relevant_chunks` **[Documented]**
• Per the v0.24.1 support matrix this covers: **[Documented]**
  – self check facts
  – alignscore
  – autoalign groundedness
  – fiddler faithfulness
  – patronus api
  – patronus lynx
• Optional third-party backends: **[To be verified]**
  – Patronus API (paid / non-OSS service)
  – Fiddler bot faithfulness (paid / non-OSS service)
  – AutoAlign groundedness and factcheck (paid / non-OSS service)
  – Cleanlab trustworthiness (paid / non-OSS service; runs on IORails)
  – AlignScore (open-source, self-hosted)
  – Patronus Lynx (open-weight model, licensing to be verified)
### R5
Summary: **Score and block decision.** The self-check option returns a 0 to 1 score and blocks below a threshold. **[Documented]** Other backends return their own results, and the exact output shape for each vendor is unconfirmed. **[Documented]** **[To be verified]**
Detail:
• Output is a score and a block decision **[Documented]**
• `self check facts` returns a 0 to 1 score **[Documented]**
• The flow blocks below a threshold **[Documented]**
• Other backends return their own pass/fail or scores **[Documented]**
• Exact output shape per vendor is unconfirmed **[To be verified]**
### R6
Summary: **Reply plus retrieved chunks.** Needs retrieved evidence, the fact-checking flag set, and for self-check a prompt and the main LLM. AlignScore needs a running server; vendors need accounts or keys. **[Documented]**
Detail:
• Input: reply plus retrieved chunks **[Documented]**
• Needs a knowledge base or `relevant_chunks` set in context **[Documented]**
• Needs the `check_facts` flag set **[Documented]**
• For self-check, needs a `self_check_facts` prompt and main LLM **[Documented]**
• AlignScore needs a running server **[Documented]**
• Vendors need accounts or keys **[Documented]**
### R7
Summary: **Minimum setup:** harness, a small knowledge base or injected retrieved chunks, supported and unsupported answer pairs, a configuration on the LLMRails engine with the chosen check, a judge LLM or AlignScore server, and a recorder. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – harness
  – a small knowledge base or injected `relevant_chunks`
  – supported and unsupported answer pairs
  – a LLMRails config with the chosen flow
  – a judge LLM or AlignScore server
  – a recorder
### R8
Summary: **Key open questions.** Thresholds for non-LLM backends, whether the IORails exclusion list holds for v0.24.1, and vendor licensing and cost.
Detail:
• Thresholds for non-LLM backends
• Verify the IORails exclusion list on v0.24.1 (matrix read from the v0.24.1 tag)
• Vendor licensing and cost
• AlignScore model licence
• Behaviour with long or multiple chunks
• False positive rates
• How `$check_facts` is set in practice
### R9
Summary: NVIDIA docs (Fact-checking guide, Rail engine support) and the NeMo Guardrails v0.24.1 engine-support page on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/fact-checking
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/reference/rail-engine-support.mdx

## Column N: NeMo Guardrails: Self-consistency hallucination detection (output)
### R1
Summary: **Self-consistency hallucination detection (output).** Samples extra generations and checks whether they agree with the original reply; disagreement suggests a hallucination. No grounding documents are needed. **[Documented]**
Detail:
• Output side **[Documented]**
• Samples extra generations **[Documented]**
• Checks whether the extra generations agree with the original reply **[Documented]**
• Disagreement suggests a hallucination **[Documented]**
• No grounding documents are needed **[Documented]**
### R2
Summary: **Fabricated facts without retrieval.** Addresses unstable answers drawn from the model's own knowledge. It cannot catch a consistent but wrong answer. **[Inferred]**
Detail:
• Addresses fabricated facts without retrieval **[Inferred]**
• Addresses unstable parametric answers **[Inferred]**
• It cannot catch a consistent but wrong answer **[Inferred]**
### R3
Summary: **Bot response, after the main model.** One flow blocks and another appends a warning, each running only when its flag is set. **[Documented]**
Detail:
• Position: bot response, after the main model **[Documented]**
• Flow `self check hallucination` (blocks) **[Documented]**
• Flow `hallucination warning` (appends a warning) **[Documented]**
• They run when `$check_hallucination` or `$hallucination_warning` is set **[Documented]**
### R4
Summary: **Resampling plus an LLM agreement check.** By default two extra responses are generated and the LLM judges whether they agree with the original. **[Documented: repo v0.24.1]** It runs on the LLMRails engine only. **[Documented]** If all extra generations fail, the reply is allowed. **[Documented: repo v0.24.1]** Supported providers are unclear. **[To be verified]**
Detail:
• Resampling plus an LLM agreement check **[Documented: repo v0.24.1]**
• By default two extra responses at temperature 1.0 are generated **[Documented: repo v0.24.1]**
• Then the LLM judges agreement with the original (a "no" blocks) **[Documented: repo v0.24.1]**
• The check only supports LLM-based agreement **[Documented: repo v0.24.1]**
• A BERT-score path is a TODO **[Documented: repo v0.24.1]**
• LLMRails only **[Documented]**
• IORails does not support it because it reads `_last_bot_prompt` **[Documented]**
• If every extra generation fails the rail allows the reply **[Documented: repo v0.24.1]**
• Supported main-LLM providers are not stated **[To be verified]**
• Code makes parallel separate calls rather than an `n` parameter **[To be verified]**
• No third-party backends are documented **[To be verified]**
### R5
Summary: **Block or warning.** The outcome is allow or block, and the warning option appends text instead of blocking. **[Documented: repo v0.24.1]**
Detail:
• Outcome is allow or block with metadata `is_hallucination` **[Documented: repo v0.24.1]**
• The warning flow appends text instead of blocking **[Documented: repo v0.24.1]**
### R6
Summary: **Bot reply and the prompt that produced it.** Needs the last bot prompt, a main LLM, a self-check prompt and the flag set. **[Documented]**
Detail:
• Input: bot reply and the prompt that produced it **[Documented]**
• Needs the last bot prompt **[Documented]**
• Needs a main LLM **[Documented]**
• Needs a `self_check_hallucination` prompt **[Documented]**
• Needs the flag set **[Documented]**
### R7
Summary: **Minimum setup:** harness, prompts with stable answers and prompts the model tends to invent answers for, a configuration on the LLMRails engine with the check and flag, a main LLM allowing temperature 1.0, and a recorder. **[Inferred from the documented rail position]**
Detail:
• Minimum setup components: **[Inferred from the documented rail position]**
  – harness
  – prompts with stable answers and prompts the model tends to invent answers for
  – a LLMRails config with the flow and flag
  – a main LLM allowing temperature 1.0
  – a recorder
### R8
Summary: **Key open questions.** Which main-LLM providers work (unconfirmed), the added latency and cost of three or more LLM calls, and that a failure of the extra calls lets the reply through.
Detail:
• Which main-LLM providers work (the docs may restrict this; not confirmed)
• Added latency and cost of three-plus LLM calls
• Accuracy of the agreement judge
• Fail-open on extra-call failure
• How the flags are set
• Interaction with streaming
### R9
Summary: NVIDIA docs (Fact-checking guide, Rail engine support) and NeMo Guardrails v0.24.1 source code on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/fact-checking
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/hallucination/actions.py
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/hallucination/rail.py
