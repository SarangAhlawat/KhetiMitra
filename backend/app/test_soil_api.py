from app.services.soil_api_service import get_soil_data

# Chandigarh coordinates (example)
# lat = 30.7333
# lon = 76.7794
lat = 28.6139
lon = 77.2090

data = get_soil_data(lat, lon)

if data:
    print("Soil API Working ✅")

    # Print sample fields
    print("Keys:", list(data.keys()))

else:
    print("Soil API Failed ❌")