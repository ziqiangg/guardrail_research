# LionGuard: Summary preview (Checkpoint 2)

Generated from lionguard_two_level.md on 2026-10-10. Format: `Rn` (words excluding the trailing label, top-level Detail bullets): Summary text. Limits: 45 words, R7 60.

## LN1: LionGuard: Localised harmful-content classification

- **R1** (44w, 12 bullets): **Localised harmful-content classification of one text string.** LionGuard is GovTech's classifier for Singapore's languages and context. It returns a probability for each harm category and severity level. GovTech publishes the classifier on Hugging Face; two variants embed text through OpenAI or Gemini, one locally. **[Documented]**
- **R2** (43w, 20 bullets): **Six harm categories plus an overall flag, with severity levels.** Hateful, insults, sexual, physical violence, self-harm and all other misconduct; four have Level 1 and Level 2. Covers English, Singlish, Chinese, Malay and Tamil; the playbook and paper call Tamil partial or moderate. **[Documented]**
- **R3** (39w, 12 bullets): **Any single text, before or after the model.** GovTech's paper shows it as both an input filter for user prompts and an output filter for model responses. The classifier call takes only an array of embeddings of the text. **[Documented]**
- **R4** (40w, 52 bullets): **Frozen embedder plus a small ordinal classifier.** The three variants differ in the embedder: OpenAI embeddings (LionGuard 2), Gemini embeddings (2.1) or local EmbeddingGemma (2 Lite). GovTech publishes the small classifier and its code on Hugging Face, not the embedder. **[Documented]**
- **R5** (39w, 36 bullets): **A probability per key, no verdict.** The model returns 11 probabilities from 0 to 1 and applies no cut-off. GovTech's paper reports binary F1 at a 0.5 point, for example 77.0 for LionGuard 2 on its own test set. **[Documented]**
- **R6** (38w, 24 bullets): **One text string, embedded first.** Embed the text with the variant's own embedder (OpenAI key, Gemini key, or local EmbeddingGemma with a task prefix), then pass the vectors to the classifier. Input widths are 3072, 3072 and 768. **[Documented]**
- **R7** (59w, 32 bullets): **Minimum setup:** Python with Hugging Face Transformers and PyTorch, loading each model with remote code enabled. LionGuard 2 Lite also needs a Hugging Face login and acceptance of Google's Gemma terms for its embedder, but no API key. LionGuard 2 needs an OpenAI key and 2.1 a Gemini key, so test text goes to those providers. No threshold ships. **[Inferred]**
- **R8** (36w, 14 bullets): **Key open questions.** Operating threshold per variant, any Lite or wider 2.1 evaluation, input length and latency, how the licence texts relate, embedder terms for test text, whether a retrained model is released, and jailbreak coverage.
- **R9** (27w, 31 bullets): GovTech Hugging Face model repos, datasets and demo Space, the Responsible AI playbook, GovTech blog posts and papers, Sentinel docs for cross-references, and the embedder owners' pages.

## Summaries changed in the merge

| Location | Words before | Words after | Reason |
|---|---|---|---|
| LN1 R1 | 37 | 44 | T49 (R031): drops 'you run it yourself from open Hugging Face weights' (embedding step is hosted for 2 and 2.1; 'open' depends on the unresolved licence reading T6) |
| LN1 R2 | 38 | 43 | T27: the Summary no longer picks the playbook's 'partial Tamil' alone; names the playbook and paper wording (43 words) |
| LN1 R3 | 39 | 39 | style 2: code identifier 'predict' removed from the Summary |
| LN1 R4 | 40 | 40 | T50: 'publishes only the small classifier' replaced; GovTech also publishes the model code and a training-data subset (the 'no training code' fact stays a Not disclosed bullet) |
| LN1 R6 | 37 | 38 | style 2: code identifier 'predict' removed from the Summary |
| LN1 R7 | 50 | 59 | T51, style 2: Hugging Face login added for Lite; package names removed from the Summary; 'Pick your own threshold' reworded (59 words) |
| LN1 R8 | 31 | 36 | T13: 'the licence reading' and 'embedder terms' reworded as questions (36 words, no label) |
| LN1 R9 | 27 | 27 | P7 optional: R9 cites two datasets |
