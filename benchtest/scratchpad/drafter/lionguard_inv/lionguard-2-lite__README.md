# status 200  final_url https://huggingface.co/api/resolve-cache/models/govtech/lionguard-2-lite/d56c17a08a937f2591a906fb5c8ec699a844c422/README.md?%2Fgovtech%2Flionguard-2-lite%2Fresolve%2Fd56c17a0%2FREADME.md=&etag=%2215d8c4f849c71b9c771fb3652a3e16716c2823ef%22  content-type text/plain; charset=utf-8
---
license: other
license_name: govtech-singapore
license_link: LICENSE
language:
- en
- ms
- ta
- zh
pipeline_tag: text-classification
tags:
- classifier
- safety
- moderation
- multilingual
---

# LionGuard 2 Lite
LionGuard 2 is a multilingual content moderation classifier tuned for English/Singlish, Chinese, Malay, and Tamil in the Singapore context.

This `lite` version leverages Google's `embeddinggemma-300m` (768-dimensional embeddings) with a multi-head classifier to return fine-grained scores for the following categories:
- Overall safety (`binary`)
- Hate (`hateful_l1`, `hateful_l2`)
- Insults (`insults`)
- Sexual content (`sexual_l1`, `sexual_l2`)
- Physical violence (`physical_violence`)
- Self-harm (`self_harm_l1`, `self_harm_l2`)
- Other misconduct (`all_other_misconduct_l1`, `all_other_misconduct_l2`)

LionGuard 2 Lite runs fully locally, with no external API calls.

---

# Taxonomy

| S/N | Category              | Level                                   | Description                                                                                               | Example                                                                                                                                                                   |
|-----|-----------------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1** | Hate                  | **1 (Discriminatory)**                | Derogatory or generalized negative statements targeting a protected group.                                | “All Chinese people are so scheming.”<br>“Malays are always late and lazy.”<br>“Indians are too noisy; I avoid them whenever possible.”                                   |
|     |                       | **2 (Hate Speech)**                    | Explicit calls for harm or violence against a protected group.                                            | “We should kick all Chinese people out of the country.”<br>“Burn down their temple…”<br>“Kill the Indians in Little India; they don’t belong here.”                      |
| **2** | Insults               | *no sub-levels*                        | Demeans, humiliates, or mocks without referencing a protected trait.                                      | “You’re so dumb, you probably failed your PSLE.”<br>“Your singing is worse than karaoke at a dodgy KTV.”                                                                  |
| **3** | Sexual                | **1 (Not appropriate for minors)**    | Mild-to-moderate sexual content.                                                                          | “Let’s talk about how condoms work.” <br>“We had a one-night stand last weekend.”                                                                                          |
|     |                       | **2 (Not appropriate for all ages)**   | Explicit or graphic sexual content.                                                                       | “Always think they very yandao … but actually is just one ** bin.”                                                                                                        |
| **4** | Physical Violence     | *no sub-levels*                        | Glorification of violence or threats of physical harm.                                                    | “If I see him at Clarke Quay, I’m going to whack him.”<br>“Someone should plant a bomb at that office…”                                                                   |
| **5** | Self-Harm             | **1 (Ideation)**                      | Expressions of suicidal thoughts or encouragement of self-harm.                                           | “I’m so stressed … I feel like ending it all.”<br>“Failing my poly exams made me want to cut myself.”                                                                     |
|     |                       | **2 (Action / Suicide)**               | Descriptions of ongoing or imminent self-harm behavior.                                                   | “I’ve locked myself in my room and taken a bunch of pills.”<br>“I’m on the rooftop at Toa Payoh, ready to jump.”                                                         |
| **6** | All Other Misconduct  | **1 (Generally not socially accepted)**| Unethical or immoral behavior not necessarily illegal.                                                    | “Let’s spread fake rumours about her …”<br>“How to secretly record someone’s private conversation?”                                                                     |
|     |                       | **2 (Illegal activities)**             | Instructions or credible threats of serious harm; facilitation of crimes.                                 | “Anyone know where to buy illegal knives in Geylang?”<br>“Let’s hack that e-commerce site to get credit card details.”                                                    |

---

# Usage

```python
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoModel

# Load model directly from Hub
model = AutoModel.from_pretrained("govtech/lionguard-2-lite", trust_remote_code=True)

# Download model from the 🤗 Hub
embedding_model = SentenceTransformer("google/embeddinggemma-300m")

# Text to classify
texts = ["hello", "world"]

# Add prompt instructions to generate embeddings that are optimized to classify texts according to preset labels
formatted_texts = [f"task: classification | query: {c}" for c in texts]
embeddings = embedding_model.encode(formatted_texts) # NOTE: use encode() instead of encode_documents()

# Run inference
results = model.predict(embeddings)
```
