from app.services.environment_service import (
    get_environment_data
)

from app.utils.environment_parser import (
    parse_environment_data
)

from app.utils.feature_validator import (
    validate_environment_features
)


# Chandigarh test
lat = 30.7333
lon = 76.7794

env_data = get_environment_data(lat, lon)

parsed = parse_environment_data(env_data)

validated = validate_environment_features(parsed)

if validated:

    print("Validation Working ✅")

    print("\nValidated Data:")

    for key, value in validated.items():

        print(f"{key}: {value}")

else:

    print("Validation Failed ❌")