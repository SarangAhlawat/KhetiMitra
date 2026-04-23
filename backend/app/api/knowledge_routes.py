from fastapi import APIRouter
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


router = APIRouter()


# =========================
# LOAD EMBEDDINGS
# =========================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =========================
# PATH SETUP
# =========================

BASE_DIR = Path(__file__).resolve().parents[3]

VECTOR_DIR = (
    BASE_DIR
    / "llm"
    / "vector_store"
)

print("Vector directory:", VECTOR_DIR)


# =========================
# LOAD INDEX (ONCE)
# =========================

def load_index(name):

    path = VECTOR_DIR / f"{name}_index"

    if not path.exists():

        raise FileNotFoundError(
            f"Vector index not found: {path}"
        )

    return FAISS.load_local(
        str(path),
        embeddings,
        allow_dangerous_deserialization=True
    )


# Load once at startup (VERY IMPORTANT)

practice_db = load_index("practices")

scheme_db = load_index("schemes")

soil_db = load_index("soil")

pest_db = load_index("pest")


# =========================
# SEARCH PRACTICES
# =========================

@router.get("/search/practices")

def search_practices(query: str):

    results = practice_db.similarity_search(
        query,
        k=3
    )

    return {

        "results":

        [r.page_content for r in results]

    }


# =========================
# SEARCH SCHEMES
# =========================

@router.get("/search/schemes")

def search_schemes(query: str):

    results = scheme_db.similarity_search(
        query,
        k=3
    )

    return {

        "results":

        [r.page_content for r in results]

    }


# =========================
# SEARCH SOIL
# =========================

@router.get("/search/soil")

def search_soil(query: str):

    results = soil_db.similarity_search(
        query,
        k=3
    )

    return {

        "results":

        [r.page_content for r in results]

    }


# =========================
# SEARCH PEST
# =========================

@router.get("/search/pest")

def search_pest(query: str):

    results = pest_db.similarity_search(
        query,
        k=3
    )

    return {

        "results":

        [r.page_content for r in results]

    }