# Llama Guard resolutions, agent 1 (model cards, Meta docs, papers, evaluations, dates, licences)

Items: T1, T3, T5, T6, T7, T8, T9, T11, T12, T20, T25, T26, T27, T39, T40, T41, T42, T43, T44, T46, T47, T48, T49, T50, T52, T53, T57, T58, T59 (29 items). Nothing else was edited.

## Method and access notes (read first)

- Short names. PL = `https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/` (append the path shown). DOCS2/3/4 = `https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/{meta-llama-guard-2,llama-guard-3,llama-guard-4}/`. PROT = `https://dev.meta.ai/llama/llama-protections/`. HF = `https://huggingface.co/meta-llama/<model>`.
- Nothing below came from a summarising fetch. WebFetch was not used. Every page was downloaded with curl and searched as raw text:
  - dev.meta.ai docs and protections pages: plain HTML, readable.
  - arXiv `/html/` versions of 2312.06674, 2411.10414, 2411.17713, 2407.21783 and the `/abs/` pages.
  - PurpleLlama model cards: GitHub blob pages with `?plain=1`, raw lines extracted from the embedded JSON at commit 172c1074.
  - HF model pages: gated, but the public page renders the full card, so the card text was read there. HF `/api/models/...` JSON gave createdAt, file sizes and chat templates. HF LICENSE files were read from the blob pages.
  - ai.meta.com blog posts.
- Not readable: HF `config.json` and raw `README.md` (HTTP 401, gated). So no `max_position_embeddings` value exists in this evidence (T5). `raw.githubusercontent.com` was not used.
- Quote rule. Quotes are verbatim, each under 40 words. Where a sentence is longer it is split.
- Out-of-list source. T46 uses the Llama 3 paper (arXiv 2407.21783). It is Meta-authored and cited by the 3-8B card, but it is not in the brief's paper list. If you want to stay strictly inside the list, treat T46 as a Reviewer-note item only.
- HTML artefact. The arXiv HTML of 2411.10414 prints "date: August 24, 2026" under the abstract. This is a build-date artefact. The `/abs/` page says "[Submitted on 15 Nov 2024]" and lists only v1.

---

### T1 — Is any first-token "unsafe" probability threshold documented?
- Verdict: RESOLVED. "No numeric threshold" stands for 3-8B, 3-8B-INT8, 3-1B, 3-1B-INT4, 3-11B-V and LG4. One minor CORRECTION is needed in the inventory (3-8B-INT8 Score method cell, below).
- Evidence:
  - 3-8B card (PL `Llama-Guard3/8B/MODEL_CARD.md`): "we look at the probability for the first token, and use that as the “unsafe” class probability. We can then apply score thresholding to make binary decisions."
  - 3-8B-INT8 HF page (`https://huggingface.co/meta-llama/Llama-Guard-3-8B-INT8`) repeats the same two sentences verbatim. The INT8 card does give the method.
  - LG2 card (PL `Llama-Guard2/MODEL_CARD.md`): "For obtaining a binary classification decision from the score, we use a threshold of 0.5."
  - LG1 card (PL `Llama-Guard/MODEL_CARD.md`): "Model users can then make binary decisions by applying a desired threshold to the probability scores." No value.
  - LG1 paper appendix B (`https://arxiv.org/html/2312.06674`): "We set every threshold to 0.5 and compute Precision, Recall and F1 Score."
  - Absence, checked as full raw text. The words threshold, probability and score do not occur as a method statement in the 3-1B card (PL and HF), the 3-1B-INT4 HF card, the 3-11B-Vision card (PL and HF), the LG4 card (PL and HF), DOCS2, DOCS3, DOCS4, PROT, the 2411.10414 paper or the 2411.17713 paper. The only hit is "F1 score" in the 11B card.
  - 3-1B-INT4: PL `Llama-Guard3/1B/ET_INSTRUCTIONS.md` uses `argmax(-1)` and the comment "19193 is safe, 39257 is unsafe". No probability.
- Label to use: [Documented] for the 3-8B and INT8 method, LG2's 0.5 and LG1's "desired threshold". [Not disclosed] for the numeric value on LG3 and LG4 versions.
- Draft impact:
  - A LG1 R5 Detail bullet 5 ("LG3-1B and LG4 cards (HF fetch) give no threshold guidance … absence in fetched text") is labelled [Documented], but an absence is not documentation (Contradiction 23). Replace with: "No numeric threshold or score method appears on the LG3-1B, LG3-1B-INT4, LG3-11B-Vision or LG4 cards, in the Meta LG3 and LG4 docs pages, or in the 11B-Vision and 1B-INT4 papers (full text searched) **[Not disclosed]**".
  - A LG1 R5, add: "LG2 card: score is the first-token probability and the evaluation uses a threshold of 0.5 **[Documented: repo PurpleLlama@172c1074]**".
  - A LG1 R5, add: "LG1 card leaves the threshold to the user; the LG1 paper uses 0.5 for its precision, recall and F1 tables **[Documented]**".
  - A LG2 R5 Detail bullet 3 ("No numeric threshold for LG3-8B, LG3-1B, LG3-11B-Vision or LG4 [Not disclosed]") is correct, so keep it.
  - INV(a) 3-8B-INT8 Score method. The draft says "Card does not give a separate method for INT8 [Not disclosed]". Replace with "Same as 3-8B: the INT8 card repeats first-token probability and 'apply score thresholding'; no value **[Documented]**".
  - INV(a) 3-1B, 3-11B-V and LG4 Score method cells stay [Not disclosed].
  - B LG3 R5, B LG3 R8 and B LG4 R4 Score bullets are correct as written.
- Changes Summary? N. A LG1 R5 and A LG2 R5 Summaries stay true.

### T3 — Any official latency or throughput figure?
- Verdict: CORRECTION. The drafts (A LG1 R4 and A LG2 R4 "No official latency figures found [Not disclosed]", and both R8 Summaries) say there is none. One official figure exists, for LG3-1B-INT4 only. No figure exists for any other version.
- Evidence:
  - arXiv 2411.17713 abstract (`https://arxiv.org/abs/2411.17713`): "achieving a throughput of at least 30 tokens per second and a time-to-first-token of 2.5 seconds or less on a commodity Android mobile CPU."
  - Same paper, section 4 (`https://arxiv.org/html/2411.17713`): "we deployed the model to a Moto-Razor phone". The HTML garbles the inequality signs; the abstract is unambiguous.
  - Same paper, section 2.2: ExecuTorch "also enables leveraging neural network accelerators … although we did not take advantage of this capability". Prompt length, batch size and output length are not stated.
  - Searched for latency, throughput, tokens/s, time-to-first and ms, and found nothing in: the 3-8B, 3-8B-INT8, 3-1B, 3-11B-V, LG4, LG1 and LG2 cards; DOCS2, DOCS3, DOCS4; the 2312.06674 and 2411.10414 papers; the ai.meta.com posts for Llama 3.2 (2024-09-25), LlamaCon and the defenders post (both 2025-04-29).
  - PROT's "average latency of 200ms" belongs to Code Shield, which is out of scope.
- Label to use: [Documented] for the INT4 figure. [Not disclosed] for every other version.
- Draft impact:
  - A LG1 R4 last bullet and A LG2 R4 last bullet. Replace "No official latency figures found [Not disclosed]" with two bullets:
    - "Only official speed figure: LG3-1B-INT4 on a Moto-Razor Android phone CPU with ExecuTorch and no accelerator reached at least 30 tokens per second and a time-to-first-token of 2.5 s or less; prompt length not stated **[Documented]** (arXiv 2411.17713)".
    - "No official latency or throughput figure for LG4, LG3-8B, LG3-8B-INT8, LG3-1B (bf16) or LG3-11B-Vision **[Not disclosed]**".
  - INV(c) ExecuTorch row Caveats. Replace "the paper abstract gives at least 30 tokens/s on mobile" with "paper: at least 30 tokens/s and time-to-first-token 2.5 s or less on a Moto-Razor phone CPU; prompt length not stated [Documented]". INV(a) 3-1B-INT4 Headline eval gets the same addition.
  - A LG1 R8 and A LG2 R8 Summaries must change (new text below).
- Changes Summary? Y. New A LG1 R8 Summary (30 words): "**Key open questions.** No documented decision threshold, unclear LG4 language coverage (which 12 languages), no prompt-only numbers for LG3-1B or LG4, and latency figures only for LG3-1B-INT4 on one phone." New A LG2 R8 Summary (26 words): "**Key open questions.** No documented decision threshold, conflicting LG4 language statements, no like-for-like response numbers across versions, and latency figures only for LG3-1B-INT4 on one phone."
- Also change the R8 Detail bullet "Official latency and throughput figures" in both columns to "Latency and throughput for versions other than LG3-1B-INT4 (only one phone measurement exists)".

### T5 — Context length of each variant
- Verdict: PARTLY RESOLVED (checked all eight HF cards, PL cards, DOCS2/3/4 and the three papers; no guard card states a context length; HF `config.json` is gated, HTTP 401).
- Evidence:
  - LG1 paper: "with sequence length of 4096" (training sequence length, `https://arxiv.org/html/2312.06674`).
  - 11B-V paper section 3.3: "We perform supervised fine-tuning using a sequence length of 8192" (`https://arxiv.org/html/2411.10414`).
  - Base-model HF cards, context length column:
    - Llama-2-7b-hf: 4k.
    - Meta-Llama-3-8B: 8k.
    - Llama-3.1-8B: 128k.
    - Llama-3.2-1B: 128k.
    - Llama-3.2-11B-Vision: 128k.
    - Llama-4-Scout-17B-16E: 10M (table row "Context length", value "10M").
  - Meta Llama 3.2 post (`https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/`): "The Llama 3.2 1B and 3B models support context length of 128K tokens".
- Label to use: [Documented] for the two fine-tuning sequence lengths. [Inferred] for any base-model value applied to a guard model (the guard cards never say it is inherited, and the LG1, 3-1B and LG4 guards are pruned or fine-tuned). [Not disclosed] for the guard's own context length.
- Draft impact (INV(a) "context" text, one change per row):
  - LG1: keep "Fine-tune sequence length 4096". Change its label from "[Documented: arXiv paper, summarised fetch]" to [Documented] (arXiv HTML read raw). Context [Not disclosed]. Add "base Llama 2 7B card: 4k [Inferred]".
  - LG2: context [Not disclosed]; add "base Llama 3 8B card: 8k [Inferred]".
  - 3-8B and 3-8B-INT8: context [Not disclosed]; add "base Llama 3.1 8B card: 128k [Inferred]".
  - 3-1B and 3-1B-INT4: context [Not disclosed]; add "base Llama 3.2 1B card: 128k [Inferred]; INT4 is pruned and quantised, so inheritance is not documented".
  - 3-11B-V: context [Not disclosed]; add "fine-tune sequence length 8192 [Documented] (arXiv 2411.10414 section 3.3); base card 128k [Inferred]".
  - LG4: context [Not disclosed]; add "base Llama 4 Scout card: 10M [Inferred]; LG4 is a 12B dense pruning, inheritance not documented".
  - Not-found list: "Context length for every variant" becomes "No guard card states a context length; HF config.json is gated".
- Changes Summary? N.

### T6 — LG4 language coverage (card vs DOCS4 vs PROT)
- Verdict: PARTLY RESOLVED. The card's list is explicit and the best-supported claim. The "12 languages" in PROT has no list anywhere in the LG4 sources, so which 12 stays open.
- Evidence:
  - LG4 card (PL `Llama-Guard4/12B/MODEL_CARD.md`; HF page identical): "supporting English and multilingual text prompts (on the languages supported by Llama Guard 3)".
  - Same card, evaluation note: "an average over the 7 shipped non-English languages of Llama Guard 3-8B: French, German, Hindi, Italian, Portuguese, Spanish, and Thai".
  - LG3-8B card: "Llama Guard 3 supports content safety for the following languages : English, French, German, Hindi, Italian, Portuguese, Spanish, Thai."
  - DOCS4, "Image Support" section: "the model has been optimized for English-language text, so the text component of the prompt should be in English."
  - The same sentence is in DOCS3 "Image Support", where the model discussed is 3-11B-Vision. DOCS3's introduction says "All the models are multilingual–for text-only prompts".
  - PROT: "It supports 12 languages and works across modalities to detect and filter policy-violating inputs and outputs across text and images." No list on that page.
  - Llama 4 Scout HF card (`https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E`): "Supported languages: Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese."
  - The Meta LlamaCon post, the defenders post and the Llama 4 post give no LG4 language list. HF metadata for the LG4 repo carries `language: [en]` only, which is a tag, not a statement.
- Label to use: [Documented] for each quote above. The reconciliation "the DOCS4 English sentence sits under Image Support and mirrors the LG3 wording" is [Inferred]. "PROT's 12 equals Llama 4's 12" is [To be verified], as nothing links them.
- Draft impact:
  - A LG1 R6 Detail, replace the bullet beginning "LG4 docs page says…" with three bullets:
    - "LG4 docs page, Image Support section: model 'optimized for English-language text', text component should be in English; the same sentence appears in the LG3 docs page for 3-11B-Vision **[Documented]**".
    - "Meta's protections page says LG4 'supports 12 languages' and lists none **[Documented]**".
    - "The Llama 4 Scout card lists 12 supported languages (Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, Vietnamese); whether the protections page means these is not stated **[To be verified]**".
  - A LG1 R6, add to the LG4 card bullet: "multilingual evaluation averages the 7 non-English LG3-8B languages: French, German, Hindi, Italian, Portuguese, Spanish, Thai **[Documented: repo PurpleLlama@172c1074]**".
  - A LG1 R8 bullet 2 becomes "LG4 language coverage: card lists English plus the 7 LG3 languages, docs page says English-optimised under Image Support, protections page says 12 languages without a list". A LG2 R6 and R8 get the same wording. B LG3 R3 bullet 33 and B LG3 R8 bullet 2: add "the docs sentence is in the Image Support section".
  - INV(a) LG4 Languages cell stays as written (card-based). Add "PROT: 12 languages, not listed [Documented]".
  - Reviewer notes: keep the contradiction, now narrowed.
- Changes Summary? N. The R8 Summaries already say "unclear" or "conflicting".

### T7 — 3-1B (and INT4) evaluation tables include Vietnamese and Indonesian
- Verdict: STILL OPEN (checked the 3-1B PL and HF cards, the 3-1B-INT4 HF card, the 2411.17713 paper, DOCS3; no source says Vietnamese or Indonesian is supported).
- Evidence:
  - 3-1B card: "Llama Guard 3-1B supports content safety for the following languages: English, French, German, Hindi, Italian, Portuguese, Spanish, Thai."
  - The same card's evaluation table has columns English, French, German, Italian, Spanish, Portuguese, Hindi, Vietnamese, Indonesian, Thai, XSTest. 3-1B Vietnamese 0.723/0.130 and Indonesian 0.875/0.083; INT4 Vietnamese 0.792/0.171 and Indonesian 0.833/0.121 (F1/FPR).
  - INT4 paper (`https://arxiv.org/html/2411.17713`) Table 1 has English plus French, German, Italian, Spanish, Portuguese, Hindi, Vietnamese, Indonesian (no Thai column). The text says "better F1 and false positive rate (FPR) than Llama Guard 3-1B for Enlish and 5 of 8 non-English languages". It never says the model supports Vietnamese or Indonesian.
  - New cross-source discrepancy. The paper's 3-1B numbers differ from the card's for several cells: Hindi 0.815/0.088 (paper) vs 0.680/0.057 (card); Vietnamese 0.819/0.099 vs 0.723/0.130; Portuguese 0.798/0.108 vs 0.763/0.114; German 0.851/0.06 vs 0.845/0.036.
  - The 3-8B row (0.939/0.040 English, 0.890/0.034 Vietnamese, 0.915/0.048 Indonesian) is identical in both. So 3-8B was also evaluated on Vietnamese and Indonesian although the 3-8B card does not list them.
- Label to use: [Documented] for the facts (list, table columns, paper); [Not disclosed] for "support for Vietnamese or Indonesian".
- Draft impact:
  - A LG1 R8, A LG2 R6 and A LG2 R8 bullets stay open. Reword: "LG3-1B and LG3-8B evaluation tables include Vietnamese and Indonesian columns, but the cards' supported-language lists do not include them **[Documented]**".
  - INV(a) 3-1B Languages and 3-1B-INT4 Languages: append "evaluation tables also show Vietnamese and Indonesian (also in arXiv 2411.17713 Table 1); support not stated [Not disclosed]".
  - INV-RN 5: add the card-versus-paper difference (Hindi 0.680 on the card vs 0.815 in the paper) and cite the card for any 3-1B number.
- Changes Summary? N.

### T8 — LG1 and LG2 languages; 3-11B-V "English only" wording
- Verdict: CORRECTION. The inventory's 3-11B-V cell says "English only"; the sources say "optimized for English". LG1 and LG2 [Not disclosed] stands.
- Evidence:
  - 3-11B-Vision card (PL `Llama-Guard3/11B-vision/MODEL_CARD.md`): "It was optimized for English language and only supports one image at the moment."
  - DOCS3: "the model has been optimized for English-language text, so the text component of the prompt should be in English."
  - HF metadata for the 11B-V repo (`https://huggingface.co/api/models/meta-llama/Llama-Guard-3-11B-Vision`) lists `language: en, de, fr, it, pt, hi, es, th`. Metadata tags are not card statements, and the 3-8B repo's tag says only `en`, so tags are unreliable.
  - LG1 and LG2: the PL and HF card texts contain no statement of supported languages. LG2's limitations mention "multilingual capability" generically. HF metadata says `language: en` for both (tag only). DOCS2 has no language statement.
- Label to use: [Documented] for "optimised for English" (11B-V). [Not disclosed] for LG1 and LG2 language support.
- Draft impact:
  - INV(a) 3-11B-V Languages. Replace `English only ("optimized for English")` with `Optimised for English per the card; not stated as English-only. DOCS3 says the text component should be in English. HF metadata tag lists 8 languages (tag only) [Documented]`.
  - INV(a) LG1 and LG2 Languages stay [Not disclosed]; add "HF metadata tag: en (not a card statement)".
  - A LG1 R6 bullet "Languages, LG3-11B-Vision: optimised for English" is correct. A LG2 R6 Summary says "LG3-11B-Vision is English with one image"; replace it (36 words): "**Prompt and response pair.** Needs the user prompt and the agent response, plus the policy prompt. LG3 text models cover eight languages; LG4 adds images and cites the same languages; LG3-11B-Vision is English-optimised with one image. **[Documented]**".
  - Brief: change "11B-V: English only" to "optimised for English".
- Changes Summary? Y (A LG2 R6 only, wording).

### T9 — LG4 image tiling (336x336 tiles plus a global tile)
- Verdict: CORRECTION. B LG3 R4 ("not stated in any source read here [To be verified]"), B LG3 R8 bullet 1 and Reviewer note 8 are wrong. DOCS4 states it. The inventory cell is right.
- Evidence (`https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/`, "Image Tokens"):
  - "We apply a dynamic image transformation strategy that divides the input image into 336×336 pixel tiles."
  - "a global tile (created by resizing the entire input image to 336×336 pixels) is appended after the local tiles to provide a global view of the input image."
  - "<|patch|> : These tokens represent subsets of the input image. Larger images have more patch tokens in the prompt."
  - "<|image|> : This token separates the regular-sized image tokens from a downsized version of it that fits in a single tile."
  - "Images that are submitted for evaluation should have the same format (resolution and aspect ratio) as the images that you submit to the Llama 4 models."
  - Not in the LG4 card (PL, HF). The 11B-V tiling is separate: PL 11B card "Images will be rescaled into 4 chunks each of 560x560"; paper 2411.10414 section 3.3 "our vision encoder rescales it into 4 chunks, each of 560 × 560 pixels".
- Label to use: [Documented] (DOCS4).
- Draft impact:
  - B LG3 R4: replace the bullet "LG4 tile size 336 by 336 plus a global tile: not stated in any source read here [To be verified]" with "LG4 image tiling: a dynamic transformation divides each image into 336×336 pixel tiles, and a global tile (whole image resized to 336×336) is appended after the local tiles; larger images get more patch tokens **[Documented]** (Meta LG4 docs page)".
  - B LG3 R4: the existing LG4 prompt-template bullet stays; DOCS4 matches it.
  - B LG3 R8: delete bullet 1 ("LG4 image tiling: 336 by 336 tiles plus a global tile (from the brief) not found …").
  - B LG3 R8 Summary must change (new text below). B Reviewer note 8 ("The 336 by 336 tiles plus global tile claim … was not found"): delete the first half. Keep the 560 by 560 statement.
  - INV(a) LG4 Modality: "dynamic 336x336 tiles [Documented: dev.meta.ai LG4 page]" becomes "dynamic 336x336 tiles plus a global tile [Documented] (DOCS4)". Remove Contradiction 8.
- Changes Summary? Y. New B LG3 R8 Summary (32 words): "**Key open questions.** No documented threshold for 3-11B-Vision or LG4, behaviour beyond about three images in LG4, and whether the OGX vision branch is reached by the Hugging Face id."

### T11 — Full text of the DOCS4 "Complete Example" with multiple images
- Verdict: RESOLVED (read raw HTML of DOCS4).
- Evidence (DOCS4, "A complete example using the new image tokens is shown below"):
  - The prompt starts with the instruction "Task: Check if there is unsafe content in 'Agent' messages in conversations according our safety policy with the below categories." Note "according our", while the template above it says "according to our".
  - The category list is S1 to S14 using short names ("Sex Crimes", "Child Exploitation", "Self-Harm").
  - The first User turn holds two `<|image_start|> … <|image_end|>` blocks, then the text "whats the color of an apple?". The first block has a 2x2 tile grid and the second a 4x4 grid, each followed by `<|image|>` and a global-tile patch run.
  - Then "Agent: its red", "User: whats the color of the sky?", "Agent: its blue".
  - Closing instruction: "Provide your safety assessment for ONLY THE LAST Agent message in the above conversation:".
  - Response block: "If the input is determined to be safe, the response will be: safe"; unsafe example "unsafe S1,S2".
  - The generic template above the example also shows two images in the User line.
- Label to use: [Documented] (DOCS4).
- Draft impact:
  - B LG3 R8: delete the last bullet ("Full text of the LG4 docs 'Complete Example' with multiple images (only a summary was returned)").
  - B LG3 R4: add "DOCS4's worked example puts two images in one user turn, then a multi-turn text exchange, and asks for a verdict on only the last Agent message **[Documented]**".
  - B LG3 R3 bullet 34 stays.
- Changes Summary? N.

### T12 — "Response is text only" and "S14 text only" premises
- Verdict: PARTLY RESOLVED. 3-11B-V response is text-only (documented). S14 is text-only in LG4 (documented). LG4's response modality is not stated.
- Evidence:
  - 11B-V card: "Its task is to classify the multimodal prompt or the multimodal prompt along with the text response."
  - 2411.10414 abstract: "is optimized to detect harmful multimodal (text and image) prompts and text responses to these prompts".
  - LG4 card: "S14: Code Interpreter Abuse (text only)" and "We include an additional category, Code Interpreter Abuse, for text-only tool-call use cases."
  - DOCS3 and DOCS4 both say: "the model does not support the evaluation of images that were themselves created using generative AI technology."
  - Neither DOCS3 nor DOCS4 contains the phrase "S14 … text-only". The LG3 8B card and DOCS3 do not say it. B's Reviewer note about an unprompted "S14 is text-only" remark is confirmed as spurious.
  - LG4 card and DOCS4 do not say whether image output is classified.
- Label to use: [Documented] for 11B-V and S14-in-LG4. [Not disclosed] for LG4 response modality.
- Draft impact:
  - B LG3 R6 bullet "Response is text only; image output is not classified [Inferred]". Replace with three bullets:
    - "LG3-11B-Vision classifies the multimodal prompt, or the prompt with a text response; the paper describes 'text responses' **[Documented]**".
    - "LG4 card and docs do not say whether image content in a response is classified **[Not disclosed]**".
    - "Docs: evaluation of images that were themselves created with generative AI is not supported **[Documented]**".
  - B LG4 R4 "LG4 card: S14 is text only (no image case) [Documented]" stays.
  - B LG4 R7 last bullet and R6 are fine.
- Changes Summary? N.

### T20 — Documented zero-shot or few-shot results for LG3 or LG4
- Verdict: RESOLVED (negative; full text searched). Only the LG1 paper reports them.
- Evidence:
  - 2411.10414 (LG3-Vision): "zero-shot" appears only in "We use GPT-4o and GPT-4o mini in a LLM-as-a-judge setup, with zero-shot prompting using MLCommons hazard taxonomy as the two baselines." The word "custom" appears once, in "better customizable safeguard models". No custom-taxonomy results.
  - 2411.17713 (INT4): "zero-shot" appears only for the GPT4 baseline.
  - Llama 3 paper section 5.4.7 (`https://arxiv.org/html/2407.21783`): no zero-shot, few-shot or custom-taxonomy results for Llama Guard 3. It says "Llama Guard 3 can be deployed for specific harms only".
  - LG3 and LG4 cards: no such results. DOCS2, DOCS3 and DOCS4 say only: "These can be customized for zero-shot or few-shot prompting."
  - Training-side hint, 2411.10414 section 3.3: "We drop a random number of categories from the model prompt if they’re not violated in the given example: this ensures that the model can learn to take into account only the included categories."
- Label to use: [Not disclosed] for results. [Documented] for the data-augmentation sentence.
- Draft impact:
  - B LG5 R2 bullet 2 ("The 3-Vision paper trains on 13 hazard categories; the fetched content showed no zero-shot or custom-category results [Inferred]"). Replace with "No zero-shot, few-shot or custom-category results appear in the LG3-Vision paper, the 1B-INT4 paper, the Llama 3 paper section on Llama Guard 3, or the LG3 and LG4 cards (full text searched) **[Not disclosed]**".
  - B LG5 R2, add "LG3-Vision training randomly drops non-violated categories from the prompt so the model attends only to the categories included **[Documented]** (arXiv 2411.10414 section 3.3)".
  - B LG5 R8 bullet 4 stays ("only the LG1 paper reports them").
- Changes Summary? N.

### T25 — LG4 evaluation on tool-use categories or S14
- Verdict: RESOLVED (negative). The LG4 card gives no S14 or tool-use metric.
- Evidence:
  - LG4 card (PL `Llama-Guard4/12B/MODEL_CARD.md`; HF identical): "All values are an average over samples from safety categories S1 through S13 listed above, weighting each category equally".
  - The card has no search-tool-call or S14 evaluation, and DOCS4 contains none either. The LlamaCon and defenders posts give no figures.
  - S14 evaluation language: not stated anywhere. The 3-8B card's Table 3 (tool use) is labelled "prompt+response classification" with no language given.
- Label to use: [Not disclosed].
- Draft impact:
  - B LG4 R4 bullet "LG4 card averages S1 to S13 only and gives no S14 or tool-use metric" keep, now backed by the verbatim sentence. Add the quote as support if space allows.
  - B LG4 R6 "S14 evaluation language not stated" keep.
  - B LG4 R8 bullets 2 and 5 stay (they are real gaps); R8 is unlabelled.
- Changes Summary? N.

### T26 — Does 3-8B-INT8 support S14 per its own card?
- Verdict: RESOLVED. Its own card lists 14 categories including S14.
- Evidence (`https://huggingface.co/meta-llama/Llama-Guard-3-8B-INT8`):
  - "The model is trained to predict safety labels on the 14 categories shown below".
  - "was optimized to support safety and security for search and code interpreter tool calls."
  - The category table lists "S14: Code Interpreter Abuse", with the same definition as the 3-8B card.
  - The HF Hub chat template for the INT8 repo (`https://huggingface.co/api/models/meta-llama/Llama-Guard-3-8B-INT8`) contains "S14: Code I…" in its category list.
  - 8B card Table 5 (quantised column) has Tool Use rows for prompt (F1 0.909, FPR 0.134) and response (F1 0.827, FPR 0.155).
- Label to use: [Documented].
- Draft impact:
  - B LG4 R1 bullet "Versions with S14: 3-8B (and 3-8B-INT8, same taxonomy per its card family)". Replace with "Versions with S14: 3-8B, 3-8B-INT8 (own card lists 14 categories) and LG4 **[Documented]**".
  - B LG4 R8 bullet 3 ("Whether 3-8B-INT8 supports S14 as documented (check its card)"): delete.
  - B Reviewer note (last): delete.
  - INV(a) 3-8B-INT8 Taxonomy: "S1-S14 [Documented: HF intro, summarised]" becomes "S1-S14 [Documented] (INT8 HF card)". INV Contradiction 16: closed.
- Changes Summary? N.

### T27 — Search tool calls have no dedicated category; prompt and agent output can both be judged
- Verdict: RESOLVED. Both inferences can be upgraded to [Documented], with the exact words below.
- Evidence (PL `Llama-Guard3/8B/MODEL_CARD.md`):
  - Training data: "For the tool use capability, we consider search tool calls and code interpreter abuse."
  - The card's 14 listed categories (S1 to S14) include no search category. The only tool-related one is S14 Code Interpreter Abuse.
  - "Table 3: Comparison of performance of various models measured on our internal test set for other moderation capabilities (prompt+response classification)."
  - Table 5 has a "Prompt Classification" block with a Tool Use row (non-quantised P 0.884, R 0.958, F1 0.920, FPR 0.126) and a "Response Classification" block with a Tool Use row (P 0.774, R 0.884, F1 0.825, FPR 0.176).
- Label to use: [Documented: repo PurpleLlama@172c1074].
- Draft impact:
  - B LG4 R2 bullet 4 ("Search tool calls: no dedicated category; the evaluation covers them under the 14-category taxonomy [Inferred]"). Replace with "Search tool calls have no dedicated category: the 8B card lists S1 to S14 and S14 is code-interpreter abuse **[Documented: repo PurpleLlama@172c1074]**". Keep "the evaluation covers them under the 14-category taxonomy" only as [Inferred] if wanted, as a separate bullet.
  - B LG4 R3 bullet 5 ("So both the user prompt and the agent's code or answer can be judged [Inferred]"). Replace with "The 8B card reports Tool Use results for both prompt classification and response classification (Table 5) **[Documented: repo PurpleLlama@172c1074]**".
- Changes Summary? N.

### T39 — PGD response classification at 8/255
- Verdict: CORRECTION. A LG2 R2 (and the brief) is wrong for 8/255. B LG3 R2 is right.
- Evidence (`https://arxiv.org/html/2411.10414`, Table 3, "Percentage of harmful prompts and conversations … misclassified as safe after applying the PGD attack"):
  - Response classification rows: no attack 0/255 = 6%; 8/255 = 22%; 128/255 = 27%; 255/255 = 27%.
  - Prompt classification rows: 0/255 = 21%; 8/255 = 70%; 128/255 = 82%; 255/255 = 82%.
  - Text: "even under an unbounded PGD attack, unsafe responses are misclassified as safe only 27% of the time."
  - Text: "this is still substantially higher than 6% of the clean baseline".
  - The brief's "6% to 27%" is the clean baseline to the unbounded setting, not 8/255.
- Label to use: [Documented].
- Draft impact:
  - A LG2 R2 bullet 7 ("PGD at 8/255 raised unsafe responses classified safe from 6% to 27%"). Replace with "LG3-Vision paper, response classification: a PGD image attack raised unsafe responses classified safe from 6% (no attack) to 22% at 8/255 and 27% at 128/255 and at 255/255 **[Documented]**".
  - B LG3 R2 sub-bullet 2 is right (6%, 22%, 27%, 27%). Keep.
  - B Reviewer note 1 ("CONTRADICTION (brief vs paper)") closes in favour of the paper. Fix the brief.
- Changes Summary? N. No Summary carries these numbers.

### T40 — Adversarial numbers (read raw, not summarised)
- Verdict: RESOLVED. Every number in the drafts is confirmed against arXiv HTML Tables 3 and 4, except the A LG2 R2 PGD response figure (see T39).
- Evidence (`https://arxiv.org/html/2411.10414`):
  - Text: "even with small perturbations (8/255), PGD attacks can significantly increase the rate of harmful prompts misclassified as safe, from 21% to 70%".
  - Table 3 prompt rows: 0/255 21%; 8/255 70%; 128/255 82%; 255/255 82%.
  - GCG text: "GCG can circumvent the safety classifier the majority of the time (72% misclassified as safe)".
  - Table 4: prompt classification, no attack 4%, GCG on user prompt 72%.
  - Table 4: response classification, no attack 16%, GCG appended to user prompt 30%, GCG appended to agent response 75%.
  - Text: "(30% vs. 16%)", and "in which case the conversations misclassified as safe go up to 75%".
  - Sample size: "PGD, an image-based attack, is evaluated on 100 harmful conversations" and "GCG, a text-only attack, is evaluated on another set of 100 text-only unsafe conversations".
  - Threat model: "The adversary has full white-box access to Llama Guard 3 Vision".
  - Worst case: "we optimized GCG suffixes placed after the harmful response it is evaluated on."
- Label to use: [Documented].
- Draft impact:
  - A LG1 R2 bullet 9 (21% to 70%; GCG 72%): correct, keep. Add sample size.
  - A LG2 R2 GCG bullet and B LG3 R2 sub-bullets 1, 3 and 4: correct, keep.
  - Add to A LG1 R2 and B LG3 R2: "Each attack was evaluated on 100 conversations (PGD on 100 harmful image conversations; GCG on 100 text-only unsafe conversations) **[Documented]**".
  - Add to B LG3 R2: "GCG suffixes were optimised with knowledge of the harmful response, a worst-case setting; the paper notes the attacker normally cannot see the agent's response **[Documented]**".
  - Reviewer notes (A and B): drop "from summarised fetch" for these numbers.
- Changes Summary? N.

### T41 — 3-1B-INT4 size: 440 MB vs 458 MB
- Verdict: RESOLVED. The figures use different units and scopes; all three are real.
- Evidence:
  - Paper abstract (`https://arxiv.org/abs/2411.17713`): "despite being approximately 7 times smaller in size (440MB)".
  - Paper section 3.3 (HTML): "a final model size of 0.4GB". Table 1: model size (GB) 0.4 for INT4, 2.8 for 3-1B, 14.9 for 3-8B.
  - Meta Llama 3.2 post (`https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/`): "bringing its size from 2,858 MB down to 438 MB".
  - HF Hub API for `meta-llama/Llama-Guard-3-1B-INT4`: `llama_guard_3_1b_pruned_xnnpack.pte` = 458,464,800 bytes; `example-prompt.txt` 744; `params.json` 455; `tokenizer.model` 2,183,982; no `config.json`.
  - HF Hub API for `meta-llama/Llama-Guard-3-1B`: `model.safetensors` = 2,996,982,344 bytes.
  - Arithmetic: 458,464,800 / 2^20 = 437.2 MiB (458.5 MB decimal). 2,996,982,344 / 2^20 = 2858.1 MiB, which matches the blog's "2,858 MB". The .pte plus tokenizer, params and example file = 439.3 MiB.
- Label to use: [Documented] for each number. [Inferred] for the unit explanation: the blog's "MB" is binary, so 438 MB is about the .pte in MiB, and the paper's "440MB" is rounded. Meta does not state the unit convention.
- Draft impact:
  - INV(a) 3-1B-INT4 Distribution: "(458 MB)" becomes "(458,464,800 bytes, about 437 MiB)". Headline eval: replace "the 440 MB vs 458 MB .pte difference is unexplained" with "paper abstract 440MB and Meta's 2024-09-25 post 438 MB (the post's 2,858 MB for the 3-1B matches its safetensors in MiB) are consistent with the 458.5 MB .pte if MB is MiB [Inferred]".
  - INV-RN 7: rewrite the same way. Remove Contradiction 7.
- Changes Summary? N.

### T42 — LG2 headline numbers on different test sets
- Verdict: RESOLVED. Both sets are documented and different. No conflict.
- Evidence:
  - LG2 card (PL `Llama-Guard2/MODEL_CARD.md`) Table 1, "measured on our internal test set": Llama Guard 2 F1 0.915, AUPRC 0.974, FPR 0.040; GPT4 0.796 / N/A / 0.151; Llama Guard 0.665 / 0.854 / 0.027.
  - LG2 card note: "The performance of Llama Guard is lower on our new test set due to expansion of the number of harm categories from 6 to 11". The LG2 card does not label Table 1 as prompt or response.
  - LG3-8B card Table 1: "Comparison of performance of various models measured on our internal English test set for MLCommons hazard taxonomy (response classification)": Llama Guard 2 0.877 / 0.927 / 0.081; Llama Guard 3 0.939 / 0.985 / 0.040; GPT4 0.805 / N/A / 0.152.
- Label to use: [Documented: repo PurpleLlama@172c1074].
- Draft impact:
  - INV(a) LG2 Headline eval: keep both, add set labels: "0.915 / 0.974 / 0.040: LG2 card Table 1, its own 11-category internal test set (prompt or response not labelled); 0.877 / 0.927 / 0.081: LG3-8B card Table 1, MLCommons English response set".
  - A LG2 R5 bullet 5 (uses 0.877 inside the 3-8B line) already names it as the 3-8B card's set; add "response classification, English test set".
  - Close INV-RN 6 and Contradiction 1 as "different sets".
- Changes Summary? N.

### T43 — LG1 paper numbers (read raw)
- Verdict: RESOLVED. All numbers in the drafts are confirmed. One nuance on what "OpenAI Mod 0.847" is.
- Evidence (`https://arxiv.org/html/2312.06674`):
  - Table 4: "OpenAI Mod API 0.856; Llama Guard (no adaptation) 0.837; Llama Guard Zero-shot (w/ OpenAI Mod categories) 0.847; Llama Guard Few-shot (w/ description and in-context examples) 0.872".
  - Table 2 (AUPRC): Llama Guard 0.945 (own prompt), 0.847 (OpenAI Mod), 0.626 (ToxicChat), 0.953 (own response); OpenAI API 0.764 / 0.856 / 0.588 / 0.769. Table 2 note: "The reported Llama Guard results are with zero-shot prompting using the target taxonomy."
  - Few-shot definition: "Few-shot prompting is similar to zero-shot but additionally includes 2 to 4 examples for each category in the prompt."
  - Abstract: "enabling the adjustment of taxonomy categories to align with specific use cases, and facilitating zero-shot or few-shot prompting with diverse taxonomies at the input".
  - Section 4.5.1: "adapting to a new policy exclusively through prompting is effective while also being low cost compared to fine-tuning".
  - Section 3.4: "with sequence length of 4096".
  - The same Table 2 numbers appear in the LG1 PL card (PL `Llama-Guard/MODEL_CARD.md`: "Llama Guard | 0.945 | 0.847 | 0.626 | 0.953").
- Label to use: [Documented].
- Draft impact:
  - B LG5 R1 bullet 3 and B LG5 R4 bullets (Table 4, few-shot definition, "adapting to a new policy…"): correct, keep; replace "(summarising fetch)" with "(arXiv HTML, read raw)".
  - INV(a) LG1 Custom and Headline eval: keep. Add "OpenAI Mod 0.847 is the zero-shot-with-target-taxonomy result (Table 2 note); no-adaptation is 0.837 (Table 4) [Documented]".
  - INV(a) LG1 Context: "Fine-tune sequence length 4096" plain [Documented].
  - INV Summarised-fetch caveats: remove the LG1 paper numbers from the list.
- Changes Summary? N.

### T44 — Prompt-only numbers for 3-1B and LG4
- Verdict: PARTLY RESOLVED. LG4's table is response (output-filtering) only, as documented. The 3-1B card does not label its table. No prompt-only number exists for either (checked the PL and HF cards, the INT4 paper, DOCS4).
- Evidence:
  - LG4 card: "Values are from output filtering, flagging model outputs as either safe or unsafe."
  - LG4 card, qualitative only: "We find that Llama Guard 4 roughly matches or exceeds the overall performance of the Llama Guard 3 models on both input and output filtering". No input-filtering numbers.
  - 3-1B card: "We evaluate the performance of Llama Guard 1B models on MLCommons hazard taxonomy and compare it across languages with Llama Guard 3-8B on our internal test." No prompt or response label.
  - The 3-8B row of the 1B table (English 0.939 / 0.040) equals the 8B card's Table 1 values, which that card labels "(response classification)". The 8B card's Table 2 multilingual (prompt+response) values also match the 1B table (French 0.943 / 0.036).
  - INT4 paper section 2.2: the demo app shows "capabilities for response classification". Its evaluation text does not label prompt or response.
- Label to use: [Documented] for the LG4 response-only labelling. [Inferred] that the 1B English column is response classification (from the matching 8B Table 1). [Not disclosed] for prompt-only numbers.
- Draft impact:
  - A LG1 R6 bullet "Evaluation, LG3-1B and LG4: the cards do not label their numbers as prompt-only; LG4 numbers are for output filtering only [Documented]". Split: "LG4 numbers are from output filtering only **[Documented]**"; "The LG3-1B card does not label its evaluation table as prompt or response **[Not disclosed]**"; "The LG3-1B English and multilingual columns for LG3-8B repeat the 8B card's response and prompt+response values, so the 1B table is probably response or prompt+response, not prompt-only **[Inferred]**".
  - A LG1 R8 bullet 4 and R8 Summary stay (no prompt-only numbers).
- Changes Summary? N.

### T46 — Llama 3 paper trade-off numbers cited by the LG3 card
- Verdict: RESOLVED (extra source, see method note).
- Evidence:
  - 3-8B card, Application: "Violation rate improvement and impact on false positives as measured on internal benchmarks are provided in the Llama 3 paper." (PL `Llama-Guard3/8B/MODEL_CARD.md`).
  - Llama 3 paper, section 5.4.7 (`https://arxiv.org/html/2407.21783`): "Llama Guard 3 is able to significantly reduce violations across capabilities (-65% violations on average across our benchmarks)."
  - Same paragraph: "Note that adding system safeguards (and any safety mitigations in general) comes at the cost of increased refusals to benign prompts."
  - Tables 25 and 26 give violation-rate and false-refusal changes per language and per category. They were not transcribed here.
- Label to use: [Documented].
- Draft impact:
  - A LG1 R2 bullet "Trade-off: LG3-8B card says … 'might increase refusals to benign prompts (False Positives)'" is verbatim-correct (card: "it might increase refusals to benign prompts (False Positives)"). Add: "Llama 3 paper: Llama Guard 3 reduced violations by 65% on average across Meta's internal benchmarks, at the cost of more refusals of benign prompts **[Documented]** (arXiv 2407.21783 section 5.4.7)".
  - A Reviewer note "Not checked: Llama 3 paper numbers": replace with "Checked: -65% average violation reduction".
- Changes Summary? N.

### T47 — LG1 release date
- Verdict: RESOLVED. LG1 was released on 2023-12-07.
- Evidence:
  - arXiv `/abs/2312.06674`: "[Submitted on 7 Dec 2023]".
  - Meta post "Introducing Purple Llama" (`https://ai.meta.com/blog/purple-llama-open-trust-safety-generative-ai/`), dated "December 7, 2023": "and Llama Guard, a safety classifier for input/output filtering that is optimized for ease of deployment."
  - HF LlamaGuard-7b LICENSE.txt: "Llama 2 Version Release Date: July 18, 2023". So the 2023-07-18 date is the Llama 2 licence date, not LG1.
  - HF Hub API: repo `createdAt` 2023-12-05T22:29:49Z. This is repository creation, two days before the announcement.
- Label to use: [Documented].
- Draft impact:
  - INV(a) LG1 Release date. Replace the cell with: "2023-12-07 [Documented] (Meta announcement post and arXiv submission date). HF page's 2023-07-18 is the Llama 2 licence date, not LG1's; HF repo created 2023-12-05 [Documented]". Remove [To be verified]. Remove Contradiction 18.
- Changes Summary? N.

### T48 — Release dates for LG2, 3-1B, 3-1B-INT4, 3-8B, 3-8B-INT8, 3-11B-V, LG4
- Verdict: RESOLVED. Each has an announcement date on an official Meta post, a licence version date, and an HF repo-creation timestamp.
- Evidence:
  - LG2: "April 18, 2024" Llama 3 post (`https://ai.meta.com/blog/meta-llama-3/`): "introducing new trust and safety tools with Llama Guard 2, Code Shield, and CyberSec Eval 2". Licence: "Meta Llama 3 Version Release Date: April 18, 2024". HF created 2024-04-17.
  - 3-8B and 3-8B-INT8: "July 23, 2024" Llama 3.1 post (`https://ai.meta.com/blog/meta-llama-3-1/`): "new components such as Llama Guard 3, a multilingual safety model and Prompt Guard". Licence: "Llama 3.1 Version Release Date: July 23, 2024". HF created 2024-07-22 (8B) and 2024-07-21 (INT8).
  - 3-1B and 3-11B-V: "September 25, 2024" Llama 3.2 post (`https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/`): "we’re releasing Llama Guard 3 11B Vision" and "Llama Guard 3 1B is based on the Llama 3.2 1B model". Licence: "Llama 3.2 Version Release Date: September 25, 2024". HF created 2024-09-20 for 1B, INT4 and 11B-V.
  - 3-1B-INT4: the paper says "open-sourced to the community during Meta Connect 2024" (abstract) and "As part of the Llama 3.2 1B release at Meta Connect 2024, we delivered Llama Guard 3-1B-INT4". Paper arXiv submitted 18 Nov 2024. The 11B-V paper was submitted 15 Nov 2024.
  - LG4: LlamaCon post dated "April 29, 2025" (T49). Licence: "Llama 4 Version Effective Date: April 5, 2025". HF created 2025-04-23. The Llama 4 Scout card says "Model Release Date: April 5, 2025".
- Label to use: [Documented] for each date, naming which kind it is. An HF `createdAt` is repo creation, not release, and is not a release date.
- Draft impact (INV(a) Release date cells; keep the kind of date explicit):
  - LG2: "2024-04-18 [Documented] (Meta Llama 3 launch post and licence version date)".
  - 3-8B and 3-8B-INT8: "2024-07-23 [Documented] (Llama 3.1 launch post names Llama Guard 3; licence version date)".
  - 3-1B and 3-11B-V: "2024-09-25 [Documented] (Llama 3.2 launch post; licence version date)". 11B-V paper 2024-11-15 stays.
  - 3-1B-INT4: "Meta Connect 2024 [Documented] (per the paper); the Llama 3.2 post dated 2024-09-25 describes a 1B guard 'pruned and quantized', so same-day release is [Inferred]; paper submitted 2024-11-18 [Documented]".
  - LG4: "2025-04-29 announcement [Documented]; licence effective 2025-04-05 [Documented]".
  - Not-found list: delete the line "Exact LG2 and LG3 announcement dates …".
- Changes Summary? N.

### T49 — LlamaCon post date and wording
- Verdict: RESOLVED (raw page read).
- Evidence (`https://ai.meta.com/blog/llamacon-llama-news/`): the page header reads "April 29, 2025". Text: "Today, we’re releasing new Llama protection tools for the open source community, including Llama Guard 4, LlamaFirewall, and Llama Prompt Guard 2."
  - The linked post (`https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/`), also "April 29, 2025": "The new Llama Guard 4 is an update to our customizable Llama Guard tool, acting as a unified safeguard across modalities, supporting protections for text and image understanding."
- Label to use: [Documented].
- Draft impact: INV(a) LG4 Release date: the wording "Today, we're releasing new Llama protection tools ... including Llama Guard 4" is verbatim-compatible; change the label from "[Documented: ai.meta.com LlamaCon post, summarised]" to "[Documented]". No other change.
- Changes Summary? N.

### T50 — LG1 O-code order
- Verdict: RESOLVED. The inventory's order (cookbook/paper) is right. The brief and the HF-summary order are wrong.
- Evidence:
  - HF chat template for LlamaGuard-7b, read from the HF Hub API (`https://huggingface.co/api/models/meta-llama/LlamaGuard-7b`, tokenizer_config chat_template), category headings in order: "O1: Violence and Hate.", "O2: Sexual Content.", "O3: Criminal Planning.", "O4: Guns and Illegal Weapons.", "O5: Regulated or Controlled Substances.", "O6: Self-Harm."
  - LG1 paper Table 1 row order (`https://arxiv.org/html/2312.06674`): Violence & Hate, Sexual Content, Criminal Planning, Guns & Illegal Weapons, Regulated or Controlled Substances, Suicide & Self-Harm. The paper says: "a letter (e.g. ’O’) followed by the 1-based category index". Table 5 abbreviations: "VH, SC, CR, GIW, RCS, SH".
  - LG1 PL card prose (`Llama-Guard/MODEL_CARD.md`) lists Violence & Hate, Sexual Content, Guns & Illegal Weapons, Regulated or Controlled Substances, Suicide & Self Harm, Criminal Planning (last). The card has no O-codes.
  - LG2 template from the same API: S1 Violent Crimes, S2 Non-Violent Crimes, S3 Sex Crimes, S4 Child Exploitation, S5 Specialized Advice, S6 Privacy, S7 Intellectual Property, S8 Indiscriminate Weapons, S9 Hate, S10 Self-Harm, S11 Sexual Content. This confirms the LG2 numbering in INV(b).
- Label to use: [Documented].
- Draft impact:
  - INV(b) intro and all LG1 code cells: correct. Change the sentence "The HF card's prose lists the same six in a different order, see Reviewer notes" to "The PL LG1 card prose lists them in a different order (Criminal Planning last); the HF chat template, the paper and the cookbook agree on O1 to O6 as used here **[Documented]**".
  - INV(a) LG1 Taxonomy: keep; add "code order per the HF chat template".
  - INV-RN 1 and Contradiction 4: close. Remove "[To be verified against raw HF README, which is gated]".
  - INV(b) row names: the HF template says "Self-Harm" for O6; the paper says "Suicide & Self-Harm" in Table 1.
  - Brief: replace "O3 Guns, O4 Substances, O5 Suicide, O6 Criminal Planning" with the order above.
- Changes Summary? N.

### T52 — Meta docs pages read only through summarising fetch
- Verdict: RESOLVED. DOCS2, DOCS3, DOCS4 and PROT were re-read as raw HTML text. Every quote the drafts rely on is confirmed or corrected below.
- Evidence:
  - Role rule, in DOCS2, DOCS3 and DOCS4: "When evaluating the user input, the agent response must not be present in the conversation." and "when evaluating the agent response, both the user input and the agent response need to be present in the conversation".
  - "{{ role }} : It can have the values: User or Agent." DOCS3 adds "Note that the capitalization here differs from that used in the prompt format for the Llama 3.1 model itself."
  - Image-only: DOCS3 and DOCS4: "It is not designed to perform image-only classification."
  - Generated images: DOCS3 and DOCS4: "the model does not support the evaluation of images that were themselves created using generative AI technology."
  - One image, DOCS3 only: "multi-turn support here does not mean multi-image support; the model evaluates only one image per prompt." DOCS4 does not contain this sentence.
  - 1B and S14, DOCS3: "The new Llama Guard 3 1B model was not optimized for category S14 Code Interpreter Abuse. If you need to screen for this category, you should use the 8B model".
  - Customisation, DOCS2, DOCS3, DOCS4: "These can be customized for zero-shot or few-shot prompting." DOCS3 and DOCS4: "This enables you to customize these descriptions to adapt the model’s behavior for your specific use cases".
  - English, DOCS3 (about 11B-V) and DOCS4: "the model has been optimized for English-language text, so the text component of the prompt should be in English." (see T6).
  - PROT: "For the first time, Llama Guard 4 is now available through the /moderations endpoint in Llama API." and "It supports 12 languages".
  - PROT: "Categories of prompt attacks include prompt injection and jailbreaking", under the Prompt Guard 2 entry.
  - New facts. DOCS4: "Llama Guard 4 is also compatible with the Llama 3 line of models and can be used as a drop-in replacement for Llama Guard 3 8B and 11B for both text-only and multimodal applications." The next sentence says Llama Guard 3 1B still holds value for "deployment on edge devices". DOCS3 introduction: "The first two models are text only", and the 1B is "for on-device and cloud safety evaluations".
  - Absent from DOCS3 and DOCS4: any tool, function-call or search-tool wording; any "S14 text-only" note; any threshold, probability or score statement. DOCS4's S14 appears only in the LG3-category examples and the complete example.
- Label to use: [Documented] (the docs pages were read directly).
- Draft impact:
  - Replace "(summarising fetch)" and "(seen on both pages through a summarising fetch)" with plain citations in B LG3 R3 and B LG5 R1, and in A and B Reviewer notes. Remove "Meta docs … via summarising fetch" from B LG4 R3 bullet 6 (the no-tool-wording statement is now a verified absence, [Not disclosed]).
  - B LG3 R3 bullet 3 is correct. B LG3 R3 bullet 5 "(Llama Guard 3 page)" is correct for DOCS3 only.
  - B Reviewer note on "S14 is text-only category … Ignored": confirm "not on the page".
  - Add to A LG1 R4 or A LG2 R4: "Meta docs say LG4 can be a drop-in replacement for LG3 8B and 11B, and the LG3 1B still suits edge devices **[Documented]**" (DOCS4).
- Changes Summary? N.

### T53 — HF card facts from summarised fetches
- Verdict: RESOLVED. HF pages were read as raw text and HF Hub API JSON. Licence names, usage code, file listing, custom-category snippets and the INT8 intro are all confirmed. Two small divergences are noted.
- Evidence:
  - Usage code on the HF pages: 3-8B and 3-1B use `AutoModelForCausalLM` with `AutoTokenizer`; 3-8B-INT8 uses `BitsAndBytesConfig(load_in_8bit= True )` with `AutoModelForCausalLM`; LG4 uses `AutoProcessor` and `Llama4ForConditionalGeneration` with `torch_dtype=torch.bfloat16`.
  - 3-11B-V: the HF card uses `from transformers import AutoModelForVision2Seq, AutoProcessor`. HF config architectures is `MllamaForConditionalGeneration`. The cookbook notebook loader is not re-read here.
  - 3-1B HF card, custom categories: "This snippet will use the categories described in this model card. You can provide your own categories instead:" with `categories = { "S1" : "My custom category" }`, and "Or you can exclude categories from the default list by specifying an array of category keys to exclude:" with `excluded_category_keys=[ "S6" ]`. The 3-11B-V HF card shows the same pattern with `[ "S1" ]`. The 3-1B snippets are not in the PL 1B MODEL_CARD.md.
  - Not on the 3-8B, 3-8B-INT8 and LG4 HF pages (no `categories` or `excluded_category_keys` text in their rendered cards). Only a plain `apply_chat_template` call.
  - INT8 intro: "This repository corresponds to 8-bit version of the model and can be loaded with bitsandbytes." and "Llama Guard 3 can be directly used with transformers and bitsandbytes."
  - 3-1B card: "This repository contains two versions of Llama-Guard-3-1B, for use with transformers and with the original llama codebase." The INT4 artefacts are in a separate repo.
  - HF Hub API file listing for `Llama-Guard-3-1B-INT4`: `llama_guard_3_1b_pruned_xnnpack.pte` 458,464,800 bytes, `params.json`, `tokenizer.model`, `example-prompt.txt`, `LICENSE.txt`, `USE_POLICY.md`; no `config.json`.
  - Licence names and dates: see T57.
- Label to use: [Documented] for each, citing the HF page.
- Draft impact:
  - A LG1 R4 bullet "Hugging Face transformers…[Documented] (HF cards, summarised fetch)" becomes "(HF cards)".
  - A LG1 R6 bullet "Custom categories: LG3-1B card shows…" becomes "(HF card)".
  - INV(a) 3-11B-V Distribution: add "HF card loads with `AutoModelForVision2Seq`; config architecture `MllamaForConditionalGeneration`".
  - INV(a) 3-1B-INT4 Distribution: label "[Documented: HF file listing, summarised]" becomes "[Documented] (HF Hub file listing)".
  - INV(a) licence and distribution cells: all "[Documented: HF page …]" become [Documented] (HF page).
  - INV-RN Summarised-fetch caveats: delete the "All HF page facts" bullet.
  - B LG5 R4 bullet 3 ("The 3-8B and LG4 HF pages (via summarising fetch)") drop "via summarising fetch" and add "3-8B-INT8".
  - B Reviewer note 4 (3-1B snippets): resolved. The HF page shows them and the PL card does not.
- Changes Summary? N.

### T57 — Licence names, versions and dates per variant
- Verdict: RESOLVED. Read from each repo's LICENSE file and HF metadata.
- Evidence (HF `LICENSE` or `LICENSE.txt`, first two lines of each):

| Variant | Licence title | Date line (verbatim) |
|---|---|---|
| LlamaGuard-7b | "LLAMA 2 COMMUNITY LICENSE AGREEMENT" | "Llama 2 Version Release Date: July 18, 2023" |
| Meta-Llama-Guard-2-8B | "META LLAMA 3 COMMUNITY LICENSE AGREEMENT" | "Meta Llama 3 Version Release Date: April 18, 2024" |
| Llama-Guard-3-8B, 3-8B-INT8 | "LLAMA 3.1 COMMUNITY LICENSE AGREEMENT" | "Llama 3.1 Version Release Date: July 23, 2024" |
| Llama-Guard-3-1B, 3-1B-INT4, 3-11B-Vision | "LLAMA 3.2 COMMUNITY LICENSE AGREEMENT" | "Llama 3.2 Version Release Date: September 25, 2024" |
| Llama-Guard-4-12B | "LLAMA 4 COMMUNITY LICENSE AGREEMENT" | "Llama 4 Version Effective Date: April 5, 2025" |

  - URLs: `https://huggingface.co/meta-llama/<model>/blob/main/LICENSE` (`LICENSE.txt` for LG1, 3-1B, 3-1B-INT4 and 3-11B-V).
  - HF metadata licence tags (Hub API): LG1 `llama2`, LG2 `llama3`, 3-8B and INT8 `llama3.1`, 3-1B, INT4 and 11B-V `llama3.2`, LG4 `license: other, license_name: llama4`.
  - The LG4 and LG1 date lines say "Effective Date" (LG4) and "Release Date" (all others). The LG1 date is the Llama 2 date, not the Llama Guard date (T47).
  - Cookbook header ("Llama 2 Community License Agreement") agrees with LG1.
- Label to use: [Documented].
- Draft impact:
  - A LG1 R4 licence bullets: add the word "Agreement" ("Llama 3.1 Community License Agreement", "Llama 3.2 Community License Agreement"); the draft says "Llama 3.1 Community License" and "Llama 3.2". LG4 bullet is right.
  - A LG2 R4 Licences bullet: same wording fix (Llama 3.1 and Llama 3.2 are the shorthand; names above are the exact ones).
  - INV(a) Licence cells: "LLAMA 2 Community License Agreement" fine; use exact titles from the table (LG2 "Meta Llama 3 Community License Agreement" already right).
  - Dates: the licence date for LG1 is not a release date (T47); the other licence dates equal the launch-post dates (T48).
- Changes Summary? N.

### T58 — Multimodal / EU restriction in Llama 3.2 and Llama 4 terms (facts only)
- Verdict: PARTLY RESOLVED. The clause text is located in both the Llama 3.2 and Llama 4 Acceptable Use Policies. Whether it covers Llama Guard 3-11B-Vision or LG4 is not stated by Meta in any document read, so applicability stays open. No legal advice is given.
- Evidence:
  - Llama 3.2 Acceptable Use Policy as rendered on the HF model pages for 3-11B-V (`https://huggingface.co/meta-llama/Llama-Guard-3-11B-Vision`), 3-1B and 3-1B-INT4: "With respect to any multimodal models included in Llama 3.2, the rights granted under Section 1(a) of the Llama 3.2 Community License Agreement are not being granted to you".
  - Same sentence: "if you are an individual domiciled in, or a company with a principal place of business in, the European Union."
  - Next sentence: "This restriction does not apply to end users of a product or service that incorporates any such multimodal models."
  - Licence incorporation, Llama 3.2 LICENSE section 1.b.iv: "adhere to the Acceptable Use Policy for the Llama Materials (available at https://www.llama.com/llama3_2/use-policy), which is hereby incorporated by reference into this Agreement." (the llama.com/llama3_2/use-policy URL itself returned 404 today.)
  - Llama 4 Acceptable Use Policy (`https://www.llama.com/llama4/use-policy/`): "With respect to any multimodal models included in Llama 4, the rights granted under Section 1(a) of the Llama 4 Community License Agreement are not being granted to you" followed by the same domicile wording and the same end-user exception.
  - Llama 4 LICENSE 1.b.iv incorporates `https://llama.com/llama4/use-policy` by reference.
  - The Llama 3.2 and Llama 4 LICENSE files themselves contain no EU wording (searched for European, EU, domiciled, multimodal).
  - HF gating: only the `Llama-Guard-3-11B-Vision` repo carries `extra_gated_eu_disallowed: true` in its Hub metadata. None of the other seven guard repos, including LG4, does. The HF LG4 page does not render the AUP text.
  - Text-only guards: the clause says "multimodal models". 3-1B and 3-1B-INT4 are text-only per their cards, but the same AUP text appears on their pages.
- Label to use: [Documented] for the clause text and the gating flag. [To be verified] for applicability to 3-11B-V and LG4 (not stated by Meta; refer to counsel).
- Draft impact (suggested addition, not currently in the drafts):
  - B LG3 R4 Detail, new bullets:
    - "The Llama 3.2 Acceptable Use Policy (shown on the 3-11B-Vision page) says rights under Section 1(a) are not granted for multimodal models to an individual domiciled, or a company with principal place of business, in the European Union; end users of a product incorporating such models are exempt **[Documented]**".
    - "The Llama 4 Acceptable Use Policy has the same clause for multimodal models in Llama 4 **[Documented]**".
    - "Whether the clause covers Llama Guard 3-11B-Vision or Llama Guard 4 is not stated by Meta; HF gates the 3-11B-Vision repo with an EU-disallowed flag, but not LG4 **[To be verified]**".
  - INV(a) 3-11B-V and LG4 Licence cells: append "see AUP multimodal EU clause [Documented]".
- Changes Summary? N.

### T59 — Redistribution and derivative terms for the quantised variants (facts only)
- Verdict: RESOLVED. The quantised variants are Meta's own repos under the same licence as their parent; the licence text is quoted below. No legal advice.
- Evidence:
  - 3-8B-INT8 repo: licence tag `llama3.1`, LICENSE (Llama 3.1 Community License Agreement). 3-1B-INT4 repo: licence tag `llama3.2`, LICENSE.txt (Llama 3.2 Community License Agreement). Both repos are published under the `meta-llama` HF org.
  - Section 1.b.i (3.1 and 3.2, same wording): "If you distribute or make available the Llama Materials (or any derivative works thereof) … you shall (A) provide a copy of this Agreement with any such Llama Materials; and (B) prominently display “Built with Llama”".
  - Same section: "you shall also include “Llama” at the beginning of any such AI model name." This applies to "an AI model, which is distributed or made available" that was created, trained, fine-tuned or improved using the Llama Materials or their outputs.
  - Section 1.b.iii: "You must retain in all copies of the Llama Materials that you distribute the following attribution notice within a “Notice” text file". Llama 3.1: “Llama 3.1 is licensed under the Llama 3.1 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved.” The Llama 3.2 notice names "Llama 3.2".
  - Section 5.b: "with respect to any derivative works and modifications of the Llama Materials that are made by you, as between you and Meta, you are and will be the owner of such derivative works and modifications."
  - Llama 4 (LG4) section 1.b.i: "prominently display “Built with Llama” on a related website, user interface, blogpost, about page, or product documentation", plus the "Llama" name prefix and a Notice text file ("Llama 4 is licensed under the Llama 4 Community License…").
  - LG2 (Llama 3) uses "Built with Meta Llama 3" and the prefix "Llama 3". LG1 (Llama 2) has "You will not use the Llama Materials or any output or results of the Llama Materials to improve any other large language model (excluding Llama 2 or derivative works thereof)."
  - The Meta-published names "Llama-Guard-3-8B-INT8" and "Llama-Guard-3-1B-INT4" both start with "Llama".
- Label to use: [Documented]. Interpretation of how a given deployment is affected is out of scope.
- Draft impact (suggested addition, not in drafts): INV(a) 3-8B-INT8 and 3-1B-INT4 Licence cells: append "derivative or redistributed copies carry copy-of-licence, 'Built with Llama', Notice-file and 'Llama' model-name-prefix duties per section 1.b [Documented]".
- Changes Summary? N.

---

## Summary table

| Tn | Verdict | Label | Changes Summary? |
|---|---|---|---|
| T1 | RESOLVED (+ minor CORRECTION, INV INT8 score cell) | [Documented] / [Not disclosed] | N |
| T3 | CORRECTION | [Documented] (INT4 only) / [Not disclosed] | Y (A LG1 R8, A LG2 R8) |
| T5 | PARTLY RESOLVED | [Documented] (fine-tune lengths) / [Inferred] / [Not disclosed] | N |
| T6 | PARTLY RESOLVED | [Documented] / [To be verified] | N |
| T7 | STILL OPEN (checked 3-1B and INT4 cards, INT4 paper, DOCS3; support not stated) | [Documented] facts / [Not disclosed] | N |
| T8 | CORRECTION (INV 3-11B-V "English only") | [Documented] / [Not disclosed] | Y (A LG2 R6) |
| T9 | CORRECTION (B LG3 R4, R8) | [Documented] | Y (B LG3 R8) |
| T11 | RESOLVED | [Documented] | N |
| T12 | PARTLY RESOLVED | [Documented] / [Not disclosed] | N |
| T20 | RESOLVED (negative) | [Not disclosed] / [Documented] | N |
| T25 | RESOLVED (negative) | [Not disclosed] | N |
| T26 | RESOLVED | [Documented] | N |
| T27 | RESOLVED | [Documented: repo PurpleLlama@172c1074] | N |
| T39 | CORRECTION (A LG2 R2) | [Documented] | N |
| T40 | RESOLVED | [Documented] | N |
| T41 | RESOLVED | [Documented] / [Inferred] (unit explanation) | N |
| T42 | RESOLVED | [Documented: repo PurpleLlama@172c1074] | N |
| T43 | RESOLVED | [Documented] | N |
| T44 | PARTLY RESOLVED | [Documented] / [Inferred] / [Not disclosed] | N |
| T46 | RESOLVED (extra source 2407.21783) | [Documented] | N |
| T47 | RESOLVED | [Documented] | N |
| T48 | RESOLVED | [Documented] ([Inferred] for INT4 same-day) | N |
| T49 | RESOLVED | [Documented] | N |
| T50 | RESOLVED (draft right; brief wrong) | [Documented] | N |
| T52 | RESOLVED | [Documented] | N |
| T53 | RESOLVED | [Documented] | N |
| T57 | RESOLVED | [Documented] | N |
| T58 | PARTLY RESOLVED | [Documented] / [To be verified] (applicability) | N |
| T59 | RESOLVED | [Documented] | N |

## Report

Counts (29 items): RESOLVED 19 (T1, T11, T20, T25, T26, T27, T40, T41, T42, T43, T46, T47, T48, T49, T50, T52, T53, T57, T59), PARTLY RESOLVED 5 (T5, T6, T12, T44, T58), STILL OPEN 1 (T7), CORRECTION 4 (T3, T8, T9, T39). T1 is counted as RESOLVED but carries one minor inventory correction.

CORRECTIONs:
- T3: A LG1 R4 and A LG2 R4 say no official latency exists; arXiv 2411.17713 gives at least 30 tokens/s and time-to-first-token of 2.5 s or less for LG3-1B-INT4 on a Moto-Razor phone CPU.
- T8: INV(a) 3-11B-V Languages "English only" should read "optimised for English" (card wording); the brief wording too.
- T9: B LG3 R4 (tile size "not stated … [To be verified]"), B LG3 R8 bullet 1 and Reviewer note 8. DOCS4 states 336×336 tiles plus a global tile.
- T39: A LG2 R2 PGD response figure should be 6% to 22% at 8/255 (27% only at 128/255 and 255/255).
- Minor inside T1: INV(a) 3-8B-INT8 Score method cell says the card gives no method; the INT8 card repeats the 8B first-token-probability and "apply score thresholding" text.
- Other items where the brief, not the draft, is wrong: T50 (LG1 O-code order), T39 (brief's 6% to 27%).

Summary lines that must change:
1. A LG1 R8 (T3). New: "**Key open questions.** No documented decision threshold, unclear LG4 language coverage (which 12 languages), no prompt-only numbers for LG3-1B or LG4, and latency figures only for LG3-1B-INT4 on one phone."
2. A LG2 R8 (T3). New: "**Key open questions.** No documented decision threshold, conflicting LG4 language statements, no like-for-like response numbers across versions, and latency figures only for LG3-1B-INT4 on one phone."
3. A LG2 R6 (T8, wording). New: "**Prompt and response pair.** Needs the user prompt and the agent response, plus the policy prompt. LG3 text models cover eight languages; LG4 adds images and cites the same languages; LG3-11B-Vision is English-optimised with one image. **[Documented]**"
4. B LG3 R8 (T9). New: "**Key open questions.** No documented threshold for 3-11B-Vision or LG4, behaviour beyond about three images in LG4, and whether the OGX vision branch is reached by the Hugging Face id."

Still open after this pass: T7 (Vietnamese and Indonesian support), T6 (which 12 languages PROT means), T58 applicability to the guard models, and T5 (guard context lengths; config.json gated).
