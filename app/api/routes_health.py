from chromadb import HttpClient
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    # FIXME: Add Chroma client as dependency
    client = HttpClient(host="chromadb", port=8000)
    client.heartbeat()
    return {"status": "ok"}
