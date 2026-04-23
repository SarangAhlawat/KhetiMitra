from fastapi import APIRouter

# from app.core.rate_limiter import limiter
# from fastapi import Request

from app.schemas.voice_schema import (
    VoiceRequest,
    VoiceResponse
)

from llm.rag_pipeline import rag_answer


# router = APIRouter()
router = APIRouter(

    prefix="",

    tags=["Voice Assistant"]

)


@router.post("/voice")

# @limiter.limit("60/minute")

def voice_endpoint(
    request: VoiceRequest
):

    user_message = request.message

    # Call RAG pipeline

    ai_response = rag_answer(
        user_message
    )

    return VoiceResponse(

        response=ai_response

    )

# inside any route (test)

# raise Exception("Test error")