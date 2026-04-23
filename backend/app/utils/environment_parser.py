from app.core.logger import get_logger

logger = get_logger(__name__)


def parse_environment_data(env_data):
    """
    Convert raw API responses
    into structured ML-ready data
    """

    try:

        parsed = {}

        # =========================
        # WEATHER PARSING
        # =========================

        weather = env_data.get("weather", {})

        try:

            weather_props = weather["properties"]["parameter"]

            temperature_data = weather_props.get("T2M", {})
            rainfall_data = weather_props.get("PRECTOTCORR", {})
            humidity_data = weather_props.get("RH2M", {})

            # Get latest available value
            parsed["temperature"] = list(temperature_data.values())[-1]

            parsed["rainfall"] = list(rainfall_data.values())[-1]

            parsed["humidity"] = list(humidity_data.values())[-1]

        except Exception:

            parsed["temperature"] = None
            parsed["rainfall"] = None
            parsed["humidity"] = None


        # =========================
        # SOIL PARSING
        # =========================

        soil = env_data.get("soil", {})

        try:

            soil_layers = soil["properties"]["layers"]

            for layer in soil_layers:

                name = layer["name"]

                if name == "phh2o":

                    parsed["soil_ph"] = (
                        layer["depths"][0]
                        ["values"]["mean"]
                    )

                if name == "soc":

                    parsed["organic_carbon"] = (
                        layer["depths"][0]
                        ["values"]["mean"]
                    )

                if name == "nitrogen":

                    parsed["nitrogen"] = (
                        layer["depths"][0]
                        ["values"]["mean"]
                    )

        except Exception:

            parsed["soil_ph"] = None
            parsed["organic_carbon"] = None
            parsed["nitrogen"] = None


        # =========================
        # LOCATION PARSING
        # =========================

        location = env_data.get("location", {})

        try:

            components = (
                location["results"][0]
                ["components"]
            )

            parsed["district"] = components.get(
                "state_district"
            )

            parsed["state"] = components.get(
                "state"
            )

            parsed["country"] = components.get(
                "country"
            )

        except Exception:

            parsed["district"] = None
            parsed["state"] = None
            parsed["country"] = None


        logger.info(
            "Environment data parsed successfully"
        )

        return parsed

    except Exception as e:

        logger.error(
            f"Parsing error: {str(e)}"
        )

        return None