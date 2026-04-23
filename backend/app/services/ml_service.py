import os
import joblib
import numpy as np

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

print("ML models loaded.")


# =========================
# FEATURE PREPROCESSING
# =========================

def preprocess_input(
    farm_data: dict
):

    """
    Convert farm data dict
    into model-ready feature vector
    """

    feature_order = [

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

    features = []

    for f in feature_order:

        value = farm_data.get(f, 0)

        features.append(value)

    return np.array(features).reshape(1, -1)


# =========================
# CROP PREDICTION
# =========================

def predict_crop(
    farm_data: dict
):

    X = preprocess_input(farm_data)

    prediction = crop_model.predict(X)

    return prediction[0]


# =========================
# YIELD PREDICTION
# =========================

def predict_yield(
    farm_data: dict
):

    X = preprocess_input(farm_data)

    prediction = yield_model.predict(X)

    return float(prediction[0])


# =========================
# RISK PREDICTION
# =========================

def predict_risk(
    farm_data: dict
):

    X = preprocess_input(farm_data)

    prediction = risk_model.predict(X)

    return prediction[0]