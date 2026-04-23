from sentence_transformers import SentenceTransformer
import numpy as np

# Load once (global)
MODEL_NAME = "all-MiniLM-L6-v2"

print("Loading embedding model...")

model = SentenceTransformer(MODEL_NAME)

print("Embedding model loaded.")


def create_embedding(text: str):

    """
    Convert text into vector embedding
    """

    if not text:
        text = "empty"

    embedding = model.encode(
        text,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embedding.astype("float32")