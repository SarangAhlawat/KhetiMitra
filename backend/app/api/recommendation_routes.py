from fastapi import APIRouter

from app.services.qssm_service import compute_qssm
from app.services.ml_service import predict_crop
from pydantic import BaseModel


class RecommendationResponse(BaseModel):

    recommended_crop: str
    sustainability_score: float

# router = APIRouter()
router = APIRouter(

    prefix="",

    tags=["Recommendations"]

)


@router.post(

    "/recommendation",

    response_model=RecommendationResponse

)

def get_recommendation(data: dict):

    qssm_score = compute_qssm(data)

    crop = predict_crop(data)

    return {

        "recommended_crop": crop,
        "sustainability_score": qssm_score

    }