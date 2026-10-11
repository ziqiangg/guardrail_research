# -*- coding: utf-8 -*-
# Rationale per group: four criteria marked with a tick or a cross, plus candidates checked and left out.
# Each entry: dict(crit=[(label, mark, text)], left=[...], terms=[...])  (terms are recorded open items only)
Y, N = "✓", "✗"

R = {}

R["C1"] = dict(
 crit=[("Test inputs", Y, "Single user messages carrying labelled PII; every member accepts a string (E R3, K R3, AF R3, AH R3, AI R3, AN R3, AP R3, AX R3, BL R3)."),
       ("Ground truth", Y, "Entity type and span per text, plus expected masked text; entity lists differ, so a harmonised subset is scored (E R2, K R2, AF R2, AH R2, AN R2, AX R2, BL R2)."),
       ("Comparable metrics", Y, "Detection and false-positive rates per entity type, and masking correctness, are computable from every output shape (AH R5, AN R5, AP R5, AX R5, BL R5, E R5, K R5, AF R5)."),
       ("Minimum architecture", Y, "A text harness with one adapter per product; no RAG, agent or tool execution is needed (E R7, K R7, AH R7, AN R7, AX R7, BL R7).")],
 left=["AO, AM, BM: authored detectors, so the ground truth is the author's rule set, not PII types (see C3).",
       "BI: fixed regex shapes, no entity spans (see C3).",
       "AJ, AQ, BN: ground truth is a restored value, not a masked one (see C5 and C6).",
       "AK, AR, BC: test inputs are images (see C7). AL: test inputs are tables (see C14; AN and AP also appear there).",
       "M: retrieval-level chunk checks, a different object and rail (see C16)."],
 terms=["Cloak Terms clause 3.4.7 (benchmarking) for BL: open (BL R8).",
        "Google AUP testing clause (R025) is recorded in Model Armor columns AT to AW, AZ, BA and BC, not in AN, AP or AX: whether it bears here is open.",
        "Sentinel (AF) is closed beta with Singapore-IP access (AF R7)."],
)
R["C2"] = dict(
 crit=[("Test inputs", Y, "Model responses carrying labelled PII, scripted or generated; each member accepts a response string (E R3, L R3, AF R3, AH R3, AI R3, AN R3, AP R3, AY R3, BL R3)."),
       ("Ground truth", Y, "Same entity and span labels as C1, plus the final user-visible text (L R5, AY R2, AF R3)."),
       ("Comparable metrics", Y, "Same detection, false-positive and masking measures as C1 (AH R5, AN R5, AY R5, L R5)."),
       ("Minimum architecture", Y, "Scripted or stub-LLM responses into the same adapters; AY uses the response method (AY R7, L R7).")],
 left=["AG: generic Bedrock moderation, not a PII function (C8, C10).",
       "Reversible and image functions follow C5, C6 and C7."],
 terms=["Cloak Terms clause 3.4.7 for BL: open (BL R8).",
        "Google AUP testing clause not recorded in AN, AP or AY: open."],
)
R["C3"] = dict(
 crit=[("Test inputs", Y, "Strings that match or miss a defined rule; every member runs on any string (N R3, AM R3, AO R3, BI R3, BK R3, BM R3, E R3)."),
       ("Ground truth", Y, "Expected match comes from the rule definition, so it is deterministic; BI and BK use their documented fixed rules (N R2, AM R2, AO R2, BI R2, BK R2, BM R2, E R4)."),
       ("Comparable metrics", Y, "Exact agreement, false-positive and false-negative rates against the rules, and latency (N R5, AM R5, AO R5, BI R5, BK R5, BM R5)."),
       ("Minimum architecture", Y, "A rule loader plus one adapter per product; no detection model is needed for N, BI or BK, and AM loads a spaCy model with its Analyzer (N R7, AM R7, BI R7, BK R7, AO R7).")],
 left=["AH: built-in recognizers whose truth is a PII type, not an authored rule (C1).",
       "BM LLM entity: a Beta few-shot model, not rule matching (BM R4).",
       "M: matches on chunks, a retrieval-level rail (C16)."],
 terms=["Cloak Terms clause 3.4.7 for BM: open (BM R8)."],
)
R["C4"] = dict(
 crit=[("Test inputs", Y, "Scripted responses that match or miss a rule; N has a separate output check, the others take any string (N R3, AM R3, AO R3, BI R3, BK R3)."),
       ("Ground truth", Y, "Deterministic from the rule definitions (N R2, AM R2, AO R2, BK R2)."),
       ("Comparable metrics", Y, "Exact agreement, false-positive and false-negative rates, latency (N R5, AM R5, AO R5, BI R5, BK R5)."),
       ("Minimum architecture", Y, "Stub LLM with scripted text and the C3 adapters (N R7, 3c Tools).")],
 left=["Output-level PII masking is C2; payload scanning of output is C18 and code scanning is C34."],
 terms=["Cloak Terms clause 3.4.7 for BM: open (BM R8)."],
)
R["C5"] = dict(
 crit=[("Test inputs", Y, "User messages with synthetic entities to tokenise before the model (AJ R3, AQ R3, BN R3)."),
       ("Ground truth", Y, "Original value and span per entity; expected: no raw value left in the outgoing text (AJ R1, AQ R1, BN R1)."),
       ("Comparable metrics", Y, "Residual-PII rate and token format conformity apply to all three (AJ R5, AQ R5, BN R5)."),
       ("Minimum architecture", Y, "Harness plus key setup per product: caller key, KMS wrapped key, Secrets Manager secret (AJ R7, AQ R7, BN R7).")],
 left=["AI, AP, BL: one-way operators; there is nothing to restore (C1).",
       "AJ with AH: the Analyzer finds entities for AJ, so detection is C1."],
 terms=["Cloak Terms clause 3.4.7 for BN: open (BN R8)."],
)
R["C6"] = dict(
 crit=[("Test inputs", Y, "Mock model replies that echo, edit or drop tokens, plus wrong-key cases (AJ R3, AQ R3, BN R3)."),
       ("Ground truth", Y, "Expected restored text with original values; failure expectations are open (AJ R8, AQ R8, BN R8)."),
       ("Comparable metrics", Y, "Restore exactness, partial-restore rate and failure handling (AJ R5, AQ R5, BN R5)."),
       ("Minimum architecture", Y, "Harness replaying replies, same key handling as C5 (AJ R6, AQ R6, BN R6).")],
 left=["The encrypt side is C5: inputs and ground truth differ (docx section 4), and each product exposes separate encrypt and restore operations (AJ R3, AQ R8, BN R3)."],
 terms=["Cloak Terms clause 3.4.7 for BN: open (BN R8)."],
)
R["C7"] = dict(
 crit=[("Test inputs", Y, "Images carrying known text with labelled PII, plus clean images (AK R3, AR R3, BC R3)."),
       ("Ground truth", Y, "Entity type and box per text item; clean images expect none (AK R2, AR R2, BC R2)."),
       ("Comparable metrics", Y, "Per-entity detection, box overlap, residual PII after redaction (AK R5, AR R5, BC R5)."),
       ("Minimum architecture", Y, "Image loader and one adapter per product; all use OCR then an analyser (AK R4, AR R4, BC R4).")],
 left=["AS: judges whole-image safety, not sensitive text (see C13).",
       "BB: files, whose embedded images are not screened (see C30).",
       "AR object detectors (faces, passports) have no counterpart in AK or BC and are reported apart."],
 terms=["Preview features (AR faces, BC): synthetic data only (R025 ruling 2).",
        "Google AUP testing clause recorded for BC (BC R8) and not for AR: open."],
)
R["C8"] = dict(
 crit=[("Test inputs", Y, "Single-turn user prompts, harmful and benign (G R3, V R3, AA R3, AG R3, AT R3, BD R3)."),
       ("Ground truth", Y, "Binary harmful label per prompt; category mapping only where taxonomies overlap (G R2, V R2, AA R2, AG R2, AT R2, BD R2)."),
       ("Comparable metrics", Y, "True-positive, false-positive and false-negative rates at each decision point; sweeps only where probabilities exist (AA R5, BD R5, AT R5)."),
       ("Minimum architecture", Y, "Prompt harness with adapters: NeMo rail, GPU Llama Guard, Sentinel key, Google template, local LionGuard (G R6, V R7, AA R7, AT R7, BD R7).")],
 left=["AB, AV, BE, BF: prompt attacks, a different threat and label (C10).",
       "X, AS: image inputs (C13). Z: author-defined taxonomy (C26). Y: S14 abuse labels (C25).",
       "Litmus (3n) is an evaluation tool, not a column: its Undesirable Content test names could be a theme list only."],
 terms=["Google AUP testing clause for AT: open (AT R8).",
       "BD embedder terms (OpenAI, Gemini, Gemma) and licence texts: open (BD R8).",
       "Sentinel closed beta (AA R7, AG R7)."],
)
R["C9"] = dict(
 crit=[("Test inputs", Y, "Model responses to benign and harmful prompts; H and W also need the prompt (H R3, W R3, AA R3, AU R3, BD R3)."),
       ("Ground truth", Y, "Binary unsafe label judged on the response; category mapping where taxonomies overlap (H R2, W R2, AA R2, AU R2, BD R2)."),
       ("Comparable metrics", Y, "Same rates as C8 at each decision point (H R5, W R5, AA R5, AU R5, BD R5)."),
       ("Minimum architecture", Y, "Scripted-response harness with the C8 adapters on the response path (H R7, W R7, AU R7, BD R7).")],
 left=["AG: Sentinel lists it input only (AG R3).",
       "X: image-plus-text responses (C24). Z: custom taxonomy (C27)."],
 terms=["Google AUP testing clause for AU: open (AU R8).",
        "BD embedder terms: open (BD R8)."],
)
R["C10"] = dict(
 crit=[("Test inputs", Y, "Single-turn jailbreak, injection and benign prompts (F R3, AB R3, AG R3, AV R3, BE R3, BF R3)."),
       ("Ground truth", Y, "Binary attack or benign label under one agreed definition, though definitions differ (F R2, AB R2, AG R2, AV R2, BE R2, BF R2)."),
       ("Comparable metrics", Y, "Rates at each decision point; AUPRC for scored outputs only (AB R5, BE R5, BF R5, AV R5)."),
       ("Minimum architecture", Y, "Prompt harness with adapters: NeMo rail, Sentinel key, Google template, local Prompt Guard 2 and LlamaFirewall (F R7, AB R7, AV R7, BE R7, BF R7).")],
 left=["AW: output and tool side (C11). BG: needs the whole agent trace (C33). O: output payloads (C18).",
       "BI: two injection phrases only, in a rule-matching group (C3). AC: off-topic is a different label (C12).",
       "CyberSecEval (3k) and Garak are possible sources of attack examples, not columns."],
 terms=["Llama 4 licence gate and use policy for BE and BF: attack-prompt testing question open (BE R8, BF R8).",
        "Google AUP testing clause for AV: open (AV R8).",
        "Sentinel closed beta (AB R7, AG R7)."],
)
R["C11"] = dict(
 crit=[("Test inputs", Y, "Untrusted text from tools, retrieval or model replies, with and without injected instructions; BE and BF on model replies is undocumented (BE R3), and BF defaults to user and tool roles (AW R3, BE R3, BF R3)."),
       ("Ground truth", Y, "Injected or clean per text under one definition (AW R2, BE R2, BF R2)."),
       ("Comparable metrics", Y, "Rates at each decision point; AUPRC for BE and BF only (AW R5, BE R5, BF R5)."),
       ("Minimum architecture", Y, "Harness that places text on the tool or response path; three adapters (AW R7, BE R7, BF R7).")],
 left=["AV: user-prompt side (C10). BK: hidden characters, a rule match (C3).",
       "BB: files (C30). M: NeMo chunk checks for configured patterns and PII, not injection (C16)."],
 terms=["Llama 4 licence gate for BE and BF: open (BE R8, BF R8).",
        "Google AUP testing clause for AW: open (AW R8)."],
)
R["C12"] = dict(
 crit=[("Test inputs", Y, "Pairs of allowed-topic policy and user message (I R6, AC R6)."),
       ("Ground truth", Y, "On-topic or off-topic label relative to the stated policy (I R2, AC R2)."),
       ("Comparable metrics", Y, "Off-topic caught and on-topic blocked rates; AUPRC for AC only (I R5, AC R5)."),
       ("Minimum architecture", Y, "Harness that injects the policy per case into each product's format (I R7, AC R7).")],
 left=["No later product offers topic control: Model Armor lists no topic filter (AT R8 asks about topic enforcement).",
       "Z (custom-policy classification, C26 and C27) could carry an off-topic category, but its ground truth is an author-defined taxonomy and it has no system-prompt input (Z R2, AC R6)."],
 terms=["Sentinel closed beta (AC R7)."],
)
R["C13"] = dict(
 crit=[("Test inputs", Y, "User-supplied images, with a fixed neutral text for X (X R6, AS R6)."),
       ("Ground truth", Y, "(approximate) Safe or unsafe per image on a harmonised subset, sexual content and violence; X labels the hazard of the image-plus-text request and expects harmful-looking images with benign text to be ambiguous (X R2, X R7), while AS labels what the image depicts (AS R1, AS R2), so agreement on the subset is measured, not assumed."),
       ("Comparable metrics", Y, "Rates at the verdict; AS sweep over likelihood buckets (X R5, AS R5)."),
       ("Minimum architecture", Y, "Image loader with two adapters: GPU Llama Guard host and a Google DLP project (X R7, AS R7).")],
 left=["BC: sensitive-data screening of images (C7); image safety through an SDP template is inferred only (BC R2) [Inferred], so BC could become a C13 member if that is confirmed.",
       "X response side (C24) judges the response text, which AS cannot score.",
       "AS output side: AS R3 says the same call scores model-generated images; by the C7 reasoning (no direction flag, test inputs do not differ) it stays in C13 with no output-side row."],
 terms=["EU licence clause for X (X R8).",
        "Google Cloud AUP limits on explicit or violent test images for AS: which images are acceptable is open (AS R7, AS R8)."],
)
R["C14"] = dict(
 crit=[("Test inputs", Y, "Small tables with known PII columns and clean columns (AL R3, AN R3, AP R3)."),
       ("Ground truth", Y, "Cell-level PII labels; the column map follows from them (AL R2, AN R2)."),
       ("Comparable metrics", Y, "Cell detection, masking correctness and latency (AL R5, AN R5, AP R5)."),
       ("Minimum architecture", Y, "Table loader with two adapters: presidio-structured and an SDP table item (AL R7, AN R7, AP R7).")],
 left=["AH, AI: take one string, not a table; AL builds on them (C1).",
       "BB: file uploads are a different object (C30); BL file input is not studied in its columns."],
 terms=["Google AUP testing clause not recorded in AN or AP: open."],
)
SINGLES = {
 "C15": ("J", "I (C12): ground truth is a topic label on single messages, not intent or flow on multi-turn dialogues (J R2, I R2); no later product has a flow engine."),
 "C16": ("M", "AH, AN, BE and BI accept retrieved text as a string but have no retrieval rail (AH R3, AN R3, BE R3); the rail position, not the detector, is what C16 tests."),
 "C17": ("P", "N and BI (C3): ground truth is a pattern, not a size or entropy threshold (P R2)."),
 "C18": ("O", "BH and BJ: ground truth is insecure coding practice with CWE ids, not exploit payloads in output (O R2, BJ R2); Code Shield shows SQL injection only as a docs example (BH R3) and no XSS rule."),
 "C19": ("Q", "Y and BG: ground truth is abuse or goal labels, not structural validity against a declared schema (Q R2, Y R2, BG R2)."),
 "C20": ("R", "AW, BE, BF and BK check tool-result text for injection or hidden characters; R checks message linkage only (R R2, AW R3, BF R3)."),
 "C21": ("U", "BI custom scanners are a similar extension route but BI is evaluated here as regex blocking (BI R1); neither has a built-in detector to compare (U R1)."),
 "C22": ("S", "AD and AE: they compare against a system prompt or a user prompt, not retrieved evidence (S R2, AD R2, AE R2); no hallucination detector exists in later products."),
 "C23": ("T", "S (C22): ground truth is support by evidence, not self-consistency across resamples (T R2, S R2)."),
 "C24": ("X", "W (C9): test inputs are text prompt-response pairs, not image-plus-text pairs (W R3, X R3). AS (C13) scores images, not response text (AS R3)."),
 "C25": ("Y", "BH and BJ (C34): ground truth is insecure-code labels, not S14 abuse (BH R2, Y R2). G and V (C8): not S14 (V R2)."),
 "C26": ("Z", "G, V, AT (C8): their taxonomies are fixed; the Z ground truth is an author-defined taxonomy (Z R2, V R2, AT R2)."),
 "C27": ("Z", "H, W, AU (C9): same reason as C26; Z response checks need both turns (Z R3, H R2)."),
 "C28": ("AD", "BG (C33): ground truth is goal alignment of an action, not leakage of a system prompt (AD R2, BG R2). AC (C12): off-topic, not leakage. AG: input-side leakage attempts, not leaked output (AG R2)."),
 "C29": ("AE", "No later column scores refusals (AE R2); Litmus (3n) test pass conditions are refusal-based but Litmus is not a column."),
 "C30": ("BB", "BL and AN accept files (BL R3, AN R3) but their columns study text; BB is a screening call over file types (BB R2). C1 holds the text side."),
 "C31": ("AZ", "No other product's column checks link reputation (AZ R2); BB runs the same Model Armor URL filter on files (BB R2); C11 and C10 look at instruction text, not link reputation."),
 "C32": ("BA", "No other column examines URLs in responses (BA R2); AW checks injection text, not link reputation."),
 "C33": ("BG", "BE and BF (C10, C11): one message, no trace (BE R3, BF R3). AC (C12): checks prompt relevance, not agent actions (AC R3)."),
 "C34": ("BH", "O: ground truth is exploit payloads, not insecure coding practice (O R2, BJ R2); BH and BJ are one engine through two Purple Llama surfaces (BH R4)."),
}

SINGLE_TERMS = {
 "C24": "EU licence clause may apply to the multimodal Llama Guard models (X R8).",
 "C30": "Google AUP testing clause is not recorded for BB: open (BB R8).",
 "C31": "Google AUP testing clause is recorded for AZ: whether it bears on bench testing is open (AZ R8).",
 "C32": "Google AUP testing clause is recorded for BA: whether it bears on bench testing is open (BA R8).",
 "C33": "Together terms and trace retention are open (BG R8); Llama 4 licence terms: see 3j (f).",
 "C34": "Semgrep licence and Code Shield terms are recorded in 3j (f): open.",
}
