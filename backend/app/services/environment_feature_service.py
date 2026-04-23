from app.services.environment_service import (
    get_environment_data
)

from app.utils.environment_parser import (
    parse_environment_data
)

from app.utils.feature_validator import (
    validate_environment_features
)

from app.core.logger import get_logger

logger = get_logger(__name__)


def get_final_environment_features(
    lat: float,
    lon: float
):
    """
    Master environment feature pipeline

    Steps:
    1 → Fetch raw API data
    2 → Parse structured data
    3 → Validate values
    4 → Return ML-ready features
    """

    try:

        logger.info(
            f"Starting environment pipeline "
            f"for lat={lat}, lon={lon}"
        )

        # STEP 1 — Fetch raw data
        env_data = get_environment_data(
            lat,
            lon
        )

        if not env_data:

            logger.error(
                "Failed to fetch environment data"
            )

            return None

        # STEP 2 — Parse data
        parsed_data = parse_environment_data(
            env_data
        )

        if not parsed_data:

            logger.error(
                "Failed to parse environment data"
            )

            return None

        # STEP 3 — Validate data
        validated_data = validate_environment_features(
            parsed_data
        )

        if not validated_data:

            logger.error(
                "Failed to validate environment data"
            )

            return None

        logger.info(
            "Environment feature pipeline completed"
        )

        return validated_data

    except Exception as e:

        logger.error(
            f"Pipeline error: {str(e)}"
        )

        return None