from fastapi import APIRouter

# from app.core.rate_limiter import limiter
# from fastapi import Request

from app.schemas.voice_schema import (
    VoiceRequest,
    VoiceResponse
)

from llm.rag_pipeline import rag_answer
from app.services.llm_service import get_agriculture_instructions
from app.core.logger import get_logger

logger = get_logger(__name__)

# router = APIRouter()
router = APIRouter(

    prefix="",

    tags=["Voice Assistant"]

)


@router.post("/voice")
def voice_endpoint(
    request: VoiceRequest
):
    user_message = request.message
    
    # Get the welcome instructions first
    instructions = get_agriculture_instructions()
    
    # Use context for agriculture-flavored queries, but answer all questions normally.
    fast_keywords = ["water", "soil", "crop", "fertilizer", "pest", "disease", "irrigation", "yield"]
    use_context = any(kw in user_message.lower() for kw in fast_keywords)
    
    ai_response = rag_answer(
        user_message,
        use_context=use_context,
        show_instructions=True
    )
    
    short_reason = "Welcome message shown first"
    for line in ai_response.splitlines():
        cleaned = line.strip()
        if cleaned.lower().startswith("reason"):
            short_reason = cleaned.split(":", 1)[-1].strip() if ":" in cleaned else cleaned
            break
    
    return VoiceResponse(
        response=ai_response,
        short_reason=short_reason
    )