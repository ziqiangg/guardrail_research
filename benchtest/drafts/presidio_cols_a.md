## Column PD1: Presidio: PII detection in text (Analyzer)
### R1
Summary: **Finds PII in text and reports where.** The Analyzer runs recognizers over one string and returns each entity type with its position and a confidence score. Rewriting the text is left to the separate Anonymizer. **[Documented]**
Detail:
• The docs describe it as: "The Presidio analyzer is a Python based service for detecting PII entities in text." (Presidio docs, analyzer page, read 2026-10-09) **[Documented]**
• Mechanism in one line: "During analysis, it runs a set of different PII Recognizers, each one in charge of detecting one or more PII entities using different mechanisms." (Presidio docs, analyzer page) **[Documented]**
• The Home page lists the modules separately: "Presidio analyzer: PII identification in text" and "Presidio anonymizer: De-identify detected PII entities using different operators" (Presidio docs, Home page) **[Documented]**
• The FAQ says: "Presidio is a library or SDK rather than a service." (Presidio docs, FAQ page) **[Documented]**
• Python entry point `AnalyzerEngine.analyze`, whose docstring reads "Find PII entities in text using different PII recognizers for a given language." (`analyzer_engine.py@2.2.364:185`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• REST entry point `POST /analyze` (`presidio-analyzer/app.py@2.2.364:67`); the same app serves `GET /recognizers` (line 134), `GET /supportedentities` (line 149) and `GET /health` (line 62) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• A list of strings in `text` is run as a batch: `batch_request = isinstance(req_data.text, list)` (`presidio-analyzer/app.py@2.2.364:76`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Presidio returns detections, not a decision: the result fields (R5) hold spans, scores and explanations but no pass, fail or block value, and the docs describe identification and anonymisation only, so it is a PII detector rather than a guardrail with a verdict **[Inferred]**
### R2
Summary: **PII entity types, English by default.** The supported-entities page lists about 80 types, mostly national identifiers. A default English setup loads 16 pattern recognizers plus a spaCy name and place model. Detection is not guaranteed complete. **[Documented]**
Detail:
• Scope: "It provides fast identification and anonymization modules for private entities in text and images such as credit card numbers, names, locations, social security numbers, bitcoin wallets, US phone numbers, financial data and more." (Presidio docs, Home page) **[Documented]**
• The entity page says: "Presidio contains predefined recognizers for PII entities." and "This page describes the different entities Presidio can detect and the method Presidio employs to detect those." (Presidio docs, supported entities page) **[Documented]**
• The page groups types into Global, 18 country sections (USA, UK, Spain, Italy, Poland, Singapore, Australia, India, Finland, Korea, Nigeria, Philippines, Canada, Sweden, South Africa, Thai, Turkey, Germany) and Medical / Clinical; 80 entity rows counted on 2026-10-09 **[Documented]**
• Global types: `CREDIT_CARD`, `CRYPTO`, `DATE_TIME`, `EMAIL_ADDRESS`, `IBAN_CODE`, `IP_ADDRESS`, `MAC_ADDRESS`, `NRP`, `LOCATION`, `PERSON`, `PHONE_NUMBER`, `MEDICAL_LICENSE`, `URL` (supported entities page) **[Documented]**
• Detection-method column examples: `CREDIT_CARD` "Pattern match and checksum"; `PERSON`, `LOCATION` and `NRP` "Custom logic and context"; `CRYPTO` is described as "Currently only Bitcoin address is supported" **[Documented]**
• Eight `MEDICAL_*` types come from the optional medical recognizer: "Detected using the MedicalNERRecognizer (requires the transformers extra). Uses the blaze999/Medical-NER model by default." (Presidio docs wording; the model itself is third-party) **[Documented]**
• Some types are weak by design: `DE_PLZ` is described with "High false-positive risk" and "base confidence is 0.05" (supported entities page) **[Documented]**
• Out of the box the shipped file `default_recognizers.yaml` has 74 recognizer entries (73 distinct names, `UkPostcodeRecognizer` appears twice), of which 50 carry `enabled: false` (counted by parsing the YAML) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Enabled entries (24, each with the suffix Recognizer): CreditCard, UsBank, UsLicense, UsItin, UsPassport, UsSsn, Nhs, EsNif, EsNie, ItDriverLicense, ItFiscalCode, ItVatCode, ItIdentityCard, ItPassport, PlPesel, Crypto, Date, Email, Iban, Ip, MedicalLicense, MacAddress, Phone, Url **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Disabled entries include UK driving licence, NINO, passport, postcode and vehicle registration; US MBI and NPI; Singapore FIN (`SgFinRecognizer`, line 135); Australia (4); India (6); Korea (4); Sweden (2); Germany (13); Turkey (2); Thai, South Africa, Nigeria (2), Philippines (2) and Canada SIN identifiers; Spanish passport; `HuggingFaceNerRecognizer`; `BasicLangExtractRecognizer` **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• An executed presidio-research notebook shows the default English engine reporting 19 supported entities (the 16 pattern types plus `PERSON`, `LOCATION`, `NRP`, with `DATE_TIME` shared) and 17 loaded recognizers, the 16 pattern recognizers plus `SpacyRecognizer` (notebook 4, cells 10 output) **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• The Spanish, Italian and Polish entries are enabled in the YAML but the registry accepts English only, and the loader drops other languages with "Recognizer not added to registry because" (`recognizers_loader_utils.py@2.2.364:177`), so they are not active in a default setup; this reading matches the notebook output above **[Inferred]**
• Source conflict C2: the entity page lists `SG_UEN`, `FI_PERSONAL_IDENTITY_CODE` and `KR_PASSPORT` with no default-off note (supported entities page) **[Documented]**
• Source conflict C2: `default_recognizers.yaml` has no entry for `SgUenRecognizer`, `FiPersonalIdentityCodeRecognizer`, `KrPassportRecognizer` or `AbaRoutingRecognizer`, although all four are exported in `predefined_recognizers/__init__.py` (the `ABA_ROUTING_NUMBER` type is not on the entity page) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Languages: "In its default configuration, it contains recognizers and models for English." and "Each recognizer can support one language." (Presidio docs, languages page) **[Documented]**
• Config: `supported_languages:` followed by `  - en` opens both `default_recognizers.yaml` (lines 1-2) and `default_analyzer.yaml` (lines 1-2) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Ready-made multi-language NLP files: `spacy_multilingual.yaml` (en `en_core_web_lg`, de `de_core_news_md`, es `es_core_news_md`) and `stanza_multilingual.yaml` (en, de) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Language caveat: "While different detection mechanisms such as regular expressions are language agnostic, the context words used to increase the PII detection confidence aren't." (languages page) **[Documented]**
• Limit: "there is no guarantee that Presidio will find all sensitive information. Consequently, additional systems and protections should be employed." (Presidio docs, Home page) **[Documented]**
• FAQ: "Every PII identification logic would have its errors, and there is a trade-off between false positives (falsely detected text) and false negatives (PII entities which are not detected)." **[Documented]**
• FAQ false-positive example: "A driver's license number, for example, could be any 9-digit number." **[Documented]**
• FAQ on hosted services: "Most of these SaaS offerings use dedicated ML models and other logic for PII detection and often have better entity coverage or accuracy than Presidio." **[Documented]**
• Prompt-injection, harmful-content and topic checks are out of purpose: the Home, analyzer, supported-entities and FAQ pages describe PII and sensitive-data identification only and list no such entity or check **[Inferred]**
• No entity type for API keys, passwords or other secrets (checked the supported entities page and `default_recognizers.yaml`) **[Not disclosed]**
### R3
Summary: **Any string, before or after the model.** The Analyzer takes one text field and a language per call and needs no system prompt or conversation history. The same call works on prompts, responses, retrieved passages and tool output. **[Inferred]**
Detail:
• The call signature takes `text` and `language` plus filters; no argument names a role, direction or conversation turn (`analyzer_engine.py@2.2.364:169`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• REST: "The text to analyze. Can be a single string or an array of strings." and `text` plus `language` are the two required fields (`docs/api-docs/api-docs.yml@2.2.364`, AnalyzeRequest) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `language` is mandatory: `raise Exception("No language provided")` (`presidio-analyzer/app.py@2.2.364:80`), and it must be one the engine supports (line 83) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `context` is a list of words, not earlier turns: ":param context: List of context words to enhance confidence score if matched" (`analyzer_engine.py@2.2.364:200`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• No direction flag or prompt role exists in the request fields (`analyzer_request.py@2.2.364:25-42`), so one column serves prompts and responses and no system or user prompt is needed as context **[Inferred]**
• Presidio's LiteLLM page shows the flow "App <-> LiteLLM Proxy + Presidio PII Masking <-> LLM Provider" (Presidio docs, not LiteLLM docs) **[Documented]**
• Presidio's OpenAI sample says the toolkit "anonymizes Personally Identifiable Information (PII) in the messages sent to the LLM and subsequently de-anonymizes the responses received from it." (Presidio docs, Data Protection toolkit for OpenAI page) **[Documented]**
• No Presidio page shows the Analyzer run on a model reply; doing so is the same call on a different string, and likewise for retrieved text and tool inputs or outputs **[Inferred]**
• Other media have their own modules: "Presidio image redactor: Redact PII entities from images using OCR and PII identification" and "Presidio structured: PII identification in structured/semi-structured data" (Home page) **[Documented]**
• Automatic language detection is not described (checked the analyzer and languages pages and `app.py`; the caller supplies `language`) **[Not disclosed]**
### R4
Summary: **Rules plus a spaCy model.** Regex, checksum and context-word recognizers run beside a spaCy name model; scores are boosted by context, thresholded and de-duplicated. Optional extras add Stanza, transformers, GLiNER and language-model recognizers. MIT licence; the project is moving to a community organisation. **[Documented]**
Detail:
• Home page: "Predefined or custom PII recognizers leveraging Named Entity Recognition, regular expressions, rule based logic and checksum with relevant context in multiple languages." **[Documented]**
• Pipeline order in `analyze`: NLP pass, each recognizer, context enhancement (line 268), then `results = self.__remove_low_scores(results, score_threshold, recognizers)` (line 280), `remove_duplicates` (line 281), allow list (line 284) (`analyzer_engine.py@2.2.364`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Default NLP engine: `nlp_engine_name: spacy` (line 1) and `model_name: en_core_web_lg` (line 5) in `conf/default.yaml`; the Docker build also defaults to this file (`Dockerfile@2.2.364`, `ARG NLP_CONF_FILE`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Correction to the brief: `default.yaml` ignores `ORGANIZATION` ("Has many false positives", line 25) and also `CARDINAL`, `EVENT`, `LANGUAGE`, `LAW`, `MONEY`, `ORDINAL`, `PERCENT`, `PRODUCT`, `QUANTITY` and `WORK_OF_ART`; it maps `PER` and `PERSON` to `PERSON`, `NORP` to `NRP`, `FAC`, `LOC`, `GPE` to `LOCATION`, `DATE` and `TIME` to `DATE_TIME` **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The spaCy recognizer gives every NER hit a fixed base score: `ner_strength: float = 0.85,` (`spacy_recognizer.py@2.2.364:41`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Pattern recognizers: "A PatternRecognizer is a type of entity recognizer that uses regular expressions to detect entities in text." (analyzer page) **[Documented]**
• Context step: "The default context-aware enhancer in Presidio is the LemmaContextAwareEnhancer which compares each recognizer's context terms with the lemma of each token in the sentence." (Presidio docs, context tutorial) **[Documented]**
• Enhancer defaults: `context_similarity_factor: float = 0.35,` (line 37), `min_score_with_context_similarity: float = 0.4,` (line 38), `context_prefix_count: int = 5,` (line 39), `context_suffix_count: int = 0,` (line 40) (`lemma_context_aware_enhancer.py@2.2.364`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Alternative NLP engines: "We also support Stanza using the spacy-stanza package" (FAQ); `TransformersNlpEngine` is "a spaCy pipeline which encapsulates a Huggingface Transformers model instead of the spaCy NER component" (transformers page); sample config model `transformers: StanfordAIMI/stanford-deidentifier-base` (`conf/transformers.yaml@2.2.364:7`) **[Documented]**
• A transformers engine still needs spaCy: "a small spaCy model (such as en_core_web_sm) is required." (Presidio docs, installation page) **[Documented]**
• Other shipped engine configs: `no_op.yaml` (`nlp_engine_name: no_op`, line 1) and `slim.yaml` (`nlp_engine_name: slim`, line 5) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Optional recognizers (none in the default YAML): GLiNER with default model `urchade/gliner_multi_pii-v1` (`gliner_recognizer.py@2.2.364:37`, extra `gliner`); `HuggingFaceNerRecognizer` with no default model (`model_name: Optional[str] = None,`, line 111); medical NER; Azure AI Language; Azure Health Data Services (extra `ahds`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Language-model recognizers use LangExtract with Ollama or Azure OpenAI; the sample page title carries "(Experimental Feature)" (Presidio docs, language-model recognizer page) **[Documented]**
• The analyzer README adds: "LangExtract recognizers do not validate connectivity during initialization." (`presidio-analyzer/README.md@2.2.364:61`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Remote detectors are supported through a base class: "A configuration for a recognizer that runs on a different process / remote machine." (`remote_recognizer.py@2.2.364:12`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Optional-extra names in the analyzer package: `server`, `transformers`, `stanza`, `azure-ai-language`, `ahds`, `gliner`, `langextract` (`presidio-analyzer/pyproject.toml@2.2.364`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Serving: Flask app, default port `DEFAULT_PORT = "3000"` (`presidio-analyzer/app.py@2.2.364:19`); Docker runs `exec gunicorn -w "$WORKERS" -b "0.0.0.0:$PORT" "app:create_app()"` (`entrypoint.sh@2.2.364:2`) with `ENV WORKERS=1` and `USER 1001` (`Dockerfile@2.2.364:15,49`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Images: `docker run -d -p 5002:3000 ghcr.io/data-privacy-stack/presidio-analyzer:latest` (Presidio docs, installation page) **[Documented]**
• Source conflict C4: the analyzer page shows `docker run -p 5002:3000 presidio-analyzer`, a locally built image name, while the installation page uses the GHCR name **[Documented]**
• Registry move: "The legacy Microsoft Container Registry images at mcr.microsoft.com/presidio-* are no longer updated." (installation page) **[Documented]**
• Other deployments: "Multiple usage options, from Python or PySpark workloads through Docker to Kubernetes." (Home page); the site navigation lists App Service, Kubernetes, Spark, Fabric and Azure Data Factory samples **[Documented]**
• Integration: LiteLLM uses `callbacks = ["presidio"]` with `PRESIDIO_ANALYZER_API_BASE="http://localhost:5002"` (Presidio docs, not LiteLLM docs) **[Documented]**
• NeMo Guardrails runs Presidio as separate input and output rails; those are sheet 3 NeMo Guardrails columns E and F (NeMo Guardrails: Input-level PII detection & masking; NeMo Guardrails: Output-level PII detection & masking) and are not repeated here **[Inferred]**
• Version: `presidio_analyzer` is `version = "2.2.364"` (`presidio-analyzer/pyproject.toml@2.2.364:7`); tag 2.2.364 is commit 779dbd28 dated 2026-07-22 (local clone log) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Whether 2.2.364 is the latest GitHub release was not re-confirmed: github.com and the GitHub API returned HTTP 403 through the proxy on 2026-10-09, and the release-note text could not be read **[To be verified]**
• The tagged code contains NoOpNlpEngine, per-recognizer `score_thresholds` and `BatchDeanonymizeEngine' while `CHANGELOG.md@2.2.364` still lists them under its unreleased heading, above 2.2.363 **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Python: the live installation page lists 3.10, 3.11, 3.12 and 3.13 (Presidio docs, read 2026-10-09) **[Documented]**
• Python: `docs/installation.md@2.2.364:24` also lists `* 3.14` (source conflict C3 with the live page) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Python: `requires-python = ">=3.10,<3.15"` (`presidio-analyzer/pyproject.toml@2.2.364:25`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Licence: `Copyright (c) Presidio Contributors.` (`LICENSE@2.2.364:3`) under the MIT text, and "Presidio will continue to be open source under the MIT license." (Presidio docs, transition page) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Ownership: "The Presidio project is in the process of transitioning from a Microsoft-owned project to an independent, community-governed open source project under the new GitHub organization Data Privacy Stack." and "Microsoft supports this transition" (Presidio docs, transition page) **[Documented]**
• Docs host: `https://data-privacy-stack.github.io/presidio/` answers HTTP 301 to `https://presidio.dataprivacystack.org/` (observed 2026-10-09); `https://microsoft.github.io/presidio/` returns a stub page saying "This page has moved." **[Documented]**
• The FAQ adds: "Presidio is not an official product of any company and comes with no warranty or SLA." **[Documented]**
### R5
Summary: **Spans and scores, no verdict.** Each hit has an entity type, start, end and a 0 to 1 score, with an optional explanation of which recognizer and context word fired. The default score threshold is 0. Vendor notebooks report F2 0.661 for default settings on synthetic data. **[Documented]**
Detail:
• Result fields: `entity_type`, `start`, `end`, `score`, `analysis_explanation`, `recognition_metadata` and nothing else (`recognizer_result.py@2.2.364:34-47`); there is no verdict or action field **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Over REST the metadata is stripped: `_exclude_attributes_from_dto` deletes `recognition_metadata` (`presidio-analyzer/app.py@2.2.364:170`) and `analysis_explanation` is null unless `return_decision_process` is true (`analyzer_engine.py@2.2.364:502`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Score range 0 to 1: `MAX_SCORE = 1.0` (`entity_recognizer.py@2.2.364:41`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Explanation fields: `recognizer`, `pattern_name`, `pattern`, `original_score`, `score`, `textual_explanation`, `score_context_improvement`, `supportive_context_word`, `validation_result` (`analysis_explanation.py@2.2.364`); the docs add "Decision-process traces explain why PIIs were detected, but not why they were not detected!" **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Decision process is opt-in: "To enable it, call the analyze method with return_decision_process set as True." and "Logging of the decision process is turned off by default." (Presidio docs, decision process page) **[Documented]**
• Threshold default: `default_score_threshold: float = 0,` (`analyzer_engine.py@2.2.364:63`) and `default_score_threshold: 0` (`conf/default_analyzer.yaml@2.2.364:3`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Threshold precedence: a per-request `score_threshold` "bypasses recognizer-level score thresholds for this request"; otherwise the entity-specific recognizer threshold, then the recognizer default, then the engine default (`analyzer_engine.py@2.2.364:192`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Threshold advice in the FAQ is generic: "Change the acceptance threshold, which defines what is the minimum confidence value for a detected entity to be returned." **[Documented]**
• Example values only: `default_score_threshold: 0.4` in the no-code tutorial (`docs/tutorial/08_no_code.md@2.2.364:41`) and `default_score_threshold: 0.7` in the engine-provider page (`docs/analyzer/analyzer_engine_provider.md@2.2.364:172`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• A German-language recipe advises "to 0.4–0.5 for production use to filter out low-confidence pattern-only matches from context-free digit strings" (`docs/recipes/german-language-support/README.md@2.2.364:125`); this is a recipe tip for German identifiers, not a general default **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• presidio-research evaluates through a wrapper whose default is `score_threshold: float = 0.4,` (`presidio_analyzer_wrapper.py@0.3.2:19`) and notebook 4 builds `AnalyzerEngine(default_score_threshold=0.4)` **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• A recommended score threshold for the default English recognizers (checked the analyzer, FAQ, evaluation, decision-process and tutorial pages; only the examples above) **[Not disclosed]**
• Score building blocks: the spaCy base score is 0.85 (R4), a weak pattern can start very low (the context tutorial uses 0.01), and a context hit adds 0.35 with a floor of 0.4 (R4) **[Documented]**
• Evaluation advice: "In PII detection, recall is often more important than precision, as we'd like to avoid missing any PII." and "we recommend to use the β=2 score, which gives more importance to recall." (Presidio docs, evaluation page) **[Documented]**
• Only vendor figures found are in presidio-research notebook 4 (default recognizers, threshold 0.4, 1500 synthetic samples in `synth_dataset_v2.json`, `SpanEvaluator(iou_threshold=0.75)`, binary PII versus O): F2 0.661, precision 0.733, recall 0.646 (cell 19 output) **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• Notebook 5 (a tuned engine with a Hugging Face NER recognizer using `OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1`, extra recognizers, threshold 0.3): F2 0.91, precision 0.921, recall 0.907 on the same set (cell 29 output); that model is third-party and not part of a default install **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• The docs say notebook 5 shows how to "boost the f score in ~30%" (Presidio docs, evaluation page) **[Documented]**
• The notebook outputs differ from that wording: 0.661 to 0.91 is +0.249 absolute and about +38 percent relative **[Inferred]**
• Notebook 4 says "Using Presidio with default parameters (not recommended for production)." (markdown cell 9) **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• These notebook figures understate the default engine on that set: it labels `STREET_ADDRESS` (3071 tokens), `TITLE`, `AGE` and `ZIP_CODE`, which have no default entity type; this is my reading of the printed entity counts against the 19 default entities **[Inferred]**
• Timing: notebook 4 prints "Wall time: 5.84 s" for predicting 1500 samples, hardware and Presidio version not stated **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• Recognizer authors are told: "Anything above 100ms per request with 100 tokens is probably not good enough." (Presidio docs, developing recognizers page), guidance for contributors, not a measured latency **[Documented]**
• Latency, throughput and memory figures for the Analyzer service (checked the Home, analyzer, FAQ, evaluation, GPU and recipe pages) **[Not disclosed]**
• Accuracy figures for non-English recognizers: the German recipe states "Formal evaluation against a labelled German dataset has not yet been performed." and lists Precision, Recall, F2 and Latency as TBD (`README.md@2.2.364:101`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Published accuracy for the GLiNER and language-model recognizers (checked their sample pages) **[Not disclosed]**
### R6
Summary: **Text and a language code; the rest is optional.** Callers can restrict entities, set a score threshold, pass an allow list, context words or per-request recognizers, and ask for the explanation. A spaCy model is needed locally; other languages need extra configuration. **[Documented]**
Detail:
• Required: `text` and `language` (ISO 639-1, "Two characters for the desired language in ISO_639-1 format") (`docs/api-docs/api-docs.yml@2.2.364`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Optional in `app.py`: `entities`, `correlation_id`, `score_threshold`, `return_decision_process`, `ad_hoc_recognizers`, `context`, `allow_list`, `allow_list_match`, `regex_flags` (`presidio-analyzer/app.py@2.2.364:85-105`; `analyzer_request.py@2.2.364:25-42`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs versus code: the API spec omits `allow_list`, `allow_list_match` and `regex_flags`, which `app.py` accepts; the code is the better guide **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `entities`: "If entities=None then all entities are looked for." (`analyzer_engine.py@2.2.364`, `analyze` docstring); `GET /supportedentities` lists what the running engine can return **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `allow_list_match` is `"exact"` by default (`analyzer_request.py@2.2.364:39`) and can be set to regex; the allow-list tutorial shows `allow_list = ["bing.com"]` removing that hit **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Batch and workers: `DEFAULT_BATCH_SIZE = "500"` (`presidio-analyzer/app.py@2.2.364:20`) and `N_PROCESS` defaults to 1 (line 21) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Config files are chosen by environment variables `ANALYZER_CONF_FILE`, `NLP_CONF_FILE` and `RECOGNIZER_REGISTRY_CONF_FILE` (`presidio-analyzer/app.py@2.2.364:46`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Models: "When packaging the code into a Docker container, NLP models are automatically installed." and the models listed in `conf/default.yaml` are installed at build (Presidio docs, languages page) **[Documented]**
• Install: `pip install presidio_analyzer` then `python -m spacy download en_core_web_lg` (Presidio docs, installation page) **[Documented]**
• Extra services need credentials only if you enable them: Azure AI Language reads `AZURE_AI_ENDPOINT` (`azure_ai_language.py@2.2.364:89`), Azure OpenAI recognizers use `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY` (analyzer README), the medical-health service uses `AHDS_ENDPOINT` (Presidio docs, AHDS page) **[Documented]**
• Cloud versus local for language-model recognizers: the Presidio table lists Azure OpenAI as "Cloud (Azure)" and Ollama as "Local (on-premises)", and advises Ollama "when data must stay on-premises" (Presidio docs, language-model recognizer page) **[Documented]**
• Azure AI Language is described as "a cloud-based service that provides Natural Language Processing (NLP) features for detecting PII in text." (supported entities page) **[Documented]**
• Enabling those recognizers means text leaves the Presidio process for the configured Azure endpoint; this follows from the endpoint and key parameters in the recognizer code **[Inferred]**
• Decision-process logging writes a trace to standard output that includes the token list of the analysed text (page example shows words and digits from the sample sentence), so PII can reach logs when `log_decision_process=True` **[Inferred]**
• Docs versus code: the decision-process page says the correlation id "can be retrieved from each API response header: x-correlation-id", but `presidio-analyzer/app.py@2.2.364` sets no such header (searched the file) **[Inferred]**
• Authentication: "Presidio API endpoints do not include built-in authentication by design." and "It is strongly recommended not to expose Presidio services directly to untrusted networks without an authentication layer in front of them." (Presidio docs, FAQ) **[Documented]**
• Maximum text length or request size (checked `app.py`, the analyzer, languages and FAQ pages; none stated or enforced) **[Not disclosed]**
• TLS for the REST service (checked the FAQ, installation and analyzer pages; not mentioned) **[Not disclosed]**
### R7
Summary: **Minimum setup:** pip install the Analyzer and a spaCy model, or run the GHCR image; no account or key is needed. Send labelled prompts and replies with known PII spans plus near-misses, compare returned spans per entity, sweep the score threshold, and score with presidio-research. **[Inferred]**
Detail:
• **Minimum setup:** `pip install presidio_analyzer presidio_anonymizer`, `python -m spacy download en_core_web_lg`, then `AnalyzerEngine().analyze(text=..., language="en")`; or run the Docker service and `POST /analyze` with `{"text": ..., "language": "en"}` **[Inferred]**
• Install steps as documented: `pip install presidio_analyzer`, `pip install presidio_anonymizer`, `python -m spacy download en_core_web_lg` (Presidio docs, installation page) **[Documented]**
• Docker alternative and a first call: `curl -d '{"text":"John Smith drivers license is AC432223", "language":"en"}' -H "Content-Type: application/json" -X POST http://localhost:3000/analyze` (Presidio docs, analyzer page) **[Documented]**
• The default config needs no account, key or network: only the optional Azure and language-model recognizers call external endpoints (R6) **[Inferred]**
• First check what is active: `GET /supportedentities?language=en` and `GET /recognizers` return the entity and recognizer lists of the running engine (`presidio-analyzer/app.py@2.2.364:134-161`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Test set: entity-level ground truth (type, start, end) for prompts, replies, retrieved text and tool output, including entities outside default coverage (street addresses, secrets) and near-misses such as plain 9-digit numbers **[Inferred]**
• presidio-research is the vendor route: "Presidio-Research is a python package with a set of tools that help you evaluate the performance of the Presidio Analyzer." (Presidio docs, evaluation page) **[Documented]**
• Its pieces: `PresidioAnalyzerWrapper` wraps an `AnalyzerEngine` (`presidio_analyzer_wrapper.py@0.3.2:12`), `InputSample` holds `full_text` and `spans` (`data_objects.py@0.3.2:207`), and notebook 4 scores with `SpanEvaluator(iou_threshold=0.75)` and F2 **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• Dataset labels differ from Presidio's, so notebook 4 maps them first with `CanonicalMapper` (markdown "Review entity mapping") **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• presidio-research 0.3.2 depends on `"presidio-analyzer>=2.2.364",` (`pyproject.toml@0.3.2:18`) and is MIT licensed (line 6) **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• Run a threshold sweep (for example 0, 0.3, 0.4, 0.5, 0.7) and per-entity checks, weighting recall with F2 as the docs advise **[Inferred]**
• Record latency per request and per batch with the default one worker, and repeat for any non-English configuration on its own labelled set **[Inferred]**
### R8
Summary: **Key open questions.** No recommended threshold or latency figure, a thin default entity set, three listed entities missing from the default config, and unclear data flow for cloud recognizers.
Detail:
• A recommended `score_threshold` per entity for the default recognizers (checked the analyzer, FAQ, evaluation, decision-process and tutorial pages and the repo docs; only examples and one German recipe tip; needs testing on a labelled set)
• Latency and throughput of the REST service, including with the default single gunicorn worker (checked the docs pages and presidio-research; one unlabelled notebook timing only; needs testing)
• Per-entity accuracy of the default recognizers (the notebooks show aggregate numbers and interactive plots that were not readable as text)
• Which Presidio version produced the presidio-research notebook outputs (not printed in the outputs; the repo requires 2.2.364 or later)
• Whether `SG_UEN`, `FI_PERSONAL_IDENTITY_CODE` and `KR_PASSPORT` are active in a default install (the entity page lists them, the YAML omits them; a call to `/supportedentities` would settle it)
• Non-English quality: no figures for any non-English recognizer or NER model (checked the languages page and the German recipe)
• What exactly leaves the network for Azure AI Language, Azure OpenAI and AHDS recognizers, and retention on the Azure side (Presidio pages do not state it; the service terms belong to Microsoft)
• Whether authentication, TLS or rate limiting is recommended beyond the FAQ paragraph (checked the FAQ, installation and Kubernetes sample list)
• Behaviour on very long inputs (checked the docs and `app.py`; nothing stated; needs testing)
• Whether 2.2.364 is the latest release and what its release notes say (github.com returned 403 here)
• Owner question Q01: the docs say the project moved to Data Privacy Stack; whether to treat that organisation as the official source is a user ruling
### R9
Summary: Presidio docs site pages, the Presidio repository at tag 2.2.364, and the presidio-research repository at tag 0.3.2.
Detail:
• https://presidio.dataprivacystack.org/
• https://presidio.dataprivacystack.org/analyzer/
• https://presidio.dataprivacystack.org/supported_entities/
• https://presidio.dataprivacystack.org/analyzer/languages/
• https://presidio.dataprivacystack.org/analyzer/decision_process/
• https://presidio.dataprivacystack.org/analyzer/developing_recognizers/
• https://presidio.dataprivacystack.org/analyzer/nlp_engines/transformers/
• https://presidio.dataprivacystack.org/tutorial/06_context/
• https://presidio.dataprivacystack.org/installation/
• https://presidio.dataprivacystack.org/faq/
• https://presidio.dataprivacystack.org/evaluation/
• https://presidio.dataprivacystack.org/project_transition/
• https://presidio.dataprivacystack.org/ahds_integration/
• https://presidio.dataprivacystack.org/samples/docker/litellm/
• https://presidio.dataprivacystack.org/samples/deployments/openai-anonymaztion-and-deanonymaztion-best-practices/
• https://presidio.dataprivacystack.org/samples/python/langextract/
• https://data-privacy-stack.github.io/presidio/
• https://microsoft.github.io/presidio/
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/analyzer_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/app.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/analyzer_request.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/recognizer_result.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/analysis_explanation.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/entity_recognizer.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/remote_recognizer.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/default.yaml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/default_analyzer.yaml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/default_recognizers.yaml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/spacy_multilingual.yaml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/stanza_multilingual.yaml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/transformers.yaml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/no_op.yaml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/slim.yaml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/recognizer_registry/recognizers_loader_utils.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/context_aware_enhancers/lemma_context_aware_enhancer.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/predefined_recognizers/nlp_engine_recognizers/spacy_recognizer.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/predefined_recognizers/ner/gliner_recognizer.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/predefined_recognizers/ner/huggingface_ner_recognizer.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/predefined_recognizers/third_party/azure_ai_language.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/predefined_recognizers/__init__.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/README.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/pyproject.toml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/Dockerfile
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/entrypoint.sh
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/LICENSE
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/CHANGELOG.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/installation.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/api-docs/api-docs.yml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/tutorial/08_no_code.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/analyzer/analyzer_engine_provider.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/recipes/german-language-support/README.md
• https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/README.md
• https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/pyproject.toml
• https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/presidio_evaluator/models/presidio_analyzer_wrapper.py
• https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/presidio_evaluator/data_objects.py
• https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/notebooks/4_Evaluate_Presidio_Analyzer.ipynb
• https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/notebooks/5_Evaluate_Custom_Presidio_Analyzer.ipynb
## Column PD2: Presidio: PII anonymisation and masking in text (Anonymizer)
