import requests
from backend.app.services.prompt_loader import load_prompt
from backend.app.services.prompt_formatter import format_prompt

from app.core.logger import get_logger

logger = get_logger(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"



def generate_farmer_response(
    question: str,
    context: str
):

    template = load_prompt(
        "farmer_query_prompt.txt"
    )

    prompt = format_prompt(
        template,
        context=context,
        question=question
    )

    return generate_response(prompt)



def generate_response(prompt: str):

    try:

        logger.info("Sending prompt to LLM")

        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=360
        )

        result = response.json()

        logger.info("LLM response received")

        return result["response"]

    except Exception as e:

        logger.error(
            f"LLM Error: {str(e)}"
        )

        return "LLM error occurred."