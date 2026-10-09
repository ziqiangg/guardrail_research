# Q14 — Pin form: PurpleLlama has no release or tag
- Product: purplellama   Phase: P0   Asked by: explorer (20261009_purplellama_p0-code.md section 1)
- Context: `git ls-remote --tags` empty and GitHub MCP `list_releases` returns `[]` for meta-llama/PurpleLlama; HEAD is 172c1074069eb88ec834124272c1b1c4f8893445 (2026-09-29). Packages on PyPI: llamafirewall 1.0.3 (matches repo pyproject), codeshield 1.0.1 (repo pyproject says 0.0.1). HF repos pinned by revision sha. drafts/README.md rule 8 says pin to latest tag unless seed or ruling says otherwise; seed says re-pin to latest commit or tag.
- Options: (a) pin code to sha `172c1074` and cite PyPI versions separately in plain text; (b) additionally cite PyPI sdist content for CodeShield 1.0.1 (not fetched); (c) wait for a tag.
- Asker's recommendation: (a). R015 release-note substitute is unavailable (no CHANGELOG); record as `[Not disclosed]`.
- Blocking? no.
