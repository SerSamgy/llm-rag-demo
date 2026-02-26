import uuid

from fastapi import APIRouter

from app.api.schemas import CollectionCreateRequest, CollectionCreateResponse

router = APIRouter()

# temporary in-memory registry (replaced later by Chroma-backed collections)
_COLLECTIONS: dict[str, dict[str, str]] = {}


@router.post("/collections", response_model=CollectionCreateResponse)
def create_collection(req: CollectionCreateRequest) -> CollectionCreateResponse:
    collection_id = f"{req.tenant_id}:{req.collection_name}:{uuid.uuid4().hex[:8]}"
    _COLLECTIONS[collection_id] = {
        "tenant_id": req.tenant_id,
        "collection_name": req.collection_name,
    }
    return CollectionCreateResponse(
        collection_id=collection_id,
        tenant_id=req.tenant_id,
        collection_name=req.collection_name,
    )
