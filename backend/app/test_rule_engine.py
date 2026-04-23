from app.services.rule_engine import (
    get_practice_recommendations,
    get_scheme_recommendations,
    detect_risks,
    get_soil_recommendations
)


user_data = {

    "soil_type": "Sandy",
    "water_condition": "Low",
    "ph": 8.7,
    "land_size": 5,
    "farming_type": "Organic"

}


print("\nPractices:")
print(
    get_practice_recommendations(
        user_data
    )
)


print("\nSchemes:")
print(
    get_scheme_recommendations(
        user_data
    )
)


print("\nRisks:")
print(
    detect_risks(
        user_data
    )
)


print("\nSoil Improvements:")
print(
    get_soil_recommendations(
        user_data
    )
)