# GovTech Sentinel — Summary preview (Checkpoint 2)


## GovTech Sentinel: Localised harmful-content classification (LionGuard 2)

- **R1** (35w, 11 bullets): **Localised harmful-content classification.** Sentinel serves GovTech's LionGuard 2 family, which scores text from 0 to 1 for an overall harm flag and six Singapore-contextualised harm categories. It applies to both user input and model output. **[Documented]**
- **R2** (41w, 22 bullets): **Six harm categories with severity levels.** Hateful, insults, sexual, physical violence, self-harm and all other misconduct, plus an overall flag. Four have Level 1 and Level 2; Level 2 also flags Level 1. Tuned for Singlish, Chinese, Malay and partial Tamil. **[Documented]**
- **R3** (40w, 7 bullets): **Any text, before or after the model.** Sentinel lists LionGuard as Input and Output, so the caller sends either the user message or the model reply in one text field. No system prompt or user prompt is needed as context. **[Documented]**
- **R4** (35w, 35 bullets): **Frozen embedder plus a small ordinal classifier.** Per the Sentinel docs the default is LionGuard 2 (OpenAI embeddings); 2.1 (Gemini) and Lite (EmbeddingGemma) are alternatives. Served through the Sentinel API, or self-hosted from Hugging Face. **[Documented]**
- **R5** (39w, 25 bullets): **Per-category score from 0 to 1, no built-in verdict.** Sentinel returns a score per guardrail and applies no threshold; it says above 0.95 "indicates high likelihood". The paper evaluates at 0.5 and GovTech's demo uses 0.4 and 0.7 bands. **[Documented]**
- **R6** (36w, 16 bullets): **One text string plus the guardrail ids.** Send the text and a guardrails dictionary; no extra parameters for LionGuard. A suite key expands to all eleven scores. Languages come from the model, not the Sentinel docs. **[Documented]**
- **R7** (51w, 9 bullets): **Minimum setup:** Sentinel beta access from a Singapore IP, or a self-hosted Hugging Face model (an OpenAI or Gemini key for LionGuard 2 and 2.1, none for Lite). Use labelled safe and unsafe texts per category and level in English, Singlish, Chinese, Malay and Tamil, with benign near-misses, then sweep thresholds. **[Inferred]**
- **R8** (29w, 11 bullets): **Key open questions.** Which variant runs per suite key, how embeddings are hosted, what threshold to use, and any evaluation of Lite or of 2.1 beyond one blog table.
- **R9** (24w, 21 bullets): Sentinel documentation pages, the Responsible AI playbook, GovTech Hugging Face model repos and demo Space, the LionGuard 2 paper and the GovTech AI blog.

## GovTech Sentinel: Prompt-attack detection

- **R1** (25w, 6 bullets): **Prompt-attack detection.** Sentinel scores text for attempts to manipulate the model, bypass system constraints or inject malicious instructions, returning a score and a confidence label. **[Documented]**
- **R2** (40w, 9 bullets): **Instructions that subvert the model.** Covers attempts to manipulate the model, bypass system constraints or inject instructions. The one documented example asks for the text above as JSON. Sentinel names no further attack types and makes no wider jailbreak claim. **[Documented]**
- **R3** (31w, 11 bullets): **User input; output use is disputed.** The aiguardian types table marks it Input only while its guardrail table marks it Input and Output. The docs list no parameters beyond the text. **[Documented]**
- **R4** (33w, 8 bullets): **Model not disclosed.** Sentinel docs, playbook and developer portal name no model, data or method for prompt-attack detection, and no matching repository appears in GovTech's Hugging Face models, Spaces or datasets by name. **[Not disclosed]**
- **R5** (35w, 8 bullets): **Score from 0 to 1 plus a confidence label.** The example returns a score of 1.0 and a confidence of "high". Sentinel applies no threshold; the generic guidance is that above 0.95 indicates high likelihood. **[Documented]**
- **R6** (25w, 7 bullets): **Text only.** Send the text to check and the guardrail name; there are no additional parameters. Languages, length limit and context handling are not stated. **[Documented]**
- **R7** (40w, 6 bullets): **Minimum setup:** Sentinel beta access from a Singapore IP and a labelled set of attack and benign prompts across attack styles and languages; send each to the guardrail, log score and confidence, and sweep thresholds. No self-hosted option was found. **[Inferred]**
- **R8** (30w, 11 bullets): **Key open questions.** The backing model, whether it runs on output, what confidence means, coverage beyond the three stated intents, and the threshold to use. Alternatives exist elsewhere in Sentinel.
- **R9** (20w, 13 bullets): Sentinel documentation pages, the Responsible AI playbook Sentinel page, the developer portal pages, and the GovTech Hugging Face org listing.

## GovTech Sentinel: Off-topic prompt detection against the system prompt

- **R1** (38w, 7 bullets): **Off-topic prompt detection.** Sentinel's off-topic guardrail scores how likely a user message is irrelevant to the application's system prompt, from 0 to 1. GovTech built it from synthetic system-prompt and user-prompt pairs, with no topic list to maintain. **[Documented]**
- **R2** (39w, 12 bullets): **Requests outside the application's scope.** Flags user prompts irrelevant to the domain set by the system prompt, benign or not. It also catches many jailbreak and harmful prompts as a side effect, but is not built to detect them. **[Documented]**
- **R3** (34w, 11 bullets): **User input, judged against the system prompt.** It checks the user message and needs the system message as context. The aiguardian types table also ticks Output, but both guardrail tables list it as Input. **[Documented]**
- **R4** (33w, 24 bullets): **Fine-tuned classifiers on synthetic pairs.** GovTech publishes a bi-encoder and a cross-encoder, trained on synthetic system-prompt and user-prompt pairs, for self-hosting from Hugging Face; Sentinel offers the off-topic guardrail through its hosted API. **[Documented]**
- **R5** (35w, 14 bullets): **Score from 0 to 1, higher means more off-topic.** Sentinel returns only a score and applies no threshold. The paper's internal studies suggest typical thresholds of 0.4 to 0.6; the playbook example rejects above 0.7. **[Documented]**
- **R6** (31w, 14 bullets): **User text plus a system message.** The aiguardian docs take the user text and a system-role message list; the playbook shows a separate system prompt parameter. English only per the paper. **[Documented]**
- **R7** (42w, 7 bullets): **Minimum setup:** Sentinel beta access from a Singapore IP, or self-hosting one open model; several system prompts, each with on-topic, off-topic and borderline user prompts in English. Send them with the system message, record scores, and sweep thresholds from 0.4 to 0.7. **[Inferred]**
- **R8** (27w, 10 bullets): **Key open questions.** Which model variant Sentinel serves, which parameter name works, whether it applies to output, behaviour on non-English or multi-turn input, and the right threshold.
- **R9** (20w, 16 bullets): Sentinel documentation pages, Responsible AI playbook pages, the off-topic paper, and the GovTech Hugging Face model repos and demo Space.

## GovTech Sentinel: System-prompt leakage detection

- **R1** (30w, 6 bullets): **Output check for leaked system prompts.** Sentinel's leakage check looks at whether a model's reply directly or indirectly reveals the application's system prompt, and returns a 0 to 1 score. **[Documented]**
- **R2** (37w, 12 bullets): **Exposure of hidden instructions in the output.** Targets the model revealing its system prompt, including paraphrased, obfuscated or reordered copies. Sentinel's types table lists it as an output-only risk. No category list or evaluation figure is published. **[Documented]**
- **R3** (36w, 7 bullets): **LLM output, judged against the system prompt.** It reads the generated reply as the checked text and needs the system prompt, passed as a message with the system role. It runs on the output side only. **[Documented]**
- **R4** (42w, 16 bullets): **Sentinel's model is not disclosed.** GovTech's only public artefact is a demo Space with a logistic regression over embeddings of the system prompt and the output; no page links it to the service, though a Sentinel docs example reuses a Space example. **[Not disclosed]**
- **R5** (33w, 11 bullets): **A 0 to 1 score, no verdict.** The score is the probability that the output fails the guardrail. Sentinel applies no threshold server-side; its general guidance is that above 0.95 is high likelihood. **[Documented]**
- **R6** (31w, 12 bullets): **Output text plus a system-role message.** The aiguardian docs take the reply text and a system-role message; the playbook shows a separate system prompt parameter. An API key header is required. **[Documented]**
- **R7** (37w, 6 bullets): **Minimum setup:** Sentinel beta access from a Singapore IP address, plus a set of system prompts each paired with leaking outputs (verbatim, paraphrased, obfuscated, partial) and non-leaking outputs, then a script that sends them and records scores. **[Inferred]**
- **R8** (24w, 9 bullets): **Key open questions.** Which model Sentinel serves, what threshold works, how it behaves on long or non-English prompts, and whether it reads user messages.
- **R9** (18w, 17 bullets): Sentinel docs on aiguardian.gov.sg, the GovTech Responsible AI playbook, and the GovTech Hugging Face Space and its files.

## GovTech Sentinel: Refusal detection

- **R1** (40w, 5 bullets): **Detects whether the AI refused the user.** Sentinel's refusal guardrail looks at the model's reply and the user prompt, and returns a score, a class label such as Reject, and a written reason. Sentinel says it is "useful for analytics". **[Documented]**
- **R2** (36w, 7 bullets): **Model declines or sets a boundary.** The condition is that the reply declines the user's request; the example flags a polite decline that does not offer an alternative. How borderline replies are classed is not published. **[Documented]**
- **R3** (30w, 5 bullets): **LLM reply, with the user prompt as context.** It runs on the output side, inspecting the generated reply, and needs the user prompt that the reply answers to judge intent. **[Documented]**
- **R4** (24w, 6 bullets): **Model not disclosed.** Sentinel names no model, prompt or rubric for refusal detection, and no GovTech model, Space or paper to self-host is listed. **[Not disclosed]**
- **R5** (37w, 7 bullets): **Score, class label and reasoning.** The response carries a 0 to 1 score, a classification string, and a reasoning sentence. The score is read as the probability the text fails the guardrail; no refusal-specific threshold is given. **[Documented]**
- **R6** (25w, 7 bullets): **Reply text plus the user prompt.** The aiguardian docs require the user prompt as a guardrail parameter; the playbook table lists no parameters for refusal. **[Documented]**
- **R7** (36w, 6 bullets): **Minimum setup:** Sentinel beta access from a Singapore IP address, and labelled (user prompt, reply) pairs covering clear refusals, partial refusals, redirects, full answers and benign replies. Send each pair and log score, class and reasoning. **[Inferred]**
- **R8** (24w, 7 bullets): **Key open questions.** The backing model, the list of class labels, how borderline replies are scored, and whether the user prompt is really required.
- **R9** (18w, 12 bullets): Sentinel docs on aiguardian.gov.sg and the GovTech Responsible AI playbook Sentinel page; the GovTech Hugging Face org listing.

## GovTech Sentinel: PII detection and masking (AWS Bedrock)

- **R1** (38w, 6 bullets): **Finds and masks personal data using AWS Bedrock Guardrails.** Sentinel's AWS-based PII check returns a score, a masked copy of the text and the list of matches. Sentinel documents the wrapper; AWS documents what the PII filter is. **[Documented]**
- **R2** (27w, 16 bullets): **Personal identifiers in prompts or replies.** Default targets are Singapore NRIC and email; other types follow AWS's entity list. Phone and address are not masked unless chosen. **[Documented]**
- **R3** (31w, 7 bullets): **Text of prompts or replies, either side.** Sentinel marks it Input/Output; the caller picks which text to send. AWS says masking covers model inputs and outputs, not logs or tool fields. **[Documented]**
- **R4** (38w, 21 bullets): **A wrapper around AWS Bedrock Guardrails.** Sentinel names AWS Bedrock Guardrails as the engine; AWS describes its sensitive-information filter as a context-dependent ML detector with optional regex. Region, configuration and how matches become a score are not disclosed. **[Documented]**
- **R5** (32w, 9 bullets): **Score, masked text and entity list.** Output has a 0 to 1 score, masked text with type tags, and a list of each match and its type. Sentinel gives no PII-specific threshold. **[Documented]**
- **R6** (35w, 14 bullets): **Text, plus an optional entity list.** Optional list of entity types, defaulting to Singapore NRIC and email. Sentinel states a 25,000-character limit for its AWS guardrails; AWS states its own limits in text units instead. **[Documented]**
- **R7** (45w, 7 bullets): **Minimum setup:** Sentinel beta access from a Singapore IP address, and a labelled set of texts with synthetic NRIC and FIN numbers, emails, phone numbers, names and addresses, plus near-miss strings and multilingual examples. Request each entity type and compare masked text with expected output. **[Inferred]**
- **R8** (27w, 10 bullets): **Key open questions.** How Singapore NRIC is detected, whether other types are accepted, region and configuration, how a result becomes a score, language coverage and limit behaviour.
- **R9** (21w, 19 bullets): Sentinel docs on aiguardian.gov.sg and the GovTech playbook; AWS official Bedrock Guardrails documentation for the wrapped PII filter (not Sentinel docs).

## GovTech Sentinel: Generic content moderation via AWS Bedrock Guardrails

- **R1** (38w, 5 bullets): **Generic harm and prompt-attack checks from AWS.** Sentinel exposes five AWS content filters (hate, insults, misconduct, sexual, violence) and an AWS prompt attack filter, each returning a 0 to 1 score. All six are listed as input checks. **[Documented]**
- **R2** (40w, 14 bullets): **Five harm categories and prompt attacks, as AWS defines them.** AWS defines hate, insults, sexual, violence and misconduct for prompts and replies, and prompt attacks as jailbreaks, prompt injection and (Standard tier only) prompt leakage. Sentinel gives only one-line descriptions. **[Documented]**
- **R3** (31w, 10 bullets): **User input, according to Sentinel.** Sentinel marks all six checks Input only, though AWS content filters also run on model replies. The AWS prompt attack filter is input-only in AWS too. **[Documented]**
- **R4** (43w, 19 bullets): **Wraps AWS Bedrock Guardrails content filters.** Sentinel names AWS Bedrock Guardrails as the backing service. AWS says its filters classify text as NONE, LOW, MEDIUM or HIGH confidence and block at a set strength. Tier, strengths, region and score mapping are not disclosed. **[Documented]**
- **R5** (41w, 11 bullets): **A 0 to 1 score per check.** Each id returns a score and time; the documented examples show only 0.0 and 1.0. Sentinel gives no AWS-specific threshold, and the playbook example uses 0.5 for prompt attack while the docs say 0.95. **[Documented]**
- **R6** (35w, 12 bullets): **Text only, no parameters.** The request is the text plus a check id or the suite key. Sentinel states a 25,000-character limit; AWS states limits in text units, and lists Malay and Tamil as supported. **[Documented]**
- **R7** (38w, 7 bullets): **Minimum setup:** Sentinel beta access from a Singapore IP address, plus labelled prompts for each category in English, Singlish, Chinese, Malay and Tamil, jailbreak and injection prompts, and benign near-misses. Send the aws suite and log every score. **[Inferred]**
- **R8** (31w, 10 bullets): **Key open questions.** Tier, strengths and region Sentinel configures, how a result becomes a score, whether output text works, AWS language coverage on Singapore text, and how this compares with LionGuard.
- **R9** (22w, 22 bullets): Sentinel docs on aiguardian.gov.sg and the GovTech playbook; AWS official Bedrock Guardrails documentation for what the wrapped filters mean (not Sentinel docs).
