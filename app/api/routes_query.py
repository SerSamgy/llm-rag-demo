from fastapi import APIRouter

from app.api.schemas import QueryRequest, QueryResponse

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
def query(req: QueryRequest) -> QueryResponse:
    # Stub: no retrieval/LLM yet
    return QueryResponse(
        collection_id=req.collection_id,
        answer="I don't know yet (pipeline not implemented).",
        citations=[],
        chunks=[],
    )
