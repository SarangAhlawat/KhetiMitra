import json
from pathlib import Path


# =========================
# RULE FILE PATHS
# =========================

# Get project root (AI-DSS)
BASE_DIR = Path(__file__).resolve().parents[3]

# Your data is directly in AI-DSS/data/
RULE_DIR = (
    BASE_DIR
    / "data"
    / "knowledge_base"
    / "rules"
)

# Debug print
print("RULE DIRECTORY:", RULE_DIR)


# Rule files
PRACTICE_RULE_FILE = RULE_DIR / "practice_rules.json"

SCHEME_RULE_FILE = RULE_DIR / "scheme_rules.json"

RISK_RULE_FILE = RULE_DIR / "risk_rules.json"

SOIL_RULE_FILE = RULE_DIR / "soil_rules.json"


# =========================
# LOAD JSON RULES
# =========================

def load_rules(file_path):

    file_path = Path(file_path)

    if not file_path.exists():

        raise FileNotFoundError(
            f"Rule file not found: {file_path}"
        )

    with open(file_path, "r") as f:

        rules = json.load(f)

    return rules


# Load rule sets
practice_rules = load_rules(
    PRACTICE_RULE_FILE
)

scheme_rules = load_rules(
    SCHEME_RULE_FILE
)

risk_rules = load_rules(
    RISK_RULE_FILE
)

soil_rules = load_rules(
    SOIL_RULE_FILE
)


# =========================
# CONDITION MATCHER
# =========================

def match_condition(user_value, rule_value):

    # Handle numeric comparison rules
    if isinstance(rule_value, str):

        try:
            user_value = float(user_value)

            if rule_value.startswith(">="):

                return user_value >= float(
                    rule_value[2:]
                )

            elif rule_value.startswith("<="):

                return user_value <= float(
                    rule_value[2:]
                )

            elif rule_value.startswith(">"):

                return user_value > float(
                    rule_value[1:]
                )

            elif rule_value.startswith("<"):

                return user_value < float(
                    rule_value[1:]
                )

        except ValueError:

            pass

    # Default equality match
    return str(user_value) == str(rule_value)


def check_conditions(
    user_data,
    conditions
):

    for key, value in conditions.items():

        if key not in user_data:

            return False

        if not match_condition(
            user_data[key],
            value
        ):

            return False

    return True


# =========================
# PRACTICE RECOMMENDER
# =========================

def get_practice_recommendations(
    user_data
):

    matched = []

    for rule in practice_rules:

        if check_conditions(
            user_data,
            rule["conditions"]
        ):

            matched.extend(
                rule["recommendations"]
            )

    return list(set(matched))


# =========================
# SCHEME MATCHER
# =========================

def get_scheme_recommendations(
    user_data
):

    matched = []

    for rule in scheme_rules:

        if check_conditions(
            user_data,
            rule["conditions"]
        ):

            matched.extend(
                rule["recommendations"]
            )

    return list(set(matched))


# =========================
# RISK DETECTOR
# =========================

def detect_risks(
    user_data
):

    risks = []

    for rule in risk_rules:

        if check_conditions(
            user_data,
            rule["conditions"]
        ):

            risks.append({

                "risk": rule["risk"],
                "severity": rule["severity"]

            })

    return risks


# =========================
# SOIL IMPROVEMENT
# =========================

def get_soil_recommendations(
    user_data
):

    improvements = []

    for rule in soil_rules:

        if check_conditions(
            user_data,
            rule["conditions"]
        ):

            improvements.extend(
                rule["recommendations"]
            )

    return list(set(improvements))