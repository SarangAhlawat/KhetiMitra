import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(BASE_DIR / ".env")


def _get(name: str, default: str = "") -> str:
    return os.getenv(name, default)


DATABASE_URL = _get("DATABASE_URL")

SECRET_KEY = _get("SECRET_KEY", "change-me-in-production")
JWT_ALGORITHM = _get("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(_get("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

OPENCAGE_API_KEY = _get("OPENCAGE_API_KEY")
GOOGLE_API_KEY = _get("GOOGLE_API_KEY")
GEMINI_MODEL = _get("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_FALLBACK_MODELS = _get(
    "GEMINI_FALLBACK_MODELS",
    "gemini-2.5-flash-lite,gemini-2.0-flash",
)
GEMINI_TIMEOUT = int(_get("GEMINI_TIMEOUT", "45"))

AWS_BUCKET_NAME = _get("AWS_BUCKET_NAME")

CORS_ALLOW_ORIGINS = _get(
    "CORS_ALLOW_ORIGINS",
    "http://localhost:5173,http://127.0.0.1:5173,https://khetimitra.vercel.app",
)
CORS_ALLOW_ORIGIN_REGEX = _get(
    "CORS_ALLOW_ORIGIN_REGEX",
    r"https://.*\.ngrok-free\.dev",
)
