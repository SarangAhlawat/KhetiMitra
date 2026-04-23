import time
from datetime import datetime
# from app.core.logger import logger
from app.core.logger import get_logger

logger = get_logger(__name__)

# Simple in-memory cache
cache = {}

# Cache expiry time (seconds)
CACHE_EXPIRY = 3600  # 1 hour


def get_cached_data(key: str):
    """
    Retrieve cached API response
    """

    try:

        if key in cache:

            data, timestamp = cache[key]

            current_time = time.time()

            # Check if expired
            if current_time - timestamp < CACHE_EXPIRY:

                logger.info(
                    f"Cache HIT for key={key}"
                )

                return data

            else:

                logger.info(
                    f"Cache EXPIRED for key={key}"
                )

                del cache[key]

        logger.info(
            f"Cache MISS for key={key}"
        )

        return None

    except Exception as e:

        logger.error(
            f"Cache retrieval error: {str(e)}"
        )

        return None


def set_cached_data(key: str, data):
    """
    Store API response in cache
    """

    try:

        cache[key] = (
            data,
            time.time()
        )

        logger.info(
            f"Cache SET for key={key}"
        )

    except Exception as e:

        logger.error(
            f"Cache storage error: {str(e)}"
        )