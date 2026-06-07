from app.services.prompt_loader import format_chat_prompt

prompt = format_chat_prompt(
    "farmer_query_prompt.txt",
    context="Drip irrigation saves water.",
    question="How to reduce water usage?"
)

print(prompt)