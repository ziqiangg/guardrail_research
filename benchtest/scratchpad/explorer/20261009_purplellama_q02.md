### Q02 - Same model or engine in two wrappers; direction label for AlignmentCheck
- Product: purplellama   Phase: P0   Asked by: explorer (p0-docs section 2)
- Context: R004 asks for Prompt Guard 2 and the LlamaFirewall PromptGuard scanner as separate columns, and Code Shield and the LlamaFirewall CodeShield scanner likewise. The model and engine are the same; the LlamaFirewall docs add role-based configuration (USER, SYSTEM, ASSISTANT, TOOL), allow/block decisions with a score, and the CHAT_BOT and CODING_ASSISTANT use cases. AlignmentCheck reads an agent trace, which is neither input nor output under R002.
- Options: (a) keep six columns PL1-PL6 as in the note, with PL2 and PL4 R-rows pointing back to PL1 and PL6 for shared facts; (b) merge each pair, giving four columns; (c) keep six and label AlignmentCheck "Trace-level" as a new level word.
- Asker's recommendation: (a) plus (c). R002 says wrappers with per-direction flows keep their own columns.
- Blocking? no, CP1.
