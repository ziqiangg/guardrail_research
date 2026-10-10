## Column LN1: LionGuard: Localised harmful-content classification
### R1
Summary: **Localised harmful-content classification of one text string.** LionGuard is GovTech's classifier for Singapore's languages and context. It returns a probability for each harm category and severity level. GovTech publishes the classifier on Hugging Face; two variants embed text through OpenAI or Gemini, one locally. **[Documented]**
Detail:
• The playbook describes it as "GovTech's localised content moderation guardrail for Singapore's linguistic and cultural context, addressing limitations in localisation and contextualisation faced by standard moderation guardrails" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• The playbook says "LionGuard assigns a risk score to each of the categories below. Some categories are further classified into severity levels, with Level 2 indicating higher severity than Level 1" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• The playbook says there are three versions of LionGuard 2 that "share the same methodology and differ only in the embedding model they use" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• The playbook says "All three versions are open-sourced for self-hosting via Hugging Face and accessible through the Sentinel API" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• The LionGuard 2 card says it is "a multilingual content moderation classifier tuned for English/Singlish, Chinese, Malay, and Tamil in the Singapore context" **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The LionGuard 2 card says it "leverages OpenAI's `text-embedding-3-large` with a multi-head classifier" **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The `predict` docstring of LionGuard 2 says "Predict the probabilities of each label being true" (`lionguard2.py@be4e38c9:148`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The LionGuard 2.1 card opens with the same sentence, naming LionGuard 2.1 **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• The LionGuard 2.1 card says it "leverages Gemini's `gemini-embedding-001` with a multi-head classifier" **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• The LionGuard 2 Lite card opens with the same sentence (it names the model "LionGuard 2") and adds "LionGuard 2 Lite runs fully locally, with no external API calls" **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• The paper abstract calls LionGuard 2 "a lightweight, multilingual moderation classifier tailored to the Singapore context, supporting English, Chinese, Malay, and partial Tamil" (arXiv 2507.15339 abstract) **[Documented]**
• The blog of 29 Jul 2025 says "LionGuard 2 is open-sourced, including model weights and part of the training data" (GovTech AI blog) **[Documented]**
### R2
Summary: **Six harm categories plus an overall flag, with severity levels.** Hateful, insults, sexual, physical violence, self-harm and all other misconduct; four have Level 1 and Level 2. Covers English, Singlish, Chinese, Malay and Tamil; the playbook and paper call Tamil partial or moderate. **[Documented]**
Detail:
• The LionGuard 2 card lists Overall safety, Hate, Insults, Sexual content, Physical violence, Self-harm and Other misconduct, as eleven output keys (`binary`, `hateful_l1`, `hateful_l2`, `insults`, `sexual_l1`, `sexual_l2`, `physical_violence`, `self_harm_l1`, `self_harm_l2`, `all_other_misconduct_l1`, `all_other_misconduct_l2`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The LionGuard 2.1 card lists the same seven groups and eleven keys **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• The LionGuard 2 Lite card lists the same seven groups and eleven keys **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• The LionGuard 2 card taxonomy gives Hate Level 1 "Discriminatory" and Level 2 "Hate Speech"; Insults and Physical Violence have no sub-levels; Sexual Level 1 "Not appropriate for minors" and Level 2 "Not appropriate for all ages" **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The same card taxonomy gives Self-Harm Level 1 "Ideation" and Level 2 "Action / Suicide", and All Other Misconduct Level 1 "Generally not socially accepted" and Level 2 "Illegal activities" **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The playbook says "If a Level 2 instance is detected, Level 1 is also flagged by design" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• The playbook defines All Other Misconduct as including "facilitating illegal acts (under Singapore law) or other forms of socially harmful activity" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• The paper adds a seventh, overall head: "we attached a single binary head (safe/unsafe) as we found it to consistently boost overall F1" (arXiv 2507.15339 section 4.2.2) **[Documented]**
• The LionGuard 2 card says it is tuned for "English/Singlish, Chinese, Malay, and Tamil"; its metadata language tags are `en`, `ms`, `ta`, `zh` **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The playbook says "Support for English, Singlish, Chinese, Malay, and partial Tamil" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• The paper says "its Tamil performance remains moderate" (arXiv 2507.15339 section 5.3); the card says Tamil without a caveat and the playbook says "partial Tamil", so the sources differ in strength **[Documented]**
• On the paper's native-speaker test set LionGuard 2 scores F1 41.1 on Tamil, 85.0 on Chinese and 81.4 on Malay (arXiv 2507.15339 Table 13) **[Documented]**
• This is a different test set from RabakBench, so the Tamil F1 of 41.1 here and 66.6 in Table 1 are not comparable (premise: Table 13 is the native-speaker set and Table 1 is RabakBench) **[Inferred]**
• The paper says all tested embedding models underperformed on Tamil, and "adding LLM-translated Tamil data worsened results" (arXiv 2507.15339 section 7.3) **[Documented]**
• The paper says its training data "contained little to no Chinese/Malay/Tamil-only examples", so non-English coverage relies on the embedder's cross-lingual transfer (arXiv 2507.15339 section 6.3) **[Documented]**
• On a noisy copy of RabakBench Singlish, binary F1 falls from 87.1 to 85.6 for LionGuard 2 (arXiv 2507.15339 Table 5) **[Documented]**
• The paper says "the system is not foolproof" and recommends "combining LionGuard 2 with human oversight in high-stakes settings" (arXiv 2507.15339 Ethical Considerations) **[Documented]**
• The model scores content harms only: every key in the card and config belongs to one of the six harm categories or the overall flag, and none is a jailbreak or prompt-injection category **[Inferred]**
• Jailbreak or prompt-injection detection: no result or claim is reported (checked the three cards, the playbook, the paper including its Appendix E.2 native-speaker test design, and the three GovTech blog posts) **[Not disclosed]**
• The paper's native-speaker annotators were encouraged to write tricky cases including "prompt-injection or role-playing scenarios" for the test set (arXiv 2507.15339 Appendix E.2) **[Documented]**
### R3
Summary: **Any single text, before or after the model.** GovTech's paper shows it as both an input filter for user prompts and an output filter for model responses. The classifier call takes only an array of embeddings of the text. **[Documented]**
Detail:
• The paper says "LionGuard 2 is designed as a lightweight moderation system for any text content" (arXiv 2507.15339 section 3) **[Documented]**
• The paper describes "both an input filter (screening user prompts) and an output filter (verifying model responses)" (arXiv 2507.15339 section 3, Figure 2 "bidirectional filter around an LLM Chatbot") **[Documented]**
• The paper adds that it "can also be used in AI application safety testing, to detect if application responses contain unsafe elements" (arXiv 2507.15339 section 3) **[Documented]**
• A GovTech blog (29 Jul 2025) has a section headed "LionGuard 2 as an input and output guardrail" (GovTech AI blog) **[Documented]**
• The `predict` method of LionGuard 2 takes "A numpy array of embeddings (N * INPUT_DIMENSION)" (`lionguard2.py@be4e38c9:151`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The `predict` method of LionGuard 2.1 has the same signature and docstring (`lionguard2.py@1c3a9ea7:151`) **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• The `predict` method of LionGuard 2 Lite has the same signature and docstring (`lionguard2lite.py@d56c17a0:151`) **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• The model therefore has no input or output flag, endpoint or config section; direction is the caller's choice of which string to embed (premise: the only runtime input is an embedding array) **[Inferred]**
• Retrieved text, tool inputs and tool outputs can be scored the same way, because the model sees one string with no role (premise: one embedded string in, no direction or role argument) **[Inferred]**
• No system prompt or user prompt is passed as context; `infer(texts)` embeds a list of strings and calls `predict` (`inference.py@be4e38c9`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• Each text in a batch is embedded and scored independently, and conversation history is not an input (premise: `infer` embeds a flat list of strings) **[Inferred]**
• Cross-reference: the hosted Sentinel service lists its LionGuard guardrails as type Input/Output (Sentinel docs, hosted API, read 2026-10-09) **[Documented]**
### R4
Summary: **Frozen embedder plus a small ordinal classifier.** The three variants differ in the embedder: OpenAI embeddings (LionGuard 2), Gemini embeddings (2.1) or local EmbeddingGemma (2 Lite). GovTech publishes the small classifier and its code on Hugging Face, not the embedder. **[Documented]**
Detail:
• The paper says "The pre-trained embeddings are frozen and fed into a trainable multi-head network" (arXiv 2507.15339 section 4.2.2) **[Documented]**
• The playbook says LionGuard 2 "pairs a pre-trained embedding model with a multi-head ordinal classifier" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• Code in LionGuard 2: shared layers Linear(input_dim, 256), ReLU, Dropout(0.2), Linear(256, 128), ReLU, Dropout(0.2), then seven heads each Linear(128, 32), ReLU, Linear(32, 2), Sigmoid, with the comment "2 thresholds for ordinal classification" (`lionguard2.py@be4e38c9:118-138`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The seven heads follow the config `category_order` (binary, hateful, insults, sexual, physical_violence, self_harm, all_other_misconduct); a head with one key returns only its first output and a head with two keys returns both, giving eleven keys (`lionguard2.py@be4e38c9:171-176`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• A GovTech blog (21 Aug 2026) says "LionGuard 2 uses a shared representation feeding into 11 classification heads" (GovTech AI blog) **[Documented]**
• The code has seven head modules and eleven output keys, so the blog's 11 probably counts output keys (premise: `lionguard2.py@be4e38c9:171-176` gives eleven keys from seven heads) **[Inferred]**
• LionGuard 2 classifier size: 848,942 float32 parameters and a `model.safetensors` of 3,398,496 bytes (Hugging Face Hub metadata of the pinned model page, read 2026-10-09) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The paper says "The resulting classifier contains 0.85M parameters and occupies only 3.2 MB on disk" (arXiv 2507.15339 section 4.2.2) **[Documented]**
• LionGuard 2.1 classifier size: 848,942 float32 parameters and 3,398,496 bytes, the same as LionGuard 2 (Hugging Face Hub metadata of the pinned model page, read 2026-10-09) **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• LionGuard 2 Lite classifier size: 259,118 float32 parameters and 1,039,200 bytes (Hugging Face Hub metadata of the pinned model page, read 2026-10-09) **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• The parameter totals equal the sum of the layer shapes in the code for input widths 3072 and 768 (arithmetic: 786,688 + 32,896 + 7 x 4,194 = 848,942; 196,864 + 32,896 + 29,358 = 259,118) **[Inferred]**
• LionGuard 2 embedder: the card says it "leverages OpenAI's `text-embedding-3-large` with a multi-head classifier" **[Documented: repo govtech/lionguard-2@be4e38c9]**
• LionGuard 2.1 embedder: the card says it "leverages Gemini's `gemini-embedding-001` with a multi-head classifier" **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• LionGuard 2 Lite embedder: the card says "This `lite` version leverages Google's `embeddinggemma-300m` (768-dimensional embeddings)" and that it "runs fully locally, with no external API calls" **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• Conflict: the docstring of `lionguard2.py` in LionGuard 2 says the input is encoded with OpenAI's `text-embedding-3-small`, while the card, `inference.py` and `config.json` use `text-embedding-3-large` at 3072 dimensions (`lionguard2.py@be4e38c9:97`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The docstring of the LionGuard 2.1 model file names its own embedder, `gemini-embedding-001` (`lionguard2.py@1c3a9ea7:97`) **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• The docstring of the LionGuard 2 Lite model file names its own embedder, `embeddinggemma-300m` (`lionguard2lite.py@d56c17a0:97`) **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• The stale name therefore occurs only in the LionGuard 2 file (premise: the 2.1 and Lite docstrings at line 97 name their own embedders) **[Inferred]**
• The paper says OpenAI `text-embedding-3-large` "achieved the highest binary F1, scoring as much as 20% above the next-best model" among six encoders (arXiv 2507.15339 section 4.2.1) **[Documented]**
• The paper limitation says LionGuard 2 "inherits its representations from OpenAI's text-embedding-3-large" and that "Any future update to this embedding model would require may re-training and benchmarking" (as written; arXiv 2507.15339 section 7.1) **[Documented]**
• The playbook recommends "LionGuard 2.1" for best performance and "LionGuard 2 Lite" for local deployment, and calls Lite the "Most lightweight, on-prem variant with no external API dependency" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• The playbook says the LionGuard 2 paper and blog "describe how each version works" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• A separate paper, card section or training description for LionGuard 2.1 or 2 Lite (checked both cards, the playbook, html v1 and v2 of the LionGuard 2 paper, which name no Gemini or Gemma embedder, and the three blog posts; the blog of 28 Sep 2026 says only that embedding generation "can be run locally or through an API depending on the variant") **[Not disclosed]**
• Custom code, LionGuard 2: `config.json` maps AutoModel to `lionguard2.LionGuard2Model` and the card loads it with `trust_remote_code=True` **[Documented: repo govtech/lionguard-2@be4e38c9]**
• Custom code, LionGuard 2.1: `config.json` maps AutoModel to `lionguard2.LionGuard2Model` and the card loads it with `trust_remote_code=True` **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• Custom code, LionGuard 2 Lite: `config.json` maps AutoModel to `lionguard2lite.LionGuard2LiteModel` and the card loads it with `trust_remote_code=True` **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• Training set: 26,207 unique texts (20,333 online comments, 2,098 synthetic, 3,776 from open-source English sets), "70% smaller" than LionGuard 1's (arXiv 2507.15339 section 4.1.4) **[Documented]**
• Labels came from three LLM annotators, Gemini 2.0 Flash, o3-mini-low and Claude 3.5 Haiku (arXiv 2507.15339 section 4.1.3) **[Documented]**
• The playbook says the model "can be fully retrained within two minutes on standard CPUs" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• Open data: the dataset card says "This dataset is a subset of the LionGuard 2 training corpus" (2,098 Singlish/English chatbot-style rewrites with embeddings for all three variants) **[Documented: repo govtech/lionguard-2-synthetic-instruct@8aa43f61]**
• Training code or an inference repository on GitHub (checked `git ls-remote` for govtech-responsibleai/lionguard, /lionguard-demo, /lionguard2 and /LionGuard, each "Repository not found", the file lists of the three model repos and the dataset card on 2026-10-09; inference code lives only in the Hugging Face repos) **[Not disclosed]**
• Serving route: the playbook says the versions are "open-sourced for self-hosting via Hugging Face" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• A blog says embedding generation "can be run locally or through an API depending on the variant" (GovTech AI blog, 28 Sep 2026) **[Documented]**
• The paper says "LionGuard 2 replaces its predecessor", LionGuard 1, and is deployed on "the Singapore Government's AI Guardian platform" (arXiv 2507.15339 section 3) **[Documented]**
• Licence, repository file: the LICENSE says "the contents of this repository are provided under the MIT License SUBJECT FURTHER TO THE FOLLOWING", then Singapore governing law and SIAC arbitration (`LICENSE@be4e38c9`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The LionGuard 2.1 repository holds a LICENSE file (md5 01aeb061dcdbf0bd0612ad2b76ac5b6c, the same as the LionGuard 2 file; checked 2026-10-09) **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• The LionGuard 2 Lite repository holds a LICENSE file (md5 01aeb061dcdbf0bd0612ad2b76ac5b6c, the same as the LionGuard 2 file; checked 2026-10-09) **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• The LICENSE excludes "any asset or code identified by the Government Technology Agency ("GovTech") as not licensed to you" and GovTech and Singapore public-sector marks and images **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The LionGuard 2 card metadata reads `license: other`, `license_name: govtech-singapore`, `license_link: LICENSE` **[Documented: repo govtech/lionguard-2@be4e38c9]**
• The LionGuard 2.1 card metadata reads `license: other`, `license_name: govtech-singapore`, `license_link: LICENSE` **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• The LionGuard 2 Lite card metadata reads `license: other`, `license_name: govtech-singapore`, `license_link: LICENSE` **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• Licence, paper: "Our model weights are published on Hugging Face exclusively for research and public interest purposes only, with clear usage guidelines that prohibit deployment for harmful applications" (arXiv 2507.15339 Ethical Considerations) **[Documented]**
• The paper's contributions say "We release the classifier weights and a portion of our training data to support future research in LLM safety" (arXiv 2507.15339 section 1) **[Documented]**
• The paper's conclusion says "By releasing our model weights and training data subset, we aim to support broader adoption of localisation-aware moderation strategies" (arXiv 2507.15339 section 8) **[Documented]**
• The "clear usage guidelines that prohibit deployment for harmful applications" named in the paper's ethics section (checked the LICENSE, the three cards, the playbook page and the three blog posts; no such guidelines found) **[Not disclosed]**
• How the repository LICENSE, the card metadata and the paper's research-only statement relate (checked the LICENSE, the three cards, the playbook page, the three blog posts, the paper's ethics, contributions and conclusion, the Hugging Face collection and organisation pages; not stated) **[Not disclosed]**
• Retraining: a GovTech blog (21 Aug 2026) says "we'll be rolling out the first retrained LionGuard 2 model, incorporating your feedback, very soon" for Sentinel users, and that "access to retrained models are currently only available to Sentinel users within the Singapore Government" **[Documented]**
• The three model repositories were last modified 2025-11-18, and their head revisions on 2026-10-09 are the pinned ones (Hugging Face Hub metadata of the pinned model page, read 2026-10-09) **[Documented]**
• No retrained model has therefore been published in those repositories (premise: no commit since 2025-11-18 and the blog says retrained models are for Sentinel users) **[Inferred]**
• Whether a retrained LionGuard 2 will be published on Hugging Face (checked the 21 Aug 2026 blog, the playbook and the three repositories) **[Not disclosed]**
• Cross-reference: Sentinel also serves the same three variants as `lionguard-2`, `lionguard-2-1` and `lionguard-2-lite`; API behaviour, ids, token limits and access stay under the Sentinel column (Sentinel docs, "LionGuard Versions", hosted API, read 2026-10-09) **[Documented]**
• Source conflict: the Sentinel docs write the OpenAI embedder as "text-embedding-large-3", while the card, paper and playbook write `text-embedding-3-large` (Sentinel docs, hosted API, read 2026-10-09) **[Documented]**
### R5
Summary: **A probability per key, no verdict.** The model returns 11 probabilities from 0 to 1 and applies no cut-off. GovTech's paper reports binary F1 at a 0.5 point, for example 77.0 for LionGuard 2 on its own test set. **[Documented]**
Detail:
• LionGuard 2 `predict` returns "A dictionary of probabilities" keyed by the eleven output keys, each a Python list of floats, one per input row (`lionguard2.py@be4e38c9:154`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• LionGuard 2.1 `predict` returns the same eleven keys with the same code (`lionguard2.py@1c3a9ea7:154`) **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• LionGuard 2 Lite `predict` returns the same eleven keys with the same code (`lionguard2lite.py@d56c17a0:154`) **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• The first output of a head is P(y>0) and the second P(y>1), the latter used only where a Level 2 key exists (code comment "j=1 uses P(y>1) if L2 category exists", `lionguard2.py@be4e38c9:175`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• LionGuard 2 ordinal rule: "If L2 category exists, and P(L2) > P(L1)," both probabilities are set to their average "to maintain ordinal consistency" (`lionguard2.py@be4e38c9:179-180`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• LionGuard 2.1 applies the same ordinal rule (`lionguard2.py@1c3a9ea7:179`) **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• LionGuard 2 Lite applies the same ordinal rule (`lionguard2lite.py@d56c17a0:179`) **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• After the averaging step `predict` converts the values to lists and returns them; the function applies no threshold and returns no verdict (`lionguard2.py@be4e38c9:193-195`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• A recommended operating threshold or calibration guidance for LionGuard 2, 2.1 or 2 Lite (checked the three cards, the two dataset cards, the label-mapping notebook, the playbook, the paper, the three blog posts and the demo Space README; only an evaluation point of 0.5 and the demo bands below appear) **[Not disclosed]**
• The paper says "we report binary F1 at a 0.5 threshold. For LionGuard 2, the score is taken from its dedicated safe/unsafe head", while baselines count as unsafe if any category exceeds the threshold (arXiv 2507.15339 section 5.1) **[Documented]**
• GovTech's demo Space shows a pass band below 0.4, a warn band from 0.4 to below 0.7 and fail at 0.7 or above on the binary score (`services.py@4ade46d1:123-125`, `script.js@4ade46d1:31-34`) **[Documented: repo govtech/lionguard-demo@4ade46d1]**
• The demo's chatbot route flags a message when the binary probability is above 0.5 (`services.py@4ade46d1:232`, called with 0.5 at line 262), and its default model is `lionguard-2.1` (`app/backend/models.py@4ade46d1:12`) **[Documented: repo govtech/lionguard-demo@4ade46d1]**
• The demo's analysis route appends each submitted text, its binary score and per-category maxima to a Google Sheet, and its chat route logs the message and scores to a Google Sheet, in both cases only when a sheet URL and service-account credentials are configured (`services.py@4ade46d1:158-165`, `:338-341`) **[Documented: repo govtech/lionguard-demo@4ade46d1]**
• The demo's chat route also sends each message to OpenAI for a chat reply and for OpenAI moderation (`services.py@4ade46d1:199-223`) **[Documented: repo govtech/lionguard-demo@4ade46d1]**
• The demo bands are demo behaviour, not a vendor recommendation (premise: the Space README says only "Demo for LionGuard 2") **[Inferred]**
• LionGuard 2 binary F1 at 0.5, own test set 77.0; RabakBench Singlish 88.1, Chinese 87.8, Malay 78.4, Tamil 66.6 in Table 1 column order SS, ZH, MS, TA (arXiv 2507.15339 Table 1) **[Documented]**
• Table 3 prints the same LionGuard 2 values under the header SS, MS, ZH, TA, so the Malay and Chinese labels are swapped between the two tables; Table 3 also gives SGHateCheck 98.8, 92.1, 97.4, 64.5 and SGToxicGuard 99.7, 98.2, 99.2, 71.5 under that header (arXiv 2507.15339 Table 3) **[Documented]**
• The GovTech blog of 29 Jul 2025 says "Performance remains robust for Chinese (88%) and Malay (78%)", which matches Table 1 **[Documented]**
• The GovTech RabakBench paper Table 4 gives LlamaGuard 4 12B Singlish 60.53, Chinese 54.20, Malay 65.92, Tamil 73.77, and AWS Bedrock Guardrail Chinese 0.59 and Malay 18.49, while Table 3 of the LionGuard 2 paper gives LlamaGuard 4 12B 60.6, 54.6, 65.2, 73.0 and AWS Bedrock 69.6, –, 21.1, – under SS, MS, ZH, TA (arXiv 2507.05980 Table 4, html v2 of 2 Feb 2026; arXiv 2507.15339 Table 3) **[Documented]**
• Table 3's Malay and Chinese labels are therefore probably swapped and Table 1's order is probably right, so the SGHateCheck and SGToxicGuard Chinese and Malay values need the same reading (premise: the RabakBench values match Table 3 only if the second column is Chinese, including the unsupported-language dash for AWS Bedrock) **[Inferred]**
• RabakBench Singlish is 88.1 in Tables 1 and 3 and 87.1 in Table 5, and RabakBench Tamil is 66.6 in Tables 1 and 3 and 66.5 in Table 8; no source explains the differences (arXiv 2507.15339 Tables 1, 3, 5 and 8) **[Documented]**
• English benchmarks, LionGuard 2 binary F1: BeaverTails 73.7, SORRY-Bench 73.7, OpenAI Moderation 70.5, SimpleSafetyTests 100.0; SORRY-Bench and SimpleSafetyTests hold only unsafe prompts, so F1 there reflects recall (arXiv 2507.15339 Table 4) **[Documented]**
• Comparators on the own test set (Table 3): OpenAI Moderation 54.7, AWS Bedrock Guardrails 57.1, LlamaGuard 3 8B 27.1, LlamaGuard 4 12B 26.5 (arXiv 2507.15339 Table 3) **[Documented]**
• Benchmark count: the paper compares on "1 internal test set and 16 public benchmarks" and its abstract says 17 benchmarks (arXiv 2507.15339 section 5.1) **[Documented]**
• A GovTech blog (29 Jul 2025) says LionGuard 2 matches or outperforms others "across 16 benchmarks" (GovTech AI blog) **[Documented]**
• The counts fit together if the 13 localised datasets include the internal test set (premise: Table 3 has 13 columns including Test, and Table 4 adds 4 English sets, giving 17 in all, or 1 internal and 16 public) **[Inferred]**
• The paper says "About 4% of examples … show disagreement between the binary head and category heads" (section 7.2); Table 11 gives an overall average of 4.19% over-predicted and 0.70% under-predicted over 43,075 samples, with RabakBench Singlish highest at 9.99% over-predict (arXiv 2507.15339 section 7.2, Appendix E.1, Table 11) **[Documented]**
• The paper says deriving the binary decision as the maximum of the category scores "removes the mismatch", and keeps the dedicated binary head because it boosts performance (arXiv 2507.15339 section 7.2) **[Documented]**
• LionGuard 2.1 binary F1 at 0.5, original test split 0.7318; RabakBench English/Singlish 0.8618, Malay 0.8420, Tamil 0.7267, Chinese 0.8688; SimpleSafetyTests 1.0000; OpenAI Moderation 0.7397 (GovTech AI blog, 28 Sep 2026) **[Documented]**
• The blog says it evaluated "on a held-out private LionGuard test split and RabakBench" and used "the same 0.5 threshold" for all models **[Documented]**
• The blog says it used "the same benchmarks used in our earlier LionGuard experiments: a held-out private LionGuard test split and RabakBench", and elsewhere calls the set "the original LionGuard 2 Test set" and "our private LionGuard 2 Test dataset" (GovTech AI blog, 28 Sep 2026) **[Documented]**
• Whether the blog's held-out private test split is the test set behind the paper's 77.0 for LionGuard 2 (checked the blog, the paper and the playbook; not stated) **[Not disclosed]**
• Calibration for LionGuard 2.1: the blog says it "had lower average calibration error on the original test set and the English/Singlish and Chinese RabakBench sets" than the Jev comparator model, which had lower error on Tamil **[Documented]**
• Comparator in the same blog table (not LionGuard): the Jev decision model scores 0.8385, 0.8745, 0.8766, 0.7805, 0.8809, 1.0000 and 0.7639 on the same seven rows, in the order given above **[Documented]**
• Evaluation of LionGuard 2 Lite (checked the card, the playbook, the paper, the three blog posts and the demo Space; none reports a figure) **[Not disclosed]**
• Per-language and per-category figures for LionGuard 2.1 beyond the seven blog numbers (checked the same sources) **[Not disclosed]**
• The paper says per-category F1 for all seven moderation systems ranges "from 30-70 %, reflecting the intrinsic difficulty of fine-grained safety labels" (arXiv 2507.15339 section 5.1, Appendix E.3) **[Documented]**
### R6
Summary: **One text string, embedded first.** Embed the text with the variant's own embedder (OpenAI key, Gemini key, or local EmbeddingGemma with a task prefix), then pass the vectors to the classifier. Input widths are 3072, 3072 and 768. **[Documented]**
Detail:
• LionGuard 2: `predict` takes an N by `input_dim` array and converts it to a float32 tensor; `input_dim` is 3072 in `config.json` **[Documented: repo govtech/lionguard-2@be4e38c9]**
• LionGuard 2.1: `input_dim` is 3072 in `config.json` **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• LionGuard 2 Lite: `input_dim` is 768 in `config.json` **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• LionGuard 2 embedding call: the card calls `client.embeddings.create(input=..., model="text-embedding-3-large", dimensions=3072)` with the comment "users to input their own OpenAI API key" **[Documented: repo govtech/lionguard-2@be4e38c9]**
• OpenAI's embeddings page says "By default, the length of the embedding vector is 1536 for text-embedding-3-small or 3072 for text-embedding-3-large" (OpenAI docs, not GovTech docs) **[Documented]**
• LionGuard 2.1 embedding call: `inference.py` uses `genai.Client(api_key=os.getenv("GEMINI_API_KEY"))` and `client.models.embed_content(model="gemini-embedding-001", contents=texts)` with the comment "users to input their own Gemini API key"; it passes no output dimension **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• Google's embeddings page says "By default, both models output a 3072-dimensional embedding" (Google Gemini API docs, not GovTech docs), matching the 3072 `input_dim` **[Documented]**
• LionGuard 2 Lite embedding call: `SentenceTransformer("google/embeddinggemma-300m")` with each text formatted as `task: classification | query: {text}` and the comment "NOTE: use encode() instead of encode_documents()" **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• LionGuard 2 Lite needs no API key (card: "runs fully locally, with no external API calls") but downloads Google's gated embedder **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• Packages, LionGuard 2: `numpy==2.3.1`, `openai==1.93.0`, `transformers==4.50.3`, `torch==2.3.1` (`requirements.txt`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• Packages, LionGuard 2.1: `numpy==2.3.1`, `transformers==4.50.3`, `torch==2.3.1`, `google-genai==1.50.1` (`requirements.txt`) **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**
• Packages, LionGuard 2 Lite: `numpy==2.3.1`, `transformers==4.50.3`, `torch==2.3.1`, `sentence-transformers==5.1.2` (`requirements.txt`) **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**
• Batch input: `infer(texts)` in LionGuard 2 embeds a list of strings in one call and passes the stacked array to `predict` (`inference.py@be4e38c9`) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• Maximum input length for LionGuard 2, 2.1 and 2 Lite (checked the three cards, the three code files, the playbook, the paper and the three blog posts; none states a limit) **[Not disclosed]**
• The classifier takes a fixed-size vector, so any length limit comes from the embedder, not from the head (premise: the first layer is Linear(input_dim, 256)) **[Inferred]**
• LionGuard 2 embedder limit: OpenAI lists a max input of 8192 for text-embedding-3-large (OpenAI docs, not GovTech docs) **[Documented]**
• LionGuard 2.1 embedder limit: Google lists an input token limit of 2,048 for gemini-embedding-001 (Google model page, not GovTech docs) **[Documented]**
• LionGuard 2 Lite embedder limit: the Hugging Face page of EmbeddingGemma lists a maximum input context length of 2048 tokens (Google page, not GovTech docs) **[Documented]**
• Speed for LionGuard 2: "Running synchronously on a single CPU, the embedding call handles ≈250 tokens/s, while the classifier head itself processes ≈1.5×10^4 tokens/s, giving an end-to-end throughput of ≈300 tokens/s" (arXiv 2507.15339 section 3, as written) **[Documented]**
• Whether the paper's "embedding call" is the hosted OpenAI request, and the CPU model used (checked the paper sections 3 and 7.1 and its hardware paragraph; not stated) **[Not disclosed]**
• The blog of 28 Sep 2026 says "A fair latency comparison would therefore require a more controlled setup" and that LionGuard "felt" similarly fast to Jev from initial impressions **[Documented]**
• Latency and hardware requirements (memory, GPU) for LionGuard 2.1 and 2 Lite (checked the cards, the playbook, the paper and the three blog posts; none states them) **[Not disclosed]**
• The dataset `lionguard-2-synthetic-instruct` ships precomputed embedding columns for all three variants, so the classifier head can be fed without an embedding call **[Documented: repo govtech/lionguard-2-synthetic-instruct@8aa43f61]**
• Cross-reference: the hosted Sentinel service lists token limits of 8192 for `lionguard-2` and 2048 for `lionguard-2-1` and `lionguard-2-lite`; these belong to that service and stay under the Sentinel column (Sentinel docs, hosted API, read 2026-10-09) **[Documented]**
### R7
Summary: **Minimum setup:** Python with Hugging Face Transformers and PyTorch, loading each model with remote code enabled. LionGuard 2 Lite also needs a Hugging Face login and acceptance of Google's Gemma terms for its embedder, but no API key. LionGuard 2 needs an OpenAI key and 2.1 a Gemini key, so test text goes to those providers. No threshold ships. **[Inferred]**
Detail:
• **Minimum setup:** `transformers`, `torch` and `numpy` installed, the chosen model loaded with `trust_remote_code=True`, each test text embedded with that variant's embedder and passed to `predict`; no threshold ships, so a bench would need to choose one **[Inferred]**
• A bench could pin each model repository to a revision, because the README loads the repository code with `trust_remote_code=True` and no revision argument, so the repository's Python runs on load (premise: the README usage and the repos can change) **[Inferred]**
• LionGuard 2 Lite path: `sentence-transformers` installed, a Hugging Face login and acceptance of Google's conditions for `google/embeddinggemma-300m`; the classifier and embedder then run locally with no embedding API key (premise: the card says "runs fully locally" and the embedder page is gated) **[Inferred]**
• Gating, from the owner's page (not GovTech docs): "This repository is publicly accessible, but you have to accept the conditions to access its files and content" (Hugging Face page of `google/embeddinggemma-300m`) **[Documented]**
• The same page shows `License: gemma`, and the Hub metadata of that repository reports `gated` as `manual` (Google's page and Hugging Face Hub metadata, not GovTech docs; read 2026-10-09) **[Documented]**
• Accepting the conditions needs a Hugging Face login: "Log in or Sign Up to review the conditions and access this model content." (Hugging Face page of google/embeddinggemma-300m, not GovTech docs) **[Documented]**
• Gemma Terms of Use section 3.2 says "You must not use any of the Gemma Services: for the restricted uses set forth in the Gemma Prohibited Use Policy" or "in violation of applicable laws and regulations" (Google page, last modified April 1, 2026, not GovTech docs) **[Documented]**
• The Gemma Terms of Use Appendix lists EmbeddingGemma among the covered models (Google page, not GovTech docs; read 2026-10-09) **[Documented]**
• The Gemma Prohibited Use Policy (last modified February 21, 2024) lists "Generating content that promotes or encourages hatred" and "Generate sexually explicit content", with a note that this "does not include content created for scientific, educational, documentary, or artistic purposes" (Google page, not GovTech docs) **[Documented]**
• The Gemma terms define Model Derivatives to include a model "created by transfer of patterns of the weights, parameters, operations, or Output of Gemma" and say "Outputs are not deemed Model Derivatives" (Google page, not GovTech docs) **[Documented]**
• LionGuard 2 path: an OpenAI API key is needed for `text-embedding-3-large`, and each text to be classified is sent to OpenAI to be embedded (premise: `inference.py` embeds the texts through the OpenAI client) **[Inferred]**
• LionGuard 2.1 path: a Gemini API key is needed for `gemini-embedding-001`, and each text to be classified is sent to Google to be embedded (premise: `inference.py` embeds the texts through `genai`) **[Inferred]**
• OpenAI's data-controls page says data sent to the OpenAI API "is not used to train or improve OpenAI models (unless you explicitly opt in to share data with us)" (OpenAI docs, not GovTech docs) **[Documented]**
• The same page lists `/v1/embeddings` with no training use, abuse-monitoring retention of 30 days, no application-state retention, and Zero Data Retention eligibility "Yes" (OpenAI docs, not GovTech docs; read 2026-10-09) **[Documented]**
• https://openai.com/policies/terms-of-use, /service-terms and /usage-policies returned HTTP 403 to a plain GET (observed 2026-10-09) **[Documented]**
• platform.openai.com/docs/guides/your-data ends at developers.openai.com/api/docs/guides/your-data (final URL, HTTP 200, observed 2026-10-09) **[Documented]**
• Gemini API Additional Terms (effective March 23, 2026) say of unpaid quota: "Do not submit sensitive, confidential, or personal information to the Unpaid Services" (Google page, not GovTech docs) **[Documented]**
• The same terms say "Your access to Gemini API is a "Paid Service" only when accessing the API through a Cloud Project associated with an active billing account", and that for Paid Services Google "doesn't use your prompts … or responses to improve our products" (Google page, not GovTech docs) **[Documented]**
• Google's Generative AI Prohibited Use Policy (last modified December 17, 2024) says "Do not engage in sexually explicit, violent, hateful, or harmful activities" and allows exceptions "based on educational, documentary, scientific, or artistic considerations" (Google page, not GovTech docs) **[Documented]**
• Whether the Gemini terms treat an embedding call differently from other calls, and whether gemini-embedding-001 has a free tier (checked the terms and pricing pages; the terms do not mention embeddings and the pricing page has no entry for gemini-embedding-001) **[Not disclosed]**
• A bench could use labelled safe and unsafe examples for each of the six categories and both levels, including Level 2 cases to check that Level 1 is also high **[Inferred]**
• A bench could add benign near-misses (for example matter-of-fact talk about sexuality, or news about violence) to measure false positives **[Inferred]**
• A bench could cover English, Singlish, Chinese, Malay and Tamil, with translated pairs, and expect weaker Tamil results (premise: the paper's Tamil figures) **[Inferred]**
• A bench could add noisy variants (casing, punctuation, misspellings) of a subset to repeat the paper's robustness check **[Inferred]**
• A bench could log the binary score and the category scores to count disagreements, since the paper reports the binary head over-predicting in about 4% of examples **[Inferred]**
• A bench could sweep thresholds per key and score the same texts as prompts and as model responses, plus any retrieved text or tool output it uses **[Inferred]**
• A bench could run the same set through LionGuard 2, 2.1 and 2 Lite and time each embedding call separately from the classifier call **[Inferred]**
• The dataset embeddings would allow a head-only smoke test with no external calls, but the set is Singlish and English only and about 2% unsafe, so it is unlikely to suit as an evaluation set (premise: dataset card statistics of 2,055 safe and 43 unsafe) **[Inferred]**
• Possible source of evaluation data: the RabakBench public set (132 samples per language), whose card lists "Benchmark moderation APIs / guardrails" as an intended use **[Documented: repo govtech/RabakBench@3c02a5b8]**
• The notebook `map_benchmark_labels.ipynb` maps seven public datasets (OpenAI moderation evaluation, BeaverTails, SimpleSafetyTests, RTP-LX, SORRY-Bench, SGHateCheck, SGToxicGuard) to the six-category taxonomy (code read, not run) **[Documented: repo govtech/lionguard-2@be4e38c9]**
• Those seven datasets could serve as further possible sources of evaluation data, with their own terms to be checked (premise: GovTech's notebook maps their labels to this taxonomy) **[Inferred]**
• A bench could avoid the hosted demo for test text, because its code may write submissions to a Google Sheet and sends chat messages to OpenAI (premise: `services.py@4ade46d1` behaviour above; whether the live Space has the sheet configured is not visible) **[Inferred]**
### R8
Summary: **Key open questions.** Operating threshold per variant, any Lite or wider 2.1 evaluation, input length and latency, how the licence texts relate, embedder terms for test text, whether a retrained model is released, and jailbreak coverage.
Detail:
• Recommended threshold for each of LionGuard 2, 2.1 and 2 Lite, and per key (checked the cards, playbook, paper, three blogs and the demo, only 0.5 and the demo bands appear; needs testing on a labelled set)
• Whether the dedicated binary key or the maximum of the category keys is the better verdict (the paper keeps the binary head because it boosts performance and says the maximum removes the mismatch; which works better per variant needs testing)
• Any evaluation of LionGuard 2 Lite, and any LionGuard 2.1 evaluation beyond one blog table with a private test split (checked the cards, playbook, paper and blogs; not stated)
• What happens on text longer than each embedder's limit, and whether Singlish, Chinese and Tamil token counts change the effective limit (the owners state the limits; GovTech states none; needs testing)
• Latency and hardware needs for LionGuard 2.1 and 2 Lite, and whether the paper's 300 tokens/s for LionGuard 2 includes the OpenAI round trip (checked the paper, cards and blogs; not stated; needs testing)
• Which of the paper's Table 1 and Table 3 column orders is right for Chinese and Malay, and the 88.1 versus 87.1 Singlish difference between Tables 3 and 5 (checked the paper, blog and RabakBench paper; needs the authors, or a rerun on the public RabakBench set)
• Table 1 of the LionGuard 2 paper prints Test 87.2 for Qwen3-Embedding-0.6B, above 77.0 for text-embedding-3-large, while section 4.2.1 says text-embedding-3-large "achieved the highest binary F1" (checked the paper html; not explained; needs the authors)
• How the repository LICENSE (MIT subject to Singapore law and SIAC arbitration) relates to the paper's statement that weights are published "exclusively for research and public interest purposes only" (checked the LICENSE, card metadata, paper, blogs and playbook; not stated)
• Whether OpenAI's usage policies and service terms (the pages returned HTTP 403) and Google's Gemini and Gemma terms allow sending harmful or explicit test text to the embedding services, and which account tier would apply (which test text may be sent is left to be decided before any testing; owners' pages only, not GovTech docs)
• Whether the retrained LionGuard 2 will be published on Hugging Face (blog of 21 Aug 2026 says only Sentinel users; the repositories are unchanged since 2025-11-18)
• Whether the Sentinel-hosted variants run the same weights as the Hugging Face repositories (checked the Sentinel docs and playbook; not stated; hosted-API question, closed beta)
• Jailbreak and prompt-injection coverage of any variant (no claim in any source; needs testing with adversarial prompts)
• Whether an embedder change would shift scores: the paper warns an OpenAI embedding update may need retraining (whether GovTech will retrain is not stated)
• Which variant could serve as a first-pass default: the playbook recommends 2.1 for performance and Lite for local use, while 2 and 2.1 need an external key (left open)
### R9
Summary: GovTech Hugging Face model repos, datasets and demo Space, the Responsible AI playbook, GovTech blog posts and papers, Sentinel docs for cross-references, and the embedder owners' pages.
Detail:
• https://huggingface.co/govtech/lionguard-2/tree/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591
• https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/lionguard2.py
• https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/LICENSE
• https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/inference.py
• https://huggingface.co/govtech/lionguard-2.1/tree/1c3a9ea7718f81ea32e6688c0ff18ac8866525e8
• https://huggingface.co/govtech/lionguard-2-lite/tree/d56c17a08a937f2591a906fb5c8ec699a844c422
• https://huggingface.co/spaces/govtech/lionguard-demo/tree/4ade46d19acee9c9088c711533a7c47fe24a8e3b
• https://huggingface.co/datasets/govtech/lionguard-2-synthetic-instruct/tree/8aa43f6172eb7eb158fd433fe3cf627c9a30db26
• https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/lionguard.md
• https://govtech-responsibleai.github.io/playbook/tools/lionguard/
• https://arxiv.org/html/2507.15339
• https://arxiv.org/html/2507.05980
• https://blog.ai.gov.sg/introducing-lionguard-2-multilingual-llm-guardrail-for-singapore/
• https://blog.ai.gov.sg/guardrails-in-the-wild-closing-the-retraining-loop-for-lionguard-2/
• https://blog.ai.gov.sg/decision-models-for-guardrails-exploring-jev-and-kev-for-moderation/
• https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails
• https://huggingface.co/google/embeddinggemma-300m
• https://ai.google.dev/gemma/terms
• https://ai.google.dev/gemini-api/docs/embeddings
• https://developers.openai.com/api/docs/guides/embeddings
• https://openai.com/policies/terms-of-use
• https://developers.openai.com/api/docs/guides/your-data
• https://openai.com/policies/usage-policies
• https://ai.google.dev/gemini-api/terms
• https://ai.google.dev/gemma/prohibited_use_policy
• https://policies.google.com/terms/generative-ai/use-policy
• https://ai.google.dev/gemini-api/docs/models/gemini-embedding-001
• https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/map_benchmark_labels.ipynb
• https://huggingface.co/datasets/govtech/RabakBench/tree/3c02a5b8574b0d0374d532704be6971e67532e22
• https://huggingface.co/spaces/govtech/lionguard-demo/blob/4ade46d19acee9c9088c711533a7c47fe24a8e3b/app/backend/services.py
• https://huggingface.co/spaces/govtech/lionguard-demo/blob/4ade46d19acee9c9088c711533a7c47fe24a8e3b/app/backend/models.py
