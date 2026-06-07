import requests

from app.core.config import OPENCAGE_API_KEY
from app.core.logger import get_logger

logger = get_logger(__name__)


def get_location_details(lat: float, lon: float):
    """
    Convert latitude/longitude into
    district, state, village information
    """

    if not OPENCAGE_API_KEY:
        logger.error("OPENCAGE_API_KEY not set")
        return None

    try:

        url = (
            "https://api.opencagedata.com/geocode/v1/json"
            f"?q={lat}+{lon}&key={OPENCAGE_API_KEY}"
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