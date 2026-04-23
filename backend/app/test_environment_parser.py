from app.services.environment_service import (
    get_environment_data
)

from app.utils.environment_parser import (
    parse_environment_data
)

# Chandigarh coordinates
lat = 30.7333
lon = 76.7794

# Fetch raw data
env_data = get_environment_data(lat, lon)

# Parse structured data
parsed_data = parse_environment_data(env_data)

if parsed_data:

    print("Parser Working ✅")

    print("\nParsed Data:")

    for key, value in parsed_data.items():

        print(f"{key}: {value}")

else:

    print("Parser Failed ❌")