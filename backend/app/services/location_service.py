import requests
# from app.core.logger import logger
from app.core.logger import get_logger

logger = get_logger(__name__)

# Replace with your real API key
API_KEY = "c000732ca8d74f79ab79e899e738b916"


def get_location_details(lat: float, lon: float):
    """
    Convert latitude/longitude into
    district, state, village information
    """

    try:

        url = (
            "https://api.opencagedata.com/geocode/v1/json"
            f"?q={lat}+{lon}&key={API_KEY}"
        )

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        logger.info(
            f"Location data fetched successfully "
            f"for lat={lat}, lon={lon}"
        )

        return data

    except Exception as e:

        logger.error(
            f"Location API error: {str(e)}"
        )

        return None