from llm.vector_store.context_builder import (
    build_context
)

from backend.app.services.prompt_loader import (
    load_prompt
)

from backend.app.services.prompt_formatter import (
    format_prompt
)

from backend.app.services.llm_service import (
    generate_response
)

# from backend.app.core.logger import logger
from backend.app.core.logger import get_logger

logger = get_logger(__name__)




# =========================
# CORE RAG PIPELINE
# =========================




def rag_answer(
    qullocalery: str,
    prompt_name: str = "farmer_query_prompt.txt"
):

    """
    Core RAG pipeline

    Steps:
    1. Validate query
    2. Retrieve context
    3. Load prompt
    4. Format prompt
    5. Generate LLM response
    """

    try:

        # STEP 0 — Query Safety Limit
        if len(query) > 1000:

            logger.warning(
                "Query too long — truncating to 1000 chars"
            )

            query = query[:1000]


        logger.info(
            f"Running RAG with prompt: {prompt_name}"
        )


        # STEP 1 — Retrieve context
        context = build_context(query)

        logger.info("Context built successfully")


        # STEP 1.5 — Handle Empty Context
        if not context:

            logger.warning(
                "No context retrieved — using fallback"
            )

            context = "No relevant agricultural knowledge found."


        # STEP 2 — Context Length Limit
        if len(context) > 4000:

            logger.warning(
                "Context too long — truncating to 4000 chars"
            )

            context = context[:4000]


        # STEP 3 — Load prompt template
        template = load_prompt(prompt_name)

        logger.info("Prompt loaded")


        # STEP 4 — Format prompt
        prompt = format_prompt(
            template,
            context=context,
            question=query
        )

        logger.info("Prompt formatted")


        # STEP 5 — Generate LLM response
        response = generate_response(prompt)

        logger.info("LLM response generated")


        return response


    except Exception as e:

        logger.error(
            f"RAG pipeline failed: {str(e)}"
        )

        return "Sorry, I couldn't process your request."





# def rag_answer(
#     query: str,
#     prompt_name: str = "farmer_query_prompt.txt"
# ):

#     """
#     Core RAG pipeline

#     Steps:
#     1. Validate query
#     2. Retrieve context
#     3. Load prompt
#     4. Format prompt
#     5. Generate LLM response
#     """

#     try:

#         # STEP 0 — Query Safety Limit
#         if len(query) > 1000:

#             logger.warning(
#                 "Query too long — truncating to 1000 chars"
#             )

#             query = query[:1000]


#         logger.info(
#             f"Running RAG with prompt: {prompt_name}"
#         )

#         if len(context) > 4000:

#             logger.warning(
#                 "Context too long — truncating to 4000 chars"
#             )

#         context = context[:4000]


#         # STEP 1 — Retrieve context
#         context = build_context(query)

#         logger.info("Context built successfully")


#         # STEP 2 — Load prompt template
#         template = load_prompt(prompt_name)

#         logger.info("Prompt loaded")


#         # STEP 3 — Format prompt
#         prompt = format_prompt(
#             template,
#             context=context,
#             question=query
#         )

#         logger.info("Prompt formatted")


#         # STEP 4 — Generate LLM response
#         response = generate_response(prompt)

#         logger.info("LLM response generated")


#         return response


    except Exception as e:

        logger.error(
            f"RAG pipeline failed: {str(e)}"
        )

        raise


# =========================
# SPECIALIZED RAG CALLS
# =========================

def get_practice_advice(query):

    logger.info("Practice advice requested")

    return rag_answer(
        query,
        prompt_name="farmer_query_prompt.txt"
    )


def get_scheme_advice(query):

    logger.info("Scheme advice requested")

    return rag_answer(
        query,
        prompt_name="scheme_prompt.txt"
    )


def get_risk_advice(query):

    logger.info("Risk advice requested")

    return rag_answer(
        query,
        prompt_name="risk_prompt.txt"
    )

















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


# # def rag_answer(query: str):

# #     context = build_context(query)

# #     template = load_prompt(
# #         "farmer_query_prompt.txt"
# #     )

# #     prompt = format_prompt(
# #         template,
# #         context=context,
# #         question=query
# #     )

# #     response = generate_response(prompt)

# #     return response