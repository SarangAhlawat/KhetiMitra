from app.services.risk_service import (
    generate_risk_report
)

user_data = {

    "soil_type": "Sandy",
    "water_condition": "Low",
    "ph": 8.7,
    "organic_matter": "Low"

}


risks = generate_risk_report(
    user_data
)

print("\nRisk Report:\n")

for r in risks:

    print("Risk:", r["risk"])
    print("Severity:", r["severity"])
    print("Action:", r["recommended_action"])
    print("---")