import logging
import os

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_DIR,
    "app.log"
)

logging.basicConfig(
    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",

    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def get_logger(name: str):

    return logging.getLogger(name)









# import logging

# from llm.rag_pipeline import rag_answer

# logger = logging.getLogger(__name__)


# def get_rag_response(query):

#     try:

#         logger.info(
#             f"RAG Query: {query}"
#         )

#         response = rag_answer(query)

#         return {

#             "success": True,
#             "response": response

#         }

#     except Exception as e:

#         logger.error(str(e))

#         return {

#             "success": False,
#             "error": str(e)

#         }