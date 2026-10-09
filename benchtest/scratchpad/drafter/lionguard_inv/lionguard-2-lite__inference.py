# status 200  final_url https://huggingface.co/api/resolve-cache/models/govtech/lionguard-2-lite/d56c17a08a937f2591a906fb5c8ec699a844c422/inference.py?%2Fgovtech%2Flionguard-2-lite%2Fresolve%2Fd56c17a0%2Finference.py=&etag=%221e510b11595977f28ce3437f586f224d748fffe9%22  content-type text/plain; charset=utf-8
import json
import os
import sys
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoModel

def format_texts(texts):
    # Add prompt instructions to generate embeddings that are optimized to classify texts according to preset labels
    return [f"task: classification | query: {c}" for c in texts]

def infer(texts):
    # Load model directly from Hub
    model = AutoModel.from_pretrained("govtech/lionguard-2-lite", trust_remote_code=True)

    # Download model from the 🤗 Hub
    embedding_model = SentenceTransformer("google/embeddinggemma-300m")
    formatted_texts = format_texts(texts)
    embeddings = embedding_model.encode(formatted_texts) # NOTE: use encode() instead of encode_documents()

    # Run inference
    results = model.predict(embeddings)
    return results


if __name__ == "__main__":

    # Load the data
    try:
        input_data = sys.argv[1]
        batch_text = json.loads(input_data)
        print("Using provided input texts")

    except (json.JSONDecodeError, IndexError) as e:
        print(f"Error parsing input data: {e}")
        print("Falling back to default sample texts")

        batch_text = ["Eh you damn stupid lah!", "Have a nice day :)"]

    # Generate the scores and predictions
    results = infer(batch_text)
    for i in range(len(batch_text)):
        print(f"Text: '{batch_text[i]}'")
        for category in results.keys():
            print(f"[Text {i+1}] {category} score: {results[category][i]:.4f}")
        print("---------------------------------------------")
