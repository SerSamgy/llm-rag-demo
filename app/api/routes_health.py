import logging
from time import perf_counter

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.api.dependencies import ChromaClientDep, SettingsDep

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/health")
def health(chroma_client: ChromaClientDep, settings: SettingsDep):
    start = perf_counter()

    try:
        heartbeat = chroma_client.heartbeat()
    except Exception:
        latency_ms = round((perf_counter() - start) * 1000, 2)
        logger.exception(
            "Health check failed: could not connect to ChromaDB at %s:%s",
            settings.chroma_host,
            settings.chroma_port,
        )
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": "degraded",
                "checks": {
                    "chromadb": {
                        "status": "down",
                        "host": settings.chroma_host,
                        "port": settings.chroma_port,
                        "latency_ms": latency_ms,
                    }
                },
            },
        )

    latency_ms = round((perf_counter() - start) * 1000, 2)
    logger.debug(
        "Health check passed for ChromaDB at %s:%s in %.2f ms",
        settings.chroma_host,
        settings.chroma_port,
        latency_ms,
    )

    return {
        "status": "ok",
        "checks": {
            "chromadb": {
                "status": "up",
                "host": settings.chroma_host,
                "port": settings.chroma_port,
                "latency_ms": latency_ms,
                "heartbeat": heartbeat,
            }
        },
    }
