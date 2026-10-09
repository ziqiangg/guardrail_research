# status 200  final_url https://huggingface.co/api/resolve-cache/datasets/govtech/lionguard-2-synthetic-instruct/8aa43f6172eb7eb158fd433fe3cf627c9a30db26/README.md?%2Fdatasets%2Fgovtech%2Flionguard-2-synthetic-instruct%2Fresolve%2F8aa43f61%2FREADME.md=&etag=%224b17d1087bc18e32fa70a65346e2cfc87d73e274%22  content-type text/plain; charset=utf-8
---
license: other
license_name: govtech-singapore
license_link: LICENSE
task_categories:
- text-classification
language:
- en
---

# LionGuard 2 Dataset (subset)
LionGuard 2 is a multilingual content moderation classifier tuned for English/Singlish, Chinese, Malay, and Tamil in the Singapore context.

This dataset is a subset of the LionGuard 2 training corpus.
All texts are Singlish/English forum comments **LLM-rewritten into a chatbot style** paired with embeddings from three models and semi-supervised moderation labels:

**Embedding columns:**
- `embedding` - OpenAI `text-embedding-3-large` embeddings used in `lionguard-2`
- `embedding_lg_2_lite` - EmbeddingGemma-300m embeddings used in `lionguard-2-lite`
- `embedding_lg_2.1` - Gemini `gemini-embedding-001` embeddings used in `lionguard-2.1`

**Moderation labels:**
- Overall safety (`binary`)
- Hate (`hateful_l1`, `hateful_l2`)
- Insults (`insults`)
- Sexual content (`sexual_l1`, `sexual_l2`)
- Physical violence (`physical_violence`)
- Self-harm (`self_harm_l1`, `self_harm_l2`)
- Other misconduct (`all_other_misconduct_l1`, `all_other_misconduct_l2`)


(Each harm category uses **0 / 1 / 2**  `(0 = safe, 1 = Level 1, 2 = Level 2)`)

**Dataset stats**

* 2 055 safe · 43 unsafe (≈ 2 % unsafe)  
* Language: Singlish/English only
