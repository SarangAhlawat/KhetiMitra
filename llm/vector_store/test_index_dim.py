import faiss

index = faiss.read_index(
    "llm/vector_store/soil_index/index.faiss"
)

print("Index dimension:", index.d)