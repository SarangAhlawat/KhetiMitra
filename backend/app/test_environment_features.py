from app.services.environment_feature_service import (
    get_final_environment_features
)

# Chandigarh test
lat = 30.7333
lon = 76.7794

features = get_final_environment_features(
    lat,
    lon
)

if features:

    print("Final Pipeline Working ✅")

    print("\nFinal Features:")

    for key, value in features.items():

        print(f"{key}: {value}")

else:

    print("Pipeline Failed ❌")