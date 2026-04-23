from app.services.llm_service import generate_response

prompt = """
Explain the benefits of drip irrigation
for small farmers in Punjab.
"""

response = generate_response(prompt)

print(response)