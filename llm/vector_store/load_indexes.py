import faiss
import pickle
import os

BASE_DIR = "llm/vector_store"

INDEX_PATHS = {
    "soil": "soil_index",
    "schemes": "schemes_index",
    "practices": "practices_index",
    "pests": "pest_index"
}


def load_all_indexes():

    indexes = {}
    metadata_store = {}

    for name, folder in INDEX_PATHS.items():

        index_path = os.path.join(
            BASE_DIR,
            folder,
            "index.faiss"
        )

        meta_path = os.path.join(
            BASE_DIR,
            folder,
            "index.pkl"
        )

        if os.path.exists(index_path):

            indexes[name] = faiss.read_index(
                index_path
            )

        if os.path.exists(meta_path):

            with open(meta_path, "rb") as f:

                metadata_store[name] = pickle.load(f)

    return indexes, metadata_store