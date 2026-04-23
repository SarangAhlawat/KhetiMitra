import pandas as pd
from pathlib import Path

from app.services.rule_engine import (
    get_practice_recommendations
)

# =========================
# LOAD PRACTICE DATA
# =========================

# Project root → AI-DSS
BASE_DIR = Path(__file__).resolve().parents[3]

# Path to CSV file
PRACTICE_FILE = (
    BASE_DIR
    / "data"
    / "knowledge_base"
    / "practices"
    / "sustainable_practices.csv"
)

# Debug print (optional but useful)
print("Practice file path:", PRACTICE_FILE)

# Load dataset
practice_df = pd.read_csv(
    PRACTICE_FILE
)


# =========================
# MATCH PRACTICES FROM RULES
# =========================

def fetch_practice_details(
    practice_names
):

    results = practice_df[

        practice_df[
            "practice_name"
        ].isin(practice_names)

    ]

    return results.to_dict(
        orient="records"
    )


# =========================
# RANK PRACTICES
# =========================

def rank_practices(
    practice_records
):

    sorted_practices = sorted(
        practice_records,
        key=lambda x: x.get(
            "impact_score",
            0
        ),
        reverse=True
    )

    return sorted_practices


# =========================
# MAIN FUNCTION
# =========================

def get_top_practices(
    user_data,
    top_n=3
):

    # Step 1 → Get rule matches

    matched_names = (
        get_practice_recommendations(
            user_data
        )
    )

    # Step 2 → Get details

    records = fetch_practice_details(
        matched_names
    )

    if not records:

        return []

    # Step 3 → Rank practices

    ranked = rank_practices(
        records
    )

    # Step 4 → Return top N

    return ranked[:top_n]