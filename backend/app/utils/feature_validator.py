from app.core.logger import get_logger

logger = get_logger(__name__)


def validate_environment_features(parsed_data):
    """
    Clean and validate parsed environment data
    Replace invalid or missing values
    """

    try:

        validated = parsed_data.copy()

        # =========================
        # WEATHER VALIDATION
        # =========================

        weather_defaults = {
            "temperature": 25.0,
            "rainfall": 0.0,
            "humidity": 60.0
        }

        for key in weather_defaults:

            value = validated.get(key)

            if value is None or value == -999:

                logger.warning(
                    f"{key} missing → using default"
                )

                validated[key] = weather_defaults[key]


        # =========================
        # SOIL VALIDATION
        # =========================

        soil_defaults = {
            "soil_ph": 6.5,
            "organic_carbon": 0.5,
            "nitrogen": 200
        }

        for key in soil_defaults:

            value = validated.get(key)

            if value is None:

                logger.warning(
                    f"{key} missing → using default"
                )

                validated[key] = soil_defaults[key]


        # =========================
        # LOCATION VALIDATION
        # =========================

        if validated.get("district") is None:

            validated["district"] = "Unknown"

        if validated.get("state") is None:

            validated["state"] = "Unknown"

        if validated.get("country") is None:

            validated["country"] = "India"


        logger.info(
            "Environment data validated successfully"
        )

        return validated

    except Exception as e:

        logger.error(
            f"Validation error: {str(e)}"
        )

        return None