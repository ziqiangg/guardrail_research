# -*- coding: utf-8 -*-
# One-off patch applied to data_rationale.py for the verifier fixes (kept for the audit trail).
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def rd(f): return open(f, encoding="utf-8").read()
def wr(f, s): open(f, "w", encoding="utf-8").write(s)


def sub(s, a, b, cnt=1):
    assert s.count(a) == cnt, (a, s.count(a))
    return s.replace(a, b)


r = rd("data_rationale.py")
r = sub(r, "AL: test inputs are tables (see C15; AN and AP also appear there).", "AL: test inputs are tables (see C14; AN and AP also appear there).")
r = sub(r, "M: retrieval-level chunk checks, a different object and rail (see C17).", "M: retrieval-level chunk checks, a different object and rail (see C16).")
r = sub(r, "no model is needed for N, AM, BI or BK (N R7, AM R7, BI R7, BK R7, AO R7)",
        "no detection model is needed for N, BI or BK, and AM loads a spaCy model with its Analyzer (N R7, AM R7, BI R7, BK R7, AO R7)")
r = sub(r, "M: matches on chunks, a retrieval-level rail (C17).", "M: matches on chunks, a retrieval-level rail (C16).")
r = sub(r, "code or payload scanning is C14.", "payload scanning of output is C18 and code scanning is C34.")
r = sub(r, "The encrypt side is C5 because its inputs and truth differ (R002 reading: prompt side versus response side).",
        "The encrypt side is C5: inputs and ground truth differ (docx section 4), and each product exposes separate encrypt and restore operations (AJ R3, AQ R8, BN R3).")
r = sub(r, "O: output payloads (C14).", "O: output payloads (C18).")
r = sub(r, " (AW R3, BE R3, BF R3).\"),\n       (\"Ground truth\", Y, \"Injected or clean per text under one definition",
        "; BE and BF on model replies is undocumented (BE R3), and BF defaults to user and tool roles (AW R3, BE R3, BF R3).\"),\n       (\"Ground truth\", Y, \"Injected or clean per text under one definition")
r = sub(r, "M: NeMo chunk checks for configured patterns and PII, not injection (C17).", "M: NeMo chunk checks for configured patterns and PII, not injection (C16).")
r = sub(r, 'left=["No later product offers topic control: Model Armor lists no topic filter (AT R8 asks about topic enforcement)."],',
        'left=["No later product offers topic control: Model Armor lists no topic filter (AT R8 asks about topic enforcement).",\n'
        '       "Z (custom-policy classification, C26 and C27) could carry an off-topic category, but its ground truth is an author-defined taxonomy and it has no system-prompt input (Z R2, AC R6)."],')
r = sub(r, '("Ground truth", Y, "Safe or unsafe per image on a harmonised subset: sexual content and violence (X R2, AS R2)."),',
        '("Ground truth", Y, "(approximate) Safe or unsafe per image on a harmonised subset, sexual content and violence; X labels the hazard of the image-plus-text request and expects harmful-looking images with benign text to be ambiguous (X R2, X R7), while AS labels what the image depicts (AS R1, AS R2), so agreement on the subset is measured, not assumed."),')
r = sub(r, 'left=["BC: reads text in images for sensitive data, not safety (C7).",\n       "X response side (C24) judges the response text, which AS cannot score."],',
        'left=["BC: sensitive-data screening of images (C7); image safety through an SDP template is inferred only (BC R2) [Inferred], so BC could become a C13 member if that is confirmed.",\n'
        '       "X response side (C24) judges the response text, which AS cannot score.",\n'
        '       "AS output side: AS R3 says the same call scores model-generated images; by the C7 reasoning (no direction flag, test inputs do not differ) it stays in C13 with no output-side row."],')
r = sub(r, 'terms=["EU licence clause for X (X R8)."],',
        'terms=["EU licence clause for X (X R8).",\n        "Google Cloud AUP limits on explicit or violent test images for AS: which images are acceptable is open (AS R7, AS R8)."],')
i = r.index('R["C14"] = dict('); j = r.index('R["C15"] = dict(')
r = r[:i] + r[j:]
r = sub(r, 'R["C15"] = dict(', 'R["C14"] = dict(')
r = sub(r, '"BL, BB: file uploads are a different object (C30)."]', '"BB: file uploads are a different object (C30); BL file input is not studied in its columns."]')
i = r.index("SINGLES = {"); j = r.index("\n}\n", i) + 3
new = '''SINGLES = {
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
'''
r = r[:i] + new + r[j:]
r = sub(r, ' "C33": "Together terms and trace retention are open (BG R8); Llama 4 licence terms: see 3j (f).",\n}',
        ' "C33": "Together terms and trace retention are open (BG R8); Llama 4 licence terms: see 3j (f).",\n "C34": "Semgrep licence and Code Shield terms are recorded in 3j (f): open.",\n}')
wr("data_rationale.py", r)
print("patched")
