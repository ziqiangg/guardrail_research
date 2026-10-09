# Presidio: Summary preview (Checkpoint 2)

Generated from presidio_two_level.md on 2026-10-09. Format: `Rn` (words excluding the trailing label, top-level Detail bullets): Summary text. Limits: 45 words, R7 60.

## PD1: Presidio: PII detection in text (Analyzer)

- **R1** (35w, 8 bullets): **Finds PII in text and reports where.** The Analyzer runs recognizers over one string and returns each entity type with its position and a confidence score. Rewriting the text is left to the separate Anonymizer. **[Documented]**
- **R2** (40w, 26 bullets): **PII entity types, English by default.** The supported-entities page groups its types into Global, 18 country sections and a medical section. A default English setup loads pattern recognizers plus a spaCy name and place model. Detection is not guaranteed complete. **[Documented]**
- **R3** (38w, 12 bullets): **Any string, before or after the model.** The Analyzer takes one text field and a language per call and needs no system prompt or conversation history. The same call works on prompts, responses, retrieved passages and tool output. **[Inferred]**
- **R4** (43w, 43 bullets): **Rules plus a spaCy model.** Regex, checksum and context-word recognizers run beside a spaCy name model; scores are boosted by context, thresholded and de-duplicated. Optional extras add Stanza, transformers, GLiNER and language-model recognizers. MIT licence; the project is moving to a community organisation. **[Documented]**
- **R5** (44w, 31 bullets): **Spans and scores, no verdict.** Each hit has an entity type, start, end and a 0 to 1 score, plus an optional explanation. The default score threshold is 0. A vendor notebook reports F2 0.661 for default recognizers at threshold 0.4 on synthetic data. **[Documented]**
- **R6** (42w, 31 bullets): **Text and a language code; the rest is optional.** Callers can restrict entities, set a score threshold, pass an allow list, context words or per-request recognizers, and ask for the explanation. A spaCy model is needed locally; other languages need extra configuration. **[Documented]**
- **R7** (45w, 12 bullets): **Minimum setup:** pip install the Analyzer and a spaCy model, or run the GHCR image; no account or key is needed. Send labelled prompts and replies with known PII spans plus near-misses, compare returned spans per entity, sweep the score threshold, and score with presidio-research. **[Inferred]**
- **R8** (29w, 10 bullets): **Key open questions.** No recommended threshold or latency figure, which listed entities are active in a default install, per-entity accuracy, and retention at the Azure Health Data Services endpoint.
- **R9** (21w, 74 bullets): Presidio docs site pages, the Presidio repository at tag 2.2.364, the presidio-research repository at tag 0.3.2, and one Microsoft Learn page.

## PD2: Presidio: PII anonymisation and masking in text (Anonymizer)

- **R1** (38w, 10 bullets): **Rewrites detected PII with a chosen operator.** The Anonymizer takes text plus the Analyzer's spans and replaces, redacts, hashes, masks or keeps each entity. It also returns a list of the changes with positions in the new text. **[Documented]**
- **R2** (38w, 28 bullets): **Hides whatever spans it is given.** One-way operators replace, redact, hash, mask, run custom code, keep a value or, with an Azure extra, generate a realistic surrogate. The default is replace, writing the entity type in angle brackets. **[Documented]**
- **R3** (42w, 10 bullets): **Text plus the Analyzer's spans, from any source.** The call needs the original string, entity spans with scores, and an operator per entity type. It has no direction flag and no prompt context, so it works on prompts, responses and other strings. **[Inferred]**
- **R4** (39w, 22 bullets): **Operators applied to detected spans.** The engine resolves overlaps, then applies the operator set for each entity type, falling back to replace. Python package or REST service on GHCR images. MIT licence, moving to the Data Privacy Stack community. **[Documented]**
- **R5** (38w, 9 bullets): **Rewritten text plus a change list.** The result holds the new text and, for each entity, its type, start and end in the new text, the replacement and the operator used. There is no score or pass-fail field. **[Documented]**
- **R6** (41w, 12 bullets): **Text, spans and an operator map.** Required are the text and the Analyzer's spans with type, start, end and score; operators are optional, with a default entry. Each operator has its own parameters, and hash salts are the caller's to manage. **[Documented]**
- **R7** (48w, 10 bullets): **Minimum setup:** pip install the Analyzer, the Anonymizer and a spaCy model, or run both GHCR images; no account or key. Feed labelled texts with known PII through the Analyzer, anonymize with each operator, and check that no original value survives and that placeholders and offsets are right. **[Inferred]**
- **R8** (36w, 9 bullets): **Key open questions.** No accuracy or latency figures, REST support for the keep and Azure surrogate operators, the effect of space merging on adjacent names, offsets for non-BMP text, and what the Azure surrogate operator retains.
- **R9** (22w, 33 bullets): Presidio docs site pages, the Presidio repository at tag 2.2.364 and one commit on its main branch, and one Microsoft Learn page.

## PD3: Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt)

- **R1** (40w, 8 bullets): **Encrypts PII in text so it can be restored later.** The encrypt operator swaps each entity for AES ciphertext, and the Deanonymize engine or the decrypt operator reverses it with the same key. Presidio keeps no session state between calls. **[Documented]**
- **R2** (38w, 10 bullets): **Lets the model see tokens, then restores the real values.** Presidio documents three routes: AES encryption, a client-held mapping in a pseudonymization sample, and LiteLLM's restore of masked tokens in replies. All start from what the Analyzer detected. **[Documented]**
- **R3** (44w, 7 bullets): **Tokens plus their positions, wherever they reappear.** Deanonymize needs the text that holds the encrypted tokens, each token's start, end and entity type, and the key. It applies to model replies or any string that still carries the tokens. No prompt context is used. **[Inferred]**
- **R4** (44w, 21 bullets): **AES-CBC with a random initialisation vector per entity.** Encrypt returns URL-safe base64 of that vector plus ciphertext; decrypt reverses it with the same 128, 192 or 256-bit key. Python, batch and REST entry points exist. MIT licence, moving to the Data Privacy Stack community. **[Documented]**
- **R5** (35w, 8 bullets): **Restored text and an item list, no verdict.** The result holds the text with tokens swapped back to the originals plus one item per restored entity, and the REST route returns the same as JSON. **[Documented]**
- **R6** (42w, 12 bullets): **Key, token text and token offsets.** Required are the same AES key used to encrypt, the text holding the tokens, and each token's start, end and entity type. The REST route takes these as JSON. The caller supplies and holds the key. **[Documented]**
- **R7** (51w, 10 bullets): **Minimum setup:** pip install the Anonymizer, make a 16, 24 or 32 character key, encrypt labelled entities, decrypt, and compare with the originals. Then replay a mock model reply that echoes, edits or drops tokens, and try a wrong key and a damaged token, to see what restores and what fails. **[Inferred]**
- **R8** (35w, 7 bullets): **Key open questions.** What happens on a wrong key or a damaged token, how a real model treats the long tokens, no key-management guidance, and whether the batch deanonymiser and its REST coverage are release-ready.
- **R9** (18w, 28 bullets): Presidio docs site pages, the Presidio repository at tag 2.2.364, and the NVIDIA NeMo Guardrails page on Presidio.

## PD4: Presidio: PII detection and redaction in images (Image Redactor)

- **R1** (38w, 10 bullets): **Image redaction by OCR.** Presidio reads text in an image with OCR, runs the Analyzer on it, and paints solid boxes over words that match PII. A second engine handles medical DICOM pixels. The package is marked beta. **[Documented]**
- **R2** (45w, 13 bullets): **PII text that OCR can read.** Finds the same entity types as the Analyzer, in English by default, but only in text the OCR engine reads from the picture. Prompt-injection, harmful-content and topic checks are out of purpose. Coverage depends on which recognizers are enabled. **[Inferred]**
- **R3** (42w, 13 bullets): **Images, not text.** Takes a picture or DICOM file sent to or from a model, covering uploads and images in responses or tool results alike, with no system or user prompt needed. The REST service accepts a form upload or base64 JSON. **[Inferred]**
- **R4** (44w, 33 bullets): **OCR, then the Analyzer, then filled boxes.** Tesseract is the default OCR engine and Azure Document Intelligence the alternative. The OCR text goes to the default English Analyzer, and each matching word box is filled. MIT licence; ownership is moving to Data Privacy Stack. **[Documented]**
- **R5** (44w, 15 bullets): **No verdict; an image comes back.** Python returns the redacted image and, optionally, one box per redacted word with entity type, offsets, score and position. REST returns only the image. The score threshold is 0 in Python and 0.4 on the REST upload form. **[Documented]**
- **R6** (43w, 16 bullets): **An image plus optional fill, language and filters.** Needs the image, an OCR engine (Tesseract installed, or an Azure endpoint and key) and the Analyzer's English spaCy model. Optional inputs are fill colour, OCR confidence cut-off, entities, language, allow list and score threshold. **[Documented]**
- **R7** (42w, 11 bullets): **Minimum setup:** install the package, Tesseract and the English spaCy model, or pull the Docker image; the default OCR needs no account. Test with images of known text carrying labelled PII plus clean images, and for DICOM use the documented ground-truth route. **[Inferred]**
- **R8** (30w, 11 bullets): **Key open questions.** Accuracy on real screenshots and scans, non-English OCR, non-text PII, the two REST thresholds, JSON fill colour, request limits, Tesseract version in the image, and beta stability.
- **R9** (43w, 40 bullets): Presidio docs site pages (image redactor, getting started with images, installation, FAQ, evaluation, concepts, transition, samples, API spec), repo files at tag 2.2.364 (image redactor package, Dockerfile, tests, API spec), the licence, the presidio-research README at tag 0.3.2, and a Microsoft Learn page.

## PD5: Presidio: PII detection and anonymisation in structured data (tables and JSON)

- **R1** (44w, 7 bullets): **Finds PII columns or keys, then masks every value in them.** For a table or a JSON object, Presidio first works out which columns or keys hold which PII type, then applies Anonymizer operators to each value there. It ships as a Python package. **[Documented]**
- **R2** (41w, 16 bullets): **Same PII types as the Analyzer, decided per column or key.** Types and languages follow the enabled recognizers, English by default. Free text inside a table is listed as future work, and prompt-injection, harmful-content or topic checks are out of purpose. **[Inferred]**
- **R3** (43w, 10 bullets): **Parsed tables and JSON, not raw prompts.** Takes a pandas table or a JSON-like dict or list, so it fits retrieved records and tool outputs after parsing; it is not a prompt-text check. Same logic for inputs and outputs, no prompt context needed. **[Inferred]**
- **R4** (42w, 27 bullets): **Two steps over the Analyzer and Anonymizer.** A builder samples and analyses values to map each column or key to one entity type, then the engine applies Anonymizer operators to every value there. Package version 0.0.8, marked alpha, under the MIT licence. **[Documented]**
- **R5** (41w, 10 bullets): **A transformed table or object plus a column map.** Output is the anonymised table or dict; the analysis step returns a column-to-entity map with no per-cell findings or scores. The detection threshold defaults to 0 and the mixed-strategy cut-off to 0.5. **[Documented]**
- **R6** (41w, 10 bullets): **Data, an entity map and operators.** Needs a table or dict, a column-to-entity map (generated or hand-written) and operators keyed by entity with a default. Sampling, language, strategy and batch settings are optional. The Analyzer's spaCy model must also be installed. **[Inferred]**
- **R7** (43w, 10 bullets): **Minimum setup:** pip install presidio-structured and the English spaCy model, then run it on a small table and a JSON object with known PII columns and clean columns. No account is needed. Score the column map and the output cells separately against labels. **[Inferred]**
- **R8** (25w, 11 bullets): **Key open questions.** The default replace output, behaviour on non-text cells and odd column names, in-place mutation, majority-vote mapping errors, and throughput on large tables.
- **R9** (35w, 29 bullets): Presidio docs site pages (structured, getting started, home, installation, FAQ, evaluation, concepts, context tutorial, transition), repo files at tag 2.2.364 (structured package, Analyzer and Anonymizer code, changelog, licence) and the presidio-research README at tag 0.3.2.

## PD6: Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers)

- **R1** (38w, 8 bullets): **Add your own detectors.** Presidio lets you define new PII entity types with regex patterns, word lists and context words, as code, YAML or a per-request JSON recognizer. An allow list does the opposite and suppresses chosen matches. **[Documented]**
- **R2** (45w, 13 bullets): **Entity types you define yourself.** Detects whatever your regexes, word lists or code describe, such as IDs, titles or internal terms, one language per recognizer. Regexes and lists carry no meaning, so paraphrase is missed, and prompt-injection, harmful-content or topic checks are out of purpose. **[Inferred]**
- **R3** (43w, 9 bullets): **Plain text, same as the Analyzer.** A custom recognizer sees the string passed to the Analyzer, so it covers prompts, responses, retrieved text and tool inputs or outputs alike, with no system or user prompt needed. Request-level context words can come from metadata. **[Inferred]**
- **R4** (45w, 24 bullets): **Regex engine plus scores, with a context boost.** A pattern recognizer runs each regex over the text and gives hits the score you set (word lists default to 1.0); context words nearby can raise it. Over REST only regex and word-list recognizers can be sent. **[Documented]**
- **R5** (42w, 12 bullets): **Spans with the score you set.** A custom recognizer returns the usual Analyzer result: entity type, start, end and score. With the decision process on, the explanation names the pattern, regex, original score and context boost. The engine threshold defaults to 0. **[Documented]**
- **R6** (38w, 13 bullets): **Entity name, patterns or words, language and optional context.** A recognizer needs a supported entity, at least one scored regex or a deny list, and a language. Context words, regex flags, allow list and request-level settings are optional. **[Documented]**
- **R7** (42w, 10 bullets): **Minimum setup:** pip install presidio-analyzer and the English spaCy model, define a recognizer in Python or send an ad-hoc recognizer to a local analyzer service, then run labelled positive and negative strings. No account is needed. Score returned spans against labelled offsets. **[Inferred]**
- **R8** (33w, 8 bullets): **Key open questions.** REST error codes for a bad regex or language, server-side regex safety under concurrent requests, how request and recognizer thresholds combine in batch calls, and score choices for weak patterns.
- **R9** (40w, 34 bullets): Presidio docs pages on adding and developing recognizers, the registry provider, tutorials (deny list, context, no-code, ad-hoc, allow list), decision process, FAQ and evaluation, plus repo files at tag 2.2.364 (Analyzer code, OpenAPI file, changelog) and presidio-research at tag 0.3.2.

## Summaries changed in the merge

| Location | Words before | Words after | Reason |
|---|---|---|---|
| PD1 R2 | 36 | 40 | T20, T58: drop the own count and the unsupported '16 pattern recognizers' from the Summary (40 words) |
| PD1 R5 | 41 | 44 | T24, R014: figure keeps its setup qualifier (was 'default settings'; the notebook ran at threshold 0.4) (44 words) |
| PD1 R8 | 29 | 29 | T7: replaces 'a thin default entity set' (no bullet states it) and the three-listed-entities / cloud data-flow clauses now answered (29 words) |
| PD1 R9 | 17 | 21 | R9 Summary updated: adds the Microsoft Learn page cited for AHDS (T7) |
| PD2 R4 | 39 | 39 | entailment (T1 contradiction 1: FAQ 'has since transitioned' versus transition page 'in the process of transitioning'): the R4 Detail says the project is moving, so the Summary says moving, as in PD1 and PD4 |
| PD2 R6 | 41 | 41 | style 2: code identifier removed from a Summary |
| PD2 R8 | 30 | 36 | T30: the NONE-strategy question is answered (36 words) |
| PD2 R9 | 11 | 22 | R9 Summary updated: adds the main-branch commit (main Q3) and the Microsoft Learn page (T7) |
| PD3 R1 | 38 | 40 | T59: sentence now entailed by a same-row bullet (40 words) |
| PD3 R4 | 43 | 44 | style 2: abbreviation 'IV' removed from a Summary; entailment (as PD2 R4): the R4 Detail says transition, so the Summary says moving |
| PD3 R9 | 11 | 18 | R9 Summary updated: adds the NVIDIA page cited in R4 (T37) |
| PD4 R2 | 45 | 45 | T57 (R015): out-of-purpose statement is [Inferred] in every column (text unchanged, 45 words) |
| PD4 R5 | 44 | 44 | T58: absence sentence (which rested on [Not disclosed] bullets) replaced by threshold facts entailed by the REST and Python bullets (44 words) |
| PD4 R9 | 31 | 43 | R9 Summary updated: adds presidio-research (T12), the live API spec (T42) and the Microsoft Learn page (T7) |
| PD5 R2 | 41 | 41 | T57 (R015): out-of-purpose statement is [Inferred] in every column (text unchanged, 41 words) |
| PD5 R3 | 43 | 43 | style 2: class name 'DataFrame' removed from a Summary |
| PD5 R4 | 40 | 42 | T44 (optional in the resolution, applied): the package is marked alpha on the getting-started page (42 words) |
| PD5 R5 | 37 | 41 | T58, style 2: absence sentence (resting on [Not disclosed] bullets) replaced by two default values; 'DataFrame' removed (41 words) |
| PD5 R6 | 41 | 41 | style 2: class name 'DataFrame' removed from a Summary |
| PD5 R7 | 43 | 43 | style 2: class name 'DataFrame' removed from a Summary |
| PD5 R8 | 32 | 25 | T3 (R016): drops the CP1 clause; T44: drops 'maturity' (answered) (25 words) |
| PD5 R9 | 27 | 35 | R9 Summary updated: adds the getting-started page (T44) and presidio-research (T12) |
| PD6 R5 | 44 | 42 | T58: absence sentence replaced by the default threshold (entailed by the engine-threshold bullet) (42 words) |
| PD6 R8 | 31 | 33 | T13, T47: drops non-pattern logic over REST and per-recognizer threshold status (both answered) (33 words) |
| PD6 R9 | 35 | 40 | R9 Summary updated: adds presidio-research (T12) |
