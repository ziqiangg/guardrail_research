## Column O: NeMo Guardrails: Execution-level custom action rails
### R1
Summary: **Execution-level custom action rails.** Checks written by the application developer that wrap the custom actions an app or the model triggers, so a developer can validate what goes into an action and what comes out. NeMo supplies the hook and the action mechanism, not a ready-made detector. **[Documented]**
Detail:
• Execution rails are checks around custom actions, meaning actions the application or the LLM invokes **[Documented]**
• The configuration reference describes them as controlling custom action calls, before and after action execution **[Documented: repo v0.24.1]**
• The rail types page describes them as validating tool or function calls, their arguments and their results **[Documented]**
• They are developer-defined: no built-in execution-rail detector is shipped **[Inferred]**
• Actions are Python functions the developer writes and registers, called from Colang flows **[Documented: repo v0.24.1]**
• Difference from the tool-call and tool-result columns: the Engine Feature Support page lists execution rails (custom actions) and tool rails as separate rows **[Documented]**
• Tool rails validate the model's own tool calls and tool results, and run on both engines; they are covered in the tool-call validation and tool-result validation columns **[Documented]**
• This column covers only the developer-authored wrapper around custom actions, which runs on LLMRails only **[Documented]**
### R2
Summary: **Unsafe or invalid use of custom actions.** Addresses an action being called with bad arguments, or returning data that should not be trusted, in whatever way the developer chooses to check. The docs name agentic security as the main use. **[Documented]** What is actually caught depends entirely on the checks written. **[Inferred]**
Detail:
• Addresses unsafe or invalid use of external functions, their arguments and their results **[Documented]**
• The rail types page lists agentic security as the use case of execution rails **[Documented]**
• Tool messages are not subject to input-rail validation, which the Tools Integration page calls a potential security risk **[Documented]**
• The same page strongly recommends output rails to validate LLM responses **[Documented]**
• No attack taxonomy or built-in checks are published for execution rails **[Not disclosed]**
• What is caught depends on the checks the developer writes **[Inferred]**
### R3
Summary: **Around a custom action call, inside the conversation flow.** A developer-written flow calls an action and then branches on its result, for example refusing and stopping. The configuration reference says execution rails act before and after action execution. **[Documented: repo v0.24.1]**
Detail:
• Position: before or after the execution of a custom action **[Documented: repo v0.24.1]**
• A custom action is called from Colang with `execute <action_name>(...)` and its result is stored in a variable **[Documented: repo v0.24.1]**
• A flow can branch on the result, for example `bot refuse to respond` then `stop` **[Documented: repo v0.24.1]**
• Actions live in `actions.py` or an `actions/` sub-package of the configuration **[Documented: repo v0.24.1]**
• Actions can also be registered through `LLMRails.register_action()` or `config.py` **[Documented: repo v0.24.1]**
• The `execute_async` option on the decorator only works in Colang 2.x and is stored with no effect in Colang 1.0 **[Documented: repo v0.24.1]**
• The `is_system_action` option makes an action always run locally, which matters when an actions server is configured **[Documented: repo v0.24.1]**
### R4
Summary: **Developer-written Python and Colang, no model of its own.** NeMo provides the action decorator, the flow runtime and action execution; the check logic comes from the developer. **[Documented: repo v0.24.1]** Execution rails run on the LLMRails engine only, because IORails does not run custom actions. **[Documented]**
Detail:
• Mechanism: developer-written Python actions called from Colang flows **[Documented: repo v0.24.1]**
• There is no built-in detector for execution rails; the protection equals the logic the developer writes **[Inferred]**
• The decorator does not treat an action's return value as a safety decision; a boolean stays data until a flow checks it **[Documented: repo v0.24.1]**
• An action that makes a rail decision should return a RailOutcome with an explicit allow, block or transform **[Documented: repo v0.24.1]**
• Engine support: Execution rails (custom actions) run on LLMRails only **[Documented]**
• IORails does not run custom actions **[Documented]**
• A tool-rail configuration is separate and runs on both engines, with the IORails part limited to supported flows **[Documented]**
• The guardrails configuration page shows `rails.execution.flows` with `check tool input` and `check tool output` **[Documented: repo v0.24.1]**
• The v0.24.1 configuration model has no `execution` field; it defines `actions.instant_actions`, `tool_output` and `tool_input` **[Documented: repo v0.24.1]**
• No flow named `check tool input` or `check tool output` was found in the library **[To be verified]**
• Colang 1.0 and 2.x both run on LLMRails **[Documented]**
• The docs list no third-party backends for this function **[Documented: none listed]**
### R5
Summary: **Whatever the developer's flow returns.** Typically a refusal message and a stopped response, but the format is not fixed by NeMo. **[Documented: repo v0.24.1]** An action may return a structured allow, block or transform decision. **[Documented: repo v0.24.1]**
Detail:
• Output is defined by the developer's flow, not by a fixed result schema **[Documented: repo v0.24.1]**
• A typical flow answers with a canned refusal and stops **[Documented: repo v0.24.1]**
• A RailOutcome carries an explicit allow, block or transform decision **[Documented: repo v0.24.1]**
• A RailOutcome exposes `is_blocked`, which a flow can test **[Documented: repo v0.24.1]**
• No score or taxonomy is returned by any built-in check **[Not disclosed]**
• Exception behaviour with `enable_rails_exceptions` is not described for custom actions **[To be verified]**
### R6
Summary: **Action name, arguments and result, plus a reference configuration we author.** The test bench cannot reuse a ready-made check, so it needs a custom-action configuration with test actions that we write. **[Inferred]** Actions can read conversation context such as the last user message. **[Documented: repo v0.24.1]**
Detail:
• Input: the action call, its arguments and its result **[Documented]**
• Actions can receive the context with the last user message and bot message **[Documented: repo v0.24.1]**
• Parameters can be strings, numbers, booleans, lists and dictionaries **[Documented: repo v0.24.1]**
• The test bench needs a reference custom-action configuration with test actions that we author **[Inferred]**
• What is evaluated is the custom-action wrapper mechanism of NeMo and our test logic, not a vendor detector **[Inferred]**
• The test actions should cover allowed and blocked arguments, and trusted and untrusted results **[Inferred]**
### R7
Summary: **Minimum setup:** harness, a configuration with a few test actions and flows that we write, a main LLM or scripted calls that trigger them, test cases with allowed and blocked inputs, the LLMRails engine and a recorder of action calls and blocks. No external model service is required by NeMo for this function. **[Inferred]**
Detail:
• Minimum setup components: **[Inferred]**
  – harness
  – reference configuration with test actions and flows that we author
  – a main LLM or scripted calls that trigger the actions
  – test cases with allowed and blocked arguments and results
  – the LLMRails engine
  – a recorder of action calls, blocks and final replies
• No external model service is required by NeMo for this function **[Inferred]**
• IORails cannot be used for this column **[Documented]**
### R8
Summary: **Key open questions.** Whether execution rails are a distinct, working configuration key in the current release, what exactly they wrap, and how they differ in practice from tool rails.
Detail:
• Whether `rails.execution` is a working key (v0.24.1 docs show it, the configuration model has no such field)
• Where the flows `check tool input` and `check tool output` are defined, if anywhere
• How execution rails and tool rails differ in practice (the rail types page describes both as validating tool calls)
• Whether a flow can intercept an action called by the LLM rather than by a flow
• Behaviour with `enable_rails_exceptions`
• Behaviour of actions run through an actions server
• Differences between Colang 1.0 and 2.x for action wrapping
• Latest-version rail types page not separately checked
### R9
Summary: NVIDIA docs (Engine Feature Support, Rail types for v0.22.0 and latest, Tools Integration) and NeMo Guardrails v0.24.1 documentation and source on GitHub.
Detail:
• https://docs.nvidia.com/nemo/guardrails/reference/engine-feature-support
• https://docs.nvidia.com/nemo/guardrails/v0.22.0/about-nemo-guardrails-library/rail-types
• https://docs.nvidia.com/nemo/guardrails/about-nemo-guardrails-library/rail-types
• https://docs.nvidia.com/nemo/guardrails/integration-with-third-party-libraries/tools-integration
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/actions/creating-actions.mdx
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/actions/index.mdx
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/yaml-schema/guardrails-configuration.mdx
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/rails/llm/config.py
