import logging

from chromadb.errors import ChromaError, NotFoundError
from fastapi import APIRouter, HTTPException, status

from app.api.dependencies import CollectionsRepoDep
from app.api.schemas import CollectionCreateRequest, ErrorResponse
from app.storage.models import CollectionKey

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post(
    "/collections",
    status_code=status.HTTP_201_CREATED,
    responses={
        409: {
            "description": "Collection already exists",
            "model": ErrorResponse,
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Collection already exists",
                        "error_code": "HTTP_409_CONFLICT",
                    }
                }
            },
        },
        500: {
            "description": "Failed to create new collection",
            "model": ErrorResponse,
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Failed to create new collection",
                        "error_code": "HTTP_500_INTERNAL_SERVER_ERROR",
                    }
                }
            },
        },
    },
)
def create_collection(req: CollectionCreateRequest, repo: CollectionsRepoDep) -> None:
    key = CollectionKey(
        # FIXME: Extract tenant_id from auth token instead!
        tenant_id=req.tenant_id,
        name=req.collection_name,
    )
    metadata_keys = sorted(req.metadata.keys())

    logger.debug(
        f"Create collection requested for tenant={req.tenant_id} name={req.collection_name} "
        f"chroma_name={key.chroma_name} metadata_keys={metadata_keys}"
    )

    try:
        repo.get(key)
    except NotFoundError:
        logger.debug(
            f"Collection does not exist yet for tenant={req.tenant_id} name={req.collection_name}; proceeding with create"
        )
    else:
        logger.warning(
            f"Create collection rejected: already exists for tenant={req.tenant_id} name={req.collection_name}"
        )
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Collection already exists for tenant="
                f"'{req.tenant_id}' with name='{req.collection_name}'."
            ),
        )

    try:
        repo.create(key, metadata=req.metadata)
    except ChromaError as exc:
        logger.exception(
            f"Create collection failed for tenant={req.tenant_id} name={req.collection_name} chroma_name={key.chroma_name}"
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=(
                "Failed to create a new Collection for tenant="
                f"'{req.tenant_id}' with name='{req.collection_name}'."
            ),
        ) from exc

    logger.info(
        f"Collection created for tenant={req.tenant_id} name={req.collection_name} chroma_name={key.chroma_name}"
    )

    return
