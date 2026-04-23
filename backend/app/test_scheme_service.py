from app.services.scheme_service import (
    get_top_schemes
)

user_data = {

    "soil_type": "Sandy",
    "water_condition": "Low",
    "ph": 8.7,
    "land_size": 5,
    "farming_type": "Organic"

}


result = get_top_schemes(
    user_data
)

print("\nEligible Schemes:\n")

for r in result:

    print(r["scheme_name"])
    print("Benefit:", r["benefit_type"])
    print("---")