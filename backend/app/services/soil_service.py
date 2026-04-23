import pandas as pd
from pathlib import Path

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

# Debug print (helps verify path)
print("Soil advisory file path:", SOIL_FILE)

# Safety check
if not SOIL_FILE.exists():

    raise FileNotFoundError(
        f"Soil file not found: {SOIL_FILE}"
    )

# Load soil dataset
soil_df = pd.read_csv(
    SOIL_FILE
)


# =========================
# FIND SOIL PROFILE
# =========================

def find_soil_profile(soil_type):

    if not soil_type:

        return None

    result = soil_df[

        soil_df[
            "soil_type"
        ].str.lower() ==
        soil_type.lower()

    ]

    if result.empty:

        return None

    return result.iloc[0]


# =========================
# BUILD SOIL ADVISORY
# =========================

def generate_soil_advisory(user_data):

    soil_type = user_data.get(
        "soil_type"
    )

    profile = find_soil_profile(
        soil_type
    )

    if profile is None:

        return {

            "message":
            "Soil type not found."

        }

    advisory = {

        "soil_type":
            profile["soil_type"],

        "ph_range":
            profile["ph_range"],

        "recommended_crops":
            profile["recommended_crops"],

        "recommended_fertilizer":
            profile["recommended_fertilizer"],

        "recommended_irrigation":
            profile["recommended_irrigation"],

        "improvement_practices":
            profile["improvement_practices"]

    }

    return advisory