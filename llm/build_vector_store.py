from pathlib import Path
import pandas as pd

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


# =========================
# BASE PATH
# =========================

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data" / "knowledge_base"

VECTOR_DIR = BASE_DIR / "llm" / "vector_store"

VECTOR_DIR.mkdir(parents=True, exist_ok=True)


# =========================
# EMBEDDING MODEL
# =========================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =========================
# CSV → TEXT
# =========================

def csv_to_documents(file_path):

    df = pd.read_csv(file_path)

    docs = []

    for _, row in df.iterrows():

        text = " | ".join(
            [f"{col}: {row[col]}" for col in df.columns]
        )

        docs.append(text)

    return docs


# =========================
# GENERIC BUILDER
# =========================

def build_index(csv_path, index_path):

    print(f"Building index from: {csv_path}")

    documents = csv_to_documents(csv_path)

    db = FAISS.from_texts(
        documents,
        embeddings
    )

    db.save_local(index_path)

    print(f"Index saved → {index_path}")


# =========================
# DATASET BUILDERS
# =========================

def build_practices_index():

    csv_path = DATA_DIR / "practices" / "sustainable_practices.csv"

    index_path = VECTOR_DIR / "practices_index"

    build_index(csv_path, index_path)


def build_scheme_index():

    csv_path = DATA_DIR / "schemes" / "government_schemes.csv"

    index_path = VECTOR_DIR / "schemes_index"

    build_index(csv_path, index_path)


def build_soil_index():

    csv_path = DATA_DIR / "soil_guidelines" / "soil_management.csv"

    index_path = VECTOR_DIR / "soil_index"

    build_index(csv_path, index_path)


def build_pest_index():

    csv_path = DATA_DIR / "pest_management" / "pest_control.csv"

    index_path = VECTOR_DIR / "pest_index"

    build_index(csv_path, index_path)


# =========================
# MASTER REBUILD FUNCTION
# =========================

def rebuild_all_indexes():

    print("\nRebuilding all indexes...\n")

    build_soil_index()
    build_practices_index()
    build_scheme_index()
    build_pest_index()

    print("\nAll indexes rebuilt successfully.\n")


# =========================
# RUN
# =========================

if __name__ == "__main__":

    rebuild_all_indexes()










# import os
# import pandas as pd

# # from langchain.vectorstores import FAISS
# from langchain_community.vectorstores import FAISS
# # from langchain.embeddings import HuggingFaceEmbeddings
# from langchain_community.embeddings import HuggingFaceEmbeddings


# # =========================
# # BASE PATH
# # =========================

# # BASE_DIR = os.path.dirname(
# #     os.path.dirname(__file__)
# # )

# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parents[1]

# DATA_DIR = BASE_DIR / "data" / "knowledge_base"

# VECTOR_DIR = BASE_DIR / "llm" / "vector_store"

# # DATA_DIR = os.path.join(
# #     BASE_DIR,
# #     "data",
# #     "knowledge_base"
# # )

# # VECTOR_DIR = os.path.join(
# #     BASE_DIR,
# #     "llm",
# #     "vector_store"
# # )


# # =========================
# # EMBEDDING MODEL
# # =========================

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )


# # =========================
# # CSV → TEXT
# # =========================

# def csv_to_documents(file_path):

#     df = pd.read_csv(file_path)

#     docs = []

#     for _, row in df.iterrows():

#         text = " | ".join(

#             [f"{col}: {row[col]}" for col in df.columns]

#         )

#         docs.append(text)

#     return docs


# # =========================
# # BUILD VECTOR INDEX
# # =========================

# def build_index(csv_path, index_path):

#     documents = csv_to_documents(csv_path)

#     db = FAISS.from_texts(
#         documents,
#         embeddings
#     )

#     db.save_local(index_path)

#     print(f"Index saved → {index_path}")






# # =========================
# # RUN BUILD
# # =========================

# def main():

#     datasets = {

#         "practices": os.path.join(
#             DATA_DIR,
#             "practices",
#             "sustainable_practices.csv"
#         ),

#         "schemes": os.path.join(
#             DATA_DIR,
#             "schemes",
#             "government_schemes.csv"
#         ),

#         "soil": os.path.join(
#             DATA_DIR,
#             "soil_guidelines",
#             "soil_management.csv"
#         ),

#         "pest": os.path.join(
#             DATA_DIR,
#             "pest_management",
#             "pest_control.csv"
#         )

#     }

#     for name, path in datasets.items():

#         index_path = os.path.join(
#             VECTOR_DIR,
#             f"{name}_index"
#         )

#         build_index(
#             path,
#             index_path
#         )


# if __name__ == "__main__":
#     main()