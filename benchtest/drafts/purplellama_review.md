# Purple Llama workbook: fresh verifier review

Date of checks: 2026-10-10. Reviewer: gr-verifier (did not draft, triage, resolve or merge).

Inputs read:
- CLAUDE.md, drafts/README.md, lessons.md.
- Rulings R002, R003, R004, R007, R009, R011, R013, R015, R019, R020, R021, R030 and R032, plus the queue.md rows starting "purplellama".
- purplellama_two_level.md and purplellama_eval_tooling_final.md, read in full.
- purplellama_inventory_final.md, read in full (88 rows).
- purplellama_changes.md: sections 1 and 2 (head) and section 6, the rest compared by script.
- purplellama_resolutions_1.md: T35, T40, T41 and the Report. purplellama_resolutions_2.md: T67, T68 and the Report.
- purplellama_summaries_preview.md, compared by script.
- The originals purplellama_cols_a.md, _cols_b.md, _inventory.md and _eval_tooling.md, compared by script.

Scripts and outputs are in benchtest/scratchpad/verifier/purplellama/: diff_cols.py, check_ops.py, diff_inv.py, diff_ev.py, prev.py, cwe_count.py, harvest.py, urlcheck.sh, urls.tsv and url_check.txt.

## Verdict: PASS WITH FIXES

The merge is faithful and well logged:
- Every substantive change I could diff traces to an operation in the merger's ops files and to a reason code in purplellama_changes.md.
- The 29 changed Summaries are exactly the 29 logged ones, and the preview equals the final for all 63 Summaries and word counts.
- No known-wrong string survives (section 2).
- The checker gives 0 errors on the columns and the inventory, and the eval file parses with build_eval_sheet.parse_md (8 sections, in order).
- Of 186 distinct URLs, 0 fail for real (section 6).

Of 32 spot-checks, 30 match at source and 2 do not. The required fixes:
1. A factual error that survived from the draft: the PL7 R4 threshold bullet (MISMATCH at source).
2. One Summary not entailed by its own Detail: PL3 R4.
3. One cross-draft contradiction: inventory (b) REGEX against PL5 R4.
4. One mixed-source fact under the wrong label: inventory (g), AlignmentCheck benchmark size.
5. One unrecorded source conflict: the Prompt Guard 2 evaluation languages, card against paper.
6. One wrong line citation in the eval file (MISMATCH at source).
7. Two label-hygiene leftovers in the inventory.

None of the fixes changes a headline number or a Covered-by value.

## Required fixes

1. **PL7 R4, bullet 2 (line 1059): the threshold claim is wrong, and it is an inference under a Documented label.**
   - Problem: the bullet says "a threshold of 1.0 or lower behaves the same". The code is `ScanDecision.BLOCK if score >= self.block_threshold` (hidden_ascii_scanner.py@172c1074:55), and the score is 0.0 or 1.0. A threshold of 0.0 or below therefore blocks every message, including clean text. Only thresholds above 0.0 and up to 1.0 behave like the default.
   - The error is in cols_b.md line 334 and was carried over unchanged.
   - Replace line 1059 with two bullets:
     - `• The constructor takes `scanner_name` and `block_threshold` (default 1.0), and the scan returns `BLOCK` when the score is at or above the threshold (`hidden_ascii_scanner.py@172c1074:20-26,50-56`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**`
     - `• Because the score is only 1.0 or 0.0, any threshold above 0.0 and up to 1.0 behaves like the default, a threshold above 1.0 never blocks, and a threshold of 0.0 or below blocks every message (premise: the comparison score >= block_threshold at line 55) **[Inferred]**`
   - The PL7 R4 Summary stays as it is; it is still entailed.
   - Log the change in purplellama_changes.md section 2 (PL7 R4).

2. **PL3 R4 Summary: not entailed by its own Detail.**
   - Problem: the Summary says the default model is "Llama 4 Maverick on Together, which Together lists as removed from serverless inference". No PL3 R4 bullet carries the removal; the fact is only in PL3 R6 (line 432).
   - Fix: add this bullet after the "Hosting:" bullet (line 387):
     `• Together's deprecation history (not Meta docs, read 2026-10-09) lists `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` among models removed from serverless inference, removal date 2026-03-31; R6 gives the details **[Documented]**`
   - The deprecations URL is already in PL3 R9. The Summary stays unchanged.
   - Verified at source: https://docs.together.ai/docs/deprecations, the table "all models removed from serverless inference" has the row "2026-03-31 | meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 | Yes".

3. **Inventory (b), REGEX row, Mechanism cell: contradicts PL5 R4.**
   - Problem: the cell ends "replacing scanner.patterns after construction would work [Inferred]".
     - PL5 R4 (line 723) says the replacement "does not persist through `LlamaFirewall`", because a new instance is created on every scan call.
     - Resolution T35 (B:207) says the same about RegexScanner being created inside create_scanner.
   - Replace "No constructor argument takes other patterns; replacing scanner.patterns after construction would work [Inferred]" with:
     `No constructor argument takes other patterns (lines 41-45) [Documented: repo meta-llama/PurpleLlama@172c1074]; replacing scanner.patterns on one instance does not persist through LlamaFirewall, which creates a new scanner on every scan call [Inferred] (premise: llamafirewall.py lines 117-118)`
   - Log the change in section 3 (b).

4. **Inventory (g), row "AlignmentCheck (paper)", first of the two rows, "Benchmark and conditions" cell: a paper fact is labelled with the dataset repo label.**
   - Problem: "while the paper says 600 scenarios, 300 benign and 300 malicious" sits under `[Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9]`. The 600, 300 and 300 come from the paper (Appendix A.1, verified: "This benchmark comprises 600 scenarios (300 benign, 300 malicious)"), not from the dataset card.
   - README section 3 rule 4 needs one labelled fact per source; PL3 R5 already does this correctly.
   - Replace the cell with:
     `In-house goal hijacking benchmark of 600 scenarios, 300 benign and 300 malicious [Documented] (PAPER Appendix A.1); the paper links the Hugging Face dataset facebook/llamafirewall-alignmentcheck-evals [Documented] (PAPER Appendix A.1); the dataset card says 577 test cases with six model responses each [Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9]; the two counts conflict and are recorded without picking one; AlignmentCheck is described as an experimental feature [Documented]`
   - Append to the row's Source URL cell: ` ; https://huggingface.co/datasets/facebook/llamafirewall-alignmentcheck-evals/tree/d50916c9ea26e374667c030268218b28c20626a3`
   - The row count is unchanged (12).

5. **PL1 R2 (and R8): an unrecorded source conflict on the Prompt Guard 2 evaluation languages.**
   - Problem: the model card (86M/MODEL_CARD.md@172c1074:25) lists eight evaluated languages including English, so seven besides English. The LlamaFirewall paper (Appendix A.2, verified) says the multilingual set is "the same dataset machine-translated into eight additional languages" and names none of them.
   - PL1 R5 line 95 quotes the paper without noting the clash, and the PL1 R2 Summary states "eight languages were evaluated" as settled. README section 3 rule 4 requires the conflict to be written.
   - Add after the "Languages evaluated" bullet (line 22):
     `• Source conflict, language count (paper side): the paper's multilingual set is "the same dataset machine-translated into eight additional languages", one more than the seven non-English languages the card lists; the paper names none of them (arXiv 2505.03574 appendix A.2) **[Documented]**`
   - Add to PL1 R8: `• Which languages the paper's "eight additional languages" are, given that the card lists seven besides English (checked the card and the paper; not stated)`
   - Change the PL1 R2 Summary's last sentence to "There is no injection sub-label, and the card lists eight evaluated languages." The new Summary has 37 words (limit 45) and keeps **[Documented]**.

6. **Eval file, Engine coverage, the "README side" bullet (line 109): wrong line number.**
   - Problem: it cites "(CSB/README.md:226)". At the pin the "temporarily removed" note is on line 227; line 226 is blank. The Tools Instruct row already says "README line 227".
   - Replace `(CSB/README.md:226)` with `(CSB/README.md:227)`.

7. **Inventory label hygiene, two leftovers.**
   - (b), HIDDEN_ASCII row, Maturity cell: this absence is labelled [Inferred]. Per README section 3 rule 2, an absence is [Not disclosed], as row (a) "Hidden ASCII scanner" already writes it. Replace the cell with:
     `Not marked experimental in code and not listed in the README components [Not disclosed] (searched LlamaFirewall/src, the README and the docs pages for experimental)`
   - (e), row "Hugging Face gated-access request", Status cell: "(Hugging Face model API, observed 2026-10-09)" is a leftover of the global change that replaced the "HF API" phrase (changes.md section 1). Replace it with `(Hugging Face Hub model metadata, observed 2026-10-09)`.

## Optional suggestions

- **PL1 R4 Summary** "Small DeBERTa classifiers, run locally." The same row documents the hosted "HF Inference API" route for the 86M model (line 56). Consider "run locally (the 86M model is also on Hugging Face's hosted inference)".
- **PL1 R6 Summary** "approved gated access". The manual approval is in R4 (line 73); R6 only says the weights are gated and that the licence must be accepted. Either add `• Access is approved manually ("manual" gate in the Hub metadata) **[Documented: repo meta-llama/Llama-Prompt-Guard-2-86M@a8ded8e6]**` to R6, or drop "approved".
- **PL3 R5, dataset-card bullet** (line 408). The card's restriction "should be for evaluation purposes only" (verified, card line 39) is used in PL3 R7 and the eval Red-teaming section, but it is not in PL3 R5. Consider adding it, so that the PL3 R7 phrase "evaluation use only" rests on a Detail bullet of the same column.
- **PL4 R4 line 566.** "file-by-file comparison of the unpacked sdist PyPI sdist codeshield-1.0.1, sha256 61866b92, read 2026-10-09 with the pin" is garbled. Suggest "file-by-file comparison of the unpacked sdist (PyPI sdist codeshield-1.0.1, sha256 61866b92, read 2026-10-09) with the pin".
- **PL4 R2 and PL6 R2 CWE bullets.** "the CyberSecEval rule set gives 62" is the count for the eight default languages. Resolution T67 gives 64 over all 15 of its languages, and my recount agrees. Suggest "62 for the eight default languages (64 over all its languages)".
- **Inventory (b) AGENT_ALIGNMENT threshold cell.** "the inherited block_threshold of 0.0 is not used there [Inferred]"; PL3 R5 (line 397) labels the same fact [Documented: repo] with the code lines. Align them; the code read supports the Documented form.
- **Eval Tools, Instruct row, Engine cell.** "the note is a leftover" is a judgement inside a [Documented: repo] cell. Consider "the note appears to be a leftover [Inferred]".
- **Inventory (e), "Automatic model download into HF_HOME".** "offline use with a pre-populated folder [Not disclosed]" sits next to the README's documented preload route (T42). Suggest "the folder name and layout the code expects (meta-llama--Llama-Prompt-Guard-2-86M under HF_HOME) [Not disclosed]".
- **Small cleanups:**
  - PL7 R5 cites hidden_ascii_scanner.py lines 52-72, but the file has 69 lines; use 52-69.
  - In inventory (f), Prompt Guard 1 row, ". the Hugging Face repo file list" needs a capital T.
  - PL2 R4 line 227 lists two later changes to promptguard_utils.py. There is a third, e9983e6 (2026-01-12), which is a Black formatting pass with no effect. Adding "among others" would make the list complete.

## 1. Unlogged differences (Check 1)

Method: difflib SequenceMatcher per (column, row) between cols_a/cols_b and the final (diff_cols.py).
- Each added or removed line was searched in purplellama_changes.md by 60, 40 and 25-character normalised prefixes and mid-line fragments.
- Lines not found there were searched in the merger's ops_*.py (check_ops.py). The log is generated from those ops calls, and multi-bullet entries are truncated with "//".

Results:
- **Columns.** 376 lines added and 206 removed; 333 matched the log directly.
  - All 43 others were found in ops calls. Examples: T6, T7, T8 and T10 licence and gate bullets in PL1 R4; T35 in PL2 R4; T41 and T42 in PL2 R6; T45 tool-call bullets in PL2 to PL5; T46 Together bullets in PL3 R6; T14 and T19 sdist-versus-pin bullets in PL6 R4; T69 and T70 in PL4 and PL6 R5.
  - Each is a later part of a logged multi-bullet operation. None is a new fact without a reason code.
- **Inventory.** Compared cell by cell (diff_inv.py, keyed by the first two cells because block (c) repeats its first cell). All 88 rows pair up and 92 cells differ. Every changed fragment matches the log or an ops call; the appended sentences in (a), (b), (d), (f), (g) and (h) are logged as "(end of cell)" appends.
- **Eval.** 57 lines added and 53 removed (diff_ev.py); every changed fragment matches.
- **Summaries.** The 29 changed Summaries (PL1 R3, R9; PL2 R6 to R9; PL3 R4, R7 to R9; PL4 R3 to R9; PL5 R1, R2, R4, R7, R9; PL6 R2, R4, R5, R7 to R9; PL7 R7) equal the 29 "(summary)" entries in section 2. The preview equals the final for all 63 Summaries and word counts, and the starred rows are the same 29.

Result: no substantive unlogged change.

## 2. Sourcing and label strength (Check 2)

**Known-wrong strings from the resolutions, grepped in all three finals:**
- "600 scenarios": 3 hits. In each one it is the paper's size beside the card's 577; none uses it as the dataset size. Fix 4 concerns only the label in one of them.
- CWE counts 47, 63, 65: 0 hits as CWE counts. The hits for " 63 " and "65 " are line numbers and a latency value.
- "2.8" as the AUP item: 0 hits. The AUP clause is "section 1 item h" everywhere. Verified: the live Llama 4 AUP page numbers it "h." under item 1.
- "1.0.0 to 1.0.3": 0 hits.
- "my count": 0 hits.
- "temporarily removed": 2 hits, both in the eval file, each attributed to the README beside the code-side registration (Tools Instruct cell and Engine coverage, lines 109 and 110). It is never stated as current behaviour.
- Others: "HTTP 401" 0, "HF API" 0, huggingface.co/api 0, "column PL" 0, R0nn ruling ids 0, "checkpoint" or "provisional" 0, "four statements" 0, "Test set for" (imperative) 0, "this half" or "the clone" 0, api.together.xyz /v1/models or slip evidence 0.
- "api.together.xyz" appears only as the code default base URL, which is a documented code value.

**Changed [Documented] facts:**
- Every changed fact I sampled traces to a resolution quote: T6, T7, T8, T10, T24, T35, T40, T41, T42, T45, T46, T48, T67 and T68, plus supplementary 1 to 5.
- The sdist facts use the main-ruled form "[Documented] (PyPI sdist name-ver, sha256 short, read date)", and the sdist-versus-pin comparisons are [Inferred].
- No by-eye chart values appear. Figure 18 is described by its axis labels only, with "no table of values".
- No API path appears in an R9 or Source URL cell. The two api.* strings are code values inside an eval Detail bullet.

**Inferences under Documented labels:**
- Fix 1 (PL7 R4).
- I also read every [Documented] bullet containing "so", "therefore", "may", "matches" or "because". Two are borderline but acceptable, because each is a straight reading of git history that resolution T40 records: PL2 R5 line 246 and PL5 R5 line 751 ("matches the code as it stood on 2025-04-29").
- The eval Instruct cell is listed under optional suggestions.

**Absence labels.** Every [Not disclosed] names what was checked. Fix 7 corrects the one absence labelled [Inferred].

**Cross-draft consistency.** The same conflict should be recorded the same way in the columns, the inventory and the eval file:
- Agree:
  - 7 against 8 languages: PL4 R2, PL6 R2, inventory (d) intro and eval Published results.
  - Code Shield latency, five sources: PL4 R5, PL6 R5, inventory (g) rows 124 to 127 and eval.
  - Maverick removal on 2026-03-31: PL3 R4, R6 and R8, PL5 R8, inventory (a), (b), (e) and (f).
  - PROMPT_INJECTION against PROMPT_GUARD: PL2 R3, inventory (b) and (c).
  - Licence text conflict for Prompt Guard 2: PL1 R4 and inventory (f).
  - 577 against 600: PL3 R5 and inventory (g), apart from the label in fix 4.
- Disagree: scanner.patterns (fix 3) and the block_threshold label in (b) AGENT_ALIGNMENT (optional).

**R032.** All R7 bullets after "Minimum setup" and every eval "Reuse for the test bench" bullet use proposal wording: "A bench could", "Possible", "(suggested)", "would". No "the bench will", "we use" or "bench rule" remains. Each of the 7 R7 Summaries starts with "**Minimum setup:**".

**Process text.** No "this draft", "I checked", "Reviewer notes", ruling ids or "checkpoint" in any final.

## 3. Summary entailment and style (Check 3)

- `python benchtest/tools/check_drafts.py columns benchtest/drafts/purplellama_two_level.md --final --expect 7` gives "RESULT: 0 errors, 1 warnings". The warning is the three prefixes, which R030 rules expected.
- 63 Summaries, none over its limit (my count matches the preview's word counts). The R8 lines start "**Key open questions.**" and carry no label; the R9 lines are plain.
- Not entailed: PL3 R4 (fix 2).
- Over-strong beside their own Detail:
  - PL1 R2 states the language count as settled (fix 5).
  - PL1 R4 says "run locally" and PL1 R6 says "approved" (both optional).
- Checked and entailed:
  - PL3 R5: "over 80% recall at under 4% false positives" is line 404.
  - PL3 R6: "Model and endpoint cannot be set through the scanner constructor" is line 429.
  - PL4 R2 and PL6 R2: the seven and eight statements.
  - PL4 R5 and PL6 R5: 96% and 79%, with latency disagreeing.
  - PL6 R4 Summary labelled [Inferred], as main confirmed (queue P6 Q1).
  - PL7 R2 [Inferred].
  - PL5 R1, R2 and R4.
  - All R7 Summaries rest on [Inferred] Minimum setup bullets.

## 4. Spot-checks at source (Check 4)

Pages were read with fetch_text.py (verbatim). Code was read in the pinned clone (172c1074). Git history was read in the resolver's blobless full clone (resolver/purplellama1/pl_full, HEAD 172c1074), metadata only. The PyPI simple index was read with curl. No API host was requested, nothing was signed in to, and no gated file was downloaded.

| # | Claim | Location | Source URL | Verbatim quote or value seen | Match |
|---|---|---|---|---|---|
| 1 | Intent-only scope; no injection sub-label | PL1 R2 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Prompt-Guard-2/86M/MODEL_CARD.md | line 22 "classify prompts as 'malicious' if the prompt explicitly attempts to override prior instructions…"; line 23 "we don't include a specific "injection" label" | MATCH |
| 2 | 86M and 22M metric rows | PL1 R5 Summary, INV (g) | same file | line 74 ".998 \| 97.5% \| .995 \| 92.4 ms"; line 75 ".995 \| 88.7% \| .942 \| 19.3 ms"; APR lines 86-87 81.2%, 78.4% | MATCH |
| 3 | Evaluation languages (card) against paper | PL1 R2, R5 | same file; https://arxiv.org/html/2505.03574 | card line 25 "English, French, German, Hindi, Italian, Portuguese, Spanish, and Thai"; paper "machine-translated into eight additional languages" | MATCH on both quotes; the conflict is unrecorded (fix 5) |
| 4 | Llama 4 licence and Additional Commercial Terms | PL1 R4, INV (f) | .../Llama-Prompt-Guard-2/86M/LICENSE | line 1 "LLAMA 4 COMMUNITY LICENSE AGREEMENT", line 2 "Effective Date: April 5, 2025"; line 22 "…greater than 700 million monthly active users in the preceding calendar month, you must request a license from Meta…" | MATCH |
| 5 | AUP section 1 item h | PL1 R4, R8; INV (f) | .../86M/USE_POLICY.md; https://www.llama.com/llama4/use-policy/ | file line 37 "8. Engage in any action, or facilitate any action, to intentionally circumvent…" (nested under 1); live page line 57 "h. Engage in any action…" | MATCH |
| 6 | Gate page: licence, form text, .998, HF Inference API | PL1 R4, R5, R6 | https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M | "License: llama4"; "Please be sure to provide your full legal name, date of birth, and full organization name with all corporate identifiers."; "LLAMA 4 COMMUNITY LICENSE AGREEMENT"; "Log in or Sign Up to review the conditions and access this model content."; ".998"; "HF Inference API" | MATCH |
| 7 | 22M page: no inference provider | PL1 R4 | https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M | "This model isn't deployed by any Inference Provider." | MATCH |
| 8 | Docs page quotes | PL1 R1, R3, R4, R5, R6 | https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/prompt-guard | "Both models detect prompt injection and jailbreaking attacks, and are trained on a large corpus of known vulnerabilities."; "drop-in replacement for Prompt Guard for all use cases"; "The input is a string that the model labels as "benign" or "malicious""; "using the input utilities available in inference.py"; "0.001", "1.000"; "We recommend splitting longer prompts into segments…" | MATCH |
| 9 | Protections page: typo, 7 languages, 200 ms | PL4 R2, PL6 R1, R2, R5; INV (g) | https://dev.meta.ai/llama/llama-protections | "Code Sheild"; "…for 7 programming languages with an average latency of 200ms." | MATCH |
| 10 | Paper prints .98 for the 86M English AUC | PL1 R5, R8; INV (g) | https://arxiv.org/html/2505.03574 | table cells ".987 … .983 … .98" | MATCH |
| 11 | AlignmentCheck numbers | PL3 R5, INV (g) | same | "over 80% recall with a false positive rate below 4%"; "detecting over 83% of goal hijacking attempts while maintaining a very low FPR of 2.5%"; "2.89% - an 84% drop … (43.1%)"; "from 0.18 (no defenses) to 0.03" | MATCH |
| 12 | 600 scenarios (paper side) | PL3 R5, INV (g) | same | "This benchmark comprises 600 scenarios (300 benign, 300 malicious), covering 7 distinct injection techniques and 8 threat categories" | MATCH (label issue in INV (g), fix 4) |
| 13 | Roles scanned in AgentDojo; tool-output mitigation | PL1 R3, PL2 R3, PL3 R3 | same | "For PromptGuard, we analyze only messages with the role of user or tool…"; "For AlignmentCheck, we restrict evaluation to messages with the role of assistant"; "Restricting inputs to only the agent's chain-of-thought and actions, excluding direct tool outputs." | MATCH |
| 14 | Code Shield in the LlamaFirewall paper | PL4 R2, R5; PL6 R2, R5; INV (g) | same | "across 8 programming languages" (section 1); "across seven programming languages" (4.4); "approximately 60 milliseconds"; "approximately 90% of inputs are fully resolved by the first layer… under 70 milliseconds… can exceed 300 milliseconds" | MATCH |
| 15 | CyberSecEval 3 Code Shield statements | PL4 R2, R5; PL6 R2, R5; EV | https://arxiv.org/html/2408.01605 | "across 7 programming languages and over 50 CWEs"; "within 60ms … approximately 300ms. Notably, in 90% of cases, only the first layer is invoked, maintaining the latency under 70ms"; "10% of queries taking longer than 300ms"; "around 190 patterns across 50 different CWEs with an accuracy of 90%" | MATCH |
| 16 | CyberSecEval 3 Prompt Guard and Llama 3 results | EV Published results | same | "identifies 71.4% of these injections with a 1% false-positive rate"; "recall of 97.5% of jailbreak prompts" with table 3.9%; "rates of 22% and 19% respectively"; "at the rate of 31%" | MATCH |
| 17 | CyberSecEval 2 ranges | EV Published results | https://arxiv.org/html/2404.13161 | "between 26% and 41% successful prompt injections"; "between 13% and 47% of the requests to help an adversarial user attack attached code interpreters"; conclusion "ranging from 13% to 47% success" | MATCH |
| 18 | Code Shield README latency | PL6 R5, INV (g) | .../CodeShield/README.md | line 27 "over 98% of the traffic is classified as benign … approximately 99% of cases, requests are processed within a swift 70ms window … the p90 latency is 450ms" | MATCH |
| 19 | Dataset card: 577 times 6, MIT, evaluation only | PL3 R5, R7; EV Red-teaming | https://huggingface.co/datasets/facebook/llamafirewall-alignmentcheck-evals/raw/d50916c9ea26e374667c030268218b28c20626a3/README.md | "license: mit"; "A total of 577 (test cases) * 6 (models) = 3462 cases"; "should be for evaluation purposes only" | MATCH |
| 20 | Together removed Maverick FP8 from serverless (not Meta docs) | PL3 R4, R6, R8; INV | https://docs.together.ai/docs/deprecations | removed-models table "2026-03-31 \| meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 \| Yes"; "a model can still appear in catalog listings while its route-level availability changes" | MATCH |
| 21 | Together terms section 4 and ZDR default (not Meta docs) | PL3 R6, R7; PL5 R6; INV (e), (f) | https://www.together.ai/terms-of-service ; https://docs.together.ai/docs/zero-data-retention | "You will not use the Services to transmit or provide to the Company any financial or medical information … sensitive personal data (e.g., social security numbers…"; "attempt to probe, scan, or test the vulnerability of the Services"; "engage in competitive analysis or benchmarking"; "ZDR is not enabled by default."; "Together stores the prompts you send and the responses models return, and may use them for product improvements" | MATCH |
| 22 | Llama 3.3 70B at $1.04 per 1M input and output tokens (not Meta docs) | PL5 R6, R8; INV (e) | https://www.together.ai/pricing | "Llama 3.3 70B \| $1.04 \| $1.04" | MATCH |
| 23 | PyPI: llamafirewall 13 releases, latest 1.0.3, sha256 54fe55c8; codeshield 1.0.0 and 1.0.1 | PL2 R4, PL4 R4, PL6 R4, INV (a) | https://pypi.org/simple/llamafirewall/ ; https://pypi.org/simple/codeshield/ | 0.0.0 to 0.0.5, 0.1.0, 0.2.0, 1.0.0, 1.0.0.post1, 1.0.1 to 1.0.3 (13); "llamafirewall-1.0.3.tar.gz#sha256=54fe55c8…"; codeshield-1.0.0, codeshield-1.0.1 | MATCH |
| 24 | LlamaFirewall code values | PL2 R1, R3, R5; PL3 R2, R4, R5; PL5 R2, R4 | prompt_guard_scanner.py, llamafirewall.py, custom_check_scanner.py, piicheck_scanner.py, regex_scanner.py, alignmentcheck_scanner.py at 172c1074 | `block_threshold: float = 0.9` (24); `BLOCK if score >= self.block_threshold` (39); default map lines 90-96 as stated; Maverick, together.xyz, TOGETHER_API_KEY, 0.0, 0.0 (35-39); PIICheck 0.7 and Llama-3.3-70B-Instruct-Turbo (45-46); the five patterns (23-28) with IGNORECASE and DOTALL (59); "Only consider the selected action, not the entire trace." (144); "When in doubt, assume the action is not misaligned" (148); `if score == 1.0: return … HUMAN_IN_THE_LOOP_REQUIRED` (127-130) | MATCH |
| 25 | Hidden ASCII threshold behaviour | PL7 R4 | .../scanners/hidden_ascii_scanner.py | line 55 `ScanDecision.BLOCK if score >= self.block_threshold else ScanDecision.ALLOW`; score 0.0 or 1.0, so a threshold at or below 0.0 blocks all text | MISMATCH (fix 1) |
| 26 | CWE counts and rule counts | PL4 R2, R8; PL6 R2, R5, R8 | rules/config.yaml, rules/regex/*.yaml, rules/semgrep/_generated_/*.json at 172c1074 | independent recount (cwe_count.py): CODESHIELD 46; CYBERSECEVAL 62 for the 8 default languages (64 over all its languages); all regex YAML plus generated JSON 64; only vulnerable-strcpy lacks a cwe_id there; 38 enabled regex ids (5, 2, 2, 14, 1, 3, 3, 0, plus 8 language-agnostic); bugprone-gets is the only enabled regex Error rule; java_codeshield.json has 6 ERROR rules | MATCH |
| 27 | Code Shield code | PL4 R5, PL6 R2, R5, INV (d), (e) | codeshield.py, languages.py, insecure_patterns.py, code_shield_scanner.py, regex/c.yaml at 172c1074 | get_supported_languages returns C, CPP, CSHARP, JAVA, JAVASCRIPT, PHP, PYTHON, RUST (72-83); load() adds language_agnostic except for CPP, OBJECTIVE_C and OBJECTIVE_CPP; `class Treatment(enum.Enum)`; the exception path returns IGNORE; `f" (CWE-{issue.cwe_id})"` (79) and c.yaml line 12 `- cwe_id: CWE-120` | MATCH |
| 28 | Git history dates | PL2 R4, R5; PL5 R4, R5; EV | git (full clone) | 55ff24c 2025-05-28 "Adding support for multi-scanner outputs"; cd9fe65 2025-04-29; e4c281b 2026-01-16; 9a3d175 2026-03-26; c6dee62 2025-01-29; 23510a3 2025-06-12; regex tutorial and adding-custom-scanner last changed in cd9fe65; pyproject 1.0.3 set in 55ff24c; 98 commits to CybersecurityBenchmarks since 2025-06-12 | MATCH |
| 29 | CyberSecEval README lines | EV Overview, Tools, Engine coverage | .../CybersecurityBenchmarks/README.md | lines 8-9, 82 "Note that python 3.10 is required.", 101 platform warning, 168-170 June 12 note; "temporarily removed" is on line 227 | MATCH, except line 109 of the eval cites 226 (fix 6) |
| 30 | Dataset sizes | EV Tools, Datasets | datasets/*.json at 172c1074 | prompt_injection 251 (196 direct, 55 indirect; 180 and 71; 15 variants); multilingual 1,004 in 17 languages; mitre_frr 750, all is_malicious false; instruct 1,916, 50 CWE ids, python 351 … php 162; interpreter 500 | MATCH |
| 31 | Root README and Prompt Guard 1 README | PL1 R4, INV (a), (h) | .../README.md ; .../Prompt-Guard/README.md | root line 42 "Prompt Guard \| Llama 3.2 Community License"; no "Firewall" or "Prompt Guard 2" in the root README; Prompt-Guard README "as of April 29th, a new version of this model, PromptGuard 2, has been released… We recommend considering an upgrade" | MATCH |
| 32 | Prompt Guard 2 README links | PL1 R4, R6 | .../Llama-Prompt-Guard-2/README.md | line 20 "github.com/facebookresearch/llama-recipes"; line 45 "The same license as Llama 4 applies: see the LICENSE (../LICENSE) file"; root LICENSE line 1 "LLAMA 3.2 COMMUNITY LICENSE AGREEMENT" | MATCH |

Tally: 32 checked, 30 MATCH, 2 MISMATCH (items 25 and 29), 0 UNVERIFIABLE. Item 3 matches on both quotes but shows an unrecorded conflict (fix 5); item 12 matches but carries a label issue (fix 4). The Figure 18 axis labels are an image and were not re-read; they are not counted.

## 5. Inventory consistency (Check 5)

- `python benchtest/tools/check_drafts.py inventory benchtest/drafts/purplellama_inventory_final.md --headers benchtest/drafts/purplellama_two_level.md` gives "RESULT: 0 errors, 0 warnings".
- Blocks and shapes: (a) 16 x 9, (b) 8 x 10, (c) 11 x 7, (d) 16 x 7, (e) 12 x 8, (f) 8 x 5, (g) 12 x 5, (h) 5 x 5. That is 88 rows, equal to the draft and to the counts in changes.md section 5. Every row has its header's cell count.
- No `**`, no backtick and no stray `|` in any cell (grep counts 0 and 0).
- Label forms are all allowed: [Documented: repo meta-llama/PurpleLlama@172c1074] 322, [Documented] 62, [Inferred] 59, [Not disclosed] 43, HF repo labels at revision (86M 10, Prompt-Guard-86M 4, 22M 2, Maverick FP8 1, Llama-3.3-70B 1, alignmentcheck-evals 1), llama-cookbook@2f22a9eb 2, semgrep@v1.69.0 and @v1.180.0, ARVO-Meta@51cfeab5, CyberSOCEval_data@ce7daa5b, and [To be verified] 1. The one bracketed non-label is a code expression, [ScannerType.PROMPT_GUARD].
- Covered-by:
  - Every value is an exact header (split on ";") or a marker.
  - The legacy marker is used only for Prompt Guard 1. The inventory-only marker is used for CyberSecEval 4, ClassifyIt and the CyberSecEval command line (main's P1 Q1 ruling and R011). The planned marker is not used.
  - The T77 role rows match their columns' R3 text: SYSTEM carries PromptGuard, Regex and Hidden ASCII; MEMORY carries PromptGuard, CodeShield, Regex and Hidden ASCII. AlignmentCheck is on the trace row only.
  - PIICheck, CustomCheckScanner and the custom-scanner route map to the Regex column, as R030 rules (PL5 is one column).
- Cross-references between blocks are consistent, apart from fixes 3, 4 and 7.

## 6. URLs (Check 6)

Scope (lessons item 12): R9 bullets of the seven columns, inventory Source URL cells and URLs in the eval file. That gives 186 distinct URLs (harvest.py, urls.tsv).

Method:
- `curl -s -L --max-time 40`, with one retry on non-200.
- github.com /blob/ URLs were checked through their raw.githubusercontent.com equivalent at the same ref (R020).
- github.com /tree/ URLs at 172c1074 were confirmed as tree objects in the pinned clone (git cat-file).
- The two PyPI sdist file URLs got a HEAD request only, with no download.
- Not requested:
  - The two api.* strings in the eval Engine coverage bullet (`https://api.together.xyz/v1`, `https://api.llama.com/v1`). They are code values, not source links.
  - No huggingface.co/api or */v1/* path was requested.

Full list: benchtest/scratchpad/verifier/purplellama/url_check.txt.

| Class | Count | URLs | Verdict |
|---|---|---|---|
| 200 direct | 54 | arxiv.org (7), dev.meta.ai (4), huggingface.co pages and raw cards (17), meta-llama.github.io (8 of 9), pypi.org (4), docs.together.ai (6), www.together.ai (5), docs.python.org, engineering.fb.com, semgrep.dev | OK |
| 200 through raw equivalent | 115 | every github.com /blob/ URL: PurpleLlama@172c1074, llama-cookbook@2f22a9eb, semgrep v1.69.0 and v1.180.0, CrowdStrike/CyberSOCEval_data@ce7daa5b, n132/ARVO-Meta@51cfeab5 | OK (R020) |
| 200 HEAD | 2 | files.pythonhosted.org llamafirewall-1.0.3.tar.gz and codeshield-1.0.1.tar.gz | OK |
| Tree confirmed in the clone | 12 | github.com/meta-llama/PurpleLlama/tree/172c1074…/ CodeShield/insecure_code_detector/rules, CybersecurityBenchmarks (and /benchmark, /datasets, /datasets/autonomous_uplift, /datasets/autopatch, /datasets/canary_exploit, /website/docs), Llama-Guard, Llama-Guard2, Llama-Guard3, Llama-Guard4 | OK (directory pages; existence confirmed at the pin) |
| 404 | 1 | https://meta-llama.github.io/PurpleLlama/docs/benchmarks/prompt_injection | Expected: the eval bullet (line 112) cites it as the dead link on the Hugging Face card, and gives the working /CyberSecEval/ page beside it, which returns 200 |
| Not requested (API code values) | 2 | https://api.together.xyz/v1 ; https://api.llama.com/v1 | Rule 5; not source links |

Real URL failures: 0.
