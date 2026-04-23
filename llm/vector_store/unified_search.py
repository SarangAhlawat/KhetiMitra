from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

import os


# Must match embedding used during index build
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


BASE_DIR = "llm/vector_store"

INDEX_NAMES = [
    "soil_index",
    "schemes_index",
    "practices_index",
    "pest_index"
]


def load_indexes():

    vectorstores = {}

    for name in INDEX_NAMES:

        path = os.path.join(
            BASE_DIR,
            name
        )

        if os.path.exists(path):

            print(f"Loading index: {name}")

            vectorstores[name] = FAISS.load_local(
                path,
                embedding_model,
                allow_dangerous_deserialization=True
            )

    return vectorstores


# Load once
vectorstores = load_indexes()


def search_all_indexes(
    query: str,
    top_k: int = 3
):

    all_results = []

    for name, store in vectorstores.items():

        docs = store.similarity_search(
            query,
            k=top_k
        )

        for doc in docs:

            all_results.append({
                "source": name,
                "text": doc.page_content
            })

    return all_results


















# import numpy as np

# from llm.vector_store.load_indexes import (
#     load_all_indexes
# )

# from llm.embeddings.embedder import (
#     create_embedding
# )


# indexes, metadata_store = load_all_indexes()


# def search_all_indexes(
#     query: str,
#     top_k: int = 3
# ):

#     query_embedding = create_embedding(query)

#     query_embedding = np.array(
#         [query_embedding]
#     ).astype("float32")

#     all_results = []

#     for name, index in indexes.items():

#         distances, indices = index.search(
#             query_embedding,
#             top_k
#         )

#         metadata = metadata_store[name]

#         for idx in indices[0]:

#             if idx < len(metadata):

#                 result_text = metadata[idx]["text"]

#                 all_results.append({
#                     "source": name,
#                     "text": result_text
#                 })

#     return all_results





# # import numpy as np

# # from llm.vector_store.load_indexes import (
# #     load_all_indexes
# # )

# # from llm.embeddings.embedder import (
# #     create_embedding
# # )


# # indexes, metadata_store = load_all_indexes()


# # def search_all_indexes(
# #     query: str,
# #     top_k: int = 3
# # ):

# #     query_embedding = create_embedding(query)

# #     query_embedding = np.array(
# #         [query_embedding]
# #     ).astype("float32")

# #     all_results = []

# #     for name, index in indexes.items():

# #         distances, indices = index.search(
# #             query_embedding,
# #             top_k
# #         )

# #         metadata = metadata_store[name]

# #         for idx in indices[0]:

# #             if idx < len(metadata):

# #                 result_text = metadata[idx]["text"]

# #                 all_results.append({
# #                     "source": name,
# #                     "text": result_text
# #                 })

# #     return all_results