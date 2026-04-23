import json
from datetime import datetime, timedelta

from sqlalchemy import text
from app.core.database import engine
from app.core.logger import get_logger

logger = get_logger(__name__)


CACHE_EXPIRY_HOURS = 6


def get_db_cached_data(cache_key: str):
    """
    Retrieve cached data from database
    """

    try:

        with engine.connect() as conn:

            query = text("""
                SELECT response_data, created_at
                FROM api_cache
                WHERE cache_key = :key
            """)

            result = conn.execute(
                query,
                {"key": cache_key}
            ).fetchone()

            if result:

                data, created_at = result

                # Check expiry
                if datetime.utcnow() - created_at < timedelta(hours=CACHE_EXPIRY_HOURS):

                    logger.info(
                        f"DB Cache HIT for key={cache_key}"
                    )

                    return data

                else:

                    logger.info(
                        f"DB Cache EXPIRED for key={cache_key}"
                    )

            logger.info(
                f"DB Cache MISS for key={cache_key}"
            )

            return None

    except Exception as e:

        logger.error(
            f"DB cache read error: {str(e)}"
        )

        return None


def set_db_cached_data(cache_key: str, data):
    """
    Store API response in database cache
    """

    try:

        with engine.connect() as conn:

            query = text("""
                INSERT INTO api_cache (
                    cache_key,
                    response_data
                )
                VALUES (
                    :key,
                    :data
                )
                ON CONFLICT (cache_key)
                DO UPDATE SET
                    response_data = EXCLUDED.response_data,
                    created_at = CURRENT_TIMESTAMP
            """)

            conn.execute(
                query,
                {
                    "key": cache_key,
                    "data": json.dumps(data)
                }
            )

            conn.commit()

            logger.info(
                f"DB Cache SET for key={cache_key}"
            )

    except Exception as e:

        logger.error(
            f"DB cache write error: {str(e)}"
        )