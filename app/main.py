import os

from fastapi import FastAPI

app = FastAPI(title="RAGDock")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/config")
def config() -> dict[str, str]:
    return {
        "redis_url": os.getenv("REDIS_URL", ""),
        "database_url": os.getenv("DATABASE_URL", ""),
        "qdrant_url": os.getenv("QDRANT_URL", ""),
    }
