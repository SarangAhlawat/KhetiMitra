from llm.vector_store.unified_search import (
    search_all_indexes
)


def build_context(query: str):

    results = search_all_indexes(
        query=query,
        top_k=5
    )

    context_blocks = []

    for r in results:

        block = f"""
Source: {r['source']}

{r['text']}
"""

        context_blocks.append(block)

    context = "\n\n".join(context_blocks)

    return context















# from llm.vector_store.unified_search import (
#     search_all_indexes
# )


# def build_context(
#     query: str,
#     top_k: int = 5
# ):

#     results = search_all_indexes(
#         query,
#         top_k
#     )

#     context_blocks = []

#     for r in results:

#         block = f"""
# Source: {r['source']}

# {r['text']}
# """

#         context_blocks.append(block)

#     context = "\n\n".join(context_blocks)

#     return context

















# # from llm.vector_store.unified_search import (
# #     search_all_indexes
# # )


# # def build_context(
# #     query: str,
# #     top_k: int = 5
# # ):

# #     results = search_all_indexes(
# #         query,
# #         top_k
# #     )

# #     context_blocks = []

# #     for r in results:

# #         block = f"""
# # Source: {r['source']}

# # {r['text']}
# # """

# #         context_blocks.append(block)

# #     context = "\n\n".join(context_blocks)

# #     return context