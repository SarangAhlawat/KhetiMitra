import re

try:
    from google import genai as google_genai
except Exception:
    google_genai = None

try:
    import google.generativeai as legacy_genai
except Exception:
    legacy_genai = None

from app.core.config import (
    GEMINI_FALLBACK_MODELS as _FALLBACK_MODELS_STR,
    GEMINI_MODEL,
    GEMINI_TIMEOUT,
    GOOGLE_API_KEY,
)
from app.services.prompt_loader import format_chat_prompt
from app.core.logger import get_logger

logger = get_logger(__name__)

DEFAULT_MODEL = GEMINI_MODEL
FALLBACK_MODELS = [
    m.strip()
    for m in _FALLBACK_MODELS_STR.split(",")
    if m.strip()
]


def _model_candidates() -> list[str]:
    # Try known-working models first even if .env still points at an exhausted model.
    models = [
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite",
        DEFAULT_MODEL,
        *FALLBACK_MODELS,
    ]
    seen = set()
    ordered = []
    for model in models:
        if model and model not in seen:
            seen.add(model)
            ordered.append(model)
    return ordered


FARMING_ADVICE = {
    "water": [
        "Install drip irrigation to deliver water directly to roots and cut wastage.",
        "Mulch the soil surface to reduce evaporation during hot weather.",
        "Harvest rainwater and store it for dry periods.",
        "Check soil moisture before irrigating instead of following a fixed schedule.",
    ],
    "soil": [
        "Add well-decomposed compost to improve structure and organic matter.",
        "Rotate crops each season to prevent nutrient depletion.",
        "Get a soil test done before applying fertilizer.",
        "Reduce chemical overuse and build soil biology with organic inputs.",
    ],
    "crop": [
        "Choose crops suited to your local climate, soil type, and water availability.",
        "Use mixed or intercropping to lower pest and market risk.",
        "Follow local agriculture department recommendations for your district.",
    ],
    "fertilizer": [
        "Base fertilizer plans on soil test results, not guesswork.",
        "Apply balanced NPK and split doses across growth stages.",
        "Combine chemical fertilizers with compost for long-term soil health.",
    ],
    "pest": [
        "Scout fields regularly and act early when pest levels rise.",
        "Use neem-based sprays, natural predators, and crop rotation first.",
        "Apply chemical pesticides only when thresholds are crossed.",
    ],
    "disease": [
        "Maintain proper plant spacing for airflow.",
        "Avoid over-irrigation and remove infected plants quickly.",
        "Rotate crops and use disease-resistant varieties where possible.",
    ],
    "irrigation": [
        "Prefer drip or sprinkler systems over flood irrigation.",
        "Irrigate early morning or evening to reduce evaporation.",
        "Monitor soil moisture and prevent waterlogging.",
    ],
    "yield": [
        "Use quality seed and correct planting spacing.",
        "Weed on time and maintain balanced nutrition.",
        "Protect crops during critical growth stages with timely irrigation and pest control.",
    ],
    "scheme": [
        "Check PM-KISAN, Soil Health Card, and drip/micro-irrigation subsidy schemes.",
        "Visit your nearest agriculture office with land and ID documents.",
        "Apply before seasonal deadlines to avoid missing benefits.",
    ],
    "organic": [
        "Build organic matter with compost, green manure, and crop residue retention.",
        "Shift gradually from synthetic inputs to reduce yield shock.",
        "Plan certification only when you have reliable organic market access.",
    ],
}

RISK_TIPS = {
    "water": "Over-irrigation can cause root rot, nutrient leaching, and higher input costs.",
    "soil": "Skipping soil tests often leads to wrong fertilizer use and long-term soil damage.",
    "pest": "Spraying pesticides too early or too often can harm beneficial insects and increase resistance.",
    "disease": "Delayed action on infected plants can spread disease across the whole field.",
    "fertilizer": "Excess nitrogen can burn plants and pollute groundwater.",
}


def _extract_response_text(result) -> str | None:
    text = getattr(result, "text", None)
    if text:
        return text.strip()

    candidates = getattr(result, "candidates", None) or []
    for candidate in candidates:
        content = getattr(candidate, "content", None)
        parts = getattr(content, "parts", None) or []
        chunks = []
        for part in parts:
            part_text = getattr(part, "text", None)
            if part_text:
                chunks.append(part_text)
        if chunks:
            return "\n".join(chunks).strip()

    return None


def _classify_gemini_error(error: Exception) -> str:
    message = str(error)

    if "GOOGLE_API_KEY" in message or "API key" in message:
        return "AI not configured. Set GOOGLE_API_KEY in your .env file."

    if "429" in message or "RESOURCE_EXHAUSTED" in message or "quota" in message.lower():
        return "Gemini API quota exceeded. Try again later or update GEMINI_MODEL."

    if "404" in message and "model" in message.lower():
        return "Configured Gemini model is unavailable."

    if google_genai is None and legacy_genai is None:
        return "Gemini SDK is not installed. Install google-genai."

    return "Gemini could not generate a response right now."


def _parse_context_blocks(context: str, limit: int = 4) -> list[dict]:
    if not context or context.strip() == "Use general agricultural best practices.":
        return []

    blocks = []
    for raw in re.split(r"\n*Source:\s*", context):
        cleaned = re.sub(r"\s+", " ", raw).strip()
        if not cleaned:
            continue

        source = "knowledge base"
        text = cleaned
        if " " in cleaned:
            first, rest = cleaned.split(" ", 1)
            if first.endswith("_index"):
                source = first.replace("_index", "").replace("_", " ")
                text = rest

        blocks.append({"source": source, "text": text[:500]})
        if len(blocks) >= limit:
            break

    return blocks


def _pick_topic_advice(question: str) -> tuple[str, list[str]]:
    q_lower = question.lower()
    for topic, tips in FARMING_ADVICE.items():
        if topic in q_lower:
            return topic, tips
    return "general", [
        "Share your crop, soil type, and location for more specific advice.",
        "Start with soil testing and water-efficient irrigation.",
        "Follow integrated pest management and crop rotation for sustainability.",
    ]


def _pick_risk_tip(topic: str, question: str) -> str:
    if topic in RISK_TIPS:
        return RISK_TIPS[topic]

    q_lower = question.lower()
    for key, tip in RISK_TIPS.items():
        if key in q_lower:
            return tip

    return "Always verify advice with local weather, soil conditions, and extension officers before large-scale changes."


def build_structured_fallback(question: str, context: str) -> str:
    """Produce an LLM-style structured answer from retrieved knowledge."""
    topic, recommendations = _pick_topic_advice(question)
    context_blocks = _parse_context_blocks(context)
    risk_tip = _pick_risk_tip(topic, question)

    overview = (
        f"Here is practical guidance based on your question about {topic if topic != 'general' else 'farming'}. "
        "The advice below combines retrieved agricultural knowledge with established sustainable practices."
    )

    if context_blocks:
        cause_lines = []
        for block in context_blocks[:2]:
            cause_lines.append(f"- From {block['source']}: {block['text'][:280]}")
        causes = "**Causes and reasoning**\n" + "\n".join(cause_lines)
    else:
        causes = (
            "**Causes and reasoning**\n"
            "- Farm outcomes depend on soil health, water availability, crop choice, and timely field management.\n"
            "- Sustainable practices improve resilience and reduce long-term input costs."
        )

    recs = "**Recommendations**\n" + "\n".join(f"- {tip}" for tip in recommendations)

    if context_blocks:
        extra = [f"- {block['text'][:220]}" for block in context_blocks[:2]]
        recs += "\n" + "\n".join(extra)

    risks = (
        "**Risks and precautions**\n"
        f"- {risk_tip}\n"
        "- Monitor field conditions after any change and adjust practices season by season."
    )

    reason = (
        f"Reason: This advice is based on retrieved agricultural knowledge and sustainable "
        f"farming practices relevant to {topic if topic != 'general' else 'your question'}."
    )

    return "\n\n".join([overview, causes, recs, risks, reason])


def _call_gemini_new_sdk(api_key: str, model: str, prompt: str) -> str | None:
    client = google_genai.Client(api_key=api_key)
    result = client.models.generate_content(model=model, contents=prompt)
    return _extract_response_text(result)


def _call_gemini_legacy(api_key: str, model: str, prompt: str, timeout: int) -> str | None:
    legacy_genai.configure(api_key=api_key)
    model_obj = legacy_genai.GenerativeModel(model)
    result = model_obj.generate_content(prompt, request_options={"timeout": timeout})
    return _extract_response_text(result)


def generate_farmer_response(question: str, context: str):
    """Generate farmer-friendly response with context."""
    prompt = format_chat_prompt(
        "farmer_query_prompt.txt",
        context=context,
        question=question,
    )
    return generate_response(
        prompt,
        question=question,
        context=context,
    )


def generate_response(
    prompt: str,
    timeout: int = None,
    show_instructions: bool = False,
    question: str | None = None,
    context: str | None = None,
):
    """Generate response using Gemini with model fallback and structured knowledge fallback."""

    if timeout is None:
        timeout = GEMINI_TIMEOUT

    last_error = None

    try:
        api_key = GOOGLE_API_KEY

        if not api_key:
            logger.error("GOOGLE_API_KEY not set")
            if question:
                return build_structured_fallback(question, context or "")
            return "AI not configured. Set GOOGLE_API_KEY."

        if google_genai is None and legacy_genai is None:
            logger.error("Gemini SDK not installed")
            if question:
                return build_structured_fallback(question, context or "")
            return "Gemini SDK is not installed. Install google-genai."

        for model in _model_candidates():
            logger.info(f"Gemini call (timeout={timeout}s, model={model})")

            if google_genai is not None:
                try:
                    text = _call_gemini_new_sdk(api_key, model, prompt)
                    if text:
                        logger.info(f"Gemini response from {model}")
                        return text
                    last_error = RuntimeError(f"{model} returned an empty response.")
                except Exception as e:
                    last_error = e
                    logger.warning(f"New SDK failed for {model}: {e}")

            if legacy_genai is not None:
                try:
                    text = _call_gemini_legacy(api_key, model, prompt, timeout)
                    if text:
                        logger.info(f"Legacy Gemini response from {model}")
                        return text
                    last_error = RuntimeError(f"Legacy {model} returned an empty response.")
                except Exception as e:
                    last_error = e
                    logger.warning(f"Legacy SDK failed for {model}: {e}")

        error_hint = _classify_gemini_error(last_error) if last_error else "Gemini unavailable."
        logger.error(f"All Gemini models failed: {error_hint} | {last_error}")

        if question:
            return build_structured_fallback(question, context or "")

        return error_hint

    except Exception as e:
        logger.error(f"Gemini error: {str(e)}")
        if question:
            return build_structured_fallback(question, context or "")
        return f"An error occurred while generating the response: {str(e)}"
