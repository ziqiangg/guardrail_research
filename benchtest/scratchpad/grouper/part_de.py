# -*- coding: utf-8 -*-
"""Sections D (changes against v2) and E (suggested first group, open items, builder notes) of groups_v3.md."""


def part_de(mem, G, ORDER, NMULTI, USED, ADD_BULLET, CARRY):
    L = []
    n = len(ORDER)
    L.append("## D. Changes against v2")
    L.append("")
    L.append(f"v2 had 24 groups (6 multi-product, 18 single-product). v3 has {n} groups ({NMULTI} multi-product, {n - NMULTI} single-product). "
             "A multi-product group has members from two or more different products. Every sheet 3 column E to BN is in at least one group (section C).")
    L.append("")
    L.append("**D1. v2 to v3 identifiers**")
    L.append("")
    L.append("| v2 | v3 | What happened |")
    L.append("|---|---|---|")
    rows = [
        ("C1 PII, input", "C1", "Kept; members added: AH, AI, AN, AP, AX, BL (E, K, AF stay)"),
        ("C2 PII, output", "C2", "Kept; members added: AH, AI, AN, AP, AY, BL (E, L, AF stay)"),
        ("C3 Harmful content, input", "C8", "Kept; members added: AT, BD (G, V, AA, AG stay)"),
        ("C4 Harmful content, output", "C9", "Kept; members added: AU, BD (H, W, AA stay)"),
        ("C5 Jailbreak and prompt attack, input", "C10", "Kept; members added: AV, BE, BF (F, AB, AG stay)"),
        ("C6 Off-topic", "C12", "Kept as it was; no later product fits"),
        ("C7 Dialog flow control (J)", "C15", "Single; renumbered"),
        ("C8 Retrieval chunk filtering (M)", "C16", "Single; renumbered"),
        ("C9 Regex blocklist, input (N)", "C3", "Became multi-product: now with E, AM, AO, BI, BK, BM"),
        ("C10 Regex blocklist, output (N)", "C4", "Became multi-product: same members as C3, output side"),
        ("C11 Context-bloat (P)", "C17", "Single; renumbered"),
        ("C12 Output injection (O)", "C18", "Single; renumbered, cells as in v2. BH and BJ were checked and not grouped with O"),
        ("C13 Tool-call validation (Q)", "C19", "Single; unchanged number"),
        ("C14 Tool-result validation (R)", "C20", "Single; renumbered"),
        ("C15 Execution-level custom action rails (U)", "C21", "Single; renumbered"),
        ("C16 Grounded fact-checking (S)", "C22", "Single; renumbered"),
        ("C17 Self-consistency hallucination (T)", "C23", "Single; renumbered"),
        ("C18 Multimodal input (X)", "C13", "Became multi-product: now with AS (image content safety)"),
        ("C19 Multimodal output (X)", "C24", "Single; renumbered"),
        ("C20 Code-interpreter abuse (Y)", "C25", "Single; renumbered"),
        ("C21 Custom policy, input (Z)", "C26", "Single; renumbered"),
        ("C22 Custom policy, output (Z)", "C27", "Single; renumbered"),
        ("C23 System-prompt leakage (AD)", "C28", "Single; renumbered"),
        ("C24 Refusal detection (AE)", "C29", "Single; renumbered"),
        ("new", "C5, C6", "Reversible tokenisation (encrypt side) and token restore (decrypt side): AJ, AQ, BN"),
        ("new", "C7", "PII and sensitive-text detection and redaction in images: AK, AR, BC"),
        ("new", "C11", "Prompt-injection detection in model output, tool output and retrieved text: AW, BE, BF"),
        ("new", "C14", "Sensitive-data detection and masking in tables and records: AL, AN, AP"),
        ("new", "C30 to C34", "Single-product: BB documents, AZ and BA malicious URLs, BG goal hijacking, BH and BJ insecure code (one Purple Llama engine)"),
    ]
    for a, b, c in rows:
        L.append(f"| {a} | {b} | {c} |")
    L.append("")
    L.append("**D2. Other changes**")
    L.append("")
    L.append("- Merges and moves: BK (hidden Unicode characters) and BI (fixed regex scanner) join the rule-based pattern groups C3 and C4 because their ground truth is a deterministic rule; AI, AL, AN and AP are placed where their input object matches (text, tables).")
    L.append("- Input and output stay separate (docx criteria, R002) for text, tokenisation versus restore, harmful content, and URLs; images are one group (C7) because AK, AR and BC have no direction flag and the test inputs do not differ (left open for the user).")
    L.append("- The C7 reasoning (no direction flag, one group) also applies to AS: it appears only in C13, and its use on model-generated images has no comparator, so there is no output-side row.")
    L.append("- A column that takes any string (for example AH, AN, BD, BE) is listed in each side it applies to, as R002 requires.")
    L.append("- Marker bullet: reworded to Single-product: no comparator among the ten products yet (main ruling, queue.md groups_v3); the build matches only the prefix Single-product:, so the coverage panel is unaffected.")
    L.append(f"- Refs: v2 cells without a Refs line now have one ({len(USED)} cells carried from v2); every text cell in v3 ends with a Refs line.")
    L.append("- Carried rows keep their v2 bullets; cross-references to renumbered groups were updated (C24, C26, C27) and two inputs bullets were added (C25 with CyberSecEval, C29 with Litmus).")
    L.append("- Bench content in new or changed rows is worded as proposals (R032): Suggested, Possible, could, would be needed. Rows carried from v2 keep their v2 wording.")
    L.append("- The v2 section Rewrite check is not carried: the word-count and format checks are run by a script kept in the grouper scratchpad.")
    L.append("- Licence and terms constraints (Google AUP, Cloak Terms 3.4.7, Llama 4 use policy, Together terms, OpenAI and Gemini embedder terms) are listed as open items where they bear on a group; none is decided.")
    L.append("")
    L.append("## E. Suggested first group, open items and builder notes")
    L.append("")
    L.append("**E1. Which group to test first (a suggestion, not a decision)**")
    L.append("")
    L.append("- Suggestion: C1 (input-level PII and sensitive-data detection and masking), then C2, which reuses its data.")
    L.append("- Reasons for C1: it has the widest membership (9 functions, joint widest with C2, on three documented independent engines, AWS, Presidio and SDP; whether Cloak reuses Presidio is undisclosed, BL R4); "
             "the ground truth (entity type and span) needs a harmonised entity subset but less taxonomy judgement than the harmful-content groups; "
             "three members need no account (AH, AI, and K over the Presidio backend); the same labelled data could seed C2, C5, C6, C7 and C14.")
    L.append("- Cautions: the entity lists differ, so a harmonised subset is needed; AF, AX and K reuse the AF/E, AX/AN and K/AH backends; BL may reuse Presidio recognisers (BL R4, inferred); BL is gated and Cloak Terms clause 3.4.7 is open.")
    L.append("- Alternative: C10 (input-level jailbreak and prompt-attack detection) has six functions, scored outputs for AUPRC, and a possible attack source in CyberSecEval (3k) with 251 English and 1,004 translated cases. It needs harmless look-alike messages that Meta did not publish, and definitions differ across products.")
    L.append("- C8 (harmful content) has several members with probability outputs (AA, BD, V if extracted), but its taxonomies differ most; it could follow.")
    L.append("")
    L.append("**E2. Recorded open items that bear on groups (listed, not decided)**")
    L.append("")
    L.append("| Item | Where recorded | Groups it touches |")
    L.append("|---|---|---|")
    L.append("| Cloak Terms clause 3.4.7 (benchmarking), R039 | BL, BM, BN R8; 3l (e) | C1, C2, C3, C4, C5, C6 |")
    L.append("| Google AUP testing clause (R025), recorded in AT, AU, AV, AW, AZ, BA, BC; not in AN, AP, AX, AY, BB | AT R8 and the others named | C1, C2, C7, C8, C9, C10, C11, C14, C30, C31, C32 |")
    L.append("| Google Cloud AUP limits on explicit or violent test images (not the testing clause) | AS R7, AS R8 | C13 |")
    L.append("| Llama 4 use policy and licence gate, 700M MAU clause | BE R8, BF R8; 3j (f) | C10, C11 |")
    L.append("| Together terms and trace retention | BG R8; BI R8 (experimental scanners); 3j (f) | C33, C3, C4 |")
    L.append("| OpenAI, Gemini and Gemma embedder terms for test text | BD R8; 3i (c) | C8, C9 |")
    L.append("| EU licence clause for the multimodal Llama Guard models | X R8 | C13, C24 |")
    L.append("| Semgrep licence and Code Shield terms | BH R8, BJ R8; 3j (f) | C34 |")
    L.append("")
    L.append("Recorded user rulings (decided, not open): R025 ruling 2, Preview features are tested with synthetic data only. It names Model Armor Preview features (BC); applying it to the AR face detector (AR R1) is a reading. It bears on C7.")
    L.append("")
    L.append("**E3. Notes for the sheet 4 builder (not done here)**")
    L.append("")
    L.append(f"- build_groups_sheet.py assumes 24 rows, six comparison groups, 29 function columns (E to AG) and reads groups_v2.md. For v3 it would need: {n} rows, {NMULTI} comparison groups, "
             "62 function columns (E to BN), the new file name, and extra totals for the new product prefixes. verify_groups_apply.py would change likewise.")
    L.append("- The coverage panel counts a group row by the substring of each sheet 3 header in column B, so every header must stay a unique substring (checked by the script).")
    L.append("")
    return L
