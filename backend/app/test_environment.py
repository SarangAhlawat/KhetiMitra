from app.services.environment_service import (
    get_environment_data
)

# Chandigarh test location
lat = 30.7333
lon = 76.7794

data = get_environment_data(lat, lon)

if data:

    print("Environment Service Working ✅")

    print("\nAvailable Modules:")

    print(list(data.keys()))

else:

    print("Environment Service Failed ❌")