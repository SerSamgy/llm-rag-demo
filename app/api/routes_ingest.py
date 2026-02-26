from fastapi import APIRouter

from app.api.schemas import IngestRequest, IngestResponse

router = APIRouter()


@router.post("/ingest", response_model=IngestResponse)
def ingest(req: IngestRequest) -> IngestResponse:
    # Stub: no chunking yet
    return IngestResponse(
        collection_id=req.collection_id,
        documents_ingested=len(req.items),
        chunks_created=0,
        chunks=[],
    )
