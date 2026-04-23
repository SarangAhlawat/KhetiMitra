from app.services.weather_service import get_weather_data

# Chandigarh coordinates (example test)
lat = 30.7333
lon = 76.7794

data = get_weather_data(lat, lon)

if data:
    print("Weather API Working ✅")
    print(list(data.keys()))

else:
    print("Weather API Failed ❌")