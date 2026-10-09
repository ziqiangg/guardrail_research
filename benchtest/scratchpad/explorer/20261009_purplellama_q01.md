### Q01 - Header prefix: Purple Llama or per-tool
- Product: purplellama   Phase: P0   Asked by: explorer (20261009_purplellama_p0-docs.md section 2)
- Context: R004 defers the prefix to CP1. Meta writes the tool names itself: "Llama Prompt Guard 2", "LlamaFirewall", "CodeShield" / "Code Shield". The header rule says the prefix is the product's own name as its owner writes it.
- Options: (a) `Purple Llama: <function (tool)>` for all six columns; (b) per-tool prefixes `Prompt Guard 2:`, `LlamaFirewall:`, `Code Shield:`; (c) mixed.
- Asker's recommendation: (b). Both header sets are in the P0 note.
- Blocking? no, CP1 decision. Note that HDR_RE derives from products.py, so option (b) needs three prefixes registered at P8.
