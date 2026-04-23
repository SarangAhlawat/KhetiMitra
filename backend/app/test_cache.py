from app.services.api_cache_service import (
    get_cached_data,
    set_cached_data
)

# Test key
key = "test_location"

# Store data
sample_data = {
    "status": "working",
    "time": "now"
}

set_cached_data(key, sample_data)

# Retrieve data
data = get_cached_data(key)

if data:
    print("Cache Working ✅")
    print(data)

else:
    print("Cache Failed ❌")