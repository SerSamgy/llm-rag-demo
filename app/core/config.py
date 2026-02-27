from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "RAGDock"
    env: str = "local"

    chroma_host: str = "chromadb"
    chroma_port: int = 8000
    chroma_tenant: str = "default_tenant"
    chroma_database: str = "default_database"


@lru_cache
def get_settings() -> Settings:
    return Settings()
