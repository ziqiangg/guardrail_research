# Q13 — Extra LlamaFirewall scanner columns beyond the R004 list (Hidden ASCII, PII check, custom LLM scanners)?
- Product: purplellama   Phase: P0   Asked by: explorer (20261009_purplellama_p0-code.md PL7, PL8, C5)
- Context: Code (172c1074) has ScannerType values HIDDEN_ASCII and PII_DETECTION and an experimental CustomCheckScanner (LLM prompt scanner); the README and docs list only PromptGuard, AlignmentCheck, Regex + Custom, CodeShield. R004 says split further only if evidence shows distinct functions (a CP1 question). Hidden ASCII is a distinct function (Unicode tag smuggling); PIICheck is an LLM-prompt PII detector with default model Llama 3.3 70B via Together; regex scanner also covers email, phone, card, SSN patterns.
- Options: (a) add PL7 (custom LLM scanners incl. PII) and PL8 (Hidden ASCII) as columns; (b) merge both into the R004 "regex/custom" column; (c) keep them in the inventory only (`— (inventory only, not in Table 3)`), since not in vendor docs' scanner list.
- Asker's recommendation: (a) for Hidden ASCII (code-only but functional and stable, no external dependency), (c) for PIICheck and CustomCheckScanner (marked experimental); needs CP1.
- Blocking? no.
