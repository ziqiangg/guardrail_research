# Proposed changes to Column D: NeMo Guardrails: Dialog-level conversational flow control

Rows not listed here (R2, R3, R5) stay exactly as they are in two_level.md. Rows below are full replacements.

## R1

OLD:
Summary: **Dialog-level conversational flow control.** Steers multi-turn conversations by mapping user messages to intents and enforcing the bot's next step through Colang flows. **[Documented]**
Detail:
• Steers multi-turn conversations **[Documented]**
• Maps user messages to intents **[Documented]**
• Enforces the bot's next step through Colang flows **[Documented]**

NEW:
Summary: **Dialog-level conversational flow control.** Steers multi-turn conversations by mapping user messages to intents and enforcing the bot's next step through conversation flows. The flows are written by the developer; NeMo provides the engine that runs them, not a ready-made detector. **[Documented]**
Detail:
• Steers multi-turn conversations **[Documented]**
• Maps user messages to intents **[Documented]**
• Enforces the bot's next step through Colang flows **[Documented]**
• Dialog rails are developer-written Colang flows: user intents, bot messages and flows **[Documented]**
• NeMo provides the Colang runtime and intent matching, not a built-in detector **[Inferred]**
• The protection depends on the flows the developer authors **[Inferred]**

REASON: The rail types page describes dialog rails as steering and constraining the multi-turn conversation, and the Colang guides show the user, bot and flow definitions are authored by the developer. https://docs.nvidia.com/nemo/guardrails/v0.22.0/about-nemo-guardrails-library/rail-types

## R4

OLD:
Summary: **Intent matching by embeddings and/or LLM.** It matches similar example messages, then asks the LLM for the intent, or uses the closest match alone. **[Documented]** The engine support table does not cover dialog rails. **[Not disclosed]** No third-party backends are documented. **[To be verified]**
Detail:
• Intent matching by embeddings and/or LLM **[Documented]**
• `generate_user_intent` finds similar user examples in a vector store, then asks the LLM for the intent **[Documented]**
• With `rails.dialog.user_messages.embeddings_only: true` the closest embedding match is used without the LLM **[Documented]**
• `rails.dialog.single_call.enabled` merges intent and response into one call **[Documented]**
• The LLMRails vs IORails support matrix does not cover dialog rails **[Not disclosed]**
• No third-party backends are documented for this function **[To be verified]**

NEW:
Summary: **Intent matching by embeddings and/or LLM, over flows the developer writes.** It matches similar example messages, then asks the LLM for the intent, or uses the closest match alone. The example messages and flows come from the developer, so the protection is only as broad as what is written. **[Documented]** Dialog rails run on the LLMRails engine only, because they need the Colang runtime, which IORails does not run. **[Documented]** No third-party backends are documented. **[To be verified]**
Detail:
• Intent matching by embeddings and/or LLM **[Documented]**
• `generate_user_intent` finds similar user examples in a vector store, then asks the LLM for the intent **[Documented]**
• With `rails.dialog.user_messages.embeddings_only: true` the closest embedding match is used without the LLM **[Documented]**
• `rails.dialog.single_call.enabled` merges intent and response into one call **[Documented]**
• The user intents, bot messages and flows are written by the developer in Colang **[Documented]**
• NeMo provides the runtime and intent matching, not a built-in detector, so the protection depends on the flows the developer authors **[Inferred]**
• Engine support: Engine Feature Support states dialog rails run on LLMRails only, because they require the Colang runtime, which IORails does not run **[Documented]**
• Colang 1.0 defines intents with `define user ...` example utterances and flows with `define flow ...`; Colang 2.x drops `define user` and `define bot` and uses `flow user expressed greeting` containing `user said "..."` statements **[Documented]**
• Colang 2.x flows must be activated explicitly, with a `main` flow as the entry point; in Colang 1.0 all flows are active by default **[Documented]**
• LLM involvement: in Colang 1.0, defining a user intent automatically activates the dialog rails and the LLM; in Colang 2.x the LLM must be switched on explicitly with `activate llm continuation`, and the `...` generation operator produces content at runtime **[Documented: repo v0.24.1]**
• Support: LLMRails runs both the Colang 1.0 and 2.x runtimes; Colang 1.0 stays the default while Colang 2.0 is in beta **[Documented]**
• No third-party backends are documented for this function **[To be verified]**

REASON: Engine Feature Support lists "Dialog rails | LLMRails yes | IORails no" with the note that they require the Colang runtime, which IORails does not run, and that LLMRails runs both Colang 1.0 and 2.x. https://docs.nvidia.com/nemo/guardrails/reference/engine-feature-support . Colang differences: https://docs.nvidia.com/nemo/guardrails/configure-guardrails/colang/colang-2/whats-changed and https://docs.nvidia.com/nemo/guardrails/configure-guardrails/colang (version history); the LLM invocation paragraph was read in the raw page at https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/colang/colang-2/whats-changed.mdx

## R6

OLD:
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

NEW:
Summary: **Conversation history, Colang definitions and an embeddings model.** Needs example utterances in Colang files, a main LLM unless matching by embeddings only, and an embedding index. Optional similarity threshold and fallback intent. **[Documented]** The test bench also needs a reference Colang configuration that we author, with example user intents, refusal flows and multi-turn flows, so that what gets evaluated is NeMo's intent matching and flow engine. **[Inferred]**
Detail:
• Input: conversation history, Colang definitions and an embeddings model **[Documented]**
• Needs Colang files with example utterances **[Documented]**
• Needs a main LLM unless embeddings-only **[Documented]**
• Needs an embedding index **[Documented]**
• Defaults: single_call false **[Documented]**
• Defaults: embeddings_only false **[Documented]**
• Optional `embeddings_only_similarity_threshold` **[Documented]**
• Optional fallback intent **[Documented]**
• The test bench needs a reference Colang configuration that we author: example user intents, refusal flows and multi-turn flows **[Inferred]**
• What is evaluated is NeMo's intent-matching and flow engine, not a vendor detector **[Inferred]**

REASON: Dialog rails contain only what the developer defines, so there is nothing to evaluate without an authored configuration (user decision). Underlying docs: https://docs.nvidia.com/nemo/guardrails/configure-guardrails/colang/colang-1/tutorials/6-topical-rails

## R7

OLD:
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

NEW:
Summary: **Minimum setup:** harness, a reference Colang configuration that we author with example user intents, refusal flows and multi-turn flows, the LLMRails engine, main LLM, embedding model, paraphrase and multi-turn test sets, and a recorder. Content-safety and topic-control model services are not needed. **[Inferred]**
Detail:
• Minimum setup components: **[Inferred]**
  – harness
  – reference Colang config that we author: example user intents, refusal flows and multi-turn flows (at least one off-topic user intent and refusal flow)
  – the LLMRails engine (dialog rails do not run on IORails)
  – main LLM
  – embedding model
  – paraphrase and multi-turn test sets
  – recorder
• The test evaluates NeMo's intent matching and flow engine over our authored configuration **[Inferred]**
• Content-safety and topic NIMs are not needed **[Inferred]**

REASON: Follows from the developer-defined framing and the LLMRails-only engine support. The label changes from "Inferred from the documented rail position" to Inferred because the authored-configuration requirement is a bench design decision. https://docs.nvidia.com/nemo/guardrails/reference/engine-feature-support

## R8

OLD:
Summary: **Key open questions.** How robust intent matching is to paraphrase and adversarial phrasing, whether IORails supports dialog rails, and the latency and extra LLM calls.
Detail:
• Robustness to paraphrase and adversarial phrasing
• Embeddings-only threshold tuning
• Whether single-call mode changes accuracy
• Colang 1.0 vs 2.x differences
• Dialog-rail support in IORails (the support matrix lists only input, output and retrieval surfaces)
• Latency and extra LLM calls

NEW:
Summary: **Key open questions.** How robust intent matching is to paraphrase and adversarial phrasing, which Colang version the test bench will use, and the latency and extra LLM calls.
Detail:
• Robustness to paraphrase and adversarial phrasing
• Embeddings-only threshold tuning
• Whether single-call mode changes accuracy
• Which Colang version to test (1.0 is the default, 2.0 is in beta), and whether the `rails.dialog` options apply to Colang 2.x
• Latency and extra LLM calls

REASON: The IORails dialog item is resolved by Engine Feature Support (LLMRails only). The Colang item is narrowed because the documented differences now sit in R4. https://docs.nvidia.com/nemo/guardrails/reference/engine-feature-support

## R9

OLD:
Summary: NVIDIA docs (Colang topical rails tutorial, Rail types and Configuration reference for v0.22.0, Rail engine support).
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/colang/colang-1/tutorials/6-topical-rails
• https://docs.nvidia.com/nemo/guardrails/v0.22.0/about-nemo-guardrails-library/rail-types
• https://docs.nvidia.com/nemo/guardrails/v0.22.0/configure-guardrails/configuration-reference
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support

NEW:
Summary: NVIDIA docs (Colang topical rails tutorial, Colang overview and What's Changed, Rail types and Configuration reference for v0.22.0, Engine feature support, Rail engine support) and one NeMo Guardrails v0.24.1 documentation page on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/colang/colang-1/tutorials/6-topical-rails
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/colang
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/colang/colang-2/whats-changed
• https://docs.nvidia.com/nemo/guardrails/v0.22.0/about-nemo-guardrails-library/rail-types
• https://docs.nvidia.com/nemo/guardrails/v0.22.0/configure-guardrails/configuration-reference
• https://docs.nvidia.com/nemo/guardrails/reference/engine-feature-support
• https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/colang/colang-2/whats-changed.mdx

REASON: New sources used for the changes above.
