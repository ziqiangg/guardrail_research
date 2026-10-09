### Q04 - AlignmentCheck depends on an external hosted LLM
- Product: purplellama   Phase: P0   Asked by: explorer (p0-docs section 5, gaps 3 and 4)
- Context: Docs say the alignment check scanner needs `TOGETHER_API_KEY`. The detector is an LLM call, so testing sends agent traces to a third-party API; the paper tested Llama 4 Maverick and Llama 3.3 70B. Meta documents no default model or cost. Applies R011 and R019.
- Options: (a) Table 3 column PL3 with R7 stating the external key, labelled `[Inferred]` for any minimal setup; (b) inventory only with the R011 marker.
- Asker's recommendation: (a), since it is a runtime LlamaFirewall scanner under R004.
- Blocking? no.
