# Q15 — Separate columns for engines and their LlamaFirewall wrappers (Prompt Guard 2 vs PromptGuard scanner; Code Shield vs CodeShield scanner)?
- Product: purplellama   Phase: P0   Asked by: explorer (20261009_purplellama_p0-code.md PL1/PL2, PL4/PL5)
- Context: R004 lists Prompt Guard 2, each LlamaFirewall scanner, and Code Shield as separate columns. The wrappers add only thresholds (0.9 for PromptGuard scanner; BLOCK on any issue for CodeShield scanner), role configuration and ScanResult shape; the engine and rules are identical (prompt_guard_scanner.py, code_shield_scanner.py at 172c1074). Duplicate columns make four near-identical test targets, but sheet 4 grouping may want distinct integration surfaces (model vs library vs framework).
- Options: (a) keep four columns as R004 says; (b) merge wrapper into engine column and describe the scanner in Detail; (c) keep columns but cross-reference rows R4 to avoid duplicated facts.
- Asker's recommendation: (a) with cross-references (c), since R004 is explicit and the test setups differ (raw model vs framework call).
- Blocking? no.
