from fastapi import APIRouter

from app.services.environment_feature_service import (
    get_final_environment_features
)


# router = APIRouter()
router = APIRouter(

    prefix="",

    tags=["Environment Data"]

)


@router.get("/environment")

def get_environment(

    lat: float,
    lon: float

):

    features = get_final_environment_features(
        lat,
        lon
    )

    return features