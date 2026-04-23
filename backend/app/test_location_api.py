from app.services.location_service import get_location_details

# Chandigarh example coordinates
lat = 30.7333
lon = 76.7794

data = get_location_details(lat, lon)

if data:

    print("Location API Working ✅")

    # Print readable location info
    result = data["results"][0]

    print("Formatted Address:")
    print(result["formatted"])

else:

    print("Location API Failed ❌")