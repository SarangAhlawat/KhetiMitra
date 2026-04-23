from llm.vector_store.context_builder import (
    build_context
)

query = "How to reduce pest attack in wheat?"

context = build_context(query)

print(context)