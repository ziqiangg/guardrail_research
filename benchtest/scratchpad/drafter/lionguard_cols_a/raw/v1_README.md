---
license: other
license_name: govtech-singapore
license_link: LICENSE
---

# LionGuard

LionGuard is a classifier for detecting unsafe content in the Singapore context. It uses pre-trained BAAI English embeddings and performs classification with a trained Ridge Classification model. 

# Usage

1. Install `transformers` , `onnxruntime` and `huggingface_hub` libraries. 
```
pip install transformers onnxruntime huggingface_hub
```

2. Run inference.
```
python inference.py '["Example text 1"]'
```

Technical report is available [here](https://arxiv.org/abs/2407.10995).
