from app.services.prompt_loader import load_prompt
from app.services.prompt_formatter import format_prompt

template = load_prompt(
    "farmer_query_prompt.txt"
)

prompt = format_prompt(
    template,
    context="Drip irrigation saves water.",
    question="How to reduce water usage?"
)

print(prompt)