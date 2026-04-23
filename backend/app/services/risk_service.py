import pandas as pd
from pathlib import Path

from app.services.rule_engine import (
    detect_risks
)

# =========================
# LOAD SOIL DATA
# =========================

# Project root → AI-DSS
BASE_DIR = Path(__file__).resolve().parents[3]

SOIL_FILE = (
    BASE_DIR
    / "data"
    / "knowledge_base"
    / "soil_guidelines"
    / "soil_management.csv"
)

# Debug print (helps verify correct path)
print("Soil file path:", SOIL_FILE)

# Safety check
if not SOIL_FILE.exists():

    raise FileNotFoundError(
        f"Soil file not found: {SOIL_FILE}"
    )


# Load soil data
soil_df = pd.read_csv(
    SOIL_FILE
)


# =========================
# RISK SOLUTION MAP
# =========================

RISK_SOLUTIONS = {

    "Alkalinity Risk":
        "Apply gypsum and increase organic matter.",

    "Acidity Risk":
        "Apply lime to neutralize soil acidity.",

    "Water Stress Risk":
        "Use drip irrigation and rainwater harvesting.",

    "Soil Fertility Risk":
        "Apply compost and biofertilizers.",

    "Erosion Risk":
        "Use mulching and contour farming."

}


# =========================
# BUILD RISK REPORT
# =========================

def generate_risk_report(user_data):

    detected = detect_risks(
        user_data
    )

    if not detected:

        return []

    report = []

    for r in detected:

        risk_name = r["risk"]

        solution = RISK_SOLUTIONS.get(
            risk_name,
            "Follow recommended soil management practices."
        )

        report.append({

            "risk": risk_name,

            "severity": r["severity"],

            "recommended_action": solution

        })

    return report