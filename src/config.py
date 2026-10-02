from pydantic import BaseSettings


class Settings(BaseSettings):
    """Service settings, read from the environment (pydantic v1 style)."""

    app_name: str = "harness-demo"
    deadline_s: float = 1.0
