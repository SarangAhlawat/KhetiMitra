import pandas as pd
from pathlib import Path

from app.services.rule_engine import (
    get_scheme_recommendations
)

# =========================
# FILE PATH
# =========================

# Project root → AI-DSS
BASE_DIR = Path(__file__).resolve().parents[3]

SCHEME_FILE = (
    BASE_DIR
    / "data"
    / "knowledge_base"
    / "schemes"
    / "government_schemes.csv"
)

# Debug print (helps catch path issues)
print("Scheme file path:", SCHEME_FILE)

# Safety check
if not SCHEME_FILE.exists():

    raise FileNotFoundError(
        f"Scheme file not found: {SCHEME_FILE}"
    )


# =========================
# LOAD SCHEME DATA
# =========================

scheme_df = pd.read_csv(
    SCHEME_FILE
)


# =========================
# MATCH SCHEMES
# =========================

def get_top_schemes(user_data):

    # Step 1 → Get rule-based schemes

    rule_schemes = get_scheme_recommendations(
        user_data
    )

    if not rule_schemes:

        return []

    # Step 2 → Filter dataset

    matched_df = scheme_df[

        scheme_df[
            "scheme_name"
        ].isin(rule_schemes)

    ]

    if matched_df.empty:

        return []

    # Step 3 → Sort by subsidy

    if "subsidy_amount" in matched_df.columns:

        try:

            matched_df = matched_df.sort_values(
                by="subsidy_amount",
                ascending=False
            )

        except Exception:

            pass

    # Step 4 → Return Top 3

    top = matched_df.head(3)

    return top.to_dict(
        orient="records"
    )