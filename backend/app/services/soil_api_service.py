import requests
# from app.core.logger import logger
from app.core.logger import get_logger

logger = get_logger(__name__)

SOILGRIDS_URL = "https://rest.isric.org/soilgrids/v2.0/properties/query"


def get_soil_data(lat: float, lon: float):
    """
    Fetch soil properties from SoilGrids API
    """

    try:

        params = {
            "lon": lon,
            "lat": lat,
            # Correct format (comma-separated string)
            # ,soc,nitrogen,clay,sand,silt
            "property": "phh2o",

            # Correct depth format
            "depth": "0-5cm",

            "value": "mean"
        }

        response = requests.get(
            SOILGRIDS_URL,
            params=params,
            timeout=55
        )

        response.raise_for_status()

        data = response.json()

        logger.info(
            f"Soil data fetched successfully "
            f"for lat={lat}, lon={lon}"
        )

        return data

    except Exception as e:

        logger.error(
            f"Soil API error: {str(e)}"
        )

        return None