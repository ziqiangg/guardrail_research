# purplellama P1 verification log (20261009), gr-drafter
Pin re-checked: `git ls-remote https://github.com/meta-llama/PurpleLlama HEAD` -> 172c1074069eb88ec834124272c1b1c4f8893445; `git ls-remote --tags` -> empty. Clone HEAD equals pin.
HF API (fetch_text.py, status 200): 86M sha a8ded8e697ce7c355e395a0df51f94adb4a2fd27; 22M sha 11614a155199674a0a95e6602d6ab0417b790ed0; v1 sha 1209add6ca7d9c1d815171b8e5571587fe3e7b03; all gated manual.
PyPI simple index: llamafirewall 1.0.3 (latest file), codeshield 1.0.1 (latest).
Code reads at pin (clone, read not run): see the conflict table in the brief for file:line.
Live pages fetched verbatim: dev.meta.ai/llama/llama-protections (7 languages, 200ms), arxiv.org/html/2505.03574 (8/eight at lines 92,112; seven at 353; 60 ms vs under 70 ms), meta-llama.github.io LlamaFirewall tutorials/regex-scanner-tutorial, tutorials/prompt-guard-scanner-tutorial (names HIDDEN_ASCII, PII_DETECTION), getting-started/adding-custom-use-case (PROMPT_INJECTION).
Docs-note gap closed: the docs site does have a regex page, under /tutorials/ (not /documentation/scanners/).
