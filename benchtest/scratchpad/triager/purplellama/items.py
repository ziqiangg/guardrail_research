# Item data for purplellama_triage.md (generator input). Written by gr-triager, 2026-10-09.
# I(key, group, item, locations, class, source_or_why, priority)
# class: a | b | b-CP1 | b-HG (honest gap) | c
ITEMS = []
GROUPS = []


def G(name):
    GROUPS.append([name, None, None])


def I(key, item, locs, cls, src, pri):
    ITEMS.append(dict(key=key, item=item, locs=locs, cls=cls, src=src, pri=pri, group=len(GROUPS) - 1))


# ---------------------------------------------------------------- G1
G("CP1 decisions")
I("cp1_prefix",
  "[CP1] Q-A header prefix: per-tool prefixes `Prompt Guard 2:`, `LlamaFirewall:`, `Code Shield:` (drafted, option B) or one `Purple Llama:` prefix with the tool in a parenthesis (option A). Meta writes the tool names three ways; R004 left the choice to CP1 (and gives `Prompt Guard:` without the 2 as its example). Option B needs three registry prefixes at P8, option A one; the checker warns on several prefixes (expected).",
  "BR Scope and Q-A (header table); A:1, A:139, A:271, A:419; B:5, B:157, B:302; INV:3 and every Covered-by cell in INV(a), (b), (c), (e); EV:22 (headers used); CLAUDE.md Products row; explorer q01, q11",
  "b-CP1",
  "User at CP1 (closes when chosen, NeMo b22 precedent). Evidence in hand: R009 (owner's own name), R004, Llama Guard precedent, brief Q-A. A swap touches 7 Column lines, the Covered-by cells and the EV Evaluates cells only; no Summary changes",
  "H")
I("cp1_pl7",
  "[CP1] Q-B PL7 Hidden ASCII (provisional): Table 3 column or inventory only (marker `— (inventory only, not in Table 3)`, R011). For: distinct, dependency-free, deterministic function named in the ScannerType enum; cheap to test. Against: no docs page, README, paper or llama.com text describes it (one tutorial enum sentence), so purpose, support and history are [Inferred] or [Not disclosed] and the PL7 R2 Summary is only [Inferred].",
  "BR Q-B alt 2; B:302-381 (esp. B:310, B:311, B:316, B:365); INV(a) row 17 (INV:17); INV(b) row 34 (INV:34); INV(c) rows 47 and 49; INV(e) row 86; explorer q13",
  "b-CP1",
  "User at CP1. If dropped, the merger moves PL7 to an inventory-only row and fixes the Covered-by cells that list the Hidden ASCII header",
  "H")
I("cp1_pl8",
  "[CP1] Q-B PL5 regex and custom scanners as one column (drafted) or split the LLM-prompt scanners (CustomCheckScanner, PIICheckScanner) into reserved PL8. For a split: different function and setup (Together key, experimental, PIICheck fails open) and PII overlap with the Presidio and Sensitive Data Protection columns for sheet 4 grouping. Against: Meta documents 'Regex + Custom' as one layer and R004 lists it as one; PIICheck has no docs page; P0 q13 suggested inventory only for PIICheck. A split needs new R1 to R9 Summaries, not only moved bullets.",
  "BR Q-B alt 1; B:167-170, B:184-186, B:212-216, B:231-233, B:247-248, B:257-258, B:272, B RN-10 (B:394); INV(a) rows 18-20; INV(b) rows 35-37; INV(e) row 91; explorer q13",
  "b-CP1",
  "User at CP1. LLM-prompt bullets are already isolated in PL5 R1 to R8, so a split is mostly a copy plus new Summaries",
  "H")
I("cp1_dir",
  "[CP1] Q-C LlamaFirewall direction: one column per scanner with roles in Detail (drafted) or split by role. Evidence for a split: R002 counts prompt roles and config sections as a direction surface and LlamaFirewall has a five-value Role map. Evidence against: scanner logic is identical for every role; defaults mix roles (PromptGuard on USER and TOOL, CodeShield on ASSISTANT and TOOL); five roles not two. Sub-point: headers PL1, PL2, PL4, PL6 carry Input-level or Output-level while their R3 says any text or any role (R002 exception wants R3 and R6 to explain both uses; the Sentinel LionGuard 2 precedent has no level word).",
  "BR Scope (Direction) and Q-C; headers A:1, A:139, A:271, A:419; A:37, A:172, A:312, A:457 (R3 any-role bullets); B:42, B:195, B:329 (Direction bullets); INV(c) (INV:39-55); explorer q12; R002",
  "b-CP1",
  "User at CP1. Role defaults are in INV(c); split alternative adds PromptGuard (USER and SYSTEM vs TOOL and MEMORY) and CodeShield (ASSISTANT vs TOOL) columns",
  "H")
I("cp1_neg",
  "[CP1, bench design] Eval Q2: may the bench build its own 'injection-removed' negative set from the CyberSecEval prompt-injection cases? Meta's CSE3 evaluation of Prompt Guard 1 used matching injection-removed negatives that are not shipped; the repo has no benign twins; the cases embed a secret-key task, so negatives made by deleting the injected text may be unrepresentative and results are not comparable to Meta's.",
  "EV:30, EV:70, EV:108, EV:113, EV:121; A:103, A:106 (PL1 R7 test set and negative controls); queue.md Open questions",
  "b-CP1",
  "User at CP1 (bench-design decision, R019 style: decided at bench design, not research). Data is Meta-written and MIT (EV:52); see also ev_neg for what CSE3 publishes",
  "M")

# ---------------------------------------------------------------- G2
G("Licensing, gating and terms (class c)")
I("c_aup",
  "Llama 4 Acceptable Use Policy item 2.8 (86M/USE_POLICY.md line 37: 'intentionally circumvent or remove usage restrictions or other safety measures') versus red-team testing of Prompt Guard 2 with jailbreak and injection prompts; no clause names security testing. The same terms reach PL2 (its default scanner loads the same gated 86M model) and PL3 (default judge is Llama 4 Maverick).",
  "A:119 (PL1 R8), A:574 (A RN-12), A:61-64 (PL1 R4), A:94 (PL1 R6); INV(f) row 101; INV(e) row 85",
  "c",
  "P5 resolver re-reads the Llama 4 AUP and Community Licence verbatim at the pin; applicability to testing is a judgement for the user or their legal contact (R025 ruling 1 precedent: quote [Documented], keep an open R8 item, settle before bench testing starts). May add a bench-rule bullet to the R7 of PL1 and PL2 (R025 ruling 2 precedent), which gates executing their minimum setups",
  "H")
I("c_mau",
  "Llama 4 Community Licence 'Additional Commercial Terms' clause at 700 million monthly active users (86M/LICENSE line 22): does it matter for the bench owner's organisation. Same licence family covers Llama 4 Maverick (AlignmentCheck default judge).",
  "A:62, A:120 (PL1 R4, R8); INV(f) row 101",
  "c",
  "LICENSE text at the pin (already read); the organisation facts are the user's. Record only; no research needed",
  "M")
I("c_lictext",
  "Which licence text governs a Prompt Guard 2 download: the folder LICENSE files are Llama 4 (effective April 5, 2025); the Prompt Guard 2 README says 'The same license as Llama 4 applies' but links ../LICENSE, the root Llama 3.2 agreement; the root README licence table has no Prompt Guard 2 row. PL1 R4 states the Llama 4 licence and omits the link target; INV(f) holds the conflict and labels the governing text [To be verified].",
  "A:61-63 (PL1 R4); INV(f) row 101; INV(a) rows 9-10; INV(f) row 103",
  "c",
  "Re-read Llama-Prompt-Guard-2/README.md line 45 and the root LICENSE at the pin; write both sides in PL1 R4 (README rule 4). Which text governs is a legal reading for the user",
  "M")
I("c_pg1",
  "Prompt Guard 1 (legacy) carries three licence versions for one model: Llama 3 (folder README), Llama 3.1 (HF tag and gate page), Llama 3.2 (root README table and root LICENSE); the folder README points to a USE_POLICY.md that is not in the folder.",
  "INV(f) row 102; INV(a) row 11",
  "c",
  "Recorded without picking one (INV); legacy, inventory only. No research",
  "L")
I("c_gate",
  "Gated access to the weights: manual approval; the form asks for full legal name, date of birth and organisation with corporate identifiers; licence and AUP acceptance; approval time [Not disclosed]. Who applies and with what identity is a bench decision (not requested during research).",
  "A:64, A:93-94 (PL1 R4, R6); INV(e) row 85; INV(f) row 101",
  "c",
  "Gate page text already read (HTTP 200). User decision at bench design; nothing to research",
  "M")
I("c_tog_pii",
  "Together AI terms of service section 4: the user must not transmit 'financial or medical information of any nature or any sensitive personal data' to the Services. AlignmentCheck sends the whole agent trace per scan and PIICheck sends the scanned text (PII by design). Decision: synthetic traces and texts only, or do not test PIICheck on personal data. INV(f) row 107 omits this clause.",
  "B:105 (PL3 R7 Summary), B:110 (PL3 R7), B:121, B:270 (R8), B:248-249, B:257 (PL5 R6, R7); INV(e) row 91; INV(f) row 107",
  "c",
  "Together terms page (third party, 'not Meta docs', R019): re-read section 4 verbatim; add the clause to INV(f) row 107; user confirms a 'synthetic data only' bench rule (R025 ruling 2 precedent). P1 Q6 routed here",
  "H")
I("c_tog_ret",
  "Together data retention and training use: terms section 3 say Zero Data Retention is an account setting (data and outputs not stored, retained or used for training only when it is chosen); the account default and the position without ZDR are not stated in the terms or in any Meta file.",
  "B:109, B:119, B:121 (PL3 R7, R8); INV(e) row 91; INV(f) row 107",
  "c",
  "Together terms section 3 and Together privacy or data-handling pages (third party, not Meta docs); decision for bench design. P1 Q6 routed here",
  "M")
I("c_tog_model",
  "Licences of the Together-hosted default models: Llama 4 Maverick (AlignmentCheck, CustomCheckScanner) and Llama 3.3 70B Turbo (PIICheck). PL3 R4 read HF metadata for the Maverick FP8 repo (license_name llama4, gated manual); INV(f) row 107 says the Maverick and Llama 3.3 licences 'were not read' [To be verified]; no column states the Llama 3.3 licence.",
  "B:61 (PL3 R4); INV(f) row 107; INV RN-4 (INV:144)",
  "c",
  "HF metadata and licence file of meta-llama/Llama-3.3-70B-Instruct (Meta, official) and the Maverick record already read; align INV(f) row 107 with B:61. Together's own statement that models carry their own terms is already cited",
  "M")
I("c_semgrep",
  "Semgrep (dependency of codeshield, run as a semgrep-core subprocess): repository LICENSE is LGPL 2.1 (read unpinned on the develop branch); Semgrep rules and registry terms not read; whether the LGPL has consequences for a bench that installs codeshield is a legal question.",
  "A:338, A:396 (PL6 R4, R8); INV(f) row 106; INV(f) row 104",
  "c",
  "Semgrep's own LICENSE (pin to a release tag) and rules-licence page (third party, 'not Meta docs', R019); legal reading for the user. Related pin clash: CyberSecEval requirements pin semgrep 1.51.0 (see cs_semgrep_pin)",
  "M")
I("c_csedata",
  "Third-party data licences inside CyberSecEval: CrowdStrike CyberSOCEval report data (git submodule symlink; licence [To be verified]), the ARVO crash collection behind AutoPatch (licence not stated), Instruct and Autocomplete prompts derived from third-party repositories listed in third-party.txt (mit, apache-2.0, bsd, isc lines; README says components 'may have their own licensing agreements'), CAPTCHA images from a third-party dataset in the visual injection set, and agency reports (IC3, CISA, NSA) for threat intelligence.",
  "EV:14, EV:49-51, EV:54, EV:59-61, EV:115, EV:130; INV(f) row 105",
  "c",
  "Owners' pages: CrowdStrike/CyberSOCEval_data, the ARVO project, the HF dataset card (all 'not Meta docs', R019). Redistribution and reuse are the user's decision",
  "M")
I("c_cseuse",
  "Use restrictions and provider terms around attack content: the visual injection card says the dataset 'should not be used for harmful, unethical, or malicious purposes'; the README warns platforms may block malicious-actor prompts; judge-based suites send attack text to hosted LLM providers (OpenAI, Anthropic, Together, Google) whose terms apply.",
  "EV:84, EV:86, EV:98, EV:114, EV:116; INV(f) row 105",
  "c",
  "Dataset card (read) and provider terms pages (third party); bench-design decision (R019: sensitive data decided at bench design)",
  "L")
I("c_stack",
  "Licence stack of a default LlamaFirewall install: MIT code, Llama 4 licence on the downloaded Prompt Guard 2 86M, separate licences for the Together-hosted models; no LlamaFirewall row in the root README licence table (applicability of the Llama 4 terms is [Inferred]).",
  "INV(f) row 103; INV:3; A:197 (PL2 R4); A:478 (PL4 R4)",
  "c",
  "LICENSE files at the pin (already read); wording only",
  "L")

# ---------------------------------------------------------------- G3
G("Pins, releases, provenance and unread sources")
I("pin_notes",
  "No release, tag or CHANGELOG exists in the repo, so release notes and version history for Prompt Guard 2, llamafirewall, codeshield and every scanner are [Not disclosed]; the R015 CHANGELOG substitute does not exist (R020).",
  "A:60, A:198, A:339, A:480; B:59, B:219, B:337, B:370; INV:3 and INV RN; BR Honesty rule",
  "b-HG",
  "Vendor publishes none (checked git ls-remote --tags, the clone file list, PyPI index). Nothing to resolve",
  "M")
I("pin_cs",
  "codeshield: repo pyproject says 0.0.1, PyPI lists 1.0.0 and 1.0.1, llamafirewall requires codeshield>=1.0.1; whether the PyPI 1.0.1 sdist equals the repo code at the pin is unread [To be verified]. The CodeShield scanner imports the installed package first, so the PyPI contents decide the rules and language list. The PL6 R4 Summary states 0.0.1 against 1.0.1.",
  "A:318 (PL6 R4 Summary), A:333-335, A:389, A:466-467, A:469-472, A:521, A:529, A:571 (A RN-9); INV(a) row 21; INV(e) row 90; INV:3",
  "a",
  "PyPI sdist for codeshield 1.0.0 and 1.0.1 (official vendor package, files from pypi.org; read the tarball, no install): diff languages.py, rules/config.yaml and insecure_code_detector.py against the pin. Main to confirm that downloading an sdist for reading is allowed under R019 (see QUESTIONS)",
  "H")
I("pin_lf",
  "llamafirewall: PyPI 1.0.3 versus the pinned commit (pyproject also 1.0.3): sdist contents unread [To be verified] in PL3, PL5, PL7 R4 and PL2 R4; sdists 1.0.0 to 1.0.3 exist.",
  "A:193-194; B:57-58, B:130, B:217, B:335; INV(a) row 12; INV:3",
  "a",
  "sdist 1.0.3 versus the pin (scanners/, llamafirewall.py, config.py); same download question as pin_cs",
  "M")
I("pin_hfcard",
  "Hugging Face card bodies of the three gated repos return HTTP 401, so card facts come from repo MODEL_CARD.md files; equality of the HF body with the repo file is unproven; the 22M card is a textual copy of the 86M card apart from size words (checked with diff).",
  "A:116 (PL1 R8), A:571 (A RN-9); INV:3, INV RN-4; BR Pin",
  "b-HG",
  "Gated; cannot be read without approved access (CLAUDE.md rule 5). The dev.meta.ai Prompt Guard page repeats card text and gives a partial cross-check",
  "M")
I("pin_site",
  "Docs-site pages are cited with repo labels (passages confirmed in pinned .md files) but their live URLs sit unpinned in R9; the docs-site deploy source and branch are not stated; the alignment-check tutorial was read only in the pinned file.",
  "B:148, B:294-296 (R9); B RN-7 (B:391); BR Official sources; INV:3",
  "a",
  "Docs deploy workflow and Docusaurus config under LlamaFirewall/website at the pin; compare 2 or 3 distinctive passages; pin only if they match (README section 3 rule 8; presidio T14 precedent)",
  "M")
I("pin_cookbook",
  "llama-cookbook Prompt Guard files not read: inference.py (get_jailbreak_score), the prompt_guard tutorial notebook; the Prompt Guard 2 README points to facebookresearch/llama-recipes (not read). INV(e) row 94 cites blob/main URLs (unpinned) and marks the content [To be verified].",
  "A:53, A:91, A:98, A:121 (PL1 R4, R6, R8); A RN-9 (A:571); INV(e) row 94; INV RN-4",
  "a",
  "meta-llama/llama-cookbook (Meta) shallow clone at a SHA (R013); check the llama-recipes redirect and record both owners (R007 rename rule); replace blob/main URLs by pinned URLs",
  "M")
I("pin_aleval",
  "HF dataset facebook/llamafirewall-alignmentcheck-evals (600 scenarios, MIT, not gated): metadata read, files unread; usability as bench input unknown.",
  "B:82, B:111, B:129; INV(g) row 121",
  "a",
  "Dataset card and file list at revision d50916c9 (public, ungated)",
  "M")
I("pin_endpoint",
  "A Meta-hosted Prompt Guard 2 endpoint is [Not disclosed]; HF metadata marks the 86M repo as served by an inference provider and the 22M repo as not deployed.",
  "A:54-56 (PL1 R4); BR gap G-i",
  "a",
  "Meta Llama API docs and dev.meta.ai pages for a Prompt Guard or LlamaFirewall endpoint; if none, the ND stands",
  "L")

# ---------------------------------------------------------------- G4
G("Prompt Guard 2 (PL1) and the PromptGuard scanner (PL2)")
I("thr_doc",
  "No recommended Prompt Guard 2 threshold or cut-off (and none for the PromptGuard scanner's 0.9 code default). Places not read: the cookbook tutorial and inference.py; the paper chooses a per-model threshold for 3% utility loss but prints no value.",
  "A:73, A:74, A:105, A:111 (PL1 R5, R7, R8); A:205-206, A:242 (PL2 R5, R8); INV(b) row 30; INV(g) intro (INV:112); BR gap G-a",
  "a",
  "Residual docs check: pin_cookbook files and the paper appendices; if nothing, the ND stands (pages are named in each bullet)",
  "M")
I("thr_test",
  "Best threshold per model and language on a labelled set, and how the 0.9 code default relates to the card's recall-at-1%-FPR operating point.",
  "A:105, A:111, A:235, A:242",
  "b",
  "Threshold sweep on the bench set (R019: bench phase)",
  "M")
I("auc",
  "Headline AUC conflict: the card prints 86M English AUC .998, the paper's table prints '.98' (other cells match); which is right is not stated. Both are written as bullets.",
  "A:79, A:117 (PL1 R5, R8); A RN-1 (A:563); INV(g) row 116",
  "a",
  "arXiv 2505.03574 version history (abs page v1, v2) and the /html/ table; the dev.meta.ai Prompt Guard page table; HF card body is gated. Quote verbatim; use a later paper version if one exists",
  "H")
I("pg2_private",
  "Prompt Guard 2 benchmark is private: size and class balance, training data names and sizes, and training languages are [Not disclosed]; Meta's figures cannot be reproduced.",
  "A:28, A:48, A:75-76; INV(g) row 116",
  "b-HG",
  "Vendor publishes none (card, docs page, paper appendices A and B checked)",
  "L")
I("pg2_params",
  "HF safetensors totals (278,810,882 for the 86M repo, 70,830,722 for the 22M repo) exceed the card's 86M and 22M 'backbone parameters'; the embedding-table explanation is [Inferred].",
  "A:49-51, A:118 (PL1 R4, R8); A RN-2 (A:564)",
  "b-HG",
  "No Meta page explains it. Microsoft's mDeBERTa and DeBERTa cards (third party, 'not Meta docs') give embedding sizes if main wants them cited",
  "L")
I("pg2_text",
  "Prompt Guard 2 and the PromptGuard scanner on tool output, retrieved text, memory text and assistant text: Meta says 'untrusted data' but evaluates only user and tool messages (AgentDojo) and documents no response use ([Not disclosed]).",
  "A:36-38, A:112 (PL1 R3, R8); A:172-174, A:247 (PL2 R3, R8)",
  "b",
  "Bench tests by role. The documentation half is an absence with pages named (card, README, docs, paper)",
  "M")
I("pg2_evasion",
  "Detection of paraphrased, encoded, obfuscated or very long jailbreaks beyond 'explicit' override intent, and whether harmful-but-non-override prompts score benign.",
  "A:26-27, A:106, A:113",
  "b",
  "Bench tests with negative controls",
  "M")
I("pg2_lang",
  "22M versus 86M gap on non-English prompts (only the 22M multilingual weakness is stated in words; AUC .942 against .995).",
  "A:23-24, A:114; INV(a) row 10",
  "b",
  "Per-language bench run",
  "M")
I("lat_all",
  "Latency, throughput, memory and cost are not published beyond: the Prompt Guard 2 A100 table (92.4 ms, 19.3 ms), the four Code Shield statements and two sample AlignmentCheck timings. No CPU latency, no scanner or framework latency, no Regex or Hidden ASCII figure, and no Together cost per call or rate limit for the default models.",
  "A:85, A:97, A:115, A:214, A:243; A:359, A:387, A:498, A:527; B:86-89, B:120, B:122, B:237, B:273, B:345; INV(g) rows 122, 124, 127; INV:3",
  "b-HG",
  "Vendor publishes none (pages named per bullet); measure on bench hardware. Together price and rate limits are in tog_cost",
  "M")
I("lf_reload",
  "Code half: LlamaFirewall.scan creates a new scanner each call (llamafirewall.py:117-118), so the PromptGuard model may load from disk on every scan and a scanner's patterns do not persist; no cache or singleton is shown. Premise is [Inferred] in three columns.",
  "A:192, A:237, A:243 (PL2 R4, R7, R8); A RN-7(a) (A:569); B:207 (PL5 R4)",
  "a",
  "Re-read llamafirewall.py create_scanner, prompt_guard_scanner.py and promptguard_utils.py constructors for a class-level cache; upgrade or drop the [Inferred] bullets",
  "M")
I("lf_reload_time",
  "Timing of the first versus later scans and the model-load cost per call.",
  "A:237, A:243",
  "b",
  "Bench timing",
  "M")
I("lastclass",
  "Whether the last class probability (probabilities[0, -1]) is the malicious class: the gated config.json is unreadable; the card prints MALICIOUS through model.config.id2label.",
  "A:71, A:191, A:245",
  "b",
  "Needs approved access to the gated config or a bench run",
  "M")
I("trunc",
  "512-token truncation: text beyond the window is not scored; the card advises splitting long inputs, the scanner does not split.",
  "A:40, A:220-221, A:244 (PL1 R3, PL2 R6, R8)",
  "b",
  "Long-input bench test",
  "M")
I("preproc",
  "The PromptGuard scanner removes whitespace, re-tokenises and rebuilds the text before scoring; effect on non-English text and code, and on the card's 'adversarial tokenization' claim.",
  "A:25, A:188, A:246, A:248",
  "b",
  "Bench test with and without preprocessing",
  "M")
I("samples",
  "Docs sample outputs differ from code: the how-to page prints reason 'prompt_guard' and a benign reason 'default' with score 0.0; the regex tutorial prints 'Reason: default' for allowed messages; the single-scanner path returns the scanner's own reason and score.",
  "A:210-211, A:249, A RN-6 (A:568); B:227-229, B:268",
  "a",
  "Read-only git history of the two docs files against llamafirewall.py (needs more than a depth-1 clone; see QUESTIONS); a run would confirm (bench)",
  "M")
I("readme_prereq",
  "README prerequisite names access to 'Llama 3.1 models' and links a Llama 3.1 collection, not the Llama 4 licensed Prompt Guard 2 repo; whether it is stale is an inference.",
  "A:227, A:250; INV(e) row 86",
  "a",
  "README line 55 and the gate page are already read; record two facts, 'stale' stays [Inferred]",
  "L")
I("offline",
  "Gated-weight acquisition without an interactive login, and offline or air-gapped use: the code checks the local HF_HOME folder first and calls login() only if the folder is missing and no token is found. R8 and INV(e) say [Not disclosed].",
  "A:185-186, A:222-223, A:251; INV(e) rows 87-88",
  "a",
  "promptguard_utils.py lines 43-69 (code read) gives the offline path; HF token behaviour belongs to Hugging Face docs (third party)",
  "M")
I("name_pi",
  "Scanner enum name: the docs use-case page writes PROMPT_INJECTION; the enum has PROMPT_GUARD only. Both sides are written; code is stronger.",
  "A:177-178; INV(b) row 30; INV(c) row 51; BR C3",
  "a",
  "None beyond a live-page re-read; docs defect, report only",
  "L")
I("py_misc",
  "PL2 code inferences: the synchronous scan uses asyncio.run (fails inside a running loop); no timeout or size limit in code; interactive login may block a headless run.",
  "A:223, A:228-229",
  "a",
  "Re-read llamafirewall.py:122 and promptguard_utils.py:57-61",
  "L")
I("tool_calls",
  "No scanner reads Message.tool_calls, so function-call arguments are not scanned. Rests on a grep of src and is [Inferred] in five columns, while the PL4 R3 Summary states it as [Documented].",
  "A:161, A:175, A:450 (PL4 R3 Summary), A:461, A:534; B:43, B:245; INV(c) intro (INV:41); BR",
  "a",
  "Re-run the grep for tool_calls over LlamaFirewall/src at the pin and name it; per R020 label the absence [Not disclosed] with the search named, or keep [Inferred]; align the PL4 R3 Summary",
  "H")

# ---------------------------------------------------------------- G5
G("AlignmentCheck (PL3)")
I("tog_avail",
  "Default judge meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 on api.together.xyz: Together's model table read 2026-10-09 lists Llama 3.3 70B Turbo and no Maverick row; Together docs show base_url api.together.ai. If Maverick is not served, the AlignmentCheck and CustomCheckScanner defaults cannot run unmodified. The PL3 R4 Summary names Maverick on Together as the default.",
  "B:46 (PL3 R4 Summary), B:61-62, B:101-103, B:119, B:269, B:388 (B RN-4); INV(a) row 14; INV(b) rows 31, 36; INV(e) row 91",
  "a",
  "Together model catalogue, deprecations and OpenAI-compatibility pages (third party, 'not Meta docs'; re-read raw because the table may be filtered or paginated, R021). R019 allows no API call, so the live check is tog_live",
  "H")
I("tog_live",
  "Whether Maverick (and Llama 3.3 for PIICheck) is actually served on the .xyz or .ai host, and what a call costs: a live request.",
  "B:102-103, B:119-120, B:269",
  "b",
  "Bench call with a Together key (R019: no vendor API calls in research)",
  "M")
I("tog_cost",
  "Together cost per call and rate limits for the default models.",
  "B:120, B:269",
  "a",
  "Together pricing and rate-limit pages (third party, 'not Meta docs')",
  "M")
I("al_ctx",
  "Long traces: the paper says the trace is 'truncated to a fixed context window'; the code joins the whole trace with no truncation, so the limit is the judge model or API (not stated).",
  "B:98-100, B:123 (PL3 R6, R8)",
  "b",
  "Long-trace test. The conflict is already written; the code side is a code absence labelled [Not disclosed] (see h_multi)",
  "M")
I("al_scope",
  "Whole trace (docs) versus 'Only consider the selected action' (system prompt): effect on multi-step hijacks.",
  "B:23-24, B:124; INV(b) row 31; INV(c) row 55",
  "b",
  "Multi-step hijack test on the bench",
  "M")
I("al_tool",
  "Tool outputs in the trace: the paper lists excluding direct tool outputs as a mitigation, the code filters nothing by role; behaviour with injected tool output.",
  "B:35-36, B:125",
  "b",
  "Bench test with injected tool output",
  "M")
I("al_judge",
  "Judge manipulable by text in the trace (paper limitation C.4) and the PromptGuard pre-scan mitigation.",
  "B:26-27, B:126",
  "b",
  "Bench test with injections aimed at the judge",
  "M")
I("al_misc",
  "Non-English traces ([Not disclosed]) and run-to-run variation at temperature 0.0 with a hosted model.",
  "B:25, B:127-128",
  "b",
  "Repeated bench runs",
  "L")
I("al_code",
  "AlignmentCheck code points not yet in bullets or still [Inferred]: require_full_trace is set True but read nowhere (B RN-2, not in a bullet); the scan_replay_build_trace empty-trace claim; configure.py accepts TOGETHER_API_TOKEN but the client reads TOGETHER_API_KEY only (already [Documented]).",
  "B:41, B:95, B:386 (B RN-2); INV(e) row 87",
  "a",
  "Re-read llamafirewall.py:230-235 and grep require_full_trace at the pin; add the bullet",
  "L")
I("al_thr",
  "AlignmentCheck threshold or calibration guidance is [Not disclosed]; the score is binary and the inherited block_threshold 0.0 is unused.",
  "B:72, B:88; INV(b) row 31",
  "b-HG",
  "Vendor publishes none (scanner page, tutorial, README, paper checked)",
  "L")

# ---------------------------------------------------------------- G6
G("Regex and custom scanners (PL5), Hidden ASCII (PL7)")
I("rx_acc",
  "Regex scanner detection and false-positive rates for the five patterns; latency; input length limits ([Not disclosed]).",
  "B:235, B:237, B:244, B:262, B:273",
  "b",
  "Labelled bench set; Meta publishes no regex or PII scanner evaluation",
  "M")
I("rx_form",
  "Pattern coverage: the phone pattern is a North American shape, SSN is the US dashed form, the card pattern matches any 16 digits in four groups with no Luhn check, the injection pattern matches two literal phrases; non-US formats, spaced or obfuscated variants and Unicode lookalikes are untested. The bullets are [Inferred] readings of regexes that are themselves [Documented: repo].",
  "B:180-181, B:263-265 (PL5 R2, R8); INV(b) row 33",
  "b",
  "Bench inputs (the reading itself can be checked by a code read)",
  "M")
I("rx_conf",
  "The pattern set cannot be changed through the constructor although the docs call the layer 'configurable'; replacing scanner.patterns does not persist through LlamaFirewall (new instance per call); whether Meta will add a pattern argument is unknown.",
  "B:205-207, B:266; BR C5",
  "b-HG",
  "Roadmap is not documented (code and docs checked)",
  "L")
I("rx_docs",
  "Custom-scanner how-to is stale (BaseScanner and editing create_scanner) versus Scanner plus register_llamafirewall_scanner in code; both sides written.",
  "B:210-211, B:267; INV(a) row 20; INV(b) row 37; BR C6",
  "a",
  "None beyond re-read; docs defect, report only",
  "L")
I("pii",
  "PIICheckScanner and CustomCheckScanner: no docs page ([Not disclosed]); accuracy on its seven PII types; fail-open on LLM error; Llama 3.3 availability and cost on Together; experimental status.",
  "B:186, B:232-233, B:248, B:269, B:271; INV(a) rows 18-19; INV(b) rows 35-36",
  "b-HG",
  "Documentation half is a vendor silence; accuracy and failure behaviour need bench tests. Depends on cp1_pl8",
  "M")
I("hid_supported",
  "Hidden ASCII is described by no Meta page beyond one enum sentence; whether it is a supported feature, its purpose and its history are [Not disclosed].",
  "B:310, B:316, B:365, B:370; INV(a) row 17; INV(b) row 34",
  "b-HG",
  "Vendor silence (docs, READMEs, paper, protections page checked). Feeds cp1_pl7",
  "M")
I("hid_emoji",
  "Tag-block false positives: emoji tag sequences (some regional flags) are blocked by the range test.",
  "B:366",
  "b",
  "Bench test",
  "M")
I("hid_misc",
  "Other invisible characters (zero-width, variation selectors, bidirectional controls), upstream normalisation that strips tag characters, and whether the decoded reason is safe to show.",
  "B:317, B:354, B:367-369",
  "b",
  "Bench pipeline questions",
  "L")

# ---------------------------------------------------------------- G7
G("Code Shield engine (PL6) and scanner (PL4)")
I("cs_lang",
  "Languages: 7 (CodeShield README, llama.com protections page, paper section 4.4, CSE3 per EV) versus 8 (ICD README, LlamaFirewall README and docs, paper summary, code). Meta does not say which seven; the code scans 8; the 16-member enum and 14-entry analyser map are not documented as supported. Both PL4 R2 and PL6 R2 Summaries state the conflict.",
  "A:283, A:292-300, A:386 (PL6 R2, R8); A:431, A:435-442, A:526 (PL4 R2, R8); INV(d) intro (INV:59); INV(g) row 127; EV:71; BR C1",
  "a",
  "CSE3 (arXiv 2408.01605 section 5.2) and the LlamaFirewall paper section 4.4 may list the languages; Meta engineering pages. If none, 'which seven' stays [Not disclosed]",
  "H")
I("cs_lat",
  "Four conflicting Code Shield latency statements (README: 99% within 70 ms, p90 450 ms; LlamaFirewall docs: first tier under 100 ms, second about 300 ms, 90% resolved by the first; paper: first tier about 60 ms; llama.com: average 200 ms); none in code; hardware and language mix not given. Both Code Shield R5 Summaries say the figures disagree.",
  "A:341 (PL6 R5 Summary), A:354-359, A:387; A:483 (PL4 R5 Summary), A:493-498, A:527; INV(g) rows 124-127; EV:71",
  "b",
  "Bench measurement on regex-only and Semgrep paths; vendor figures stay as separate bullets (README rule 4)",
  "H")
I("cs_cse3",
  "A fifth Code Shield source exists only in the eval sheet: CSE3 'around 190 patterns across 50 different CWEs with an accuracy of 90%', 'within 60ms' first layer, 'approximately 300ms', '7 programming languages'. The columns and INV(g) say 'four statements'.",
  "EV:71; A:341, A:483; INV(g) intro (INV:112), INV:124-127",
  "a",
  "Re-read arXiv 2408.01605 section 5.2 verbatim; add CSE3 as a bullet in PL4 and PL6 R5 and a row in INV(g), or state in the Summaries that the count is of four statements in the columns' sources",
  "H")
I("cs_cwe",
  "CWE claim 'over 50' / '50+' versus own counts of distinct CWE ids in enabled rules (about 47 for CODESHIELD, 63 for the CyberSecEval rule set, 65 for all enum languages); CSE3 says '50 different CWEs'. Counts are [Inferred] and two R8 bullets use first-person wording ('my count').",
  "A:290-291, A:395, A:434, A:447-448, A:531, A:570 (A RN-8); EV:71",
  "a",
  "Re-run the count over the pinned rule files and keep the method in the change log; label [Inferred] 'counted by parsing'",
  "M")
I("cs_cov",
  "Rule paths by language (code half): PHP Semgrep rules exist but the analyser map lists regex only; Rust is in the default scan list but config.yaml enables no Rust rules; C++ generated Semgrep JSON holds 16 rules while config.yaml lists an empty Semgrep list for cpp (77 versus 93 rule ids); Kotlin is in the map with 0 rules.",
  "A:301-303, A:322, A:328, A:390-391, A:447, A:530; INV(d) rows 64, 69, 72, 75; INV RN-2 (INV:142)",
  "a",
  "Re-read insecure_code_detector.py lines 126-137 and 314-330 and config.yaml; settle whether the generated cpp JSON runs under CODESHIELD; labels stay [Inferred] unless the code is explicit",
  "M")
I("cs_sev",
  "Semgrep issues carry a raw severity string while the treatment check compares with the Severity enum, so Semgrep findings may never give BLOCK; the only enabled regex Error rule is C bugprone-gets. Bears on what 'recommended treatment' means for PL6.",
  "A:349-350, A:392; A RN-7(b)",
  "a",
  "Code read: insecure_code_detector.py around line 282, codeshield.py 87-93, issues.py Severity (str Enum or not); run confirms (cs_run)",
  "M")
I("cs_tmp",
  "Smaller code observations: temporary-file leak on fast-mode early returns; usage notebook compares recommended_treatment with the strings 'block' and 'warn'; the PL4 threshold 1.0 is unused.",
  "A:352, A:368, A:393-394, A:488, A:508, A:532; A RN-7(c)",
  "a",
  "Code read; consequences need a run",
  "L")
I("cs_run",
  "Runtime confirmation of the Code Shield observations: PHP, Rust and C++ rule paths, Semgrep severity BLOCK, temporary files, notebook comparison, cold start of Semgrep, per-language precision and recall on the bench's own labelled set (Meta's 96% and 79% rest on 50 manual completions per language).",
  "A:379-380, A:387-388, A:390-394, A:519, A:522, A:527-528, A:530",
  "b",
  "Bench run (R019: no installs in research)",
  "M")
I("cs_pr",
  "Per-language precision and recall: the paper's figure was not read as text [To be verified].",
  "A:492 (PL4 R5)",
  "a",
  "arXiv 2505.03574 /html/ figure alt text or e-print source; if unreadable the TBV stays",
  "M")
I("cs_policy",
  "Block on every finding (including low severity) versus the engine's warn treatment, and code inside non-content message fields.",
  "A:489, A:533-534",
  "b-HG",
  "Product-design questions; no Meta statement",
  "L")
I("cs_import",
  "The CodeShield scanner imports the installed codeshield package first and falls back to the repo copy, so PyPI content (not the pin) supplies rules.",
  "A:466-467, A:521; A RN-7(f)",
  "a",
  "Import try/except (code_shield_scanner.py:9-19) is documented; the consequence ties to pin_cs",
  "L")
I("cs_semgrep_pin",
  "Dependency pins clash: codeshield needs semgrep>1.68, CyberSecEval requirements pin semgrep==1.51.0, so one environment cannot satisfy both; absent from PL4 and PL6 R6 and R7 and from INV(f).",
  "EV:28, EV:104; A:330, A:365, A:505",
  "a",
  "Add one Detail bullet or INV note from requirements.txt and CodeShield/pyproject.toml (already read)",
  "L")

# ---------------------------------------------------------------- G8
G("Inventory only")
I("inv_status",
  "Status and maturity cells 'Available [Inferred]' and 'Not marked experimental [Inferred]' for the PromptGuard, CodeShield, Regex and Hidden ASCII scanners (premise: not under experimental/ and no marking).",
  "INV:13, INV:15, INV:16, INV:17, INV:30, INV:32, INV:33, INV:34",
  "a",
  "Docs pages and code docstrings (presidio T60 precedent)",
  "L")
I("inv_cov",
  "Covered-by convention: SYSTEM and MEMORY rows list all five LlamaFirewall headers (INV RN-7) while TOOL and ASSISTANT list only the default scanners; PIICheck, CustomCheckScanner and the custom route map to the PL5 header (changes with cp1_pl8); the llamafirewall package row lists five.",
  "INV:12, INV:18-20, INV:45-49, INV:86-87, INV:91; INV RN-7 (INV:147)",
  "a",
  "Main or merger convention; test: list a header only where that column's Detail cites the row's function (presidio P5 Q2). The marker check passes either way",
  "L")
I("inv_notnamed",
  "Language rows say 'Not named [Not disclosed] (checked six docs files)' for HACK, KOTLIN, OBJECTIVE_C, OBJECTIVE_CPP, RUBY, SWIFT, XML and LANGUAGE_AGNOSTIC; 'no unit test file found in tests/' (HACK, OBJECTIVE_CPP) carries no label.",
  "INV:66, INV:69-71, INV:74, INV:76-78",
  "a",
  "Re-grep the six docs files; label or drop the test-file remark",
  "L")
I("inv_gaps",
  "Inventory honest gaps: MEMORY role direction, HF approval time, Together data handling absent from Meta files, no gating terms stated for Code Shield and CyberSecEval code, root README silent on LlamaFirewall and Prompt Guard 2.",
  "INV:49, INV:85, INV:91, INV:104, INV:105, INV:107, INV:137",
  "b-HG",
  "Vendor silence; checked files named in each cell",
  "L")
I("inv_letters",
  "Sheet letter wording: 'sheet 3x' and 'proposed 3j' in the scope note, (a) row CyberSecEval 4, (h) row CyberSecEval and the eval title; letters are assigned at P8 in queue order (R003); sheet names must be 31 characters or fewer; the eval builder needs MD, TITLE and NOTE (queue eval Q1).",
  "INV:1, INV:3, INV:23, INV:135; EV:1; queue.md",
  "a",
  "Main convention; note for the P8 xlsx-writer",
  "L")

# ---------------------------------------------------------------- G9
G("CyberSecEval evaluation sheet")
I("ev_paper",
  "CyberSecEval 4 paper or announcement: EV records [Not disclosed] (arXiv title search, README, dev.meta.ai) while INV(a) row 23 and the brief record [To be verified] for the same fact.",
  "EV:13, EV:120; INV:23; BR Evaluation-tooling sheet",
  "a",
  "ai.meta.com research publications, Meta engineering blog index, arXiv listing by Meta authors; then use one label in both files",
  "M")
I("ev_neg",
  "CSE3's Prompt Guard evaluation: the matching injection-removed negatives and the 'selected' threshold are unpublished (not in the repo, dataset cards or paper text checked).",
  "EV:70, EV:108, EV:113, EV:121, EV:123",
  "a",
  "Re-read CSE3 section 5.1 and appendices and the facebook/ HF dataset list; if nothing, [Not disclosed] stands. Feeds cp1_neg",
  "M")
I("ev_lb",
  "HF leaderboard Space: maintenance and presence of CSE3 or CSE4 results (last modified 2024-04-18).",
  "EV:75, EV:122",
  "a",
  "Space README and file list at the cited revision",
  "L")
I("ev_maint",
  "Whether the project is maintained after the 2025-06-12 note (pinned commit dated 2026-09-29).",
  "EV:16, EV:124; INV:23",
  "a",
  "Read-only git log for CybersecurityBenchmarks/ (needs history; see QUESTIONS)",
  "L")
I("ev_instruct",
  "Instruct and Autocomplete: README line 227 says they are 'temporarily removed from the default list' but run.py:24,34 imports and registers them; whether they run at this commit.",
  "EV:28-29, EV:125",
  "a",
  "Rewrite as a README-versus-code conflict (two bullets) from the files; running them is a bench task",
  "M")
I("ev_conf",
  "Document-versus-file conflicts recorded as [Documented: repo] inside Open questions: AutoPatch case counts (README 142/120/20, files 136/113/20, blog 136/113), docs-site command names and a 404 link, provider lists (README five, docs-site OpenAI/Anyscale/Together, code five).",
  "EV:36, EV:59, EV:92-95, EV:126-128; BR C8",
  "a",
  "Already resolved from files; move to Detail or Tools notes and drop from Open questions (README section 6: open questions carry [To be verified] or [Not disclosed])",
  "L")
I("ev_cse2",
  "CSE2 prompt-injection range: 26 to 41% (results text) versus 13 to 47% (conclusion) inside the same paper.",
  "EV:68, EV:129",
  "a",
  "Keep two quoted bullets; the paper is inconsistent, so 'which is right' cannot be settled from sources",
  "L")
I("ev_enable",
  "--enable-lf is stored but used nowhere in this commit and caught_by_promptguard is copied but absent from the data; later commits unknown.",
  "EV:100-101, EV:131; INV(e) row 95; INV RN-2",
  "b-HG",
  "Vendor silence about intent; code facts already recorded",
  "L")
I("ev_vpi",
  "Visual prompt-injection dataset: the card header says size under 1K while it states 1000 cases and the Hub tag says 1K to 10K; the card says not every sample was manually reviewed.",
  "EV:54",
  "a",
  "Dataset card at revision 79336620 (already read); record as two facts",
  "L")

# ---------------------------------------------------------------- G10
G("Summary labels and entailment")
I("s_pl4r4",
  "PL4 R4 Summary [Documented] says the scanner needs 'no model, key or network access'; the Detail has no model as [Inferred] (A:481) and no key or network statement in R4 (it is [Inferred] in R6).",
  "A:464, A:481, A:513",
  "a",
  "Relabel the Summary [Inferred], reword to the documented parts (imports, Semgrep dependency), or add a [Documented: repo] bullet from the scanner imports",
  "H")
I("s_pl4r6",
  "PL4 R6 Summary [Documented] says 'needs no key or model' and 'No size limit or timeout is set in code'; the Detail has [Inferred] (A:513) and [Not disclosed] (A:512).",
  "A:500, A:512-513",
  "a",
  "Reword to documented facts (Python 3.10, Semgrep, temporary files) or relabel",
  "H")
I("s_pl5r2",
  "PL5 R2 Summary [Documented] says 'four US-style PII shapes'; 'US-style' is an [Inferred] reading (B:180) and email is not a US-style shape; B RN-6 says this Summary uses only [Documented] facts.",
  "B:172, B:180, B RN-6 (B:390)",
  "a",
  "Drop 'US-style' from the Summary or relabel [Inferred]; keep the pattern list",
  "H")
I("s_pl1r3",
  "PL1 R3 Summary [Documented] says 'with no direction setting'; the supporting bullet (no input-or-output flag, takes no system prompt) is [Inferred] (A:37).",
  "A:30, A:37",
  "a",
  "Add a [Documented] bullet (the card's single-string usage, A:33, already supports 'one string') and reword, or relabel the Summary",
  "H")
I("s_pl2r6",
  "PL2 R6 Summary [Documented] says 'text over 512 tokens is truncated'; the R6 bullet is [Inferred] (A:220) and the documented truncation sits in R4 (A:189).",
  "A:217, A:220, A:189",
  "a",
  "Add the [Documented: repo] truncation bullet to R6 (promptguard_utils.py:113)",
  "H")
I("s_other",
  "Summary claims whose support sits in another row or is missing: PL3 R1 ('latest action', 'original request', 'earlier trace' are R2 and R3 facts); PL5 R1 (the pattern list is R2); PL2 R1 ('the message role decides whether it runs' is R3); PL6 R4 'It has no model' (no PL6 R4 bullet); PL6 R2 'buffer-overflow functions' (strcpy rule is an interpretation); PL5 R4 'compiled once' versus a new instance per call (B:207).",
  "B:7, B:159, B:200; A:141, A:283, A:318",
  "a",
  "Add the supporting bullet to the same row or trim the sentence (presidio T59 precedent); watch word counts (several Summaries sit at 43 to 45)",
  "H")
I("s_ev",
  "EV Overview, Red-teaming and Engine coverage Summaries end with two bold labels ('**[Documented]** **[Inferred]** (note)'); README section 4 rule 5 gives one label equal to the weakest fact.",
  "EV:6, EV:80, EV:90",
  "a",
  "Keep one label per Summary ([Inferred] where the sentence mixes); move the parenthetical out",
  "H")

# ---------------------------------------------------------------- G11
G("Label hygiene, style and process")
I("h_brace",
  "Non-standard label form `{I}` in INV(h) (README section 5 allows six forms only). The checker did not catch it.",
  "INV:135",
  "a",
  "Replace by [Inferred] with the premise",
  "M")
I("h_counts",
  "Own counts and parsed sizes carried as [Documented: repo]: INV(d) cells marked 'counted from the file' (16 rows), rule counts at A:301, A:328, A:447, and EV dataset sizes. Presidio convention (T20): [Documented: repo] only where the vendor states the number; otherwise [Inferred] 'counted by parsing' or plain text '(count made from the file)'.",
  "INV:59, INV:63-78; A:301, A:328, A:447; EV:22, EV:26-38, EV:46-61",
  "a",
  "Merger convention; no source needed",
  "M")
I("h_multi",
  "Bullets that carry two facts or two labels: B:55 (paper claim and code claim under one [Documented]; B RN-1c admits it), B:57 (pins and PyPI), B:99 (a code absence labelled [Not disclosed]), EV:16 and EV:83 (two labels).",
  "B:55, B:57, B:99; EV:16, EV:83",
  "a",
  "Split into one fact per bullet (README section 3 rule 5)",
  "L")
I("h_process",
  "Session and process language in Detail and cells: 'research does not install or run it (R019)' (B:107, B:253, B:358), 'because research makes no vendor API calls (R019)' (B:102), 'checkpoint' (B:170, B:258, B:272, B:311), 'Decision for the bench design, not research' (B:121), 'my count' (A:395, A:531), 'so the repo file was used' (A:116), 'Not requested during research (read-only rule)' (INV:85), 'no API call was made' (B:119). Finals must not carry process language.",
  "B:102, B:107, B:119, B:121, B:170, B:253, B:258, B:270, B:272, B:311, B:358; A:116, A:395, A:531; INV:85",
  "a",
  "Reword as product-neutral statements (R019 may be named once in the inventory scope paragraph as the bench rule); merger applies",
  "M")
I("h_ids",
  "Draft ids used as cross-references in Detail and in the eval Evaluates cells ('column PL1', 'column PL4', 'see PL5'): about 20 in A and B plus the PL ids in EV:22-32. The workbook shows headers and sheet letters, not PL ids.",
  "A:66, A:147, A:197, A:236, A:281, A:427, A:519; B:63, B:198, B:234; EV:22, EV:26-32",
  "a",
  "Replace by header text or sheet column letters assigned at P8 (follows cp1_prefix)",
  "M")
I("h_rn",
  "Reviewer notes sections to leave the finals and move into the change log: A RN-1 to 13 (A:562-575), B RN-1 to 10 (B:385-394), INV RN-1 to 7 (INV:141-147).",
  "A:561-575; B:384-394; INV:139-147",
  "a",
  "Merger",
  "L")
I("h_loc",
  "Locator inconsistencies between files: Prompt Guard 2 AgentDojo cited to paper section 4.3 (A:82, A:213) and 4.3.2 (INV:120); AlignmentCheck experimental status cited to section 1 and Figure 2 (B:10-11) and section 4.2 (INV:14); card line ranges (A:81 lines 86-87; INV:118 lines 83-87; A:77 line 74; INV:116 lines 71-74).",
  "A:77, A:81-82, A:213; B:10-11; INV:14, INV:116, INV:118, INV:120",
  "a",
  "Re-read the sections and standardise; no new source",
  "L")
I("h_url",
  "URL hygiene: R9 of PL1 lists huggingface.co/api/models JSON URLs; INV(e) row 94 lists blob/main URLs; PL3 R9 lists live docs-site and Together URLs that are not pinned; INV(h) row 135 cites the CyberSecEval docs site unpinned.",
  "A:134-135; B:148, B:153-155; INV:94, INV:135",
  "a",
  "Pin or note the read date; main to rule on API JSON as a cited source (see q_hfapi)",
  "M")
I("q_hfapi",
  "Hugging Face public model and dataset API JSON (huggingface.co/api/...) was read as evidence for revisions, parameter counts, licence metadata and inference status; CLAUDE.md hard rule 5 says never to call vendor APIs. The sdp precedent (Google discovery doc) was accepted, but this is a different host and kind.",
  "A:49-50, A:54, A:58-59, A:63, A:134-135; B:61, B:82; INV:3 and INV(a) rows 9-11; INV RN-4",
  "a",
  "Main ruling (CLAUDE.md rule 5; R007 item 1; sdp P4 Q7). If refused, the HF-metadata bullets fall back to [To be verified] and the revisions to gate-page text",
  "M")
