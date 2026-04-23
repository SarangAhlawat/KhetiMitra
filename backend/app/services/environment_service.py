from app.services.db_cache_service import (
    get_db_cached_data,
    set_db_cached_data
)

from app.services.weather_service import get_weather_data
from app.services.soil_api_service import get_soil_data
from app.services.location_service import get_location_details

from app.core.logger import get_logger

logger = get_logger(__name__)


def get_environment_data(lat: float, lon: float):

    try:

        cache_key = f"env_{lat}_{lon}"

        # DB Cache check
        cached_data = get_db_cached_data(cache_key)

        if cached_data:

            return cached_data

        # Fetch APIs
        weather_data = get_weather_data(lat, lon)

        soil_data = get_soil_data(lat, lon)

        location_data = get_location_details(lat, lon)

        combined_data = {

            "weather": weather_data,
            "soil": soil_data,
            "location": location_data

        }

        # Store in DB cache
        set_db_cached_data(
            cache_key,
            combined_data
        )

        logger.info(
            "Environment data cached in database"
        )

        return combined_data

    except Exception as e:

        logger.error(
            f"Environment service error: {str(e)}"
        )

        return None










# from app.services.weather_service import get_weather_data
# from app.services.soil_api_service import get_soil_data
# from app.services.location_service import get_location_details

# from app.services.api_cache_service import (
#     get_cached_data,
#     set_cached_data
# )

# from app.core.logger import get_logger

# logger = get_logger(__name__)


# def get_environment_data(lat: float, lon: float):
#     """
#     Unified environment intelligence service

#     Combines:
#     - Weather data
#     - Soil data
#     - Location data
#     - Cache system
#     """

#     try:

#         # Create unique cache key
#         cache_key = f"env_{lat}_{lon}"

#         # Check cache first
#         cached_data = get_cached_data(cache_key)

#         if cached_data:

#             logger.info(
#                 f"Environment data loaded from cache "
#                 f"for lat={lat}, lon={lon}"
#             )

#             return cached_data

#         logger.info(
#             f"Fetching fresh environment data "
#             f"for lat={lat}, lon={lon}"
#         )

#         # Fetch APIs
#         weather_data = get_weather_data(lat, lon)

#         soil_data = get_soil_data(lat, lon)

#         location_data = get_location_details(lat, lon)

#         # Combine all data
#         combined_data = {

#             "weather": weather_data,

#             "soil": soil_data,

#             "location": location_data

#         }

#         # Store in cache
#         set_cached_data(
#             cache_key,
#             combined_data
#         )

#         logger.info(
#             "Environment data successfully created"
#         )

#         return combined_data

#     except Exception as e:

#         logger.error(
#             f"Environment service error: {str(e)}"
#         )

#         return None