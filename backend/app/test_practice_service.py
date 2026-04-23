from app.services.practice_service import (
    get_top_practices
)


user_data = {

    "soil_type": "Sandy",
    "water_condition": "Low",
    "ph": 8.7,
    "land_size": 5,
    "farming_type": "Organic"

}


result = get_top_practices(
    user_data
)


print("\nTop Practices:\n")

for r in result:

    print(r["practice_name"])
    print("Impact:", r["impact_score"])
    print("Cost:", r["cost_level"])
    print("---")