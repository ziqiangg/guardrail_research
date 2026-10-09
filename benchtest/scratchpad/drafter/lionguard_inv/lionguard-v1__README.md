# status 200  final_url https://huggingface.co/api/resolve-cache/models/govtech/lionguard-v1/92cc0491764602c97031693a7f1a2bcc82c6aaf9/README.md?%2Fgovtech%2Flionguard-v1%2Fresolve%2F92cc0491%2FREADME.md=&etag=%227261689c0e2392491e3d89e5174b09337cdf3c8e%22  content-type text/plain; charset=utf-8
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
