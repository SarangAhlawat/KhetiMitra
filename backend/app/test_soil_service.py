from app.services.soil_service import (
    generate_soil_advisory
)

user_data = {

    "soil_type": "Sandy Soil"

}

result = generate_soil_advisory(
    user_data
)

print("\nSoil Advisory:\n")

for key, value in result.items():

    print(key, ":", value)