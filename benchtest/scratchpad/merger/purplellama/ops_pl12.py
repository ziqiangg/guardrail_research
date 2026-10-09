"""PL1 and PL2 edits (cols_a). r1 = purplellama_resolutions_1.md, r2 = purplellama_resolutions_2.md."""
PR = "**[Documented: repo meta-llama/PurpleLlama@172c1074]**"
DOC = "**[Documented]**"
INF = "**[Inferred]**"
ND = "**[Not disclosed]**"
CB = "**[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**"
G86 = "**[Documented: repo meta-llama/Llama-Prompt-Guard-2-86M@a8ded8e6]**"
PGB = "https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/"
CBB = "https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb030f92d0e99227e57e9a1123af1f9532/getting-started/responsible_ai/prompt_guard/"
HDR1 = "Prompt Guard 2: Input-level prompt-attack detection (jailbreak and injection)"


def apply(K):
    C = "PL1"
    # ------------------------------------------------------------ PL1 R3
    K.summary(C, 3,
        "Summary: **A single text string.** The model receives one string and labels it benign or malicious, with no message roles or conversation structure in the card's usage. "
        "Meta describes it as meant for user prompts and untrusted data such as web content. " + DOC,
        "T93 (r2 text): the old 'no direction setting' rested on an [Inferred] bullet; the new wording draws only on documented bullets")
    K.sub(C, 3, "Retrieved and tool text:", "(arXiv 2505.03574 section 4.3)", "(arXiv 2505.03574 section 4.3.1)",
          "T103: the role sentence sits in section 4.3.1", kind="style")
    K.ins_after(C, 3, "Retrieved and tool text:",
        '• The cookbook tutorial describes scanning "content from untrusted third party sources, like tools, web searches, or APIs" with the model (prompt_guard_tutorial.ipynb, cell 12) ' + CB,
        "T23, supplementary 2: documented intended use on untrusted third-party content")

    # ------------------------------------------------------------ PL1 R4
    K.repl(C, 4, "Docs page example calls a helper named", [
        '• The docs page example, introduced as "using the input utilities available in inference.py", calls get_jailbreak_score(benign_text) with one argument (dev.meta.ai Prompt Guard page, read 2026-10-09) ' + DOC,
        "• In the cookbook, inference.py defines get_jailbreak_score(model, tokenizer, text, temperature), so the one-argument call in the docs example matches the helper defined in the tutorial notebook (cell 7) and not inference.py (inference.py:89-94) " + CB],
        "T23: the cookbook files were read at a pinned commit; the helper mismatch is now a documented fact", kind="replace")
    K.repl(C, 4, "Hosted endpoint: the Hugging Face metadata marks the 86M repo",
        '• Hosted route: the Hugging Face page of the 86M repo lists the "HF Inference API" under Inference Providers and the metadata shows inference "warm" (86M revision a8ded8e6, HF page and Hub metadata, read 2026-10-09); this is Hugging Face\'s service, not Meta\'s ' + G86,
        "T25: names the serving provider and says whose service it is", kind="replace")
    K.repl(C, 4, "A Meta-run hosted Prompt Guard 2 endpoint",
        "• A Meta-run hosted Prompt Guard 2 endpoint (checked the Prompt Guard docs page, protections page, repo README, LlamaFirewall docs and the Meta Model API overview and models pages; none names one) " + ND,
        "T25: checked list extended", kind="replace")
    K.repl(C, 4, "Gate: access is \"manual\"; the form asks for", [
        '• Gate: access is "manual" (Hugging Face model metadata) ' + G86,
        '• The form\'s instruction text reads: "Please be sure to provide your full legal name, date of birth, and full organization name with all corporate identifiers." ' + G86,
        "• The form fields are first name, last name, date of birth, country, affiliation, job title and an IP-location field, plus a checkbox that accepts the licence and the Meta Privacy Policy " + G86,
        '• The form text says the information "will be collected, stored, processed and shared in accordance with the Meta Privacy Policy" ' + G86,
        "• Approval time and criteria (checked the gate pages and the metadata of the 86M, 22M and v1 repos; not stated) " + ND],
        "T10: form fields and instruction text read from the Hub metadata; the old bullet attributed the instruction text to 'the form asks for'", kind="replace")
    K.repl(C, 4, "The 86M and 22M LICENSE files are the Llama 4 Community License Agreement", [
        "• The 86M and 22M LICENSE files are the Llama 4 Community License Agreement, Version Effective Date April 5, 2025 (86M/LICENSE@172c1074:1-2; the 22M file is identical) " + PR,
        "• The README link target ../LICENSE is the repository root file, which is the Llama 3.2 Community License Agreement (LICENSE@172c1074:1), not the Llama 4 text of the folder LICENSE files " + PR,
        "• The root README licence table has no Prompt Guard 2 row; its Prompt Guard row names the Llama 3.2 Community License (README.md@172c1074:42) " + PR,
        "• The Hugging Face gate pages of the 86M and 22M repos display the Llama 4 Community License Agreement, Version Effective Date April 5, 2025, as the text to accept (gate pages, read 2026-10-09) " + DOC,
        "• Which licence text prevails when the README link and the folder files differ (checked the README, the root licence table, the gate pages and the Prompt Guard docs page; not stated) " + ND,
        "• Additional Commercial Terms: if, on the Llama 4 version release date, the monthly active users of the licensee's products or services, or of its affiliates, were greater than 700 million in the preceding calendar month, a licence must be requested from Meta (86M/LICENSE@172c1074:22) " + PR,
        '• Acceptable Use Policy, section 1 item h (86M/USE_POLICY.md@172c1074:37): "Engage in any action, or facilitate any action, to intentionally circumvent or remove usage restrictions or other safety measures, or to enable functionality disabled by Meta" ' + PR,
        "• No clause of the Llama 4 licence or the Acceptable Use Policy names testing, evaluation, research or red-teaming (searched 86M/LICENSE and 86M/USE_POLICY.md for test, evaluat, research, benchmark and red-team; the only security wording is a bug-reporting address) " + ND],
        "T7 (exact clause, the old '700 million' wording was imprecise), T8 (README link target, root table, gate page, which text prevails), T6 (AUP item 1.h; no clause names testing); placed in one run after the README licence quote",
        kind="replace")
    K.sub(C, 4, "Engine and wrapper: the LlamaFirewall PromptGuard scanner (column PL2)", "(column PL2)",
          '(the "LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner)" column)',
          "T101: draft id replaced by the header text", kind="style")
    K.gsub(C, 4, "HF API,", "Hugging Face Hub model metadata,",
           "T104, T105: source phrase 'HF API' replaced; the Hub metadata is public vendor-org metadata (main ruling, purplellama P4 Q1)", kind="edit")

    # ------------------------------------------------------------ PL1 R5
    K.ins_after(C, 5, "The card's example prints \"MALICIOUS\"",
        '• The cookbook scores the malicious class as probabilities[0, 1], and its tutorial says "The model\'s positive label (1) corresponds to an input that contains a jailbreaking technique" (inference.py:109; prompt_guard_tutorial.ipynb, cell 6) ' + CB,
        "T23, supplementary 4: the class index is documented for the 86M model")
    K.sub(C, 5, "Recommended decision threshold or score cut-off",
        "(checked the model card, Llama-Prompt-Guard-2 README, Prompt Guard docs page, protections page, LlamaFirewall README, docs pages and paper; none gives one)",
        "(checked the model card, the Llama-Prompt-Guard-2 README, the Prompt Guard docs page, the protections page, the LlamaFirewall README, docs pages and paper including Appendix B, and the llama-cookbook inference.py, tutorial notebook and README; none gives one)",
        "T26: the cookbook files and paper appendices were read; the absence stands")
    K.ins_after(C, 5, "86M row: AUC English .998",
        "• The model card text shown on the Hugging Face page of the 86M repo prints the same row, with .998 for the English AUC (HF 86M page, read 2026-10-09) " + DOC,
        "T28: second copy of the card agrees with .998")
    K.repl(C, 5, "Source conflict: the paper's table prints the 86M English AUC",
        '• Source conflict: the paper\'s table prints the 86M English AUC as ".98" (card copies: ".998"); the other cells match the card; the paper has one version, v1 of 6 May 2025 (arXiv 2505.03574 section 4.1 and abs page) ' + DOC,
        "T28: the paper has a single version; which figure is right is still not stated", kind="replace")
    K.sub(C, 5, "Paper, 86M alone on AgentDojo", "(arXiv 2505.03574 section 4.3)", "(arXiv 2505.03574 section 4.3.2)",
          "T103: the AgentDojo numbers sit in section 4.3.2", kind="style")
    K.ins_before(C, 5, "Latency on a CPU or on other GPUs",
        '• The cookbook tutorial notebook prints "Execution time: 0.088 seconds" for one call whose device argument defaults to "cpu"; the hardware is not stated (prompt_guard_tutorial.ipynb, cell 16) ' + CB,
        "Supplementary 3 (T34 partial): one timing printed by the cookbook")
    K.sub(C, 5, "Latency on a CPU or on other GPUs", "Latency on a CPU or on other GPUs (checked the card, docs pages and paper;",
          "Hardware-qualified latency on a CPU or on other GPUs (checked the card, docs pages, paper and cookbook;",
          "Supplementary 3: the absence is now about hardware-qualified figures", kind="edit")

    # ------------------------------------------------------------ PL1 R6
    K.sub(C, 6, "Meta points to inference utilities", ' in the llama-cookbook repo (not read) (', ' in the llama-cookbook repo (',
          "T23: the cookbook files were read", kind="edit")
    K.ins_after(C, 6, "Meta points to inference utilities",
        '• The cookbook inference.py splits each text into chunks of 512 tokens, scores the chunks in batches (default batch size 16, default device "cpu") and takes the highest chunk score as the text\'s score (inference.py:18-21,168-188) ' + CB,
        "T23: chunked scoring read in the cookbook")
    K.ins_after(C, 6, "The Llama-Prompt-Guard-2 README download section is empty",
        "• The facebookresearch/llama-recipes and meta-llama/llama-recipes addresses redirect (HTTP 301) to meta-llama/llama-cookbook, whose HEAD is the same commit (observed 2026-10-09) " + DOC,
        "T23: the README's llama-recipes link resolves to the cookbook; both owners are Meta's")

    # ------------------------------------------------------------ PL1 R7 (R032 wording, r1 supplementary 7)
    K.sub(C, 7, "Test set for Table 3:", "• Test set for Table 3:", "• A possible test set for Table 3:",
          "R032: proposal wording", kind="style")
    K.repl(C, 7, "Cover the evaluated languages and add long inputs above 512 tokens",
        "• A bench could cover the evaluated languages and add long inputs above 512 tokens, scored whole and split into segments, to measure the window effect (premise: the card's 512-token guidance) " + INF,
        "R032: proposal wording", kind="style")
    K.repl(C, 7, "Compare both sizes on the same set and sweep a score cut-off",
        "• A bench could compare both sizes on the same set and sweep a score cut-off to read recall at a fixed false-positive rate, since Meta gives no cut-off (premise: the card's 1% FPR operating point) " + INF,
        "R032: proposal wording", kind="style")
    K.repl(C, 7, "Negative controls: harmful but non-override prompts should score benign",
        "• Possible negative controls: harmful but non-override prompts, which should score benign if the intent-only scope holds (premise: the card's scope text) " + INF,
        "R032: proposal wording", kind="style")

    # ------------------------------------------------------------ PL1 R8
    K.sub(C, 8, "Recommended decision threshold for the benign or malicious score",
        "(checked the card, README, docs pages, protections page and paper; not stated)",
        "(checked the card, README, docs pages, protections page, paper and the cookbook files; not stated)", "T26: checked list extended")
    K.delete(C, 8, "Whether the Hugging Face model card body equals the repo MODEL_CARD.md",
        "Supplementary 1 (T21 premise, T100): the card text is readable on the public gate page and equals the repo card; the bullet's premise and its process wording are gone")
    K.sub(C, 8, "The paper prints an 86M English AUC", "which is correct is not stated",
        "which is correct is not stated (checked both card copies and the single paper version)", "T28")
    K.repl(C, 8, "Whether the Llama 4 Acceptable Use Policy limits using attack and jailbreak prompts",
        "• Whether the Llama 4 Acceptable Use Policy permits using attack and jailbreak prompts to test the model: section 1 item h bars intentionally circumventing or removing safety measures, and no clause names security testing (licensing question; the full licence and policy text were searched)",
        "T6: clause locator corrected from 2.8 to item 1.h and the search named", kind="replace")
    K.repl(C, 8, "Whether the 700 million monthly-active-user clause",
        [ "• Whether the Additional Commercial Terms clause (more than 700 million monthly active users of the licensee and its affiliates on the Llama 4 release date) applies to the bench owner's organisation (licensing question)",
          "• Which licence text governs a Prompt Guard 2 download: the Llama 4 text on the gate and in the folder LICENSE files, or the Llama 3.2 text the README link reaches (legal reading; Meta's gate shows the Llama 4 text)"],
        "T7 (exact clause), T8 (new open item for the conflicting licence texts)", kind="replace")
    K.delete(C, 8, "Whether the Prompt Guard docs page example helper",
        "T23: answered by the cookbook read (the helper in the docs example is the tutorial notebook's)")

    # ------------------------------------------------------------ PL1 R9
    for u in ("https://huggingface.co/api/models/meta-llama/Llama-Prompt-Guard-2-86M", "https://huggingface.co/api/models/meta-llama/Llama-Prompt-Guard-2-22M"):
        K.delete(C, 9, u, "main ruling (purplellama P5 r2 Q4, lessons 12): R9 cites the public gate and tree pages, not API paths; the Hub facts keep their tree-URL pins")
    for u in (PGB + "Llama-Prompt-Guard-2/86M/USE_POLICY.md", PGB + "LICENSE", PGB + "README.md",
              CBB + "inference.py", CBB + "prompt_guard_tutorial.ipynb", "https://dev.meta.ai/docs/overview", "https://dev.meta.ai/docs/models"):
        K.add_url(C, u, "T6, T8, T23, T25: page or file cited in R4 to R6")
    K.summary(C, 9, "Summary: Meta Prompt Guard model cards and licence files in the PurpleLlama repo, Meta docs pages, the llama-cookbook files, Hugging Face gate pages and model pages, and the LlamaFirewall paper.",
              "R9 Summary lists the new sources (cookbook, Meta Model API pages)")

    # ============================================================ PL2
    C = "PL2"
    K.ins_after(C, 1, "Selected in configuration by the scanner type",
        '• Role selection: the framework runs only the scanners configured for the message\'s role: "scanners = self.scanners.get(input.role, [])" (llamafirewall.py@172c1074:113) ' + PR,
        "T95 (PL2 R1 part; r1 and r2 agree): supports the Summary clause 'the message role decides whether it runs'")
    K.sub(C, 1, "Role of the wrapper versus the model", "described in column PL1", 'described in the "' + HDR1 + '" column',
          "T101: draft id replaced by the header text", kind="style")
    K.sub(C, 2, "Scope wording differs", "(PL1 column)", "(Prompt Guard 2 column)", "T101", kind="style")
    K.repl(C, 2, "Out of scope: the scanner does not read tool-call arguments", [
        "• Tool-call arguments: the message type has an optional tool_calls field, which appears in LlamaFirewall/src only in llamafirewall_data_types.py (lines 54, 77, 79); this scanner reads message.content only (prompt_guard_scanner.py@172c1074:34) " + PR,
        "• Scanning of function-call arguments by any LlamaFirewall scanner (searched LlamaFirewall/src, README, docs pages and paper; no scanner or page describes it) " + ND],
        "T45 (r1 and r2 agree): grep re-run and named; per R020 the absence is Not disclosed with the search named", kind="replace")
    K.repl(C, 3, "The message type has an optional `tool_calls` field, but this scanner does not read it", [
        "• Tool-call arguments: the message type has an optional tool_calls field, which appears in LlamaFirewall/src only in llamafirewall_data_types.py (lines 54, 77, 79); this scanner reads message.content only (prompt_guard_scanner.py@172c1074:31-34) " + PR,
        "• Scanning of function-call arguments by any LlamaFirewall scanner (searched LlamaFirewall/src, README, docs pages and paper; no scanner or page describes it) " + ND,
        "• So a malicious function-call argument is seen only if it also appears in the message content (premise: the scanner reads message.content only) " + INF],
        "T45", kind="replace")
    K.sub(C, 3, "Meta's own AgentDojo evaluation scanned only user and tool messages with it", "(arXiv 2505.03574 section 4.3)",
          "(arXiv 2505.03574 section 4.3.1)", "T103", kind="style")
    K.sub(C, 3, "Name conflict: the custom use case page uses", "(adding-custom-use-case.md@172c1074:19-20)",
          "(adding-custom-use-case.md@172c1074:19-20; live docs page also read 2026-10-09)", "T43: live page re-read, the defect is confirmed")
    # R4
    K.repl(C, 4, "The framework builds a new scanner object for each scan call", [
        "• The framework creates a new scanner for every scan call (create_scanner at llamafirewall.py@172c1074:118), the PromptGuard scanner constructor creates PromptGuard (prompt_guard_scanner.py@172c1074:29), and that constructor loads the model and tokenizer (promptguard_utils.py@172c1074:30,72-75) " + PR,
        "• Reuse of one loaded model across scan calls (searched LlamaFirewall/src for cache, lru_cache, singleton and instance-level reuse; none found) " + ND,
        "• Model loading from disk may therefore happen on every scan call (premise: the construction chain above) " + INF],
        "T35 (r1): the construction chain is documented code; the absence names its search; the cost stays an inference", kind="replace")
    K.sub(C, 4, "The last class is taken to be \"malicious\"",
        "(premise: the card lists two labels, benign then malicious, and the Hugging Face config is not readable without approved access)",
        "(premise: the card lists two labels, benign then malicious; the cookbook scores index 1 as the jailbreak class; the gated Hugging Face config was not read)",
        "Supplementary 4 (T37 partial)")
    K.repl(C, 4, "PyPI simple index lists llamafirewall 1.0.3 as the latest file", [
        "• PyPI lists llamafirewall 1.0.3 as the latest of 13 releases (PyPI simple index, observed 2026-10-09) " + DOC,
        "• The 1.0.3 sdist (PyPI sdist llamafirewall-1.0.3, sha256 54fe55c8, read 2026-10-09) has promptguard_utils.py calling HfFolder.get_token() and loading the tokenizer without fix_mistral_regex (src/llamafirewall/scanners/promptguard_utils.py lines 12, 59, 66, 73) " + DOC,
        "• At the pin, promptguard_utils.py uses huggingface_hub get_token and passes fix_mistral_regex=True (promptguard_utils.py@172c1074:12,57,64-66,73-75) " + PR,
        "• The sdist has the same PromptGuard scanner file as the pin, so the model loader is the one behavioural difference found in this scanner's files (premise: file-by-file comparison of the unpacked sdist with LlamaFirewall/ at the pin, line endings ignored) " + INF,
        "• The pinned code is newer than release 1.0.3: the version was set on 2025-05-28 (commit 55ff24c) and promptguard_utils.py changed on 2026-01-16 (e4c281b) and 2026-03-26 (9a3d175) " + PR],
        "T20 (r1 and r2): sdist read and compared; sdist facts use [Documented] with the sdist, hash and date in plain text, comparisons are [Inferred] (main ruling on the PyPI label form)", kind="replace")
    K.repl(C, 4, "LlamaFirewall code is MIT licensed; the model keeps its own Llama 4 licence", [
        "• LlamaFirewall code is MIT licensed (LlamaFirewall/LICENSE@172c1074:1) " + PR,
        "• The model this scanner downloads, meta-llama/Llama-Prompt-Guard-2-86M, is under the Llama 4 Community License (license_name llama4; Hugging Face Hub model metadata, read 2026-10-09; see the Prompt Guard 2 column) " + G86],
        "T17, T101: two facts, two labels; draft id replaced", kind="replace")
    K.sub(C, 4, "Release notes for llamafirewall", "PyPI lists versions 1.0.2 and 1.0.3 without notes", "PyPI lists 13 releases without notes",
          "T20: PyPI lists 13 releases (0.0.0 to 1.0.3)")
    # R5
    K.sub(C, 5, "A Meta-recommended threshold for the scanner or model",
        "(checked the README, docs pages, tutorials, paper and model card; none gives one)",
        "(checked the README, docs pages, tutorials, paper including Appendix B, model card and the llama-cookbook files; none gives one)", "T26")
    K.ins_after(C, 5, "Code behaviour differs from that sample",
        '• History: the benign sample reason "default" with score 0.0 matches scan() as released on 2025-04-29 (commit cd9fe65) and was replaced by single-scanner pass-through on 2025-05-28 (commit 55ff24c); the docs page was last edited on 2025-04-29; the blocked sample reason "prompt_guard" matches no scanner reason text in either version ' + PR,
        "T40 (PL2 half, r1): git history read")
    K.sub(C, 5, "Paper, AgentDojo with Prompt Guard 2 86M on user and tool messages", "(arXiv 2505.03574 section 4.3)",
          "(arXiv 2505.03574 sections 4.3.1 and 4.3.2)", "T103", kind="style")
    # R6
    K.summary(C, 6,
        "Summary: **A message with role and text content, plus gated model access.** Weights are downloaded from Hugging Face on first use, with an interactive login if no token exists. Python 3.10 or later is needed, and text over 512 tokens is truncated. " + DOC,
        "T94 (r2): the class name 'Message' is a code identifier; the truncation clause now has a documented R6 bullet")
    K.ins_before(C, 6, "Only content is scanned and truncated at 512 tokens",
        '• Truncation: the tokenizer call uses "padding=True, truncation=True, max_length=512" (promptguard_utils.py@172c1074:113) ' + PR,
        "T94 (r2 text): documented truncation bullet in the row the Summary draws on")
    K.ins_after(C, 6, "Access: the Hugging Face repo is gated, and without a token", [
        '• The README\'s manual setup offers two routes: "Preload the Model" to the local cache directory, or log in to Hugging Face so missing models download automatically (LlamaFirewall/README.md@172c1074:159-170) ' + PR,
        "• The model folder the code checks is $HF_HOME/meta-llama--Llama-Prompt-Guard-2-86M, written by save_pretrained; with that folder present and no token the login() call is not reached (premise: promptguard_utils.py lines 53-61) " + INF],
        "T42 (CORRECTION, r1): the README does describe a preload route; the folder layout is what it does not describe")
    K.repl(C, 6, "Interactive login may block a headless test run",
        '• Without a token and without the folder, login() prompts in the terminal (Hugging Face docs: "Displays a prompt to log in to the HF website and store the token"; promptguard_utils.py@172c1074:57-61), which may block a headless run ' + INF,
        "T42", kind="replace")
    K.repl(C, 6, "Prerequisite text says", [
        '• The prerequisite line says "Access to HuggingFace Meta\'s Llama 3.1 models & evals" and links a Hugging Face collection that, on 2026-10-09, was last updated Dec 13, 2024 and lists Prompt-Guard-86M, not the Prompt Guard 2 repos (LlamaFirewall/README.md@172c1074:55; collection page) ' + DOC,
        "• The line is probably out of date for the Llama 4 licensed Prompt Guard 2 model (premise: the collection predates it) " + INF],
        "T41 (r1): two facts and an inference", kind="replace")
    K.repl(C, 6, "The synchronous scan call uses asyncio.run", [
        "• The synchronous scan call runs the scanner with asyncio.run (llamafirewall.py@172c1074:122) " + PR,
        '• asyncio.run "cannot be called when another asyncio event loop is running in the same thread" (Python asyncio-runner docs, not Meta docs, read 2026-10-09) ' + DOC,
        "• The synchronous scan call therefore cannot be used inside a running event loop; scan_async is the route there (premise: the two facts above) " + INF],
        "T44 (r1)", kind="replace")
    K.repl(C, 6, "No scanner timeout or size limit is set in code",
        "• Scanner timeout or input size limit other than the 512-token truncation (searched LlamaFirewall/src for timeout, split, chunk and max_length; only promptguard_utils.py line 113 matches) " + ND,
        "T44 (r1): absence with the search named (R020)", kind="replace")
    # R7
    K.summary(C, 7,
        "Summary: **Minimum setup:** install llamafirewall, accept the Llama 4 licence on Hugging Face so the 86M model can download, configure a USER role with the PromptGuard scanner, and scan labelled strings. "
        "A bench could also set the threshold explicitly and try other roles for retrieved text and tool output. " + INF,
        "R032 (r1): proposal wording")
    K.repl(C, 7, "Record the score for every case, not only the decision",
        "• A bench could record the score for every case, not only the decision, so that thresholds from 0.5 to 0.99 can be compared with the 0.9 default (premise: the score field in `ScanResult`) " + INF,
        "R032", kind="style")
    K.repl(C, 7, "Compare scan on `USER` with the model run directly",
        "• A bench could compare scan on `USER` with the model run directly (Prompt Guard 2 column) to see whether the wrapper adds differences beyond whitespace cleaning and truncation (premise: preprocessing code) " + INF,
        "R032, T101", kind="style")
    K.repl(C, 7, "Time the first scan separately from later scans",
        "• A bench could time the first scan separately from later scans, because the model may be loaded on every call (premise: create_scanner inside scan) " + INF,
        "T35 (r1), R032", kind="style")
    # R8
    K.summary(C, 8,
        "Summary: **Key open questions.** No recommended threshold, unknown scanner latency, model reloading per call, silent truncation of long text, a docs sample output that differs from the code, and whether the model's Llama 4 terms allow attack-prompt testing.",
        "T6 (r1): the licence question is now an R8 bullet of this column")
    K.sub(C, 8, "Recommended block threshold, and how the 0.9 default relates",
        "(checked the README, docs pages, paper and card; not stated)", "(checked the README, docs pages, paper, card and the cookbook files; not stated)", "T26")
    K.repl(C, 8, "Whether the last class probability is the malicious class in the gated model config",
        "• Whether the last class probability is the malicious class in the gated model config (the cookbook scores index 1 as malicious and the wrapper takes the last index; the gated config was not read; needs testing)",
        "Supplementary 4 (T37 partial)", kind="replace")
    K.repl(C, 8, "Whether the docs sample output (reason",
        "• Which output a user sees for a single scanner: the docs sample (reason 'default', 'prompt_guard') or the code (scanner reason text and probability); the docs page predates commit 55ff24c, and the code is the later behaviour (checked the git history)",
        "T40 (PL2 half, r1): history read; the question narrows to what a run shows", kind="replace")
    K.repl(C, 8, "How a hosted or air-gapped deployment obtains the gated weights", [
        '• Whether a hosted or air-gapped deployment can use the preload route: the README says to preload the model to "~/.cache/huggingface" and the code looks for a folder named meta-llama--Llama-Prompt-Guard-2-86M under HF_HOME, a layout the README does not describe (needs testing)',
        "• Whether the Llama 4 licence and Acceptable Use Policy that govern the model this scanner downloads (see the Prompt Guard 2 column) limit testing with attack prompts (licensing question)"],
        "T42 (CORRECTION), T6", kind="replace")
    # R9
    for u in ("https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M/tree/a8ded8e697ce7c355e395a0df51f94adb4a2fd27",
              "https://pypi.org/project/llamafirewall/",
              "https://files.pythonhosted.org/packages/70/f5/9dbd3b0a74c11323d967b0e1210a9fac0de068abc0c2e5dc08a6ee2094a5/llamafirewall-1.0.3.tar.gz",
              "https://docs.python.org/3/library/asyncio-runner.html",
              "https://huggingface.co/collections/meta-llama/metas-llama-31-models-and-evals",
              "https://huggingface.co/docs/huggingface_hub/en/package_reference/authentication",
              CBB + "inference.py"):
        K.add_url(C, u, "T17, T20, T41, T42, T44: page or file cited in R4 to R6")
    K.summary(C, 9, "Summary: LlamaFirewall source files, README and docs pages in the PurpleLlama repo, the PyPI index and sdist, the Prompt Guard 2 model card, Hugging Face and Python documentation pages, and the LlamaFirewall paper.",
              "R9 Summary lists the new source kinds")
