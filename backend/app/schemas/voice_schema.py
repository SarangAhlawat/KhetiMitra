from pydantic import BaseModel


class VoiceRequest(BaseModel):

    user_id: int
    message: str


class VoiceResponse(BaseModel):

    response: str