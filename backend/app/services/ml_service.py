import os
import joblib
import numpy as np
import pandas as pd

# =========================
# PATH CONFIG
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    )
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)

# =========================
# LOAD MODELS (ONCE)
# =========================

print("Loading ML models...")

crop_model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "crop_model",
        "crop_model.pkl"
    )
)

yield_model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "yield_model",
        "yield_model.pkl"
    )
)

risk_model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "risk_model",
        "risk_model.pkl"
    )
)

label_encoders = joblib.load(
    os.path.join(
        MODEL_DIR,
        "encoders",
        "label_encoders.pkl"
    )
)

print("ML models loaded.")


# =========================
# FEATURE PREPROCESSING
# =========================


def _safe_float(value, default=0.0):

    try:
        if value is None:
            return float(default)
        return float(value)
    except (TypeError, ValueError):
        return float(default)


def _decode_crop_label(prediction):

    crop_encoder = None

    if isinstance(label_encoders, dict):
        crop_encoder = label_encoders.get("crop")

    if crop_encoder is not None and hasattr(crop_encoder, "inverse_transform"):
        try:
            decoded = crop_encoder.inverse_transform([int(prediction)])[0]
            return str(decoded)
        except Exception:
            pass

    # Fallback: make sure API always returns string type.
    return str(prediction)


def _categorize_rainfall(rainfall):

    if rainfall < 500:
        return 0.0
    if rainfall < 900:
        return 1.0
    return 2.0


def _categorize_water_stress(stress_index):

    if stress_index < 0.35:
        return 0.0
    if stress_index < 0.65:
        return 1.0
    return 2.0


def _build_feature_values(farm_data: dict):

    ph = _safe_float(farm_data.get("ph"), 7.0)
    nitrogen = _safe_float(farm_data.get("nitrogen_kg_per_ha"), 100.0)
    phosphorus = _safe_float(farm_data.get("phosphorus_kg_per_ha"), 45.0)
    potassium = _safe_float(farm_data.get("potassium_kg_per_ha"), 55.0)
    organic = _safe_float(farm_data.get("organic_carbon_percent"), 0.6)
    moisture = _safe_float(farm_data.get("moisture_percent"), 25.0)

    avg_temp = _safe_float(
        farm_data.get("avg_temp", farm_data.get("temperature_c")),
        28.0
    )
    max_temp = _safe_float(farm_data.get("max_temp"), avg_temp + 5)
    min_temp = _safe_float(farm_data.get("min_temp"), avg_temp - 5)

    rainfall = _safe_float(
        farm_data.get("rainfall", farm_data.get("rainfall_mm")),
        650.0
    )
    humidity = _safe_float(
        farm_data.get("humidity", farm_data.get("humidity_percent")),
        58.0
    )

    annual_recharge = _safe_float(
        farm_data.get("annual_recharge_mcm"),
        100.0
    )
    annual_extraction = _safe_float(
        farm_data.get("annual_extraction_mcm"),
        80.0
    )
    future_groundwater = _safe_float(
        farm_data.get("future_groundwater_availability_mcm"),
        90.0
    )

    area = _safe_float(
        farm_data.get("area_hectares", farm_data.get("farm_size")),
        1.5
    )

    extraction_percent = _safe_float(
        farm_data.get("extraction_percent"),
        (annual_extraction / annual_recharge * 100.0) if annual_recharge else 0.0
    )

    water_stress_index = _safe_float(
        farm_data.get("water_stress_index"),
        min(1.0, annual_extraction / future_groundwater) if future_groundwater else 0.0
    )

    temp_range = _safe_float(
        farm_data.get("temp_range"),
        max_temp - min_temp
    )

    fertility_score = _safe_float(
        farm_data.get("fertility_score"),
        (nitrogen * 0.35) + (phosphorus * 0.3) + (potassium * 0.2) + (organic * 40)
    )

    climate_stress_score = _safe_float(
        farm_data.get("climate_stress_score"),
        (temp_range * 1.8) + (water_stress_index * 45) + max(0.0, (humidity - 70) * 0.5)
    )

    values = {
        "district": _safe_float(farm_data.get("district"), 0.0),
        "year": _safe_float(farm_data.get("year"), 2024.0),
        "season": _safe_float(farm_data.get("season"), 1.0),
        "crop": _safe_float(farm_data.get("crop"), 0.0),
        "area_hectares": area,
        "yield_kg_per_ha": _safe_float(farm_data.get("yield_kg_per_ha"), 0.0),
        "soil_type": _safe_float(farm_data.get("soil_type"), 0.0),
        "ph": ph,
        "nitrogen_kg_per_ha": nitrogen,
        "phosphorus_kg_per_ha": phosphorus,
        "potassium_kg_per_ha": potassium,
        "organic_carbon_percent": organic,
        "moisture_percent": moisture,
        "avg_temp": avg_temp,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "rainfall": rainfall,
        "humidity": humidity,
        "wind_speed": _safe_float(farm_data.get("wind_speed"), 6.0),
        "air_pressure": _safe_float(farm_data.get("air_pressure"), 1013.0),
        "annual_recharge_mcm": annual_recharge,
        "annual_extraction_mcm": annual_extraction,
        "extraction_percent": extraction_percent,
        "future_groundwater_availability_mcm": future_groundwater,
        "water_stress_index": water_stress_index,
        "temp_range": temp_range,
        "rainfall_category": _safe_float(
            farm_data.get("rainfall_category"),
            _categorize_rainfall(rainfall)
        ),
        "water_stress_category": _safe_float(
            farm_data.get("water_stress_category"),
            _categorize_water_stress(water_stress_index)
        ),
        "fertility_score": fertility_score,
        "climate_stress_score": climate_stress_score,
    }

    return values


def _build_model_input(model, farm_data: dict):

    feature_values = _build_feature_values(farm_data)

    model_features = list(getattr(model, "feature_names_in_", []))

    if model_features:
        row = {
            feature: _safe_float(feature_values.get(feature), 0.0)
            for feature in model_features
        }
        return pd.DataFrame([row], columns=model_features)

    # Fallback for models without feature names metadata.
    feature_order = [
        "ph",
        "nitrogen_kg_per_ha",
        "phosphorus_kg_per_ha",
        "potassium_kg_per_ha",
        "organic_carbon_percent",
        "rainfall",
        "avg_temp",
        "humidity",
        "area_hectares"
    ]

    features = [feature_values.get(f, 0.0) for f in feature_order]

    return np.array(features, dtype=float).reshape(1, -1)

def preprocess_input(
    farm_data: dict
):

    """
    Convert farm data dict
    into model-ready feature vector
    """

    return _build_model_input(crop_model, farm_data)


# =========================
# CROP PREDICTION
# =========================

def predict_crop(
    farm_data: dict
):

    X = _build_model_input(crop_model, farm_data)

    prediction = crop_model.predict(X)

    return _decode_crop_label(prediction[0])


# =========================
# YIELD PREDICTION
# =========================

def predict_yield(
    farm_data: dict
):

    X = _build_model_input(yield_model, farm_data)

    prediction = yield_model.predict(X)

    return float(prediction[0])


# =========================
# RISK PREDICTION
# =========================

def predict_risk(
    farm_data: dict
):

    X = _build_model_input(risk_model, farm_data)

    prediction = risk_model.predict(X)

    return prediction[0]