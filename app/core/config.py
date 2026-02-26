from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = Field(default="RAGDock")
    env: str = Field(default="local")
    log_level: str = Field(default="INFO")

    chroma_host: str = Field(default="chromadb")
    chroma_port: int = Field(default=8000)


@lru_cache
def get_settings() -> Settings:
    return Settings()
