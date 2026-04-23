import requests
from datetime import datetime
# from app.core.logger import logger
from app.core.logger import get_logger

logger = get_logger(__name__)

NASA_POWER_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"


def get_weather_data(lat: float, lon: float):
    """
    Fetch daily weather data from NASA POWER API
    """

    try:
        params = {
            "parameters": "T2M,PRECTOTCORR,RH2M",
            "community": "AG",
            "longitude": lon,
            "latitude": lat,
            "start": "20240101",
            "end": datetime.today().strftime("%Y%m%d"),
            "format": "JSON"
        }

        response = requests.get(
            NASA_POWER_URL,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        logger.info(
            f"Weather data fetched successfully "
            f"for lat={lat}, lon={lon}"
        )

        return data

    except Exception as e:

        logger.error(
            f"Weather API error: {str(e)}"
        )

        return None