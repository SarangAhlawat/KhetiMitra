import os
from dotenv import load_dotenv

load_dotenv()

try:
    from google import genai as google_genai
except Exception:
    google_genai = None

try:
    import google.generativeai as legacy_genai
except Exception:
    legacy_genai = None

from app.services.prompt_loader import load_prompt
from app.services.prompt_formatter import format_prompt
from app.core.logger import get_logger

# A small keyword set remains available for optional agriculture-aware fallback logic.
AGRICULTURE_KEYWORDS = {
    "water", "soil", "crop", "fertilizer", "pest", "disease", "irrigation", "yield",
    "compost", "organic", "pesticide", "neem", "fungicide", "harvest", "planting",
    "seed", "farming", "agriculture", "farm", "field", "scheme", "subsidy", "loan",
    "weather", "drip", "sprinkler", "rotation", "intercrop", "mulch", "soil test"
}

WELCOME_RESPONSE = """WELCOME: I'm an Agriculture Assistant with general LLM capabilities.
I can help with agriculture topics like crops, soil, water, irrigation, pests,
diseases, fertilizer, schemes, sustainability, and yield.

I can also answer general questions normally, then connect them back to farming
when relevant."""

FARMING_ADVICE = {
    "water": "For water conservation: Use drip irrigation (water directly to roots), mulch soil to retain moisture, rainwater harvesting, and monitor soil moisture with sensors.",
    "soil": "For soil health: Add organic compost regularly, use crop rotation, avoid overuse of chemicals, do soil testing annually to check pH and nutrients.",
    "crop": "Choose crops suited to your region's climate and soil. Mix different crops to reduce pest risk. Check local government recommendations for your district.",
    "fertilizer": "Use soil testing results to fertilize. Balanced NPK (nitrogen, phosphorus, potassium) is key. Split doses over the season for better absorption.",
    "pest": "Integrated Pest Management: Use natural predators, neem oil spray, companion planting, and avoid pesticides when possible. Alternate pest control methods.",
    "disease": "Prevent disease: Proper spacing for air flow, manage irrigation properly, remove diseased plants early, and rotate crops yearly.",
    "irrigation": "Smart irrigation: Use drip systems for efficiency, irrigate early morning/evening to reduce evaporation, monitor soil moisture, avoid waterlogging.",
    "yield": "Increase yield: Use quality seeds, proper spacing, timely weeding, balanced nutrition, pest management, and water at right times.",
}

logger = get_logger(__name__)

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
GEMINI_TIMEOUT = int(os.getenv("GEMINI_TIMEOUT", "30"))


def get_agriculture_instructions() -> str:
    """Get the welcome message shown before every response."""
    return WELCOME_RESPONSE


def format_with_instructions(response: str, show_instructions: bool = True) -> str:
    """Format response with the welcome message shown first."""
    if show_instructions:
        return f"{WELCOME_RESPONSE}\n\n---\n\n{response}"
    return response


def generate_farmer_response(question: str, context: str):
    """Generate farmer-friendly response with context."""
    template = load_prompt("farmer_query_prompt.txt")
    prompt = format_prompt(template, context=context, question=question)
    return generate_response(prompt, show_instructions=True)


def generate_response(prompt: str, timeout: int = None, show_instructions: bool = False):
    """Generate response from Gemini with timeout, SDK fallback, and instructions."""

    if timeout is None:
        timeout = GEMINI_TIMEOUT

    try:
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            logger.error("GOOGLE_API_KEY not set")
            return format_with_instructions(
                "AI not configured. Set GOOGLE_API_KEY.",
                show_instructions=show_instructions
            )

        logger.info(f"Gemini call (timeout={timeout}s)")

        if google_genai is not None:
            try:
                client = google_genai.Client(api_key=api_key)
                result = client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=prompt,
                )
                text = getattr(result, "text", None)
                if text:
                    return format_with_instructions(text.strip(), show_instructions=show_instructions)
            except Exception as e:
                logger.warning(f"New SDK failed: {e}")

        if legacy_genai is not None:
            try:
                legacy_genai.configure(api_key=api_key)
                model = legacy_genai.GenerativeModel(GEMINI_MODEL)
                result = model.generate_content(prompt, request_options={"timeout": timeout})
                text = getattr(result, "text", None)
                if text:
                    return format_with_instructions(text.strip(), show_instructions=show_instructions)
            except Exception as e:
                logger.warning(f"Legacy SDK failed: {e}")

        logger.error("No Gemini SDK available")
        # Provide fallback advice based on keywords
        prompt_lower = prompt.lower()
        for keyword, advice in FARMING_ADVICE.items():
            if keyword in prompt_lower:
                response = f"{advice}\n\nReason: This is based on best agricultural practices for sustainable farming."
                return format_with_instructions(response, show_instructions=show_instructions)
        
        response = "I can answer questions about: water, soil, crops, fertilizer, pests, diseases, irrigation, and yield. Try asking about these topics."
        return format_with_instructions(response, show_instructions=show_instructions)

    except Exception as e:
        logger.error(f"Gemini error: {str(e)}")
        return format_with_instructions(
            "Error generating response. Try again.",
            show_instructions=show_instructions
        )