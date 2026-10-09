## Column: NeMo Guardrails: Input-level jailbreak detection (expanded)

- **R1:** **Input-level jailbreak detection.** Checks whether a user input may be attempting to bypass the application's safeguards. NeMo ships two flows: `jailbreak detection heuristics` (perplexity-based) and `jailbreak detection model` (embedding classifier, via the NemoGuard JailbreakDetect NIM). **[Documented]**

- **R2:** **Jailbreak attempts in user inputs.** The heuristics target unusually long or high-perplexity inputs and GCG-style adversarial prefix/suffix strings; the model flow is described as a general jailbreak classifier. **[Documented]** The heuristics are intended for English only and give more false positives on non-English text, including code. **[Documented]** No jailbreak taxonomy is published, so precise coverage of the model flow is unclear. **[Not disclosed] [To be verified]**

- **R3:** **User messages before the main model.** It operates as an input rail that evaluates the user message before normal LLM processing continues. **[Documented]** Both flows read the current user message only. **[Documented: repo v0.24.1 actions.py]**

- **R4:** **Depends on the selected flow.** Heuristics: length-per-perplexity (threshold 89.79) and prefix/suffix perplexity (threshold 1845.65, inputs over 20 words), using GPT-2-large with torch and transformers. **[Documented]** In-process mode is for testing only; production should set `server_endpoint`. **[Documented]** Model flow: a random forest on Snowflake Arctic embeddings, called through the NemoGuard JailbreakDetect NIM (`nim_base_url`, `nim_server_endpoint`, `api_key_env_var`). **[Documented]** Engine support: heuristics on LLMRails only (IORails blocks it); model flow on both. **[Documented]** If the detector is unreachable the rail allows the request (fails open). **[Documented]** NIM training data is not published. **[Not disclosed]** The docs list no third-party jailbreak backends. **[Documented: none listed]**

- **R5:** **Block or allow outcome.** On a block the bot replies "I'm sorry, I can't respond to that." and aborts; with `enable_rails_exceptions` set it raises `JailbreakDetectionRailException` instead. **[Documented]** The underlying actions return a `RailOutcome` (`is_blocked`) and expose no score. **[Documented: repo v0.24.1]** The NIM is described as returning a binary result; its threshold is not specified. **[Documented] [Not disclosed]**

- **R6:** **Jailbreak and benign user prompts.** Single-turn prompts suffice because only the current user message is checked. **[Documented: repo v0.24.1]** Reported heuristic performance: length/perplexity detects 31.19% with 7.44% FPR; prefix/suffix catches 49/50 GCG attacks at 0.04% FPR. **[Documented]** Benign sets should include non-English text and code, which raise false positives. **[Inferred] [To be verified]**

- **R7:** **Minimum setup:** test-data loader, configured NeMo input rail, selected flow, product adapter, result recorder and evaluator. For the model flow, a reachable NIM (hosted or local) and API key; for heuristics, a `server_endpoint` service for production-like runs, or torch and transformers for in-process testing. A basic prompt-submission harness is sufficient. RAG, tool execution and multi-agent components are not required. **[Inferred from the documented rail position]**

- **R8:** Selected flow (heuristics or model), jailbreak definition (not documented), engine (LLMRails or IORails), thresholds (heuristics), NIM endpoint and API key, `enable_rails_exceptions`, fail-open behaviour on detector outage, output format (blocked or allowed only, no score), English-only limitation, torch/transformers dependencies

- **R9:** https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/jailbreak-protection ; https://docs.nvidia.com/nemo/guardrails/get-started/tutorials/nemoguard-jailbreakdetect-deployment ; https://docs.nvidia.com/nemo/guardrails/reference/rail-engine-support ; https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/jailbreak_detection/flows.co ; https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/jailbreak_detection/actions.py

## Reviewer notes
- Verified via WebFetch (summarised by a small model, not raw page text) and the repo files at v0.24.1 (read directly). Re-check exact numbers (89.79, 1845.65, 31.19%, 7.44%, 49/50, 0.04%, ">20 words") against the page if they will be cited.
- The catalog page states random forest on `Snowflake/snowflake-arctic-embed-m-long`. The tutorial page did not state the model type, and the "NemoGuard" name was not found on the catalog page in this fetch. Linking NemoGuard to that random forest rests on the flow description ("embedding-based jailbreak detection models") and the NIM config keys. Treat it as probable but confirm.
- Fail-open: the docs state it generally. The code confirms it for both flows (heuristics endpoint failure returns allow; model flow sets result False on None, RuntimeError or ImportError).
- The rail-engine page says heuristics are blocked on IORails because both backends share a manifest, so the dependency need cannot be determined (issue #2285).
- The refusal text comes from the tutorial page; flows.co only says `bot refuse to respond`.
- Code also supports a local in-process model path and a `server_endpoint` model route, plus an optional result cache for the model flow. These are not in the catalog facts and are not in the cells.
- No score is exposed by the actions (`RailOutcome.block()/allow()`). No taxonomy, NIM training data or NIM threshold was found.
- No third-party jailbreak backends were listed on the fetched pages, so the "Optional third-party backends" line was omitted. Other rails pages may list some; not checked.
- R4 slightly exceeds ~100 words because of the engine and fail-open facts; trim if needed.
