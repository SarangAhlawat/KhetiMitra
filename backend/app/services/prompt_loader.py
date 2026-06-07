from pathlib import Path

from app.services.prompt_formatter import format_prompt

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
PROMPT_DIR = BASE_DIR / "llm" / "prompts"


def load_prompt(prompt_name: str) -> str:
    file_path = PROMPT_DIR / prompt_name
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_guidelines() -> str:
    return load_prompt("response_guidelines.txt")


def format_chat_prompt(template_name: str, **kwargs) -> str:
    """Load a prompt template and inject shared response guidelines."""
    template = load_prompt(template_name)
    kwargs.setdefault("guidelines", load_guidelines())
    return format_prompt(template, **kwargs)
