# status 200  final_url https://huggingface.co/govtech/lionguard-2.1/raw/1c3a9ea7718f81ea32e6688c0ff18ac8866525e8/README.md  content-type text/plain; charset=utf-8
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

# LionGuard 2.1
LionGuard 2.1 is a multilingual content moderation classifier tuned for English/Singlish, Chinese, Malay, and Tamil in the Singapore context. 

It leverages Gemini's `gemini-embedding-001` with a multi-head classifier to return fine-grained scores for the following categories:
- Overall safety (`binary`)
- Hate (`hateful_l1`, `hateful_l2`)
- Insults (`insults`)
- Sexual content (`sexual_l1`, `sexual_l2`)
- Physical violence (`physical_violence`)
- Self-harm (`self_harm_l1`, `self_harm_l2`)
- Other misconduct (`all_other_misconduct_l1`, `all_other_misconduct_l2`)

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
import os
import numpy as np
from transformers import AutoModel
from google import genai

# Load model directly from HF
model = AutoModel.from_pretrained("govtech/lionguard-2.1", trust_remote_code=True)

# Text to classify
texts = ["hello", "world"]

# Get embeddings (users to input their own Gemini API key)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts
)
embeddings = np.array([emb.values for emb in response.embeddings])

# Run inference
results = model.predict(embeddings)
```
