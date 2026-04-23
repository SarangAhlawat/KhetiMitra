from llm.rag_pipeline import rag_answer

from app.core.logger import get_logger

logger = get_logger(__name__)

def get_rag_response(
    query: str
):

    """
    Main RAG interface
    used by backend APIs
    """

    try:

        logger.info(
            f"RAG Query Received: {query}"
        )

        response = rag_answer(query)

        logger.info(
            "RAG Response generated successfully"
        )

        return {
            "success": True,
            "response": response
        }

    except Exception as e:

        logger.error(
            f"RAG Error: {str(e)}"
        )

        return {
            "success": False,
            "error": str(e)
        }

from backend.app.services.ml_service import (
    predict_crop,
    predict_yield
)

from backend.app.services.rule_engine import (
    get_practice_recommendations
)


def get_full_recommendation(
    farm_data: dict
):

    """
    Hybrid DSS response
    """

    crop = predict_crop(farm_data)

    yield_prediction = predict_yield(farm_data)

    practices = get_practice_recommendations(
        farm_data
    )

    rag_query = f"""
Recommended crop: {crop}

Practices:
{practices}

Explain why these recommendations
are suitable for the farm.
"""

    explanation = rag_answer(rag_query)

    return {

        "crop": crop,

        "yield": yield_prediction,

        "practices": practices,

        "explanation": explanation

    }




# from llm.vector_store.context_builder import (
#     build_context
# )


# def get_knowledge_context(
#     query: str
# ):

#     context = build_context(
#         query=query,
#         top_k=5
#     )

#     return context