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
• The tagged code contains NoOpNlpEngine, per-recognizer `score_thresholds` and `BatchDeanonymizeEngine` while `CHANGELOG.md@2.2.364` still lists them under its unreleased heading, above 2.2.363 **[Documented: repo data-privacy-stack/presidio@2.2.364]**
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
Summary: **Hides whatever spans it is given.** Built-in one-way operators replace, redact, hash, mask, run custom code, keep a value, or, with an Azure extra, generate a realistic surrogate. The default is replace with the entity type in angle brackets. It acts only on the spans it receives. **[Documented]**
Detail:
• Default operator: `DEFAULT = "replace"` (`anonymizer_engine.py@2.2.364:16`); `__check_or_add_default_operator` adds it when the operator map is empty or lacks a `DEFAULT` entry (line 106 calls it) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Docs note: "The replacing value will be the entity type e.g.: <PHONE_NUMBER>" (Presidio docs, anonymizer page) **[Documented]**
• Code: `Replace` returns `return f"<{params.get('entity_type')}>"` when `new_value` is empty (`replace.py@2.2.364:18`); this settles the default replacement string left open in the NeMo Guardrails PII columns **[Documented: repo data-privacy-stack/presidio@2.2.364]**
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
• Entity types are plain strings: the REST example uses `NAME`, `FIRST_NAME` and `LAST_NAME`, which the Analyzer does not emit (Presidio docs, anonymizer page) **[Documented]**
• No direction flag, prompt role or conversation input exists, so one column covers prompts and responses and no system or user prompt is needed **[Inferred]**
• Presidio's OpenAI sample uses it on chat input: the toolkit "anonymizes Personally Identifiable Information (PII) in the messages sent to the LLM" (Presidio docs, Data Protection toolkit for OpenAI page) **[Documented]**
• LiteLLM: "This will mask the input going to the llm provider" (Presidio docs, not LiteLLM docs) **[Documented]**
• LiteLLM can mask only the logged copy: "Only apply PII Masking before logging to Langfuse, etc." and "Not on the actual llm api request / response." (same page) **[Documented]**
• Applying the Anonymizer to model replies, retrieved passages or tool results is the same call on a different string; no Presidio page shows it on replies **[Inferred]**
• Images and tables have their own modules (image redaction column and structured-data column); this column is for text strings **[Documented]**
### R4
Summary: **Operators applied to detected spans.** A factory holds the built-in operators; the engine resolves overlaps, then applies the operator set for each entity type and falls back to replace. Python package or REST service on GHCR images. MIT licence, now under the Data Privacy Stack community. **[Documented]**
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
• Detecting the PII is the Analyzer column; one-way operators are the anonymisation column **[Documented]**
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
Summary: **AES-CBC with a random IV per entity.** Encrypt returns URL-safe base64 of the IV plus ciphertext; decrypt reverses it with the same 128, 192 or 256-bit key. Python engines, a batch engine and a REST route exist. MIT licence, now under the Data Privacy Stack community. **[Documented]**
Detail:
• Cipher: """Advanced Encryption Standard (aka Rijndael) en/decryption in CBC mode.""" (`aes_cipher.py@2.2.364:9`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
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
• REST: the Flask service on port 3000 serves `POST /deanonymize`; the docs example sends the key in the JSON body, `"key": "WmZq4t7w!z%C&F)J"` (Presidio docs, anonymizer page) **[Documented]**
• Dependency: `"cryptography (>=48.0.1,<49.0.0)"` (`presidio-anonymizer/pyproject.toml@2.2.364:26`); the changelog records "Bumped `cryptography` lower bound to `>=48.0.1` to resolve GHSA-537c-gmf6-5ccf" (`CHANGELOG.md@2.2.364:34`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
• Version: `presidio_anonymizer` is `version = "2.2.364"` (`presidio-anonymizer/pyproject.toml@2.2.364:7`); Python: live installation page 3.10 to 3.13 (read 2026-10-09) versus 3.14 added in `docs/installation.md@2.2.364:24` (source conflict C3) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
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
• Token size: the docs samples turn the 10-character name "James Bond" (start 11, end 21 in the encrypt tutorial) into a token spanning start 11 to end 55 (anonymizer page), 44 characters **[Inferred]**
• Accuracy, latency or throughput figures for encrypt and decrypt (checked the anonymizer page, encrypt and decrypt tutorial and sample, FAQ and evaluation page) **[Not disclosed]**
### R6
Summary: **Key, token text and token offsets.** Required are the same AES key used to encrypt, the text holding the tokens, and each token's start, end and entity type. The REST route takes these as JSON. The caller supplies and holds the key. **[Documented]**
Detail:
• Python call: `engine.deanonymize(text=anonymized_text, entities=anonymized_entities, operators={"DEFAULT": OperatorConfig("decrypt", {"key": crypto_key})})` (Presidio docs, encrypt and decrypt tutorial) **[Documented]**
• The entities come from the earlier anonymize result: "Fetch the anonynized entities from the result." (tutorial, spelling as printed) **[Documented]**
• REST payload: `text`, `deanonymizers` (`{"PERSON": {"type": "decrypt", "key": ...}}`) and `anonymizer_results` with `start`, `end`, `entity_type` (Presidio docs, anonymizer page) **[Documented]**
• The API spec marks `text`, `anonymizer_results` and `deanonymizers` as required (`docs/api-docs/api-docs.yml@2.2.364:470-480`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**
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
