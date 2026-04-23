from llm.rag_pipeline import rag_answer


query = "Which scheme supports drip irrigation?"

response = rag_answer(query)

print("\nRAG RESPONSE:\n")
print(response)