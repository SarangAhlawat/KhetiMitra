from backend.app.services.knowledge_service import (
    get_rag_response
)


query = "How to prevent pest attack in wheat?"

result = get_rag_response(query)

print(result)