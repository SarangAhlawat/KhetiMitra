from llm.vector_store.context_builder import build_context

from app.services.prompt_loader import format_chat_prompt
from app.services.llm_service import generate_response
from app.core.logger import get_logger

logger = get_logger(__name__)


def rag_answer(query: str, prompt_name: str = "farmer_query_prompt.txt", use_context: bool = True, show_instructions: bool = False):
    """Core RAG pipeline: retrieve context, format prompt, query Gemini.
    
    Args:
        query: User question
        prompt_name: Prompt template file
        use_context: Whether to retrieve vector context (faster if False)
        show_instructions: Whether to show agriculture instructions in response
    """

    try:
        if not query:
            return "Please share your farming question so I can help."

        if len(query) > 500:
            logger.warning("Query truncated to 500 chars for speed")
            query = query[:500]

        logger.info(f"RAG (context={use_context}, instructions={show_instructions})")

        context = ""
        if use_context:
            try:
                context = build_context(query)
                logger.info("Context retrieved")
            except Exception as e:
                logger.warning(f"Context retrieval failed: {e}, continuing without")
                context = ""

        if not context.strip():
            context = "Use general agricultural best practices."

        if len(context) > 3500:
            logger.warning("Context truncated to 3500 chars")
            context = context[:3500]

        prompt = format_chat_prompt(prompt_name, context=context, question=query)

        response = generate_response(
            prompt,
            show_instructions=show_instructions,
            question=query,
            context=context,
        )
        logger.info("LLM response generated")

        return response

    except Exception as e:
        logger.error(f"RAG pipeline failed: {str(e)}")
        return "Sorry, I couldn't process your request."


def get_practice_advice(query, show_instructions: bool = False):
    logger.info("Practice advice requested")
    return rag_answer(query, prompt_name="farmer_query_prompt.txt", show_instructions=show_instructions)


def get_scheme_advice(query, show_instructions: bool = False):
    logger.info("Scheme advice requested")
    return rag_answer(query, prompt_name="scheme_prompt.txt", show_instructions=show_instructions)


def get_risk_advice(query, show_instructions: bool = False):
    logger.info("Risk advice requested")
    return rag_answer(query, prompt_name="risk_prompt.txt", show_instructions=show_instructions)

















# from llm.vector_store.context_builder import (
#     build_context
# )

# from backend.app.services.prompt_loader import (
#     load_prompt
# )

# from backend.app.services.prompt_formatter import (
#     format_prompt
# )

# from backend.app.services.llm_service import (
#     generate_response
# )


# def rag_answer(
#     query: str,
#     prompt_name: str = "farmer_query_prompt.txt"
# ):

#     """
#     Core RAG pipeline

#     Steps:
#     1. Retrieve context
#     2. Load prompt
#     3. Format prompt
#     4. Generate LLM response
#     """

#     # Step 1 — Retrieve context
#     context = build_context(query)

#     # Step 2 — Load prompt template
#     template = load_prompt(prompt_name)

#     # Step 3 — Format prompt
#     prompt = format_prompt(
#         template,
#         context=context,
#         question=query
#     )

#     # Step 4 — Generate response
#     response = generate_response(prompt)

#     return response



# from llm.rag_pipeline import rag_answer


# def get_practice_advice(query):

#     return rag_answer(
#         query,
#         prompt_name="farmer_query_prompt.txt"
#     )


# def get_scheme_advice(query):

#     return rag_answer(
#         query,
#         prompt_name="scheme_prompt.txt"
#     )


# def get_risk_advice(query):

#     return rag_answer(
#         query,
#         prompt_name="risk_prompt.txt"
#     )








# # from backend.app.services.llm_service import (
# #     generate_response
# # )

# # from llm.vector_store.context_builder import (
# #     build_context
# # )

# # from backend.app.services.prompt_loader import (
# #     load_prompt
# # )

# # from backend.app.services.prompt_formatter import (
# #     format_prompt
# # )