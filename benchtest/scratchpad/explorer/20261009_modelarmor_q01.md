### Q01 - Model Armor column split and count
- Product: modelarmor   Phase: P0   Asked by: explorer (20261009_modelarmor_p0.md section 2)
- Context: R002 defines direction as a property of the product's own surface; Model Armor has `sanitizeUserPrompt` and `sanitizeModelResponse` (plus streaming variants) and advises separate input and output templates. Filters, thresholds and result schema are identical across directions.
- Options: (a) 10 columns MA1-MA10 as in the P0 note; (b) 6 columns using the R002 exception; (c) (a) with MA9/MA10 folded into Detail; (d) add MA11 for MCP tool screening and/or antivirus.
- Asker's recommendation: (a), antivirus and MCP in inventory unless a config doc for antivirus appears.
- Blocking? no, CP1 decision.
