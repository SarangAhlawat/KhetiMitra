from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
# services → app → backend → AI-DSS

PROMPT_DIR = BASE_DIR / "llm" / "prompts"


def load_prompt(prompt_name: str):

    file_path = PROMPT_DIR / prompt_name

    print("PROMPT_DIR:", PROMPT_DIR)
    print("FILE_PATH:", file_path)

    with open(file_path, "r") as f:
        return f.read()


# import os


# BASE_DIR = os.path.dirname(
#     os.path.dirname(
#         os.path.dirname(__file__)
#     )
# )

# PROMPT_DIR = os.path.join(
#     BASE_DIR,
#     "llm",
#     "prompts"
# )


# def load_prompt(prompt_name: str):

#     file_path = os.path.join(
#         PROMPT_DIR,
#         prompt_name
#     )

#     with open(file_path, "r") as f:
#         return f.read()


