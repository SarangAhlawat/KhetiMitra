from fastapi import APIRouter

from app.services.ml_service import predict_crop
from pydantic import BaseModel


class RecommendationResponse(BaseModel):

    recommended_crop: str
    sustainability_score: float


class ExplanationFactor(BaseModel):

    feature: str
    contribution: float
    direction: str
    note: str


class RecommendationExplainResponse(BaseModel):

    recommended_crop: str
    sustainability_score: float
    confidence_score: float
    explanation: list[ExplanationFactor]

# router = APIRouter()
router = APIRouter(

    prefix="",

    tags=["Recommendations"]

)


def estimate_sustainability_score(data: dict) -> float:
    """
    Lightweight score estimator for API response-time usage.
    The full QSSM pipeline is dataset-oriented and not suitable
    for single-request dict inputs.
    """

    ph = float(data.get("ph", 7.0))
    organic = float(data.get("organic_carbon_percent", 0.6))
    rainfall = float(data.get("rainfall_mm", 600))
    humidity = float(data.get("humidity_percent", 55))

    score = 50.0

    score += 12 if 6.0 <= ph <= 7.5 else -7
    score += min(15, organic * 18)
    score += 10 if 500 <= rainfall <= 1000 else -5
    score += 8 if 40 <= humidity <= 75 else -4

    return round(max(0.0, min(100.0, score)), 2)


def build_explanation(data: dict) -> list[dict]:
    """
    Lightweight SHAP-like contribution builder for UI explainability.
    Positive values support recommendation quality and sustainability,
    negative values highlight risk contributors.
    """

    ph = float(data.get("ph", 7.0))
    organic = float(data.get("organic_carbon_percent", 0.6))
    rainfall = float(data.get("rainfall_mm", 600))
    humidity = float(data.get("humidity_percent", 55))
    nitrogen = float(data.get("nitrogen_kg_per_ha", 100))

    ph_contrib = 0.18 if 6.0 <= ph <= 7.5 else -0.14
    organic_contrib = min(0.22, max(-0.1, (organic - 0.5) * 0.25))
    rainfall_contrib = 0.16 if 500 <= rainfall <= 1000 else -0.12
    humidity_contrib = 0.12 if 40 <= humidity <= 75 else -0.08
    nitrogen_contrib = 0.11 if 80 <= nitrogen <= 140 else -0.09

    factors = [
        {
            "feature": "Soil pH",
            "contribution": round(ph_contrib, 3),
            "direction": "positive" if ph_contrib >= 0 else "negative",
            "note": "Balanced pH improves nutrient availability." if ph_contrib >= 0 else "Adjust pH for better root uptake."
        },
        {
            "feature": "Organic Carbon",
            "contribution": round(organic_contrib, 3),
            "direction": "positive" if organic_contrib >= 0 else "negative",
            "note": "Higher carbon supports soil structure and resilience." if organic_contrib >= 0 else "Add compost or residue retention."
        },
        {
            "feature": "Rainfall",
            "contribution": round(rainfall_contrib, 3),
            "direction": "positive" if rainfall_contrib >= 0 else "negative",
            "note": "Rainfall is in a supportive range." if rainfall_contrib >= 0 else "Use irrigation scheduling and water storage."
        },
        {
            "feature": "Humidity",
            "contribution": round(humidity_contrib, 3),
            "direction": "positive" if humidity_contrib >= 0 else "negative",
            "note": "Humidity currently supports crop health." if humidity_contrib >= 0 else "Watch disease risk and moisture stress."
        },
        {
            "feature": "Nitrogen",
            "contribution": round(nitrogen_contrib, 3),
            "direction": "positive" if nitrogen_contrib >= 0 else "negative",
            "note": "Nitrogen level is close to ideal." if nitrogen_contrib >= 0 else "Split fertilizer doses to optimize uptake."
        }
    ]

    return factors


def estimate_confidence(data: dict, score: float) -> float:
    fields = [
        "ph",
        "nitrogen_kg_per_ha",
        "phosphorus_kg_per_ha",
        "potassium_kg_per_ha",
        "organic_carbon_percent",
        "rainfall_mm",
        "temperature_c",
        "humidity_percent",
        "area_hectares"
    ]

    present = sum(1 for field in fields if data.get(field) is not None)
    completeness = present / len(fields)

    stability = 1.0
    if score < 50:
        stability = 0.78
    elif score < 65:
        stability = 0.86

    confidence = 0.55 + (0.3 * completeness) + (0.15 * stability)
    return round(max(0.0, min(1.0, confidence)), 2)


@router.post(

    "/recommendation",

    response_model=RecommendationResponse

)

def get_recommendation(data: dict):
    qssm_score = estimate_sustainability_score(data)
    crop = predict_crop(data)

    return {

        "recommended_crop": crop,
        "sustainability_score": qssm_score

    }


@router.post(
    "/recommendation/explain",
    response_model=RecommendationExplainResponse
)
def explain_recommendation(data: dict):

    qssm_score = estimate_sustainability_score(data)
    crop = predict_crop(data)
    explanation = build_explanation(data)
    confidence = estimate_confidence(data, qssm_score)

    return {
        "recommended_crop": crop,
        "sustainability_score": qssm_score,
        "confidence_score": confidence,
        "explanation": explanation
    }