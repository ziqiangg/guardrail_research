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
• An executed presidio-research notebook shows the default English engine reporting 19 supported entities (16 pattern-based types, which include `DATE_TIME`, plus `PERSON`, `LOCATION` and `NRP`) and 17 loaded recognizers, the 16 pattern recognizers plus `SpacyRecognizer` (notebook 4, cell 10 output) **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
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
• `default.yaml` ignores `ORGANIZATION` ("Has many false positives", line 25) and also `CARDINAL`, `EVENT`, `LANGUAGE`, `LAW`, `MONEY`, `ORDINAL`, `PERCENT`, `PRODUCT`, `QUANTITY` and `WORK_OF_ART`; it maps `PER` and `PERSON` to `PERSON`, `NORP` to `NRP`, `FAC`, `LOC`, `GPE` to `LOCATION`, `DATE` and `TIME` to `DATE_TIME` **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The spaCy recognizer gives every NER hit a fixed base score: `ner_strength: float = 0.85,` (`spacy_recognizer.py@2.2.364:41`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Pattern recognizers: "A PatternRecognizer is a type of entity recognizer that uses regular expressions to detect entities in text." (analyzer page) **[Documented]**
• Context step: "The default context-aware enhancer in Presidio is the LemmaContextAwareEnhancer which compares each recognizer's context terms with the lemma of each token in the sentence." (Presidio docs, context tutorial) **[Documented]**
• Enhancer defaults: `context_similarity_factor: float = 0.35,` (line 37), `min_score_with_context_similarity: float = 0.4,` (line 38), `context_prefix_count: int = 5,` (line 39), `context_suffix_count: int = 0,` (line 40) (`lemma_context_aware_enhancer.py@2.2.364`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Alternative NLP engines: "We also support Stanza using the spacy-stanza package" (FAQ) and `TransformersNlpEngine` is "a spaCy pipeline which encapsulates a Huggingface Transformers model instead of the spaCy NER component" (Presidio docs, transformers page) **[Documented]**
• Sample transformers config: `transformers: StanfordAIMI/stanford-deidentifier-base` (`conf/transformers.yaml@2.2.364:7`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• A transformers engine still needs spaCy: "a small spaCy model (such as en_core_web_sm) is required." (Presidio docs, installation page) **[Documented]**
• Other shipped engine configs: `no_op.yaml` (`nlp_engine_name: no_op`, line 1) and `slim.yaml` (`nlp_engine_name: slim`, line 5) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Optional recognizers, none enabled by default: GLiNER with default model `urchade/gliner_multi_pii-v1` (`gliner_recognizer.py@2.2.364:37`, extra `gliner`); `HuggingFaceNerRecognizer` with no default model (`model_name: Optional[str] = None,`, line 111); medical NER; Azure AI Language; Azure Health Data Services (extra `ahds`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
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
• The tagged code contains NoOpNlpEngine, per-recognizer `score_thresholds` and `BatchDeanonymizeEngine` while `CHANGELOG.md@2.2.364` still lists them under its unreleased heading, above 2.2.363 **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Python: the live installation page lists 3.10, 3.11, 3.12 and 3.13 (Presidio docs, read 2026-10-09) **[Documented]**
• Python: `docs/installation.md@2.2.364:24` also lists `* 3.14` (source conflict C3 with the live page) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Python: `requires-python = ">=3.10,<3.15"` (`presidio-analyzer/pyproject.toml@2.2.364:25`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Licence file: `Copyright (c) Presidio Contributors.` (`LICENSE@2.2.364:3`) under the MIT text **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• "Presidio will continue to be open source under the MIT license." (Presidio docs, transition page) **[Documented]**
• Ownership: "The Presidio project is in the process of transitioning from a Microsoft-owned project to an independent, community-governed open source project under the new GitHub organization Data Privacy Stack." and "Microsoft supports this transition" (Presidio docs, transition page) **[Documented]**
• Docs host: `https://data-privacy-stack.github.io/presidio/` answers HTTP 301 to `https://presidio.dataprivacystack.org/` (observed 2026-10-09); `https://microsoft.github.io/presidio/` returns a stub page saying "This page has moved." **[Documented]**
• The FAQ adds: "Presidio is not an official product of any company and comes with no warranty or SLA." **[Documented]**
### R5
Summary: **Spans and scores, no verdict.** Each hit has an entity type, start, end and a 0 to 1 score, plus an optional explanation. The default score threshold is 0. A vendor notebook reports F2 0.661 for default settings on synthetic data. **[Documented]**
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
• Context effect on scores: "The confidence score is now 0.4, instead of 0.01, since the LemmaContextAwareEnhancer default context similarity factor is 0.35 and default minimum score with context similarity is 0.4." (Presidio docs, context tutorial) **[Documented]**
• Evaluation advice: "In PII detection, recall is often more important than precision, as we'd like to avoid missing any PII." and "we recommend to use the β=2 score, which gives more importance to recall." (Presidio docs, evaluation page) **[Documented]**
• Only vendor figures found are in presidio-research notebook 4 (default recognizers, threshold 0.4, 1500 synthetic samples in `synth_dataset_v2.json`, `SpanEvaluator(iou_threshold=0.75)`, binary PII versus O): F2 0.661, precision 0.733, recall 0.646 (cell 19 output) **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• Notebook 5 (a tuned engine with a Hugging Face NER recognizer using `OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1`, extra recognizers, threshold 0.3): F2 0.91, precision 0.921, recall 0.907 on the same set (cell 29 output); that model is third-party and not part of a default install **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• The docs say notebook 5 shows how to "boost the f score in ~30%" (Presidio docs, evaluation page) **[Documented]**
• The notebook outputs differ from that wording: 0.661 to 0.91 is +0.249 absolute and about +38 percent relative **[Inferred]**
• Notebook 4 says "Using Presidio with default parameters (not recommended for production)." (markdown cell 9) **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• Part of the gap is coverage: the notebook set labels `STREET_ADDRESS` (3071 tokens), `TITLE`, `AGE` and `ZIP_CODE`, which have no default entity type, although the mapping step may fold some labels into others (not checked); this is a reading of the printed entity counts against the 19 default entities **[Inferred]**
• Timing: notebook 4 prints "Wall time: 5.84 s" for predicting 1500 samples, hardware and Presidio version not stated **[Documented: repo data-privacy-stack/presidio-research@0.3.2]**
• Recognizer authors are told: "Anything above 100ms per request with 100 tokens is probably not good enough." (Presidio docs, developing recognizers page), guidance for contributors, not a measured latency **[Documented]**
• Latency, throughput and memory figures for the Analyzer service (checked the Home, analyzer, FAQ, evaluation, GPU and recipe pages) **[Not disclosed]**
• Accuracy figures for non-English recognizers: the German recipe states "Formal evaluation against a labelled German dataset has not yet been performed." and lists Precision, Recall, F2 and Latency as TBD (`docs/recipes/german-language-support/README.md@2.2.364:101`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Published accuracy for the GLiNER and language-model recognizers (checked their sample pages) **[Not disclosed]**
### R6
Summary: **Text and a language code; the rest is optional.** Callers can restrict entities, set a score threshold, pass an allow list, context words or per-request recognizers, and ask for the explanation. A spaCy model is needed locally; other languages need extra configuration. **[Documented]**
Detail:
• Required: `text` and `language` (ISO 639-1, "Two characters for the desired language in ISO_639-1 format") (`docs/api-docs/api-docs.yml@2.2.364`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Optional in `app.py`: `entities`, `correlation_id`, `score_threshold`, `return_decision_process`, `ad_hoc_recognizers`, `context`, `allow_list`, `allow_list_match`, `regex_flags` (`presidio-analyzer/app.py@2.2.364:85-105`; `analyzer_request.py@2.2.364:25-42`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs versus code: the API spec omits `allow_list`, `allow_list_match` and `regex_flags`, which `app.py` accepts; the code is the better guide **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `entities`: "If entities=None then all entities are looked for." (`analyzer_engine.py@2.2.364`, `analyze` docstring); `GET /supportedentities` lists what the running engine can return **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `allow_list_match` is `"exact"` by default (`analyzer_request.py@2.2.364:39`) and can be set to regex **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Allow-list example: passing `allow_list = ["bing.com"]` stops `bing.com` being reported while `microsoft.com` still is (Presidio docs, allow-list tutorial) **[Documented]**
• Batch and workers: `DEFAULT_BATCH_SIZE = "500"` (`presidio-analyzer/app.py@2.2.364:20`) and `N_PROCESS` defaults to 1 (line 21) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Config files are chosen by environment variables `ANALYZER_CONF_FILE`, `NLP_CONF_FILE` and `RECOGNIZER_REGISTRY_CONF_FILE` (`presidio-analyzer/app.py@2.2.364:46`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Models: "When packaging the code into a Docker container, NLP models are automatically installed." and the models listed in `conf/default.yaml` are installed at build (Presidio docs, languages page) **[Documented]**
• Install: `pip install presidio_analyzer` then `python -m spacy download en_core_web_lg` (Presidio docs, installation page) **[Documented]**
• Azure AI Language credentials: the recognizer reads `AZURE_AI_ENDPOINT` when no endpoint is passed (`azure_ai_language.py@2.2.364:89`); only needed if that recognizer is enabled **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Azure OpenAI recognizer credentials: "Or use environment variables (AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY)" (`presidio-analyzer/README.md@2.2.364`); only needed if that recognizer is enabled **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Azure Health Data Services credentials: the AHDS integration page lists the environment variable "AHDS_ENDPOINT: Your AHDS de-identification service endpoint" (Presidio docs, AHDS page) **[Documented]**
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
• A first call against the Python runtime (the Docker mapping in the docs is `5002:3000`): `curl -d '{"text":"John Smith drivers license is AC432223", "language":"en"}' -H "Content-Type: application/json" -X POST http://localhost:3000/analyze` (Presidio docs, analyzer page) **[Documented]**
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
• https://presidio.dataprivacystack.org/tutorial/13_allow_list/
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
### R1
Summary: **Rewrites detected PII with a chosen operator.** The Anonymizer takes text plus the Analyzer's spans and replaces, redacts, hashes, masks or keeps each entity. It also returns a list of the changes with positions in the new text. **[Documented]**
Detail:
• The docs describe it as: "The Presidio anonymizer is a Python based module for anonymizing detected PII text entities with desired values." (Presidio docs, anonymizer page, read 2026-10-09) **[Documented]**
• "Anonymizers are used to replace a PII entity text with some other value by applying a certain operator (e.g. replace, mask, redact, encrypt)" (Presidio docs, anonymizer page) **[Documented]**
• Input comes from the Analyzer: "It uses the results from the AnalyzerEngine to perform the anonymization." (anonymizer page) **[Documented]**
• Python entry point `AnonymizerEngine.anonymize(text, analyzer_results, operators, conflict_resolution, merge_entities_with_spaces)` (`anonymizer_engine.py@2.2.364:29`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• REST entry point `POST /anonymize` (`presidio-anonymizer/app.py@2.2.364:48`) with `GET /anonymizers` (line 89) listing the operators **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Batch use: "The BatchAnonymizerEngine is a class in Presidio that is responsible for anonymizing PII entities in a batch of texts." (anonymizer page) **[Documented]**
• Built-in anonymize operators: `replace`, `redact`, `hash`, `mask`, `custom`, `keep`, `surrogate_ahds` and `encrypt`; `encrypt` is reversible and is covered by the reversible-anonymisation column (Presidio docs, operator table) **[Documented]**
• Presidio returns rewritten text, not a verdict: the output carries no score or pass-fail value, so the Anonymizer is a transformation step rather than a guardrail check **[Inferred]**
### R2
Summary: **Hides whatever spans it is given.** One-way operators replace, redact, hash, mask, run custom code, keep a value or, with an Azure extra, generate a realistic surrogate. The default is replace, writing the entity type in angle brackets. **[Documented]**
Detail:
• Default operator: `DEFAULT = "replace"` (`anonymizer_engine.py@2.2.364:16`); `__check_or_add_default_operator` adds it when the operator map is empty or lacks a `DEFAULT` entry (line 106 calls it) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs note: "The replacing value will be the entity type e.g.: <PHONE_NUMBER>" (Presidio docs, anonymizer page) **[Documented]**
• Code: `Replace` has `return f"<{params.get('entity_type')}>"` when `new_value` is empty (`replace.py@2.2.364:18`); the NeMo Guardrails PII columns list this default string as unverified in the Presidio docs **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `redact`: "Remove the PII completely from text" (Presidio docs, operator table) **[Documented]**
• Code: `Redact.operate` has `return ""` (`redact.py@2.2.364:13`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `mask`: "Replace the PII with a given character" with `chars_to_mask`, `masking_char` and `from_end` (Presidio docs, operator table) **[Documented]**
• Code: `masking_char` must be one character, "Invalid input, {self.MASKING_CHAR} must be a character" (`mask.py@2.2.364:50`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `hash`: "Hashes the PII text using salted hashing for security"; `hash_type` is `sha256` by default or `sha512` (Presidio docs, operator table) **[Documented]**
• Hash salt: "If not provided, a random salt is generated per entity to prevent brute-force attacks." and "Starting from version 2.2.361, the hash operator uses random salt by default for security." (anonymizer page) **[Documented]**
• Code: no salt means `salt = os.urandom(32)` (`hash.py@2.2.364:54`), so the same value gets a different hash each time; a supplied salt shorter than 16 bytes is rejected (line 47) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Referential integrity needs a caller-held salt: "Presidio does not store or maintain stateful sessions. For referential integrity across records or calls, users must securely manage and provide their own salt." (anonymizer page) **[Documented]**
• `custom`: "Replace the PII with the result of the function executed on the PII" and "The lambda return type must be a string." (Presidio docs, operator table) **[Documented]**
• Code: `raise InvalidParamError("Function return type must be a str")` (`custom.py@2.2.364:23`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `keep`: "Preserver the PII unmodified" (operator table, spelling as printed); the entity stays in the text but is still listed in the result items **[Documented]**
• `surrogate_ahds`: "Generate realistic, medically-appropriate surrogates using Azure Health Data Services de-identification service surrogation"; "Requires: pip install presidio-anonymizer[ahds]" (operator table) **[Documented]**
• Overlaps: "Full overlap of PII entity spans: When entities have overlapping substrings, the PII with the higher score will be taken." (anonymizer page) **[Documented]**
• Overlaps: "One PII is contained in another: Presidio Anonymizer will use the PII with the larger text even if it's score is lower." (anonymizer page) **[Documented]**
• Overlaps: "Partial intersection: Presidio Anonymizer will anonymize each individually and will return a concatenation of the anonymized text." (anonymizer page) **[Documented]**
• Defaults in code: `ConflictResolutionStrategy.MERGE_SIMILAR_OR_CONTAINED` (`anonymizer_engine.py@2.2.364:35`) and `merge_entities_with_spaces: bool = True,` (line 37), whose helper "Merge adjacent entities of the same type separated by whitespace." (line 223) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The enum has two members, `MERGE_SIMILAR_OR_CONTAINED` and `REMOVE_INTERSECTIONS = "remove_intersections"` (`conflict_resolution_strategy.py@2.2.364:19`), but its docstring also describes "NONE: No conflict resolution will be performed." (line 15), which has no member **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs versus code on names: the docs example calls the AHDS operator `"surrogate"` (Presidio docs, AHDS page) **[Documented]**
• Docs versus code on names: the code registers it as `return "surrogate_ahds"` (`ahds_surrogate.py@2.2.364:366`) and the operator table also says `surrogate_ahds`; the code is the better guide **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Over REST, custom lambdas are refused: `raise BadRequest("Custom type anonymizer is not supported")` (`presidio-anonymizer/app.py@2.2.364:58`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The Anonymizer does not detect PII: an entity the Analyzer misses stays in the text unchanged, so leakage depends on the Analyzer's recall (premise: the engine only operates on the spans passed in) **[Inferred]**
• Out of purpose: it does not judge harmful content, injection attempts or topics, and it sees no model or policy context **[Inferred]**
### R3
Summary: **Text plus the Analyzer's spans, from any source.** The call needs the original string, entity spans with scores, and an operator per entity type. It has no direction flag and no prompt context, so it works on prompts, responses and other strings. **[Inferred]**
Detail:
• Signature: `anonymize(text, analyzer_results, operators=None, conflict_resolution=..., merge_entities_with_spaces=True)`; no argument names a role, direction or language (`anonymizer_engine.py@2.2.364:29-37`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Spans must fit the text: `start` and `end` must be non-negative integers and start must not exceed end, otherwise `InvalidParamError` (`pii_entity.py@2.2.364`, lines 50-56) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Result positions refer to the new text, not the original; the docs example lists items with their new `start` and `end` (keep-entities sample) **[Documented]**
• Entity types are plain strings: the REST example uses `NAME`, `FIRST_NAME` and `LAST_NAME`, which the default Analyzer does not emit (Presidio docs, anonymizer page) **[Documented]**
• No direction flag, prompt role or conversation input exists, so one column covers prompts and responses and no system or user prompt is needed **[Inferred]**
• Presidio's OpenAI sample uses it on chat input: the toolkit "anonymizes Personally Identifiable Information (PII) in the messages sent to the LLM" (Presidio docs, Data Protection toolkit for OpenAI page) **[Documented]**
• LiteLLM: "This will mask the input going to the llm provider" (Presidio docs, not LiteLLM docs) **[Documented]**
• LiteLLM can mask only the logged copy: "Only apply PII Masking before logging to Langfuse, etc." and "Not on the actual llm api request / response." (same page) **[Documented]**
• Applying the Anonymizer to model replies, retrieved passages or tool results is the same call on a different string; no Presidio page shows it on replies **[Inferred]**
• Images and tables have their own modules (image redaction column and structured-data column); this column is for text strings **[Documented]**
### R4
Summary: **Operators applied to detected spans.** The engine resolves overlaps, then applies the operator set for each entity type, falling back to replace. Python package or REST service on GHCR images. MIT licence, now under the Data Privacy Stack community. **[Documented]**
Detail:
• Operator list: `ANONYMIZERS = [Custom, Encrypt, Hash, Keep, Mask, Redact, Replace]` (`operators_factory.py@2.2.364:24`) plus the AHDS surrogate when its extra is installed (line 26) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Flow in `anonymize`: copy results, sort by `(start, end)` (`anonymizer_engine.py@2.2.364:93`), remove conflicts, merge spaced same-type entities, add the default operator (line 106), then operate **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Operators run over entities in reverse order, `sorted_pii_entities = sorted(pii_entities, reverse=True)` (`core/engine_base.py@2.2.364:45`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Extensible: "Presidio anonymizer can be easily extended to support additional operators." (Presidio docs, anonymizer page) **[Documented]**
• Code: `def add_anonymizer(self, anonymizer_cls: Type[Operator]) -> None:` (`anonymizer_engine.py@2.2.364:115`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Dependencies: only `"cryptography (>=48.0.1,<49.0.0)"` (`presidio-anonymizer/pyproject.toml@2.2.364:26`) with extras `server` and `ahds`; the Anonymizer alone needs no spaCy model **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Serving: Flask app, `DEFAULT_PORT = "3000"` (`presidio-anonymizer/app.py@2.2.364:14`), gunicorn via `entrypoint.sh`, `ENV WORKERS=1` and `USER 1001` (`presidio-anonymizer/Dockerfile@2.2.364:8,26`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Images: `docker pull ghcr.io/data-privacy-stack/presidio-anonymizer` and `docker run -d -p 5001:3000 ghcr.io/data-privacy-stack/presidio-anonymizer:latest` (Presidio docs, installation page) **[Documented]**
• Source conflict C4: the anonymizer page shows `docker run -p 5001:3000 presidio-anonymizer`, a locally built name, while the installation page uses the GHCR name; "The legacy Microsoft Container Registry images at mcr.microsoft.com/presidio-* are no longer updated." **[Documented]**
• REST surface: `POST /anonymize`, `POST /deanonymize`, `GET /anonymizers`, `GET /deanonymizers`, `GET /health` (`presidio-anonymizer/app.py@2.2.364`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• REST cannot set the conflict strategy or the space-merge flag: the `anonymize` call passes only `text`, `analyzer_results` and `operators` (`presidio-anonymizer/app.py@2.2.364:63`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The API spec lists five operator schemas for `/anonymize` (Replace, Redact, Mask, Hash, Encrypt) while the code accepts every registered operator except `custom` (`docs/api-docs/api-docs.yml@2.2.364`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Batch: `BatchAnonymizerEngine.anonymize_list` (line 19) and `anonymize_dict` (line 48) (`batch_anonymizer_engine.py@2.2.364`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Integrations: LiteLLM proxy callback (`PRESIDIO_ANONYMIZER_API_BASE="http://localhost:5001"`, Presidio docs, not LiteLLM docs) **[Documented]**
• NeMo Guardrails masks with Presidio's default replace in its input and output rails; those are sheet 3 NeMo Guardrails columns E and F (NeMo Guardrails: Input-level PII detection & masking; NeMo Guardrails: Output-level PII detection & masking) and are not repeated here **[Inferred]**
• Version: `presidio_anonymizer` is `version = "2.2.364"` (`presidio-anonymizer/pyproject.toml@2.2.364:7`); tag 2.2.364 is commit 779dbd28 dated 2026-07-22 **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Python: the live installation page lists 3.10 to 3.13 (read 2026-10-09) **[Documented]**
• Python: `docs/installation.md@2.2.364:24` also lists `* 3.14`, and `requires-python = ">=3.10,<3.15"` (`presidio-anonymizer/pyproject.toml@2.2.364:24`); source conflict C3 with the live page **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Licence MIT (`LICENSE@2.2.364`); "Presidio will continue to be open source under the MIT license." (Presidio docs, transition page) **[Documented]**
• Ownership: the project is moving from Microsoft to the community-governed Data Privacy Stack organisation; "Microsoft supports this transition" (Presidio docs, transition page) **[Documented]**
### R5
Summary: **Rewritten text plus a change list.** The result holds the new text and, for each entity, its type, start and end in the new text, the replacement and the operator used. There is no score or pass-fail field. **[Documented]**
Detail:
• Result classes in the docs: `EngineResult` holds `text` and `items`; each item is an `OperatorResult` with `start`, `end`, `entity_type`, `text` and `operator` (Presidio docs, anonymizer page, class diagram) **[Documented]**
• Printed example: `{'start': 33, 'end': 43, 'entity_type': 'LOCATION', 'text': '<LOCATION>', 'operator': 'replace'}` (Presidio docs, keep-entities sample) **[Documented]**
• `keep` leaves the value in the text but tracks it: "The person name is preserved in the result text, but remains tracked in the items list." (keep-entities sample) **[Documented]**
• REST returns the result as JSON: `return Response(anoymizer_result.to_json(), mimetype="application/json")` (`presidio-anonymizer/app.py@2.2.364:68`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Errors: parameter problems return HTTP 422 (`presidio-anonymizer/app.py@2.2.364:104`), bad JSON or a custom operator returns 400, and other failures return `jsonify(error="Internal server error"), 500` (line 113) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Missing spans: the REST path raises "Invalid input, request must contain analyzer results" (`app_entities_convertor.py@2.2.364:23`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Output is deterministic except `hash` without a salt and `encrypt`, which draw random values (`hash.py@2.2.364:54`, `aes_cipher.py@2.2.364:24`) **[Inferred]**
• Accuracy, latency or throughput figures for the Anonymizer (checked the anonymizer page, FAQ and evaluation page, which covers the Analyzer and DICOM redaction only) **[Not disclosed]**
• presidio-research has no Anonymizer evaluator: only `presidio_pseudonymize.py` in the data generator imports `AnonymizerEngine` (searched the repository; README and docs/evaluation.md describe Analyzer evaluation) **[Not disclosed]**
### R6
Summary: **Text, spans and an operator map.** Required are the text and the Analyzer's spans with type, start, end and score; operators are optional, with a DEFAULT entry. Each operator has its own parameters, and hash salts are the caller's to manage. **[Documented]**
Detail:
• Operator parameters (Presidio docs, operator table): `replace` takes `new_value`; `redact` and `keep` take none; `hash` takes `hash_type` and `salt`; `mask` takes `chars_to_mask`, `masking_char`, `from_end`; `custom` takes `lambda`; `surrogate_ahds` takes `endpoint`, `entities`, `input_locale`, `surrogate_locale` **[Documented]**
• REST payload: `text`, `anonymizers` (entity type or DEFAULT mapped to `{"type": ..., params}`) and `analyzer_results` with `start`, `end`, `score`, `entity_type` (Presidio docs, anonymizer page example) **[Documented]**
• `anonymizers` is optional: "Object where the key is DEFAULT or the ENTITY_TYPE and the value is the anonymizer definition" (`docs/api-docs/api-docs.yml@2.2.364:449`); `analyzer_results` is required **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Validation: `mask` needs a one-character `masking_char`, an integer `chars_to_mask` and a boolean `from_end` (`mask.py@2.2.364:47`); `replace` needs a string `new_value` (`replace.py`); `hash` needs `sha256` or `sha512` (`hash.py`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Hash salt: at least 16 bytes, empty rejected: "Salt must be at least 16 bytes (128 bits)." (`hash.py@2.2.364:49`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs advice: "Never include the salt in anonymized output" (Presidio docs, anonymizer page) **[Documented]**
• Salt handling advice: "Discard the salt after processing" and, if it must be kept, use "secure storage (e.g., key vault or secrets manager)" (Presidio docs, anonymizer page) **[Documented]**
• AHDS surrogate needs `pip install presidio-anonymizer[ahds]`, an AHDS endpoint (`AHDS_ENDPOINT`) and Azure role-based access (Presidio docs, AHDS page) **[Documented]**
• Install: `pip install presidio_anonymizer` (Presidio docs, installation page) **[Documented]**
• Maximum text length or request size (checked `app.py`, the anonymizer page and FAQ; none stated or enforced) **[Not disclosed]**
• Authentication: "Presidio API endpoints do not include built-in authentication by design." (Presidio docs, FAQ) **[Documented]**
### R7
Summary: **Minimum setup:** pip install the Analyzer, the Anonymizer and a spaCy model, or run both GHCR images; no account or key. Feed labelled texts with known PII through the Analyzer, anonymize with each operator, and check that no original value survives and that placeholders and offsets are right. **[Inferred]**
Detail:
• **Minimum setup:** `pip install presidio_analyzer presidio_anonymizer`, `python -m spacy download en_core_web_lg`, run the Analyzer on a labelled text, pass its results to `AnonymizerEngine().anonymize(text, results, operators)`, and inspect `result.text` and `result.items` **[Inferred]**
• Install and run commands as documented, including `docker run -d -p 5001:3000 ghcr.io/data-privacy-stack/presidio-anonymizer:latest` (Presidio docs, installation page) **[Documented]**
• Leak check: assert that every labelled PII value is absent from the output text; the `items` list holds replacements (except for `keep`), not originals **[Inferred]**
• Per-operator cases: `replace` default `<ENTITY_TYPE>`, `redact` empty, `mask` with and without `from_end`, `hash` with and without a 16-byte salt (random versus repeatable), `custom` lambda, `keep` tracked in items **[Inferred]**
• Overlap cases from the docs (full overlap, containment, partial intersection) with their documented outcomes as expected values **[Inferred]**
• Measure end-to-end leakage, not the Anonymizer alone: Analyzer false negatives pass through untouched (R2) **[Inferred]**
• Run on prompt strings and on reply strings, since the call has no direction **[Inferred]**
• REST check: `curl -XPOST http://localhost:3000/anonymize -H "Content-Type: application/json" -d @payload` (Presidio docs, anonymizer page) **[Documented]**
• presidio-research does not score the Anonymizer (R5), so build the leak check yourself; its data generator can supply texts with known spans **[Inferred]**
• Leave the AHDS surrogate out of a minimum setup because it needs an Azure account **[Inferred]**
### R8
Summary: **Key open questions.** No accuracy or latency figures, unclear whether a NONE conflict strategy exists, REST gaps for some operators, and an unspecified data flow for the Azure surrogate operator.
Detail:
• Latency and throughput of the Anonymizer service (checked the anonymizer page, FAQ and evaluation page; not stated; needs testing)
• Whether a no-conflict-resolution mode exists (the enum docstring names NONE, the enum has no such member; needs testing)
• Whether `keep` and `surrogate_ahds` work over REST (the API spec lists five operator schemas; needs testing)
• Effect of the default `merge_entities_with_spaces=True` on spans such as two names separated by a space (needs testing against expected output)
• Offset behaviour on non-BMP characters and mixed scripts (not discussed in the docs; needs testing)
• What the AHDS surrogate operator sends to Azure and retention there (checked the AHDS integration page; the endpoint is configurable but data flow is not described)
• Which operator is best per entity type for LLM prompts (the docs give examples only; needs testing against model answer quality)
• Whether the hash output length or format leaks anything useful to a model (needs testing)
• Release notes for 2.2.364 could not be read (github.com returned 403)
• Owner question Q01: official status of the Data Privacy Stack organisation (user ruling)
### R9
Summary: Presidio docs site pages and the Presidio repository at tag 2.2.364.
Detail:
• https://presidio.dataprivacystack.org/anonymizer/
• https://presidio.dataprivacystack.org/installation/
• https://presidio.dataprivacystack.org/faq/
• https://presidio.dataprivacystack.org/project_transition/
• https://presidio.dataprivacystack.org/ahds_integration/
• https://presidio.dataprivacystack.org/samples/python/keep_entities/
• https://presidio.dataprivacystack.org/samples/docker/litellm/
• https://presidio.dataprivacystack.org/samples/deployments/openai-anonymaztion-and-deanonymaztion-best-practices/
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/app.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/pyproject.toml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/Dockerfile
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/anonymizer_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/batch_anonymizer_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/core/engine_base.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/entities/conflict_resolution_strategy.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/entities/engine/pii_entity.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/services/app_entities_convertor.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/operators_factory.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/replace.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/redact.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/mask.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/hash.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/custom.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/aes_cipher.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/ahds_surrogate.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/api-docs/api-docs.yml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/installation.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/LICENSE
• https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/README.md
• https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/presidio_evaluator/data_generator/presidio_pseudonymize.py
• https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/docs/evaluation.md
## Column PD3: Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt)
### R1
Summary: **Encrypts PII in text so it can be restored later.** The encrypt operator swaps each entity for AES ciphertext, and the Deanonymize engine or the decrypt operator reverses it with the same key. Presidio stores nothing between calls. **[Documented]**
Detail:
• "Deanonymizers are used to revert the anonymization operation." (Presidio docs, anonymizer page, read 2026-10-09) **[Documented]**
• "The DeanonymizerEngine is a class in Presidio that is responsible for deanonymizing text that has been anonymized by the AnonymizerEngine, given that the operation is reversible (e.g. encryption)." (anonymizer page) **[Documented]**
• Tutorial: "The encryption is using AES cypher in CBC mode and requires a cryptographic key as an input for both the encryption and the decryption." (Presidio docs, encrypt and decrypt sample) **[Documented]**
• Code: `ANONYMIZERS = [Custom, Encrypt, Hash, Keep, Mask, Redact, Replace]` (`operators_factory.py@2.2.364:24`) and `DEANONYMIZERS = [Decrypt, DeanonymizeKeep]` (line 28) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Entry points: `DeanonymizeEngine.deanonymize` (`deanonymize_engine.py@2.2.364:16`), `BatchDeanonymizeEngine` (exported at `presidio_anonymizer/__init__.py@2.2.364:29`), REST `POST /deanonymize` (`presidio-anonymizer/app.py@2.2.364:70`) and `GET /deanonymizers` (line 94) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• FAQ: "Pseudonymization is a de-identification technique in which the real data is replaced with fake data in a reversible way." and "we provide a simple sample which can be extended for more sophisticated usage." (Presidio docs, FAQ) **[Documented]**
• Presidio returns restored text, not a verdict, so this column is a data-handling step rather than a guardrail check **[Inferred]**
### R2
Summary: **Lets the model see tokens, then restores the real values.** Presidio documents three routes: AES encryption, a client-held mapping in a pseudonymization sample, and LiteLLM's restore of masked tokens in replies. All start from what the Analyzer detected. **[Documented]**
Detail:
• LiteLLM page: "LLM responses can sometimes contain the masked tokens." and "For presidio 'replace' operations, LiteLLM can check the LLM response and replace the masked token with the user-submitted values." (Presidio docs, not LiteLLM docs) **[Documented]**
• The same page switches this on with `output_parse_pii: true` under `litellm_settings`; the restoring is done by LiteLLM, not by the Presidio engines (Presidio docs, not LiteLLM docs) **[Documented]**
• OpenAI sample question: "how can we ensure that the responses processed by OpenAI, which are also anonymized, remain meaningful to the user?" (Presidio docs, Data Protection toolkit for OpenAI page) **[Documented]**
• Its core concept: "The core concept of the toolkit revolves around sessions, which encapsulate the anonymization context." and the toolkit "ensures that the LLM never has access to actual PII, while still facilitating meaningful conversations." **[Documented]**
• That guarantee holds only for PII the Analyzer detects; the Home page says "there is no guarantee that Presidio will find all sensitive information." **[Inferred]**
• Pseudonymization sample: "Since the user/client is holding the entity_mapping, it is possible to use it for de-anonymization as well." (Presidio docs, pseudonymization sample) **[Documented]**
• Same sample warns: "The following logic is not thread-safe and may produce incorrect results if run concurrently in a multi-threaded environment, since the mapping has to be shared between threads/workers/processes." **[Documented]**
• Encrypt gives each occurrence its own token: the IV is random per call (`iv = os.urandom(16)`, `aes_cipher.py@2.2.364:24`), so the same name encrypts differently each time and a model cannot tell that two tokens are the same person **[Inferred]**
• For repeatable but irreversible tokens the hash operator with a caller-held salt is the documented route (anonymisation column); a mapping dictionary gives both repeatable and reversible tokens at the cost of storing the mapping **[Inferred]**
• Ciphertext length tracks plaintext length in 16-byte blocks, so token length still hints at the original value's length (premise: AES-CBC with PKCS7 padding, `aes_cipher.py@2.2.364:22`) **[Inferred]**
### R3
Summary: **Tokens plus their positions, wherever they reappear.** Deanonymize needs the text that holds the encrypted tokens, each token's start, end and entity type, and the key. It applies to model replies or any string that still carries the tokens. No prompt context is used. **[Inferred]**
Detail:
• Tutorial: "The output contains both the anonymized text, as well as the location of the encrypted entities. This is useful as we would need to decrypt only the entities and not the full text:" (Presidio docs, encrypt and decrypt sample) **[Documented]**
• Signature: `deanonymize(text, entities: List[OperatorResult], operators)` (`deanonymize_engine.py@2.2.364:16`); the anonymizer page example passes `OperatorResult(start=11, end=55, entity_type="PERSON")` **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The engine cuts each token by its given offsets: `text_to_operate_on = text_replace_builder.get_text_in_position(` (`core/engine_base.py@2.2.364:48`), so offsets must match the text being restored; a model reply that moves or edits tokens needs the offsets recomputed **[Inferred]**
• A single token can be decrypted without offsets: "Alternatively, call the Decrypt operator directly" with `Decrypt().operate(text=encrypted_entity_value, params={"key": crypto_key})` (Presidio docs, encrypt and decrypt tutorial) **[Documented]**
• The OpenAI sample rebuilds the offsets by searching the reply for each known token: `start_index = text.find(entity_id, start_index)` (`docs/samples/deployments/openai-anonymaztion-and-deanonymaztion-best-practices/index.md@2.2.364:157`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Encrypt runs before the model and decrypt after it; there is no direction flag or system-prompt input **[Inferred]**
• The same restore step works on any returned string that still carries the tokens, such as retrieved passages or tool output **[Inferred]**
### R4
Summary: **AES-CBC with a random IV per entity.** Encrypt returns URL-safe base64 of the IV plus ciphertext; decrypt reverses it with the same 128, 192 or 256-bit key. Python, batch and REST entry points exist. MIT licence, now under the Data Privacy Stack community. **[Documented]**
Detail:
• Cipher docstring: "Advanced Encryption Standard (aka Rijndael) en/decryption in CBC mode." (`aes_cipher.py@2.2.364:9`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Padding and IV: `padder = padding.PKCS7(algorithms.AES.block_size).padder()` (line 22) and `iv = os.urandom(16)` (line 24); the output is `base64.urlsafe_b64encode(` of the IV plus ciphertext (line 27) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Decrypt: `decoded_text = base64.urlsafe_b64decode(text)` (line 41) and `iv = decoded_text[:16]` (line 42) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Keys: "Invalid input, {self.KEY} must be of length 128, 192 or 256 bits" (`encrypt.py@2.2.364:43`); a string key is encoded with `key = key.encode("utf8")` (line 25) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The cipher code uses plain CBC with no authentication tag or MAC, so altered ciphertext is not detected by the cipher itself (premise: `aes_cipher.py` has no integrity step) **[Inferred]**
• `deanonymize_keep` is a second Deanonymize operator: "No-op deanonymizer that keeps the PII text unmodified." (`deanonymize_keep.py@2.2.364:6`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs versus code: the docs operator table lists `decrypt` as the only Deanonymize operator (Presidio docs, anonymizer page) **[Documented]**
• Docs versus code: the API spec says the deanonymizer value "is decrypt since it is the only one supported" (`docs/api-docs/api-docs.yml@2.2.364:479`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Batch: `deanonymize_list` (`batch_deanonymize_engine.py@2.2.364:23`) and `deanonymize_dict` (line 54); items whose type is not str, bool, int or float are left unchanged (line 33) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `CHANGELOG.md@2.2.364:38` lists `BatchDeanonymizeEngine` under its unreleased heading although the class is in the tagged code **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• No docs page describes the batch deanonymiser (searched `docs/` at the tag and the anonymizer page for its name) **[Not disclosed]**
• Release-note wording for 2.2.364 could not be read because github.com returned HTTP 403 through the proxy on 2026-10-09 **[To be verified]**
• Custom reversible route: the pseudonymization sample defines operators with an `entity_mapping` dictionary held by the client, registered with `add_anonymizer`, which output tokens like `<PERSON_1>` (Presidio docs, pseudonymization sample) **[Documented]**
• The OpenAI sample lists its components as "Api (Deployed in AKS)", "Client" and "Redis" and keeps sessions in persistent storage (Presidio docs, Data Protection toolkit for OpenAI page) **[Documented]**
• REST: the docs example sends the key in the JSON body, `"key": "WmZq4t7w!z%C&F)J"` to `POST /deanonymize` (Presidio docs, anonymizer page) **[Documented]**
• Dependency: `"cryptography (>=48.0.1,<49.0.0)"` (`presidio-anonymizer/pyproject.toml@2.2.364:26`); the changelog records "Bumped `cryptography` lower bound to `>=48.0.1` to resolve GHSA-537c-gmf6-5ccf" (`CHANGELOG.md@2.2.364:34`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Version: `presidio_anonymizer` is `version = "2.2.364"` (`presidio-anonymizer/pyproject.toml@2.2.364:7`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Python: the live installation page lists 3.10 to 3.13 (read 2026-10-09) **[Documented]**
• Python: `docs/installation.md@2.2.364:24` also lists `* 3.14` (source conflict C3 with the live page) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Licence MIT, "Presidio will continue to be open source under the MIT license." (Presidio docs, transition page) **[Documented]**
• Ownership: transition from Microsoft to the community-governed Data Privacy Stack organisation (Presidio docs, transition page) **[Documented]**
• NeMo Guardrails columns E and F wrap Presidio detection and masking; they do not describe restoring values, so this column covers the reverse step (checked their text for restore, deanonymise, decrypt) **[Inferred]**
### R5
Summary: **Restored text and an item list, no verdict.** The result holds the text with tokens swapped back to the originals plus one item per restored entity, and the REST route returns the same as JSON. **[Documented]**
Detail:
• Return type: ":return: EngineResult - the new text and data about the deanonymized entities." (`deanonymize_engine.py@2.2.364:28`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• REST: `deanonymized_response.to_json()` is returned as `application/json` (`presidio-anonymizer/app.py@2.2.364:86`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Direct use of `Decrypt().operate(...)` returns the original entity string (Presidio docs, encrypt and decrypt tutorial) **[Documented]**
• A key of the wrong length raises `InvalidParamError` (`encrypt.py@2.2.364:43`, reused by `decrypt.py@2.2.364:37`), returned as HTTP 422 (`presidio-anonymizer/app.py@2.2.364:104`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• A wrong key or damaged token probably fails inside `unpadder.finalize()` or the UTF-8 decode (`aes_cipher.py@2.2.364:46`) and, over REST, becomes `jsonify(error="Internal server error"), 500` (`presidio-anonymizer/app.py@2.2.364:113`); this is a reading of the code paths, not tested **[Inferred]**
• Encrypting the same value twice gives different tokens (random IV), so outputs are not repeatable **[Inferred]**
• Token size: AES-CBC pads to 16-byte blocks and prefixes a 16-byte IV, so a value of 1 to 15 bytes becomes 32 bytes, which is 44 base64 characters; the docs samples agree, with the 10-character name "James Bond" (start 11, end 21 in the encrypt tutorial) shown as a token from start 11 to end 55 (anonymizer page) **[Inferred]**
• Accuracy, latency or throughput figures for encrypt and decrypt (checked the anonymizer page, encrypt and decrypt tutorial and sample, FAQ and evaluation page) **[Not disclosed]**
### R6
Summary: **Key, token text and token offsets.** Required are the same AES key used to encrypt, the text holding the tokens, and each token's start, end and entity type. The REST route takes these as JSON. The caller supplies and holds the key. **[Documented]**
Detail:
• Python call, condensed from the tutorial: `engine.deanonymize(text=anonymized_text, entities=anonymized_entities, operators={"DEFAULT": OperatorConfig("decrypt", {"key": crypto_key})})` (Presidio docs, encrypt and decrypt tutorial) **[Documented]**
• The entities come from the earlier anonymize result: "Fetch the anonynized entities from the result." (tutorial, spelling as printed) **[Documented]**
• REST payload: `text`, `deanonymizers` (`{"PERSON": {"type": "decrypt", "key": ...}}`) and `anonymizer_results` with `start`, `end`, `entity_type` (Presidio docs, anonymizer page) **[Documented]**
• The API spec marks `text`, `anonymizer_results` and `deanonymizers` as required (`docs/api-docs/api-docs.yml@2.2.364:467-472`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Key rules: the decrypt operator validates with `Encrypt().validate(params)` (`decrypt.py@2.2.364:37`), so a str or bytes key of 128, 192 or 256 bits is needed, the same key as for encryption **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• A str key is UTF-8 encoded, so 16, 24 or 32 ASCII characters give 128, 192 or 256 bits **[Inferred]**
• Batch input: `deanonymize_list(texts, entities_list, operators)` and `deanonymize_dict(anonymizer_results, operators)` (`batch_deanonymize_engine.py@2.2.364:23,54`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Mapping route input: a client-held `entity_mapping` dictionary shared across calls (Presidio docs, pseudonymization sample) **[Documented]**
• Key generation, storage, rotation and access control (checked the anonymizer page, encrypt and decrypt tutorial and sample, and FAQ; the only secret-handling advice is for hash salt) **[Not disclosed]**
• The key travels in the HTTP request body in the docs example, and the FAQ says "Presidio API endpoints do not include built-in authentication by design." **[Documented]**
• TLS for the REST service (checked the FAQ, installation and anonymizer pages; not mentioned) **[Not disclosed]**
• Install: `pip install presidio_anonymizer` (Presidio docs, installation page) **[Documented]**
### R7
Summary: **Minimum setup:** pip install the Anonymizer, make a 16, 24 or 32 character key, encrypt labelled entities, decrypt, and compare with the originals. Then replay a mock model reply that echoes, edits or drops tokens, and try a wrong key and a damaged token, to see what restores and what fails. **[Inferred]**
Detail:
• **Minimum setup:** `pip install presidio_analyzer presidio_anonymizer`, `python -m spacy download en_core_web_lg`, analyse a labelled text, call `AnonymizerEngine().anonymize` with `OperatorConfig("encrypt", {"key": key})`, then `DeanonymizeEngine().deanonymize` with the returned `items` and a `decrypt` operator **[Inferred]**
• Documented commands and the full encrypt and decrypt example are in the encrypt and decrypt tutorial and the installation page (Presidio docs) **[Documented]**
• Round trip: decrypted text must equal the original across entity types, lengths and non-ASCII names **[Inferred]**
• Mock model replies: echo the token, change its case, split it, drop it, or move it; restore with offsets found by search (as in the OpenAI sample) or per token with `Decrypt().operate` **[Inferred]**
• Error cases: wrong key, key of the wrong length, truncated or edited ciphertext; record the exception types and, over REST, the HTTP codes **[Inferred]**
• Repeated entities: confirm that the same name gets different tokens and check whether the model's answers still make sense **[Inferred]**
• Cost: compare token length with the original and count model tokens for the encrypted text **[Inferred]**
• Compare with the mapping route from the pseudonymization sample, noting its thread-safety warning **[Inferred]**
• presidio-research has no reversibility test (checked its README and `docs/evaluation.md`, which cover Analyzer evaluation), so these checks are hand-built **[Not disclosed]**
• A LiteLLM proxy run is an optional extension, not part of a minimum setup, because it needs a separate product **[Inferred]**
### R8
Summary: **Key open questions.** What happens on a wrong key or a damaged token, how a real model treats the long tokens, no key-management guidance, and whether the batch deanonymiser and its REST coverage are release-ready.
Detail:
• Behaviour with a wrong key, a damaged token or non-UTF-8 plaintext (the code paths suggest an exception, the REST service a generic 500; needs testing)
• Whether an LLM keeps 44-character base64 tokens intact, and what they cost in tokens (needs testing with a model)
• Key generation, rotation and storage guidance (checked the anonymizer page, tutorials, samples and FAQ; only hash salt advice exists)
• Whether authenticated encryption or a deterministic mode is planned (checked the changelog at the tag and the docs; nothing stated)
• Whether `deanonymize_keep` works over REST (the API spec says `decrypt` is the only supported deanonymizer; needs testing)
• Whether the batch deanonymiser is part of the 2.2.364 release notes (code is in the tag, the changelog lists it as unreleased, release notes could not be read)
• Whether the NeMo Guardrails PII flows (sheet 3 NeMo columns E and F) can restore masked values in the reply (not described in those columns)
• What LiteLLM does beyond the Presidio page (the LiteLLM behaviour is not Presidio evidence)
• Owner question Q01: official status of the Data Privacy Stack organisation (user ruling)
### R9
Summary: Presidio docs site pages and the Presidio repository at tag 2.2.364.
Detail:
• https://presidio.dataprivacystack.org/anonymizer/
• https://presidio.dataprivacystack.org/tutorial/12_encryption/
• https://presidio.dataprivacystack.org/samples/python/encrypt_decrypt/
• https://presidio.dataprivacystack.org/samples/python/pseudonymization/
• https://presidio.dataprivacystack.org/samples/docker/litellm/
• https://presidio.dataprivacystack.org/samples/deployments/openai-anonymaztion-and-deanonymaztion-best-practices/
• https://presidio.dataprivacystack.org/faq/
• https://presidio.dataprivacystack.org/installation/
• https://presidio.dataprivacystack.org/project_transition/
• https://presidio.dataprivacystack.org/
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/app.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/pyproject.toml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/__init__.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/deanonymize_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/batch_deanonymize_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/core/engine_base.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/operators_factory.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/aes_cipher.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/encrypt.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/decrypt.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/deanonymize_keep.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/api-docs/api-docs.yml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/installation.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/samples/deployments/openai-anonymaztion-and-deanonymaztion-best-practices/index.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/CHANGELOG.md
• https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/README.md
• https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/docs/evaluation.md

## Reviewer notes
• Method: docs pages were read as raw text with `python benchtest/tools/fetch_text.py` (final URL on presidio.dataprivacystack.org, HTTP 200, read 2026-10-09) and stripped of navigation locally; no summarising fetch supplied any quote or number. Every double-quoted string and every inline code snippet of 10 or more characters in the three columns was matched mechanically against the fetched pages and the local checkouts; the only unmatched items are route names, signature summaries and two condensed code lines (PD1 R7 first bullet; PD3 R6 first bullet, marked "condensed").
• Code was read from the shallow clone at tag 2.2.364 (commit 779dbd286d5ef4d1fbe2514275fb1bce358f2417, committed 2026-07-22, confirmed with `git log -1`). Line numbers are from `grep -n` on that checkout.
• presidio-research was readable: `git clone --depth 1` worked, and `git fetch --depth 1 origin tag 0.3.2` also worked. The repo has tags up to 0.3.2 (06d2030688ece62f58047e567aecd70e4bb5f104, 2026-08-04); HEAD (0cb36502, 2026-09-30) is ahead with an Unreleased section. The facts used (wrapper default threshold 0.4, notebook 4 and 5 outputs, `synth_dataset_v2.json`, `presidio_pseudonymize.py`) were checked at tag 0.3.2 and are identical at HEAD for the wrapper, notebook 4, `docs/evaluation.md` and the dataset; notebook 5 and `pyproject.toml` differ between 0.3.2 and HEAD but notebook 5 prints the same F2 0.91 at 0.3.2. The `requires-python` of presidio-research 0.3.2 is `>=3.11,<3.14`; HEAD is `>=3.11,<3.15`.
• Not readable: the GitHub release page for 2.2.364 (github.com and api.github.com returned HTTP 403 through the proxy, and the GitHub MCP is restricted to the working repo). So "2.2.364 is the latest release" and the release-note wording quoted in the brief (batch deanonymization, no-op NLP engine, Python 3.14, CLI threshold flag) are `[To be verified]`. The code for those features is in the tag; `CHANGELOG.md` at the tag still lists them under its unreleased heading, which is a conflict between the changelog heading and the tag contents, not a conflict about behaviour.
• Corrections to the brief (all from the tag): (1) `conf/default.yaml` ignores many spaCy labels, not only `ORGANIZATION` (`labels_to_ignore` lines 24-35). (2) The brief expected no published numbers; the presidio-research notebooks print F2 0.661 / P 0.733 / R 0.646 (default recognizers, threshold 0.4) and F2 0.91 / P 0.921 / R 0.907 (tuned engine) on a 1500-sample synthetic set. (3) The default English setup loads 16 pattern recognizers plus the spaCy recognizer (the YAML has 24 enabled entries, but the Spanish, Italian and Polish ones are dropped by the English-only registry); the executed notebook 4 output agrees (19 entities, 17 recognizers). (4) `default_recognizers.yaml` omits `SgUenRecognizer` (as the brief found) and also `FiPersonalIdentityCodeRecognizer`, `KrPassportRecognizer` and `AbaRoutingRecognizer`; it lists `UkPostcodeRecognizer` twice. (5) The supported-entities page has about 80 entity rows (the brief estimated about 120); I counted 80 on the live page and 81 matching rows in `docs/supported_entities.md` at the tag and did not reconcile the difference. (6) The FAQ does state that the HTTP services have no built-in authentication (the brief's G10); it does not mention TLS. (7) The anonymizer operator table does not list `deanonymize_keep` (as the brief said), and the docs AHDS example calls the operator `surrogate` while the table and code say `surrogate_ahds`.
• Source conflicts logged: C2 (entity page versus YAML on SG_UEN and others, PD1 R2); C3 (Python versions: live page 3.10-3.13, `docs/installation.md` at the tag 3.10-3.14, `pyproject.toml` `>=3.10,<3.15`; PD1 R4, PD2 R4, PD3 R4); C4 (analyzer and anonymizer pages show local image names, the installation page shows GHCR names; PD1 R4, PD2 R4); API spec versus code (omitted `allow_list`, `allow_list_match`, `regex_flags`; five operator schemas; `decrypt` as the only deanonymizer; PD1 R6, PD2 R4, PD3 R4); decision-process page says an `x-correlation-id` response header exists but `app.py` sets none (PD1 R6, `[Inferred]` because it rests on a search of one file); `ConflictResolutionStrategy` docstring names `NONE` but the enum has two members (PD2 R2); the evaluation page says notebook 5 boosts the F score "in ~30%" while the printed outputs give +0.249 absolute (PD1 R5).
• Inferences worth a second look: (a) "16 active pattern recognizers" combines the YAML, the loader's language filter (`recognizers_loader_utils.py` line 177) and the notebook 4 output; the code was read, not run. (b) "No verdict" is stated as `[Documented]` in PD1 R5 because the result class has an exhaustive field list in code, and as `[Inferred]` in R1 and the PD2 R1 / PD3 R1 bullets where it is a classification of the product. (c) The wrong-key and damaged-token behaviour in PD3 R5 is a reading of `aes_cipher.py` and the REST error handler, not a test. (d) Token-size arithmetic (32 bytes, 44 characters) is derived from the cipher code and agrees with the two docs samples. (e) "Text leaves the process" for Azure recognizers follows from the endpoint and key parameters; Presidio pages do not describe data flow.
• Notebook caveats: the notebook outputs carry no Presidio version, hardware or date except the experiment file name `experiment_20260723-102549.json` in notebook 5; the evaluation is span-level at IoU 0.75 on PII-versus-other, and dataset labels such as `STREET_ADDRESS` have no default entity type, so the figures mix coverage gaps with recognizer quality. The third-party model in notebook 5 (`OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1`) was not read and is not Presidio-authored.
• The German recipe (`docs/recipes/german-language-support/README.md`) is in the repo `docs/` tree but not in the `mkdocs.yml` navigation (only recipes index, contributing and template are); I did not check whether the live site serves it, so it is cited as repo content. It is where the 0.4-0.5 threshold tip and the "TBD" accuracy table come from.
• Judgement calls: (1) `encrypt` is listed in the PD2 operator overview but its mechanics, keys and sizes sit in PD3. (2) LiteLLM facts come only from the Presidio LiteLLM page; LiteLLM's own behaviour is not evidence. (3) The OpenAI sample (Data Protection toolkit for OpenAI) is cited as a Presidio-authored deployment sample; it is in the site's samples index but not in the left navigation. (4) PD1 R4 carries the ownership move, licence and version bullets; PD2 and PD3 repeat them briefly so each column stands alone after a merge. (5) The cross-reference to NeMo Guardrails columns E and F is `[Inferred]` because it describes the workbook rather than a Presidio page; I only checked that those columns do not mention restore, deanonymise or decrypt.
• Not covered here by design: image redaction, presidio-structured and custom-recognizer authoring (columns PD4 to PD6), the inventory rows, and `presidio-cli`. PD1 R6 names `ad_hoc_recognizers` only as a request field.
• Everything labelled `[Inferred]` is my reading and each states its premise; every `[Not disclosed]` names the pages or files checked in that bullet.
## Column PD4: Presidio: PII detection and redaction in images (Image Redactor)
### R1
Summary: **Image redaction by OCR.** Presidio reads text in an image with OCR, runs the Analyzer on it, and paints solid boxes over words that match PII. A second engine handles medical DICOM pixels. The package is marked beta. **[Documented]**
Detail:
• The Image Redactor is described as "a Python based module for detecting and redacting PII text entities in images" (Presidio docs, image-redactor page, read 2026-10-09) **[Documented]**
• The same page says: "Please notice, this package is still in beta and not production ready." (Presidio docs, image-redactor page, read 2026-10-09) **[Documented]**
• The docs source at the tag carries the same beta sentence (docs/image-redactor/index.md@2.2.364:3) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Concepts page: "The ImageRedactorEngine is a class in Presidio that is responsible for redacting PII entities in images. It leverages the AnalyzerEngine to detect PII entities in the text extracted from the images." (Presidio docs, concepts page) **[Documented]**
• Home page module list: "Presidio image redactor: Redact PII entities from images using OCR and PII identification" (Presidio docs, home page) **[Documented]**
• Redaction is a filled rectangle drawn over each box: `draw.rectangle([x0, y0, x1, y1], fill=fill)` (image_redactor_engine.py@2.2.364:79) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The fill is a grey level (int) or an RGB tuple, default black (0, 0, 0) (image_redactor_engine.py@2.2.364:31) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The engine works on a copy: "Please notice, this method duplicates the image, creates a new instance and manipulate it." (image_redactor_engine.py@2.2.364:38) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• A separate class redacts medical images: "The DicomImageRedactorEngine class may be used to redact text PII present as pixels in DICOM images." (Presidio docs, image-redactor page) **[Documented]**
• Getting-started page: "Presidio has two main modules for image de-identification: General purpose, and specifically for DICOM (medical) images." (Presidio docs, getting started with images page) **[Documented]**
### R2
Summary: **PII text that OCR can read.** Finds the same entity types as the Analyzer, in English by default, but only in text the OCR engine reads from the picture. Prompt-injection, harmful-content and topic checks are out of purpose. Coverage depends on which recognizers are enabled. **[Documented]**
Detail:
• Home page scope: "It provides fast identification and anonymization modules for private entities in text and images such as credit card numbers, names, locations, social security numbers, bitcoin wallets…" (Presidio docs, home page) **[Documented]**
• Out of purpose: the home page lists the modules as PII identification (analyzer), de-identification (anonymizer), image redaction and structured-data identification; none is a prompt-injection, harmful-content or topic check (Presidio docs, home page, read 2026-10-09) **[Documented]**
• The image pipeline hands the OCR text to the Analyzer: `analyzer_result = self.analyzer_engine.analyze(` is called on the joined OCR text (image_analyzer_engine.py@2.2.364:76-78) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• With no analyzer supplied, the engine builds a default `AnalyzerEngine()` (image_analyzer_engine.py@2.2.364:31-33), so the entity list is whatever the default recognizers detect (see the Analyzer column) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Language defaults to English: `text_analyzer_kwargs["language"] = "en"` (image_analyzer_engine.py@2.2.364:74-75) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The default NLP model is `en_core_web_lg` (conf/default.yaml@2.2.364:5) and the default analyzer configuration has `supported_languages` set to `en` only (conf/default_analyzer.yaml@2.2.364:1-2) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Installation page: "Presidio image redactor uses the presidio-analyzer … which requires a spaCy language model:" (Presidio docs, installation page) **[Documented]**
• OCR keyword arguments are passed straight to Tesseract through `pytesseract.image_to_data(image, output_type=output_type, …)` (tesseract_ocr.py@2.2.364:18); the docs do not list which keys (such as an OCR language) are expected **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• DICOM scope: "This class only redacts pixel data and does not scrub text PII which may exist in the DICOM metadata." (Presidio docs, image-redactor page) **[Documented]**
• The DICOM docs add: "We highly recommend using the DICOM image redactor engine to redact text from images BEFORE scrubbing metadata PII." (Presidio docs, image-redactor page) **[Documented]**
• By default the DICOM engine builds a PERSON deny-list from the file's own metadata values and adds it as an ad-hoc recognizer: `use_metadata: bool = True` and `PatternRecognizer(supported_entity="PERSON", deny_list=phi_list)` (dicom_image_redactor_engine.py@2.2.364:32 and :928-930) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Whether faces, photographs, signatures, handwriting, barcodes or QR codes are in scope is not stated (checked the image-redactor, getting-started-images, home, FAQ and concepts pages; only "PII text entities" is named) **[Not disclosed]**
• Overview limit: "there is no guarantee that Presidio will find all sensitive information. Consequently, additional systems and protections should be employed." (Presidio docs, home page) **[Documented]**
### R3
Summary: **Images, not text.** Takes a picture or DICOM file sent to or from a model, covering uploads and images in responses or tool results alike, with no system or user prompt needed. The REST service accepts a form upload or base64 JSON. **[Inferred]**
Detail:
• Python input is a PIL image: `redact(self, image: Image.Image, fill=..., ocr_kwargs=..., ad_hoc_recognizers=..., plus extra Analyzer keyword arguments)` (image_redactor_engine.py@2.2.364:83-89) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs example opens the image with Pillow: `image = Image.open("./docs/image-redactor/ocr_text.png")` (Presidio docs, image-redactor page) **[Documented]**
• REST service example in the docs: `curl -XPOST "http://localhost:3000/redact" -H "content-type: multipart/form-data" -F "image=@ocr_test.png" -F "data=\"{'color_fill':'255'}\""` (Presidio docs, image-redactor page) **[Documented]**
• The service has two input forms: a JSON body with a base64 `image` field and optional `analyzer_entities`, or a multipart upload with an `image` file (app.py@2.2.364:52-65) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The service has only two routes, `/health` and `/redact` (POST), and no field for text, so it cannot be given a prompt string (app.py@2.2.364:42 and :47) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• There is no input or output flag; the caller chooses which image to send, so one column covers images attached to prompts and images in responses, retrieved documents or tool results (premise: routes and parameters above carry no direction) **[Inferred]**
• No system prompt, user prompt or conversation is accepted or needed (premise: no such parameter in `redact` or in the REST routes) **[Inferred]**
• Accepted image formats are whatever Pillow's `Image.open` can read; the docs give no format list (checked the image-redactor and getting-started-images pages) **[Not disclosed]**
• DICOM input is a loaded pydicom dataset: a type other than `FileDataset` or `Dataset` raises `TypeError`, and a missing `PixelData` raises `AttributeError` (dicom_image_redactor_engine.py@2.2.364:58-63) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• DICOM docs show four entry points: redact a loaded instance, redact and return boxes, redact from a file, redact from a directory (Presidio docs, image-redactor page, DICOM section) **[Documented]**
• PDF is not an input to the image engine; the PDF sample extracts the text layer with another library and adds highlight annotations (Presidio docs, PDF annotation sample) **[Documented]**
• The PDF sample warns that PII can be missed, including "Text present in images. (requires OCRing)" (Presidio docs, PDF annotation sample) **[Documented]**
• Azure Document Intelligence OCR accepts one page only: `raise ValueError("DocumentIntelligenceOCR only supports 1 page documents")` (document_intelligence_ocr.py@2.2.364:181-182) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
### R4
Summary: **OCR, then the Analyzer, then filled boxes.** Tesseract is the default OCR engine and Azure Document Intelligence the alternative. The OCR text goes to the default English Analyzer, and each matching word box is filled. MIT licence; ownership is moving to Data Privacy Stack. **[Documented]**
Detail:
• Pipeline in code: preprocess the image, run OCR, drop empty boxes, optionally drop low-confidence words, join the words with spaces, run the Analyzer, map hits back to word boxes (image_analyzer_engine.py@2.2.364:55-84) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The default image preprocessor changes nothing: `return image, {}` (image_processing_engine.py@2.2.364:22-30); four optional preprocessors exist: BilateralFilter, SegmentedAdaptiveThreshold, ImageRescaling, ContrastSegmentedImageEnhancer (image_processing_engine.py@2.2.364:100, :148, :226, :274) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs on OCR engines: "Presidio offers two engines for OCR based PII removal. The first is the default engine which uses Tesseract OCR." (Presidio docs, image-redactor page) **[Documented]**
• Docs on the second engine: "The second is the Document Intelligence OCR engine which uses Azure's Document Intelligence service, which requires an Azure subscription." (Presidio docs, image-redactor page) **[Documented]**
• Default OCR in code is `TesseractOCR()` (image_analyzer_engine.py@2.2.364:35-37), a thin wrapper over `pytesseract` (tesseract_ocr.py@2.2.364:18) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Tesseract is a separate install: "Install Tesseract OCR by following the instructions on how to install it for your operating system." (Presidio docs, image-redactor page) **[Documented]**
• Tested version: "Presidio was tested with v5.2.0." (Presidio docs, image-redactor page) **[Documented]**
• The Docker image installs the distribution package with `apt-get install build-essential tesseract-ocr …` and no version pin (Dockerfile@2.2.364:24) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Which Tesseract version the published GHCR image contains is not stated (checked the image-redactor and installation pages and the Dockerfile) **[Not disclosed]**
• Document Intelligence OCR sends the image bytes to the configured Azure endpoint: `self.client.begin_analyze_document(self.model_id, imgbytes, …)` (document_intelligence_ocr.py@2.2.364:166) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Document Intelligence default model is `prebuilt-document` and the class accepts nine prebuilt model ids (document_intelligence_ocr.py@2.2.364:34-44 and :50) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs: "Presidio offers only word-level processing on the result for PII redaction purposes, as all prebuilt document models support this interface." (Presidio docs, image-redactor page) **[Documented]**
• Box mapping is word-level: a word gets a box when its position overlaps the entity span and its text is contained in, or contains, the entity text (image_analyzer_engine.py@2.2.364:167-169) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• DICOM engine: converts pixel data to a greyscale or RGB PIL image, pads it (default 25 pixels), runs the same analysis, then writes filled boxes back into `PixelData`; fill is `contrast` or `background` (dicom_image_redactor_engine.py@2.2.364:29-30, :71-80, :887) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Verification engines draw boxes instead of filling them: `ImagePiiVerifyEngine.verify` and `DicomImagePiiVerifyEngine.verify_dicom_instance` (image_pii_verify_engine.py@2.2.364:23; dicom_image_pii_verify_engine.py@2.2.364:47) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Package `presidio-image-redactor` version 0.0.60, Python `>=3.10,<3.15`, depends on presidio-analyzer `>=2.2.0,<3.0.0`, pytesseract, pydicom, opencv-python and azure-ai-formrecognizer (pyproject.toml@2.2.364:7, :23-33) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Python versions conflict (three sources, none picked): package metadata lists 3.10 to 3.14 **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The live installation page lists 3.10, 3.11, 3.12 and 3.13 (Presidio docs, installation page, read 2026-10-09) **[Documented]**
• REST service: Flask app with `/health` and `/redact`, default port `3000`, bound to `0.0.0.0` (app.py@2.2.364:18, :42, :47, :90); Flask and gunicorn come from the optional `server` extra (pyproject.toml@2.2.364:39) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docker (docs): "docker pull ghcr.io/data-privacy-stack/presidio-image-redactor" and "docker run -d -p 5003:3000 ghcr.io/data-privacy-stack/presidio-image-redactor:latest" (Presidio docs, image-redactor page) **[Documented]**
• The image runs as user 1001 under gunicorn with one worker by default (Dockerfile@2.2.364:15, :42; entrypoint.sh@2.2.364:2) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The Dockerfile sets `ANALYZER_CONF_FILE`, `NLP_CONF_FILE` and `RECOGNIZER_REGISTRY_CONF_FILE`, but no Python file in the image-redactor package reads them and `app.py` builds `ImageRedactorEngine()` with defaults (premise: search of the package at the tag), so the analyzer configuration of the service is probably not changeable by those files **[Inferred]**
• API reference: the docs say "the API Spec for the Image Redactor REST API reference details" (Presidio docs, image-redactor page) **[Documented]**
• The OpenAPI file at the tag lists `/analyze`, `/recognizers`, `/supportedentities`, `/anonymize`, `/anonymizers`, `/deanonymize`, `/deanonymizers` and `/health` and has no `/redact` path (docs/api-docs/api-docs.yml@2.2.364:26-269) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Ownership: "The Presidio project is in the process of transitioning from a Microsoft-owned project to an independent, community-governed open source project under the new GitHub organization Data Privacy Stack." (Presidio docs, project transition page) **[Documented]**
• HTTP 301 from data-privacy-stack.github.io/presidio/ to presidio.dataprivacystack.org/ observed 2026-10-09 on the image-redactor and structured pages; the new host answers 200 **[Documented]**
• Licence: "Presidio will continue to be open source under the MIT license." (Presidio docs, project transition page) **[Documented]**
• The repo LICENSE reads "The MIT License (MIT)" and "Copyright (c) Presidio Contributors." (LICENSE@2.2.364:1-3) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
### R5
Summary: **No verdict; an image comes back.** Python returns the redacted image and optionally one box per redacted word with entity type, offsets, score and pixel position. The REST service returns only the image. No threshold advice or accuracy figure is published for standard images. **[Documented]**
Detail:
• There is no allow or block decision; `redact` returns a PIL image and `redact_and_return_bbox` returns the image plus a list of results (image_redactor_engine.py@2.2.364:35 and :104) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Each result has `entity_type`, `start`, `end`, `score`, `left`, `top`, `width` and `height` (image_recognizer_result.py@2.2.364:18-33) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• One result is created per OCR word inside an entity, each carrying the entity's offsets and score (image_analyzer_engine.py@2.2.364:177-215) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The score is the Analyzer's score for the text entity; the OCR confidence is not returned and is used only for the optional `ocr_threshold` filter, valid from -1 to 100 (image_analyzer_engine.py@2.2.364:87-109) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• REST returns only the image: raw bytes for the multipart form, base64 text for the JSON form; no boxes or entity types (app.py@2.2.364:55-67) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• REST errors: missing image gives HTTP 422 with `{"error": "Invalid parameter, please add image data"}`; any other failure gives HTTP 500 "Internal server error" (app.py@2.2.364:69-81; e2e-tests/tests/test_api_image_redactor.py@2.2.364:24-32) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Python default threshold: no score threshold is passed, so the Analyzer default of 0 applies (image_redactor_engine.py@2.2.364:57-63; analyzer_engine.py@2.2.364:63) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• REST multipart form hard-codes `score_threshold=0.4`, while the REST JSON form passes no threshold (app.py@2.2.364:65 and :55-57) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• So the two REST input forms probably redact different sets of words for the same image (premise: the lines above) **[Inferred]**
• Recommended threshold for image redaction is not stated (checked the image-redactor, getting-started-images, FAQ and evaluation pages and the Python API page) **[Not disclosed]**
• DICOM evaluation outputs are documented: precision, recall, all positives (true and false) and an image with boxes, via `DicomImagePiiVerifyEngine` (Presidio docs, evaluating DICOM redaction page) **[Documented]**
• The DICOM evaluation notebook says: "In the case of these sample images, the precision and recall of the Presidio DicomImageRedactorEngine redact function is 1.0 when we use the default values padding_width=25 and tolerance=50." (Presidio docs, DICOM evaluation notebook) **[Documented]**
• The sample set behind it, `ground_truth.json` at the tag, holds 4 DICOM files and 19 labelled text items (count made from the file) (docs/samples/python/sample_data/ground_truth.json@2.2.364) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The same notebook shows recall 0.2 on one image when `padding_width=1`, so padding changes OCR coverage (Presidio docs, DICOM evaluation notebook) **[Documented]**
• These notebook results are a demonstration on four sample files, not a benchmark; no accuracy, latency or throughput figure is published for standard images or for real scans (checked the image-redactor, evaluation, FAQ and home pages and `Evaluation_Approach.md`) **[Not disclosed]**
### R6
Summary: **An image plus optional fill, language and filters.** Needs the image, an OCR engine (Tesseract installed, or an Azure endpoint and key) and the Analyzer's English spaCy model. Optional inputs are fill colour, OCR confidence cut-off, entities, language, allow list and score threshold. **[Documented]**
Detail:
• Python parameters: `image`, `fill`, `ocr_kwargs`, `ad_hoc_recognizers` and extra keyword arguments (`text_analyzer_kwargs`), the last forwarded to `AnalyzerEngine.analyze` (image_redactor_engine.py@2.2.364:83-89 and :101-102) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Analyzer options such as `entities`, `score_threshold`, `allow_list` and `language` pass through `text_analyzer_kwargs`; `language` defaults to `en` (image_analyzer_engine.py@2.2.364:74-76) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Allow list: words in it get no box (`word not in allow_list`, image_analyzer_engine.py@2.2.364:174) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The docs navigation lists a sample named "Using an allow list with image redaction" (Presidio docs, image-redactor page navigation) **[Documented]**
• `ad_hoc_recognizers` must be a non-empty list of `PatternRecognizer` objects or the call raises `TypeError` (image_redactor_engine.py@2.2.364:117-147) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• OCR confidence filter, docs example: `ocr_kwargs = {"ocr_threshold": 50}` (Presidio docs, image-redactor page) **[Documented]**
• The allowed `ocr_threshold` range is -1 to 100 (image_analyzer_engine.py@2.2.364:95-96) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• REST multipart: form field `image` (file) and optional form field `data` holding `{'color_fill':'255'}` (Presidio docs, image-redactor page) **[Documented]**
• Colour parsing: one integer gives a grey level, three comma-separated integers give RGB, anything else gives HTTP 422 (api_request_convertor.py@2.2.364:38-50) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The REST code reads the fill colour from the form field `data` in both input forms, and a JSON body has no form field, so a JSON request is probably always filled black (premise: app.py@2.2.364:50-57) **[Inferred]**
• DICOM options: `fill` (`contrast` or `background`), `padding_width=25`, `crop_ratio=0.75`, `use_metadata=True`, `ocr_kwargs`, `ad_hoc_recognizers` (dicom_image_redactor_engine.py@2.2.364:29-32) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Document Intelligence needs an endpoint plus a key or an Azure credential, taken from arguments or from `DOCUMENT_INTELLIGENCE_ENDPOINT` and `DOCUMENT_INTELLIGENCE_KEY`; passing both key and credential raises an error (document_intelligence_ocr.py@2.2.364:56-69) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs: "You will need to register with Azure to get an API key and endpoint." (Presidio docs, image-redactor page) **[Documented]**
• Authentication: "Presidio API endpoints do not include built-in authentication by design." (Presidio docs, FAQ) **[Documented]**
• Image size, resolution, request-size limits, latency and concurrency are not stated (checked the image-redactor, getting-started-images and FAQ pages and `app.py`) **[Not disclosed]**
• TLS for the REST service is not mentioned (checked the same pages and the Dockerfile; the app is started with plain gunicorn on port 3000) **[Not disclosed]**
### R7
Summary: **Minimum setup:** install the package, Tesseract and the English spaCy model, or pull the Docker image; the default OCR needs no account. Test with images of known text carrying labelled PII plus clean images, and for DICOM use the documented ground-truth route. **[Inferred]**
Detail:
• **Minimum setup:** `pip install presidio-image-redactor`, `python -m spacy download en_core_web_lg` and a Tesseract install (docs tested v5.2.0), or `docker pull ghcr.io/data-privacy-stack/presidio-image-redactor` and run it on port 3000; the default OCR runs locally with no account or key **[Inferred]**
• Test images: render known synthetic PII strings (names, emails, phone numbers, card numbers, IDs) at several font sizes, resolutions, rotations and backgrounds, plus screenshots and photographed documents, since OCR misses decide recall **[Inferred]**
• Include clean images and images with non-text PII (faces, signatures) as negative controls, because scope beyond text is not stated **[Inferred]**
• Ground truth needed: per image, each PII string with its box or at least its text; the documented DICOM format is JSON keyed by file name, each item with `label`, `left`, `top`, `width`, `height` (Presidio docs, evaluating DICOM redaction page) **[Documented]**
• Documented scorer is DICOM only: `DicomImagePiiVerifyEngine.eval_dicom_instance(instance, ground_truth)` returns precision and recall, with a default matching `tolerance` of 50 pixels (dicom_image_pii_verify_engine.py@2.2.364:137-142) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• For standard images the repo has `ImagePiiVerifyEngine.verify`, which returns an annotated image for visual checking but computes no precision or recall (image_pii_verify_engine.py@2.2.364:23-105) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Check redaction by running OCR again on the output image and confirming labelled strings no longer appear (premise: redaction is a pixel fill) **[Inferred]**
• presidio-research (R010): "Presidio-Research is a python package with a set of tools that help you evaluate the performance of the Presidio Analyzer." (Presidio docs, evaluation page) **[Documented]**
• Its README, version and any image or OCR feature were not read (github.com returned 403 here) **[To be verified]**
• Use presidio-research for the text step: score the same labelled text through the Analyzer to separate detection errors from OCR errors, then compare with the image result (premise: the image engine passes OCR text to the same Analyzer) **[Inferred]**
• Run both REST input forms on the same image and compare, because the multipart form uses a 0.4 threshold and the JSON form does not **[Inferred]**
### R8
Summary: **Key open questions.** Accuracy on real screenshots and scans, non-English OCR, non-text PII, the two REST thresholds, JSON fill colour, request limits, Tesseract version in the image, and beta stability.
Detail:
• Accuracy of OCR plus detection on screenshots, scans, photographed documents, low resolution and rotated text (needs testing; checked the image-redactor, evaluation, FAQ and home pages, no figures)
• Whether faces, signatures, handwriting, barcodes or QR codes are in scope (checked the image-redactor, getting-started-images, home, FAQ and concepts pages, not stated)
• How to set the Tesseract language and the Analyzer language together for non-English text (docs show no example; needs testing)
• Which score threshold to use, given Python default 0, REST multipart 0.4 and REST JSON default (no recommendation stated; needs testing)
• Whether the JSON REST form can set a fill colour (code reads it only from the form field; needs testing)
• Whether the Tesseract version in the GHCR image matches the tested v5.2.0 (run `tesseract -v` in the image)
• Maximum image size, multi-frame images (TIFF, GIF) and whether all frames are redacted (not stated; needs testing)
• Whether metadata such as EXIF or PNG text chunks survives in the output file, since only pixels are painted over (not stated; needs testing)
• Why the REST API spec at the tag has no /redact path although the image-redactor page points to an API spec for it (checked docs/api-docs/api-docs.yml at the tag; the live spec page is rendered by script and was not readable as text)
• What leaves the network when Document Intelligence is used and under which Azure data terms (Presidio docs only say it needs an Azure subscription; not stated)
• Roadmap from beta to a stable release (checked the image-redactor page, home page and CHANGELOG, not stated)
• Release-note wording for 2.2.364 was not re-read because github.com returned 403 here
### R9
Summary: Presidio docs site pages (image redactor, getting started with images, installation, FAQ, evaluation, concepts, transition, samples), repo files at tag 2.2.364 (image redactor package, Dockerfile, tests, API spec) and the licence.
Detail:
• https://presidio.dataprivacystack.org/image-redactor/
• https://presidio.dataprivacystack.org/image-redactor/evaluating_dicom_redaction/
• https://presidio.dataprivacystack.org/getting_started/getting_started_images/
• https://presidio.dataprivacystack.org/installation/
• https://presidio.dataprivacystack.org/api/image_redactor_python/
• https://presidio.dataprivacystack.org/faq/
• https://presidio.dataprivacystack.org/evaluation/
• https://presidio.dataprivacystack.org/learn_presidio/concepts/
• https://presidio.dataprivacystack.org/
• https://presidio.dataprivacystack.org/project_transition/
• https://presidio.dataprivacystack.org/samples/python/example_pdf_annotation/
• https://presidio.dataprivacystack.org/samples/python/example_dicom_redactor_evaluation/
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/image-redactor/index.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/api-docs/api-docs.yml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/samples/python/sample_data/ground_truth.json
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/Evaluation_Approach.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/LICENSE
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/e2e-tests/tests/test_api_image_redactor.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/app.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/Dockerfile
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/entrypoint.sh
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/pyproject.toml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/presidio_image_redactor/image_redactor_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/presidio_image_redactor/image_analyzer_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/presidio_image_redactor/image_processing_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/presidio_image_redactor/tesseract_ocr.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/presidio_image_redactor/document_intelligence_ocr.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/presidio_image_redactor/dicom_image_redactor_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/presidio_image_redactor/dicom_image_pii_verify_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/presidio_image_redactor/image_pii_verify_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/presidio_image_redactor/entities/api_request_convertor.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/presidio_image_redactor/entities/image_recognizer_result.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/analyzer_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/default.yaml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/default_analyzer.yaml

## Column PD5: Presidio: PII detection and anonymisation in structured data (tables and JSON)
### R1
Summary: **Finds PII columns or keys, then masks every value in them.** For a table or a JSON object, Presidio first works out which columns or keys hold which PII type, then applies Anonymizer operators to each value there. It ships as a Python package. **[Documented]**
Detail:
• Description: "The Presidio structured package is a flexible and customizable framework designed to identify and protect structured sensitive data." (Presidio docs, structured page, read 2026-10-09) **[Documented]**
• Detection: "It leverages the detection capabilities of Presidio-Analyzer to identify columns or keys containing personally identifiable information (PII), and establishes a mapping between these column/keys names and the detected PII entities." (Presidio docs, structured page) **[Documented]**
• Anonymisation: "Presidio-Anonymizer is used to apply de-identification techniques to each value in columns identified as containing PII" (Presidio docs, structured page) **[Documented]**
• Home page module list: "Presidio structured: PII identification in structured/semi-structured data" (Presidio docs, home page) **[Documented]**
• Format coverage: "focusing on structured data formats such as tabular formats and semi-structured formats (JSON)" (Presidio docs, structured page) **[Documented]**
• In code the work is split in two: a builder produces a `StructuredAnalysis` (an `entity_mapping` dict), and `StructuredEngine.anonymize(data, structured_analysis, operators)` applies the operators (structured_engine.py@2.2.364:32-49; structured_analysis.py@2.2.364:8-20) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Install: "pip install presidio-structured" (Presidio docs, structured page) **[Documented]**
### R2
Summary: **Same PII types as the Analyzer, decided per column or key.** Types and languages follow the enabled recognizers, English by default. Free text inside a table is listed as future work, and prompt-injection, harmful-content or topic checks are out of purpose. **[Documented]**
Detail:
• Home page scope: "It provides fast identification and anonymization modules for private entities in text and images such as credit card numbers, names, locations, social security numbers, bitcoin wallets…" (Presidio docs, home page) **[Documented]**
• Out of purpose: the home page lists the modules as PII identification (analyzer), de-identification (anonymizer), image redaction and structured-data identification; none is a prompt-injection, harmful-content or topic check (Presidio docs, home page, read 2026-10-09) **[Documented]**
• Entity detection reuses the Analyzer: each builder creates `AnalyzerEngine(default_score_threshold=...)` and a `BatchAnalyzerEngine` unless an analyzer is passed in (analysis_builder.py@2.2.364:39-47) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Language defaults to English in both builders: `language: str = "en"` (analysis_builder.py@2.2.364:95 and :174) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• One entity type per column: the builder reduces the per-cell hits to a single type by a selection strategy, and a column with no hits is labelled `NON_PII` and left out of the mapping (analysis_builder.py@2.2.364:205-209 and :286-289) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs: "Most Common (default): Identifies the most frequently occurring PII entity in a data column or field." (Presidio docs, structured page) **[Documented]**
• Docs: "Highest Confidence: Selects PII entities based on the highest confidence scores, irrespective of their occurrence frequency." (Presidio docs, structured page) **[Documented]**
• Docs: "Mixed: Combines the strengths of both the above strategies." (Presidio docs, structured page) **[Documented]**
• Limit: "Note that sensitive data might not be automatically detected in some cases. Consequently, additional systems and protections should be employed." (Presidio docs, structured page) **[Documented]**
• Future work on the same page: "Improve support for datasets with mixed free-text and structure data (e.g. some columns contain free text)" and "Add support for the detection of sensitive column names" (Presidio docs, structured page) **[Documented]**
• JSON key names are given to the Analyzer as context words (`context=[key]`), so a key such as "email" can raise scores; the table builder passes no context (batch_analyzer_engine.py@2.2.364:108-114; analysis_builder.py@2.2.364:255-260) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs on context from metadata: "This is useful when there is context coming from metadata such as column names or a specific user input." (Presidio docs, context tutorial) **[Documented]**
• Limit on lists: "Nesting objects in lists is not supported in JsonAnalysisBuilder for now," (Presidio docs, structured page) **[Documented]**
• The batch engine raises "Lists of objects are not yet supported." (batch_analyzer_engine.py@2.2.364:148) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Workaround in docs: write the mapping by hand, `StructuredAnalysis(entity_mapping={"users.name": "PERSON", "users.email": "EMAIL_ADDRESS"})` (Presidio docs, structured page) **[Documented]**
• JSON analysis casts numbers and booleans to text before detection (`text=str(value)`) and keeps only the first recognizer result per key (batch_analyzer_engine.py@2.2.364:113-114; analysis_builder.py@2.2.364:149) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
### R3
Summary: **Parsed tables and JSON, not raw prompts.** Takes a pandas DataFrame or a JSON-like dict or list, so it fits retrieved records and tool outputs after parsing; it is not a prompt-text check. Same logic for inputs and outputs, no prompt context needed. **[Inferred]**
Detail:
• Engine input type: `data: Union[Dict, DataFrame]` (structured_engine.py@2.2.364:34); the pandas processor rejects anything but a DataFrame and the JSON processor accepts only a dict or list (data_processors.py@2.2.364:118-119 and :199-200) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• File helpers read a CSV into a DataFrame or a JSON file into a dict: `CsvReader`, `JsonReader` (data_reader.py@2.2.364:29-70) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• No REST route, Docker image or command-line entry for presidio-structured was found: the package folder has no `app.py` or Dockerfile, docker-compose.yml lists no structured service, and the structured page shows `pip install` only (checked the repo tree at the tag, docker-compose.yml and the structured page) **[Not disclosed]**
• The package has no input or output flag and takes data objects, so one column covers retrieved records, tool-call arguments and tool results that are JSON or tabular, once parsed (premise: no direction parameter anywhere in the package) **[Inferred]**
• A prompt or response that is plain text is not a valid input; it must first be parsed into a dict or DataFrame (premise: the type checks in the data processors) **[Inferred]**
• No system or user prompt is needed (premise: no such parameter) **[Inferred]**
• No docs page ties presidio-structured to LLM prompts, retrieved records or tool outputs; the stated use is protecting structured datasets (checked the structured page, home, FAQ and concepts pages) **[Not disclosed]**
• Each operator receives the whole cell value, not just a matching span: `operator.operate(params=params, text=text)` on `getattr(row, key)` (data_processors.py@2.2.364:56 and :124) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• So a free-text cell in a mapped column is replaced or masked as a whole, not edited around the PII (premise: the line above) **[Inferred]**
• Scope note for CP1: used on retrieved records or tool output it is on the AI data path; used to de-identify bulk database exports unrelated to an AI conversation it is inventory-only under the scope guide, and the docs describe the second use more than the first **[Inferred]**
### R4
Summary: **Two steps over the Analyzer and Anonymizer.** A builder samples and analyses values to map each column or key to one entity type, then the engine applies Anonymizer operators to every value there. Package version 0.0.8 under the MIT licence. **[Documented]**
Detail:
• Package `presidio-structured` version 0.0.8, Python `>=3.10,<3.15`, depends on presidio-analyzer `>=2.2.0,<3.0.0`, presidio-anonymizer `>=2.2.364,<3.0.0`, pandas `>=1.5.2,<4.0.0` and click (pyproject.toml@2.2.364:7, :23-30) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Exported classes: `StructuredEngine`, `JsonAnalysisBuilder`, `PandasAnalysisBuilder`, `StructuredAnalysis`, `CsvReader`, `JsonReader`, `PandasDataProcessor`, `JsonDataProcessor` (__init__.py@2.2.364:17-26) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Table analysis: samples `n` rows (default all) with `df.sample(n, random_state=123)`, sends each column through `BatchAnalyzerEngine.analyze_iterator`, then picks one entity per column (analysis_builder.py@2.2.364:190-211 and :255-260) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Strategies: `selection_strategy` is `most_common` (default), `highest_confidence` or `mixed`; `mixed_strategy_threshold` defaults to 0.5 (analysis_builder.py@2.2.364:168 and :175-176) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs: "Mixed … selects the entity with the highest confidence score if that score exceeds a specified threshold (controlled by mixed_strategy_threshold); otherwise, it defaults to the most common entity." (Presidio docs, structured page) **[Documented]**
• For `most_common` the stored score is the share of hits with that type (analysis_builder.py@2.2.364:316) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• JSON analysis: `BatchAnalyzerEngine.analyze_dict` walks nested dicts and builds dotted key paths such as `user.email` (analysis_builder.py@2.2.364:104-119 and :142-147) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Operators come from the Anonymizer's factory with the type fixed: "NOTE: hardcoded OperatorType.Anonymize, as this is the only one supported." (data_processors.py@2.2.364:78) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The factory's anonymise list is Custom, Encrypt, Hash, Keep, Mask, Redact, Replace, plus the AHDS surrogate when its extra is installed (operators_factory.py@2.2.364:24-26) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `StructuredEngine` has an `anonymize` method only, so decrypt and the other deanonymise operators are not reachable through it (structured_engine.py@2.2.364:32; premise: no other public method) **[Inferred]**
• Default operator: `DEFAULT = "replace"`; a missing `DEFAULT` key is filled with `OperatorConfig(DEFAULT)` (structured_engine.py@2.2.364:13 and :61-67) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Operator lookup per column: `operators.get(entity, operators.get("DEFAULT", None))`, error if none (data_processors.py@2.2.364:75-77) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `replace` without `new_value` returns `f"<{params.get('entity_type')}>"` (replace.py@2.2.364:16-18), but the structured path passes only the operator's own params, so the default probably yields the text "<None>" and not "<PERSON>" (premise: data_processors.py@2.2.364:56) **[Inferred]**
• Both processors write results into the object passed in: `data.at[row.Index, key] = operated_text` and `_set_nested_value(data, keys, operated_text)` (data_processors.py@2.2.364:128 and :216-222) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `hash` uses a random salt per value unless `salt` is given, so equal cells hash differently by default (hash.py@2.2.364:53-54); the Anonymizer docs say "Starting from version 2.2.361, the hash operator uses random salt by default for security." (docs/anonymizer/index.md@2.2.364:259) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Concepts page says "The StructuredEngine is a class in Presidio that is responsible for detecting PII entities in structured data." (Presidio docs, concepts page) **[Documented]**
• In code `StructuredEngine` only anonymises; detection sits in the analysis builders (structured_engine.py@2.2.364:32-49; analysis_builder.py@2.2.364:89-119) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Maturity: the changelog entry for 2.2.352 reads "Added alpha of presidio-structured, a library (presidio-structured) which re-uses existing logic from existing presidio components…" (CHANGELOG.md@2.2.364:531) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Current maturity label for presidio-structured is not stated (checked the structured page, the package README, home page and FAQ) **[Not disclosed]**
• Python versions conflict (three sources, none picked): package metadata lists 3.10 to 3.14 **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The live installation page lists 3.10 to 3.13 (Presidio docs, installation page, read 2026-10-09) **[Documented]**
• Ownership: "The Presidio project is in the process of transitioning from a Microsoft-owned project to an independent, community-governed open source project under the new GitHub organization Data Privacy Stack." (Presidio docs, project transition page) **[Documented]**
• HTTP 301 from data-privacy-stack.github.io/presidio/ to presidio.dataprivacystack.org/ observed 2026-10-09 on the image-redactor and structured pages **[Documented]**
• Licence: the package declares `license = "MIT"` (presidio-structured/pyproject.toml@2.2.364:10) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The transition page says "Presidio will continue to be open source under the MIT license." (Presidio docs, project transition page) **[Documented]**
### R5
Summary: **A transformed table or object plus a column map.** Output is the anonymised DataFrame or dict; the analysis step returns a column-to-entity map with no per-cell findings or scores. No recommended threshold or accuracy figure is published. **[Documented]**
Detail:
• `anonymize` returns the same kind of object it was given, a dict or a DataFrame (structured_engine.py@2.2.364:37-49) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Analysis result is `StructuredAnalysis` holding `entity_mapping: Dict[str, str]`; its docstring says "Currently, this class only contains entity mapping." (structured_analysis.py@2.2.364:12 and :20) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Spans, scores and decision-process explanations are not returned: the mapping keeps only each key's entity type (analysis_builder.py@2.2.364:115-119 and :205-209) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Columns judged `NON_PII` are not in the mapping, so they are not anonymised (analysis_builder.py@2.2.364:205-209) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Score threshold for detection: the builders accept `analyzer_score_threshold`, used as `default_score_threshold` of a new `AnalyzerEngine`, default 0 (analysis_builder.py@2.2.364:28 and :39-46) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The abstract `generate_analysis` lists `score_threshold`, the concrete builders do not, and `_remove_low_scores` is defined but never called in the module (analysis_builder.py@2.2.364:56, :95, :170-177 and :66) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `mixed_strategy_threshold` must lie between 0 and 1 or `ValueError` is raised (analysis_builder.py@2.2.364:372-375); the docs example uses 0.75 (Presidio docs, structured page) **[Documented]**
• Recommended threshold or strategy per use case is not stated (checked the structured page, package README, FAQ and home page) **[Not disclosed]**
• No accuracy, latency or throughput figure for presidio-structured is published (checked the structured, evaluation, FAQ and home pages and the package README) **[Not disclosed]**
### R6
Summary: **Data, an entity map and operators.** Needs a DataFrame or dict, a column-to-entity map (generated or hand-written) and operators keyed by entity with a default. Sampling, language, strategy and batch settings are optional. The Analyzer's spaCy model must also be installed. **[Inferred]**
Detail:
• Table analysis call: `PandasAnalysisBuilder().generate_analysis(df, n=None, language="en", selection_strategy="most_common", mixed_strategy_threshold=0.5)` (analysis_builder.py@2.2.364:170-177) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• JSON analysis call: `JsonAnalysisBuilder().generate_analysis(data, language="en")` (analysis_builder.py@2.2.364:92-96) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Builder constructor: `analyzer`, `analyzer_score_threshold`, `n_process=1`, `batch_size=1` (analysis_builder.py@2.2.364:25-31) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Hand-written map: keys are column names or dotted JSON paths (Presidio docs, structured page, `StructuredAnalysis(entity_mapping={"users.name": "PERSON", …})`) **[Documented]**
• Operators are a dict of entity to `OperatorConfig`, for example `"PERSON": OperatorConfig("replace", {"new_value": "REDACTED"})` and a `custom` operator with a lambda (Presidio docs, structured page) **[Documented]**
• JSON data needs `StructuredEngine(data_processor=JsonDataProcessor())`; the table processor is the default (Presidio docs, structured page) **[Documented]**
• The builders create a default `AnalyzerEngine` unless one is passed, and that loads `en_core_web_lg` (analysis_builder.py@2.2.364:42-46; conf/default.yaml@2.2.364:5) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The structured page's install block shows only `pip install presidio-structured`, so the spaCy model has to be downloaded separately (premise: the two lines above) **[Inferred]**
• `analyze_iterator` accepts only int, float, bool and str values (batch_analyzer_engine.py@2.2.364:142-150) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Dataset size, row limits and memory use are not stated (checked the structured page, package README and FAQ) **[Not disclosed]**
### R7
Summary: **Minimum setup:** pip install presidio-structured and the English spaCy model, then run it on a small DataFrame and a JSON object with known PII columns and clean columns. No account is needed. Score the column map and the output cells separately against labels. **[Inferred]**
Detail:
• **Minimum setup:** `pip install presidio-structured` plus `python -m spacy download en_core_web_lg`, then a script using `PandasAnalysisBuilder`, `JsonAnalysisBuilder` and `StructuredEngine`; it runs locally with no account **[Inferred]**
• Starter data exists in the repo: `docs/samples/python/sample_data/test_structured.json` and `test_structured_complex.json` (file listing at the tag) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Table cases: clearly PII columns (names, emails, phones, IDs), clean columns (counts, codes), a free-text column with a name inside, a column with PII in only a few rows, and misleading column names **[Inferred]**
• JSON cases: flat object, nested object, list of plain values, list of objects (expected to need a hand-written map), numbers stored as integers **[Inferred]**
• Ground truth needed at two levels: column or key to entity, and per-cell PII spans or at least flags for whether a cell contains PII; the labelled set needs entity-level ground truth **[Inferred]**
• Score separately: column-map precision and recall, and leaks (PII still visible in output cells) **[Inferred]**
• Operator checks: run `replace`, `redact`, `mask`, `hash`, `custom` and `encrypt` on string, number and empty cells and confirm no errors and no input mutation surprises **[Inferred]**
• presidio-research (R010): "Presidio-Research is a python package with a set of tools that help you evaluate the performance of the Presidio Analyzer." (Presidio docs, evaluation page); the FAQ adds that it "also features a simple PII data generator" (Presidio docs, FAQ) **[Documented]**
• Whether presidio-research has any table or JSON mode was not checked (its README was not readable here) **[To be verified]**
• Use presidio-research to score the cell-level detection layer, since the builders call the same Analyzer (premise: analysis_builder.py@2.2.364:39-47) **[Inferred]**
### R8
Summary: **Key open questions.** Whether this should be a column or inventory only (CP1), the default replace output, behaviour on non-text cells and odd column names, in-place mutation, majority-vote mapping errors, and maturity.
Detail:
• Column or inventory only: no docs page links presidio-structured to LLM traffic (checked the structured, home, FAQ and concepts pages); the decision belongs to CP1
• What `replace` with no `new_value` returns inside presidio-structured (code suggests "<None>"; needs testing)
• Behaviour of `mask`, `hash`, `redact` and `encrypt` on integer, float and empty cells (needs testing; `hash` calls `text.encode()`)
• DataFrame column names with spaces or other non-identifier characters, since the processor reads columns with `getattr(row, key)` (needs testing)
• Whether callers must copy their data first, because both processors write into the object passed in (code reading; needs testing)
• How often the one-entity-per-column rule mislabels sparse, mixed or free-text columns (needs testing; docs list mixed free text as future work)
• Why `_remove_low_scores` and `score_threshold` are not applied by the concrete builders (code reading; not stated in docs)
• Referential integrity across tables: `hash` needs a shared salt and Presidio keeps no session state (needs testing)
• Throughput on large tables, given a per-cell loop in the pandas processor (no figures published; needs testing)
• Maturity label and roadmap: alpha in 2024, now version 0.0.8, PySpark and k-anonymity listed as future work (checked the structured page, README and changelog)
• Whether a REST or Docker route for structured data is planned (checked the repo tree at the tag, docker-compose.yml and docs, not stated)
• Release-note wording for 2.2.364 was not re-read because github.com returned 403 here
### R9
Summary: Presidio docs site pages (structured, home, installation, FAQ, evaluation, concepts, context tutorial, transition) and repo files at tag 2.2.364 (structured package, Analyzer and Anonymizer code, changelog, licence).
Detail:
• https://presidio.dataprivacystack.org/structured/
• https://presidio.dataprivacystack.org/
• https://presidio.dataprivacystack.org/installation/
• https://presidio.dataprivacystack.org/faq/
• https://presidio.dataprivacystack.org/evaluation/
• https://presidio.dataprivacystack.org/learn_presidio/concepts/
• https://presidio.dataprivacystack.org/tutorial/06_context/
• https://presidio.dataprivacystack.org/project_transition/
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/CHANGELOG.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/anonymizer/index.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/samples/python/sample_data/test_structured.json
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/samples/python/sample_data/test_structured_complex.json
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docker-compose.yml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-structured/pyproject.toml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-structured/presidio_structured/__init__.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-structured/presidio_structured/structured_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-structured/presidio_structured/analysis_builder.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-structured/presidio_structured/config/structured_analysis.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-structured/presidio_structured/data/data_processors.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-structured/presidio_structured/data/data_reader.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/batch_analyzer_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/default.yaml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/operators_factory.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/replace.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/hash.py

## Column PD6: Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers)
### R1
Summary: **Add your own detectors.** Presidio lets you define new PII entity types with regex patterns, word lists and context words, as code, YAML or a per-request JSON recognizer. An allow list does the opposite and suppresses chosen matches. **[Documented]**
Detail:
• "Presidio can be extended to support detection of new types of PII entities, and to support additional languages." (Presidio docs, adding recognizers page, read 2026-10-09) **[Documented]**
• "These PII recognizers could be added via code or ad-hoc as part of the request." (Presidio docs, adding recognizers page) **[Documented]**
• Pattern class: "The PatternRecognizer is an class for supporting regex and deny-list based recognition logic, including validation (e.g., with checksum) and context support." (Presidio docs, adding recognizers page) **[Documented]**
• Deny list example: `PatternRecognizer(supported_entity="TITLE", deny_list=["Mr.","Mrs.","Miss"])` (Presidio docs, adding recognizers page) **[Documented]**
• No-code route: "There's an existing set of regular expressions / deny-lists that should be leveraged within Presidio." names one use of the YAML configuration (Presidio docs, no-code tutorial) **[Documented]**
• Ad-hoc route: "it is possible to create ad-hoc recognizers via the Presidio Analyzer API for regex and deny-list based logic." (Presidio docs, ad-hoc recognizers tutorial) **[Documented]**
• Allow-list route: "we will pass a short list of tokens which should not be marked as PII even if detected by one of the recognizers." (Presidio docs, allow-list tutorial) **[Documented]**
• Class hierarchy: "The EntityRecognizer is an abstract class for all recognizers." and "The abstract class LocalRecognizer is implemented by all recognizers running within the Presidio-analyzer process." (Presidio docs, adding recognizers page) **[Documented]**
### R2
Summary: **Entity types you define yourself.** Detects whatever your regexes, word lists or code describe, such as IDs, titles or internal terms, one language per recognizer. Regexes and lists carry no meaning, so paraphrase is missed, and prompt-injection, harmful-content or topic checks are out of purpose. **[Inferred]**
Detail:
• Docs examples of custom entities: `TITLE` (word list), `ZIP` (regex with score 0.01 and context "zip", "code"), `MR_TITLE`, `MS_TITLE` (Presidio docs, adding recognizers page) **[Documented]**
• The entity name is free text chosen by the author: `PatternRecognizer` requires `supported_entity` and holds exactly one entity (pattern_recognizer.py@2.2.364:63-64 and :73) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• A recognizer needs patterns or a deny list, otherwise `ValueError` (pattern_recognizer.py@2.2.364:66-70) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs: "Each recognizer can support one language." (Presidio docs, languages page) **[Documented]**
• `supported_language` defaults to `en` in `PatternRecognizer` (pattern_recognizer.py@2.2.364:54) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• A request only uses recognizers whose `supported_language` equals the request language, ad-hoc ones included; if none match the entities, `ValueError("No matching recognizers were found to serve the request.")` (recognizer_registry.py@2.2.364:218-229 and :248) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• A YAML recognizer with several `supported_languages` creates one instance per language (conf/default_recognizers.yaml@2.2.364:28) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs: "Many PII entities are undetectable using naive approaches like deny-lists or regular expressions." (Presidio docs, developing recognizers page) **[Documented]**
• Docs: "Each recognizer, regardless of its complexity, could have false positives and false negatives." (Presidio docs, developing recognizers page) **[Documented]**
• Rule-based logic beyond regex needs a subclass: "The Presidio EntityRecognizer API allows you to use spaCy extracted features like lemmas, part of speech, dependencies and more to create your logic." (Presidio docs, developing recognizers page) **[Documented]**
• A custom recognizer is added next to the default ones: with `entities` omitted, every recognizer for the request language runs, built-in and custom (analyzer_engine.py@2.2.364:227-234; recognizer_registry.py@2.2.364:217-222) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Out of purpose: the home page lists Presidio's modules as PII identification, de-identification, image redaction and structured-data identification; none is a prompt-injection, harmful-content or topic check (Presidio docs, home page, read 2026-10-09) **[Documented]**
• Pattern and word-list recognizers match strings, not meaning, so reworded or obfuscated secrets are not found (premise: they are regexes over the text, pattern_recognizer.py@2.2.364:216-226) **[Inferred]**
### R3
Summary: **Plain text, same as the Analyzer.** A custom recognizer sees the string passed to the Analyzer, so it covers prompts, responses, retrieved text and tool inputs or outputs alike, with no system or user prompt needed. Request-level context words can come from metadata. **[Inferred]**
Detail:
• Custom recognizers run inside `AnalyzerEngine.analyze(text, language, …)`, which takes one string and a language (analyzer_engine.py@2.2.364:169-171) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The REST `/analyze` route takes `text` as a string or a list of strings and requires `language` (app.py@2.2.364:72-80) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• There is no input or output flag and no prompt parameter, so one column applies to prompts and responses and to retrieved text and tool inputs or outputs (premise: the signature above) **[Inferred]**
• Ad-hoc recognizers: "are added to the /analyze request and are only used in the context of this request." (Presidio docs, ad-hoc recognizers tutorial) **[Documented]**
• Docs: "These ad-hoc recognizers could be useful if Presidio is already deployed, but requires additional detection logic to be added." (Presidio docs, ad-hoc recognizers tutorial) **[Documented]**
• Request-level context: "additional context words could be passed on the request level. This is useful when there is context coming from metadata such as column names or a specific user input." (Presidio docs, context tutorial) **[Documented]**
• The allow list is applied to the matched text of each result after detection, either as exact strings or, with `allow_list_match="regex"`, as one joined regex (analyzer_engine.py@2.2.364:417-471) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The live Python API reference lists `allow_list_match: Optional[str] = "exact"` and `regex_flags` for `analyze` (Presidio docs, Analyzer Python API page) **[Documented]**
• The image engine also takes `ad_hoc_recognizers`, restricted to `PatternRecognizer` objects (image_redactor_engine.py@2.2.364:117-147) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
### R4
Summary: **Regex engine plus scores, with a context boost.** A pattern recognizer runs each regex over the text and gives hits the score you set (word lists default to 1.0); context words nearby can raise it. Over REST only regex and word-list recognizers can be sent. **[Documented]**
Detail:
• Constructor: `PatternRecognizer(supported_entity, name, supported_language="en", patterns, deny_list, context, deny_list_score=1.0, global_regex_flags=DOTALL|MULTILINE|IGNORECASE, version, country_code)` (pattern_recognizer.py@2.2.364:50-62) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• A deny list becomes one regex of escaped words with word-boundary guards: `r"(?:^|(?<=\W))(" + "|".join(escaped_deny_list) + r")(?:(?=\W)|$)"` (pattern_recognizer.py@2.2.364:133) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `Pattern` checks that the regex compiles and that the score is between 0 and 1 (pattern.py@2.2.364:26-39) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Optional hooks `validate_result` and `invalidate_result`: a true validation sets the score to 1.0, false sets it to 0, invalidation sets 0, and results with score 0 are dropped (pattern_recognizer.py@2.2.364:136-156 and :257-268) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Supplying real validation logic therefore needs a subclass of `PatternRecognizer` that overrides the two hooks (premise: both hooks return `None` in the base class) **[Inferred]**
• Regex timeout: `REGEX_TIMEOUT_SECONDS = int(os.environ.get("REGEX_TIMEOUT_SECONDS", 60))`, and a timed-out pattern is skipped with a warning (pattern_recognizer.py@2.2.364:21 and :217, :272-278) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The changelog lists it: "Configurable regex execution timeout (default 60 seconds) via `REGEX_TIMEOUT_SECONDS` environment variable to prevent catastrophic backtracking" (CHANGELOG.md@2.2.364:161, under 2.2.362) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Context boost: the default `LemmaContextAwareEnhancer` uses `context_similarity_factor=0.35`, `min_score_with_context_similarity=0.4`, `context_prefix_count=5`, `context_suffix_count=0`, substring matching (lemma_context_aware_enhancer.py@2.2.364:37-41) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs worked example: "The confidence score is now 0.4, instead of 0.01, since the LemmaContextAwareEnhancer default context similarity factor is 0.35 and default minimum score with context similarity is 0.4." (Presidio docs, context tutorial) **[Documented]**
• Code route: `registry.add_recognizer(titles_recognizer)` then `AnalyzerEngine(registry=registry)` (Presidio docs, adding recognizers page) **[Documented]**
• YAML route: `add_recognizers_from_yaml` loads each entry through `add_pattern_recognizer_from_dict`, so it accepts pattern recognizers only (recognizer_registry.py@2.2.364:331-379) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Registry-provider YAML: "type: this could be either predefined or custom. As this is optional, if not stated otherwise, the default type is custom." (Presidio docs, recognizer registry page) **[Documented]**
• Custom entries are built with `PatternRecognizer.from_dict`, one instance per language (recognizers_loader_utils.py@2.2.364:188-225) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Documented custom-entry fields: `patterns`, `enabled`, `supported_entity`, `deny_list`, `deny_list_score`, and context words inside `supported_languages` (Presidio docs, recognizer registry page) **[Documented]**
• REST ad-hoc recognizers are built with `PatternRecognizer.from_dict(rec)` (analyzer_request.py@2.2.364:31-36), so regex and deny-list only; the Python `analyze` accepts any `EntityRecognizer` list (analyzer_engine.py@2.2.364:177) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Remote recognizers: "A remote recognizer is an EntityRecognizer object interacting with an external service." (Presidio docs, adding recognizers page) **[Documented]**
• Per-recognizer score thresholds: the tagged docs say `score_thresholds` accepts a `default` and entity overrides, with precedence "analyzer.analyze(score_threshold=...) > an entity specific threshold > a recognizer default threshold (`default`) > the Presidio Analyzer `default_score_threshold`" (docs/analyzer/recognizer_registry_provider.md@2.2.364:113) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The code at the tag implements it (analyzer_engine.py@2.2.364:357-414; score_thresholds.py@2.2.364:22-38), while `CHANGELOG.md` lists it under `[unreleased]` (CHANGELOG.md@2.2.364:10) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Conflict, live API text: the live Analyzer Python API page describes the request parameter as "score_threshold: A minimum value for which to return an identified entity", with no mention of recognizer-level thresholds (Presidio docs, Analyzer Python API page, read 2026-10-09) **[Documented]**
• The live registry page lists the YAML recognizer parameters without `score_thresholds` (checked the page text for "threshold", no hit, read 2026-10-09) **[Not disclosed]**
• Package `presidio-analyzer` version 2.2.364 (presidio-analyzer/pyproject.toml@2.2.364:7) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Ownership and licence: "The Presidio project is in the process of transitioning from a Microsoft-owned project to an independent, community-governed open source project under the new GitHub organization Data Privacy Stack." and "Presidio will continue to be open source under the MIT license." (Presidio docs, project transition page) **[Documented]**
• Related column on sheet 3: NeMo Guardrails: Regex pattern blocklist (input/output) decides to block a message; a Presidio custom recognizer instead returns spans and scores and leaves the decision to the caller (premise: R5 below and the NeMo column title) **[Inferred]**
### R5
Summary: **Spans with the score you set.** A custom recognizer returns the usual Analyzer result: entity type, start, end and score. With the decision process on, the explanation names the pattern, regex, original score and context boost. No threshold advice or accuracy figure is published. **[Documented]**
Detail:
• Result fields: `entity_type`, `start`, `end`, `score`, `analysis_explanation`, `recognition_metadata` (recognizer_result.py@2.2.364:34-55) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Explanation fields include `recognizer`, `pattern_name`, `pattern`, `original_score`, `score`, `score_context_improvement`, `supportive_context_word`, `validation_result`, `regex_flags` (analysis_explanation.py@2.2.364:18-37) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Pattern hits get an explanation of the form Detected by `<recognizer name>` using pattern `<pattern name>` (pattern_recognizer.py@2.2.364:178-180) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs: "To enable it, call the analyze method with return_decision_process set as True." (Presidio docs, decision process page) **[Documented]**
• Otherwise the explanation is removed: `result.analysis_explanation = None` (analyzer_engine.py@2.2.364:508) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The REST service also deletes `recognition_metadata` from every result before returning (app.py@2.2.364:168-175) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Score sources for a custom recognizer: the pattern's own score (0 to 1), 1.0 for a true validation, 0 for a false validation or invalidation, then any context boost (pattern_recognizer.py@2.2.364:234 and :257-265) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Default engine threshold is 0 (analyzer_engine.py@2.2.364:63), and a request `score_threshold` overrides recognizer-level thresholds (analyzer_engine.py@2.2.364:192-195) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Guidance on weak patterns: "Zip regex patterns (essentially 5 digits) are very weak, so we would want the initial confidence to be low, and increased with the existence of context words." (Presidio docs, context tutorial) **[Documented]**
• A single recommended pattern score or threshold is not stated; docs examples use 0.01, 0.5 and 1 (checked the adding recognizers, developing recognizers, context, regex and deny-list tutorials) **[Not disclosed]**
• Docs give a speed target for recognizer authors: "Anything above 100ms per request with 100 tokens is probably not good enough." (Presidio docs, developing recognizers page); it is advice, not a measured result **[Documented]**
• No published accuracy or latency figure for custom recognizers (checked the developing recognizers, adding recognizers, evaluation and FAQ pages) **[Not disclosed]**
### R6
Summary: **Entity name, patterns or words, language and optional context.** A recognizer needs a supported entity, at least one scored regex or a deny list, and a language. Context words, regex flags, allow list and request-level settings are optional. **[Documented]**
Detail:
• Required in code: `supported_entity` plus `patterns` or `deny_list` (pattern_recognizer.py@2.2.364:63-70) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• REST ad-hoc recognizer JSON: `name`, `supported_language`, `patterns` (each `name`, `regex`, `score`), `deny_list`, `context`, `supported_entity` (docs/api-docs/api-docs.yml@2.2.364:575-602) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `/analyze` fields read by the service: `text`, `language`, `entities`, `correlation_id`, `score_threshold`, `return_decision_process`, `ad_hoc_recognizers`, `context`, `allow_list`, `allow_list_match`, `regex_flags` (analyzer_request.py@2.2.364:24-42) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The OpenAPI schema for `AnalyzeRequest` omits `allow_list`, `allow_list_match` and `regex_flags` (docs/api-docs/api-docs.yml@2.2.364:392-436), so the spec and the code differ **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• `language` is required (`raise Exception("No language provided")`) (app.py@2.2.364:79-80) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• If `entities` is sent it must include the custom entity name, otherwise the custom recognizer is not selected (recognizer_registry.py@2.2.364:224-231) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• The docs ad-hoc example lists `"ZIP"` in `entities` next to the ad-hoc recognizer for `ZIP` (Presidio docs, ad-hoc recognizers tutorial) **[Documented]**
• Default regex flags are `DOTALL | MULTILINE | IGNORECASE`, so matching is case-insensitive unless changed (pattern_recognizer.py@2.2.364:59; analyzer_engine.py@2.2.364:181) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Regex flags for one recognizer: `global_regex_flags` in the constructor; for all: `global_regex_flags` on `RecognizerRegistry` or `global_regex_flags: 26` in YAML (Presidio docs, adding recognizers and registry pages) **[Documented]**
• Context words: a `context` list on the recognizer, per language in YAML (`supported_languages: - language: en  context: [zip, code]`), and an optional request-level `context` list (Presidio docs, registry page and context tutorial) **[Documented]**
• Batch size and processes for the service come from the environment: `BATCH_SIZE` default 500 and `N_PROCESS` default 1 (app.py@2.2.364:20-21 and :89, :103) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Request size limit is not stated (checked the adding recognizers page, FAQ, OpenAPI file and `app.py`) **[Not disclosed]**
• Authentication: "Presidio API endpoints do not include built-in authentication by design." (Presidio docs, FAQ) **[Documented]**
### R7
Summary: **Minimum setup:** pip install presidio-analyzer and the English spaCy model, define a recognizer in Python or send an ad-hoc recognizer to a local analyzer service, then run labelled positive and negative strings. No account is needed. Score returned spans against labelled offsets. **[Inferred]**
Detail:
• **Minimum setup:** `pip install presidio-analyzer`, `python -m spacy download en_core_web_lg`, then `PatternRecognizer(...)` with `analyzer.registry.add_recognizer(...)`, or `docker run` of the Analyzer image and a `POST /analyze` with `ad_hoc_recognizers`; runs locally with no account **[Inferred]**
• Direct unit check without the engine: the docs call `titles_recognizer.analyze(text="Mr. Schmidt", entities="TITLE")` (Presidio docs, adding recognizers page) **[Documented]**
• Cases: exact hits, near misses, word-boundary cases for deny lists, upper and lower case, overlap with built-in types (a digit regex next to PHONE_NUMBER), context word present and absent, wrong request language, allow-list suppression **[Inferred]**
• Route parity: run the same recognizer from code, YAML and REST ad-hoc and compare spans and scores **[Inferred]**
• Safety check for ad-hoc regex: send a pattern prone to catastrophic backtracking and confirm the timeout (default 60 seconds) and that other requests are not blocked **[Inferred]**
• Ground truth needed: span start, end and entity type per labelled string; a labelled test set needs entity-level ground truth **[Inferred]**
• presidio-research (R010): "For tools and documentation on evaluating and analyzing recognizers, refer to the presidio-research GitHub repository." (Presidio docs, developing recognizers page) **[Documented]**
• The evaluation page describes it as "a python package with a set of tools that help you evaluate the performance of the Presidio Analyzer" (Presidio docs, evaluation page) **[Documented]**
• Its README, release tag and data format were not read (github.com returned 403 here) **[To be verified]**
### R8
Summary: **Key open questions.** Non-pattern logic over REST, REST error codes for bad regex or language, server-side regex safety, per-recognizer threshold status in the released package, and score choices for weak patterns.
Detail:
• Whether non-pattern recognizers can be sent per request over REST (code builds only `PatternRecognizer`; docs say regex and deny-list only; no statement about others)
• HTTP status for an invalid regex, a score outside 0 to 1, or a language with no matching recognizer (code suggests HTTP 500 through the generic handler; needs testing)
• Whether lowering `REGEX_TIMEOUT_SECONDS` is advisable in shared deployments, and how the timeout behaves with batch and multi-process runs (not stated; needs testing)
• Who may send ad-hoc recognizers, given the FAQ says Presidio endpoints have no built-in authentication (deployment question)
• Whether per-recognizer `score_thresholds` is in the released 2.2.364 package: it is in the tagged code and docs but under `[unreleased]` in the changelog and absent from the live docs (release notes not re-read, github.com returned 403)
• How a request-level `score_threshold` should be used with recognizer-level thresholds in batch REST calls (precedence is documented only at the tag; needs testing)
• Recommended scores for weak patterns, and how a custom entity that overlaps a built-in one is resolved (not stated; needs testing)
• Context words with `NoOpNlpEngine`: the code warns the Lemma enhancer cannot use words from the text then, only explicit request context (analyzer_engine.py@2.2.364:114-122; behaviour needs testing)
• Accuracy and latency of typical custom recognizers (none published; developing recognizers page gives only a 100 ms guideline)
• Whether the live docs lag the tag for other features, since the live registry page and the tagged page differ
### R9
Summary: Presidio docs pages on adding and developing recognizers, the registry provider, tutorials (deny list, context, no-code, ad-hoc, allow list), decision process, FAQ and evaluation, plus repo files at tag 2.2.364 (Analyzer code, OpenAPI file, changelog).
Detail:
• https://presidio.dataprivacystack.org/analyzer/adding_recognizers/
• https://presidio.dataprivacystack.org/analyzer/developing_recognizers/
• https://presidio.dataprivacystack.org/analyzer/recognizer_registry_provider/
• https://presidio.dataprivacystack.org/analyzer/languages/
• https://presidio.dataprivacystack.org/analyzer/decision_process/
• https://presidio.dataprivacystack.org/api/analyzer_python/
• https://presidio.dataprivacystack.org/tutorial/06_context/
• https://presidio.dataprivacystack.org/tutorial/08_no_code/
• https://presidio.dataprivacystack.org/tutorial/09_ad_hoc/
• https://presidio.dataprivacystack.org/tutorial/13_allow_list/
• https://presidio.dataprivacystack.org/faq/
• https://presidio.dataprivacystack.org/evaluation/
• https://presidio.dataprivacystack.org/
• https://presidio.dataprivacystack.org/project_transition/
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/CHANGELOG.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/analyzer/recognizer_registry_provider.md
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/api-docs/api-docs.yml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/app.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/pyproject.toml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/analyzer_engine.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/analyzer_request.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/analysis_explanation.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/pattern.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/pattern_recognizer.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/recognizer_result.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/score_thresholds.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/default_recognizers.yaml
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/context_aware_enhancers/lemma_context_aware_enhancer.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/recognizer_registry/recognizer_registry.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/recognizer_registry/recognizers_loader_utils.py
• https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/presidio_image_redactor/image_redactor_engine.py

## Reviewer notes
• Sources and method: code and repo docs were read in a shallow clone at /tmp/presidio_probe (tag 2.2.364, commit 779dbd286d5ef4d1fbe2514275fb1bce358f2417, `git describe` = 2.2.364, committed 2026-07-22); all line numbers refer to that checkout. Live docs pages were read as raw text with benchtest/tools/fetch_text.py on 2026-10-09 and saved under benchtest/scratchpad/drafter/pd_b/pages/. WebFetch was not used, so no number or quote comes from a summarising fetch.
• Quotes and line cites were checked mechanically (scratchpad/drafter/pd_b/verify_quotes.py and verify_cites.py): every double-quoted passage of 12 characters or more was found in the fetched pages or in the clone, and every file@2.2.364:line cite exists. The one exception flagged by the quote script is the curl example with escaped quotes, which matches the live page.
• Not read: the GitHub release page and notes for 2.2.364 (github.com returns 403 here), so no release-note fact is used; CHANGELOG.md [unreleased] is mentioned only as a flag. The data-privacy-stack/presidio-research repo (README, tags) was not readable; its facts rest on the Presidio docs evaluation, FAQ and developing-recognizers pages and are [To be verified] where they go further. The live OpenAPI page (api-docs.html) is rendered by script and returned no text, so the tagged docs/api-docs/api-docs.yml was used instead.
• Corrections to the brief: (1) the brief says presidio-structured has release title "Release 2.2.364 / 0.0.60"; at the tag presidio-structured/pyproject.toml says version 0.0.8 and 0.0.60 is the presidio-image-redactor version (presidio-image-redactor/pyproject.toml line 7). (2) The brief's note that per-recognizer score thresholds sit only under CHANGELOG [unreleased] needs a qualifier: the code (score_thresholds.py, analyzer_engine.py) and docs/analyzer/recognizer_registry_provider.md at the tag already implement it, but the live registry and Python API pages do not mention it; written as two bullets in PD6 R4, labelled with the repo pin and not as develop/unreleased because the content is in tagged code.
• Source conflicts carried (two bullets each): C3 Python versions (package metadata 3.10 to 3.14 versus live installation page 3.10 to 3.13; PD4 R4, PD5 R4); live Python API text for score_threshold versus tagged docstring (PD6 R4); live registry page without score_thresholds versus tagged docs (PD6 R4); Concepts page says StructuredEngine "is responsible for detecting PII entities" versus code where detection is in the analysis builders (PD5 R4); image-redactor page points to an API spec for the Image Redactor REST API versus the tagged OpenAPI file with no /redact path (PD4 R4); OpenAPI AnalyzeRequest omits allow_list, allow_list_match and regex_flags that the service reads (PD6 R6); REST image redactor uses score_threshold 0.4 on multipart uploads and no threshold on JSON (PD4 R5).
• Inferences worth a second look: (a) PD4 R6, a JSON REST request probably cannot set the fill colour because colour is read from the form field `data`; (b) PD5 R4, `replace` with no `new_value` probably returns "<None>" inside presidio-structured because the entity type is not in the operator params; (c) PD4 R4, the image-redactor container sets analyzer config env vars that the package code never reads; (d) PD6 R8, HTTP 500 for invalid ad-hoc regex or language mismatch is read from app.py, not run. None was executed.
• Applied the brief literally: the "out of purpose" bullets (prompt injection, harmful content, topics) are labelled [Documented] and rest on the home page module list; strictly this is a scope statement drawn from what the page lists, not a sentence that says "not a prompt-injection tool". Change to [Inferred] or [Not disclosed] if CP1 prefers.
• Mixed-source facts were split into separate bullets (docs page versus repo file) so each carries one label; the 4 files and 19 labelled items in the DICOM sample set are my count from ground_truth.json, not a vendor figure.
• Published numbers: the only figures found for any of PD4, PD5 or PD6 are the DICOM notebook results (precision and recall 1.0 on four sample files; recall 0.2 on one image with padding_width=1) and the 100 ms per 100 tokens guideline for recognizer authors. Both are written as demonstrations or advice, not as accuracy or latency claims. Notebook 4 and 5 statements from the evaluation page are PD1 material and were not used here.
• CP1 question on PD5 (column or inventory only): facts for the decision. For a column: it reuses the Analyzer and Anonymizer on JSON and table data that can sit on the AI data path (retrieved records, tool-call arguments and results), and it adds logic not in PD1 or PD2 (per-column majority-vote entity mapping, JSON key names used as context). For inventory only: it is a Python package only with no REST service, Docker image or CLI at the tag (version 0.0.8, alpha in 2024, no current maturity label); the docs describe dataset de-identification and never mention LLM traffic; it transforms whole cell values, so it cannot edit PII inside free text; lists of objects in JSON need a hand-written map; the detection and operator behaviour it relies on is already covered by PD1 and PD2. Tests for it need only a small Python harness. No decision is taken here.
• Other notes: DICOM docs say metadata is not scrubbed, while the code uses metadata values to build a PERSON deny list for the pixel text; these do not conflict but are easy to misread. The adding-recognizers page says the LLM-based recognizer "uses LangExtract with Ollama (local models)" while the brief lists Azure OpenAI as a provider; not used in these columns, left for PD1. The ellipsis character is used inside quotes for omissions, as the format allows; Summaries are ASCII.
