# Q12 — R002 direction: do LlamaFirewall scanners split into input and output columns by role?
- Product: purplellama   Phase: P0   Asked by: explorer (20261009_purplellama_p0-code.md PL2, PL5, PL6)
- Context: LlamaFirewall takes `Configuration = Mapping[Role, Sequence[ScannerType]]` with roles USER, SYSTEM, ASSISTANT, TOOL, MEMORY (config.py, llamafirewall.py at 172c1074). The same PromptGuard scanner can be attached to USER (input) or TOOL (retrieved/tool output) or ASSISTANT. R002 says a wrapper with per-direction flows keeps its split, but the scanner behaviour itself is identical across roles and there are five roles, not two. Prompt Guard 2 model alone is a string classifier (one column).
- Options: (a) one column per scanner, R3/R6 list roles (like Sentinel AA exception); (b) split PromptGuard scanner into input (USER/SYSTEM) and tool-output/retrieval columns; (c) split every scanner by role.
- Asker's recommendation: (a), because no per-direction flag or rail exists and the scanner logic is role-agnostic; record role default tables in Detail and inventory block (c).
- Blocking? no (CP1).
