import json
import pandas as pd

from app.models.sustainability import QSSM_INDICATORS
from app.utils.preprocessing import min_max_scale


# Load weights
with open(
    "../models/qssm_model/qssm_weights.json"
) as f:

    QSSM_WEIGHTS = json.load(f)



def compute_dimension_score(
    df,
    indicators
):

    scores = []

    for col in indicators:

        scaled = min_max_scale(
            df[col]
        )

        scores.append(scaled)

    dimension_score = sum(scores) / len(scores)

    return dimension_score



def compute_qssm(df):

    dimension_scores = {}

    for dimension, indicators in QSSM_INDICATORS.items():

        dimension_scores[dimension] = compute_dimension_score(
            df,
            indicators
        )

    total_score = 0

    for dim, score in dimension_scores.items():

        weight = QSSM_WEIGHTS[dim]

        total_score += score * weight

    df["QSSM_score"] = total_score

    df["QSSM_class"] = df[
    "QSSM_score"
    ].apply(classify_qssm)

    return df

def classify_qssm(score):

    if score >= 80:
        return "Highly Sustainable"

    elif score >= 60:
        return "Moderately Sustainable"

    elif score >= 40:
        return "At Risk"

    else:
        return "Unsustainable"