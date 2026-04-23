from llm.embeddings.embedder import create_embedding

text = "Drip irrigation saves water."

embedding = create_embedding(text)

print("Vector shape:", embedding.shape)