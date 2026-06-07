import re

from fastapi import APIRouter

from app.schemas.voice_schema import (
    VoiceRequest,
    VoiceResponse
)

from llm.rag_pipeline import rag_answer
from app.core.logger import get_logger

logger = get_logger(__name__)

router = APIRouter(
    prefix="",
    tags=["Voice Assistant"]
)


def _strip_markdown(text: str) -> str:
    cleaned = re.sub(r"\*\*|__", "", text)
    cleaned = re.sub(r"^[_*]+|[_*]+$", "", cleaned)
    return cleaned.strip()


def extract_short_reason(response: str) -> str:
    for line in response.splitlines():
        cleaned = line.strip()
        if cleaned.lower().startswith("reason"):
            return _strip_markdown(
                cleaned.split(":", 1)[-1].strip() if ":" in cleaned else cleaned
            )

    for line in response.splitlines():
        cleaned = _strip_markdown(line)
        if cleaned.startswith("- ") and len(cleaned) > 24:
            return cleaned[2:][:160] + ("..." if len(cleaned) > 162 else "")

    text = _strip_markdown(response.replace("\n", " "))
    if not text:
        return "Based on agricultural knowledge and best practices."

    sentences = re.split(r"(?<=[.!?])\s+", text)
    for sentence in sentences:
        cleaned = _strip_markdown(sentence)
        if len(cleaned) >= 20 and not cleaned.lower().startswith("gemini api"):
            return cleaned[:160] + ("..." if len(cleaned) > 160 else "")

    return text[:160] + ("..." if len(text) > 160 else "")


@router.post("/voice")
def voice_endpoint(
    request: VoiceRequest
):
    user_message = request.message
    ai_response = rag_answer(user_message)
    short_reason = extract_short_reason(ai_response)

    return VoiceResponse(
        response=ai_response,
        short_reason=short_reason
    )
