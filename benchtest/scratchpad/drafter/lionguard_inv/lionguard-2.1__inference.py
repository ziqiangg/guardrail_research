# status 200  final_url https://huggingface.co/api/resolve-cache/models/govtech/lionguard-2.1/1c3a9ea7718f81ea32e6688c0ff18ac8866525e8/inference.py?%2Fgovtech%2Flionguard-2.1%2Fresolve%2F1c3a9ea7%2Finference.py=&etag=%22acc20ef9eb4de3f848871e3c6c48c60266f52f8f%22  content-type text/plain; charset=utf-8
import json
import os
import sys
import numpy as np
from google import genai
from transformers import AutoModel


def infer(texts):
    # Load model directly from Hub
    model = AutoModel.from_pretrained("govtech/lionguard-2.1", trust_remote_code=True)

    # Get embeddings (users to input their own Gemini API key)
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texts
    )
    embeddings = np.array([emb.values for emb in result.embeddings])

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
