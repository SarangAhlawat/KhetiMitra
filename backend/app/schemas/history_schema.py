from pydantic import BaseModel
from datetime import datetime


class HistoryCreate(BaseModel):

    farm_id: int
    crop: str
    yield_value: float
    fertilizer: float
    pesticide: float
    profit: float


class HistoryResponse(BaseModel):

    history_id: int
    farm_id: int
    crop: str
    yield_value: float
    fertilizer: float
    pesticide: float
    profit: float
    created_at: datetime

    class Config:
        from_attributes = True