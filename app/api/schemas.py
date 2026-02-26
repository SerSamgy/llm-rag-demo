from typing import Any

from pydantic import BaseModel, Field


class CollectionCreateRequest(BaseModel):
    tenant_id: str = Field(min_length=1)
    collection_name: str = Field(min_length=1)


class CollectionCreateResponse(BaseModel):
    collection_id: str
    tenant_id: str
    collection_name: str


class IngestTextItem(BaseModel):
    text: str = Field(min_length=1)
    source: str | None = None
    time: str | None = None  # ISO8601 string for now
    tags: list[str] = []
    extra: dict[str, Any] = {}


class IngestRequest(BaseModel):
    collection_id: str = Field(min_length=1)
    items: list[IngestTextItem] = Field(min_length=1, default=[])


class IngestChunk(BaseModel):
    chunk_id: str
    document_id: str
    text: str
    metadata: dict[str, Any] = {}


class IngestResponse(BaseModel):
    collection_id: str
    documents_ingested: int
    chunks_created: int
    # FIXME: Leave it for now for debugging. Remove before deploying on prod.
    chunks: list[IngestChunk] = []


class QueryRequest(BaseModel):
    collection_id: str = Field(min_length=1)
    question: str = Field(min_length=1)
    top_k: int = Field(default=5, ge=1, le=50)


class Citation(BaseModel):
    chunk_id: str
    document_id: str
    source: str | None = None
    score: float | None = None


class RetrievedChunk(BaseModel):
    chunk_id: str
    document_id: str
    text: str
    score: float | None = None
    metadata: dict[str, Any] = {}


class QueryResponse(BaseModel):
    collection_id: str
    answer: str
    citations: list[Citation] = []
    # FIXME: Leave it for now for debugging. Remove before deploying on prod.
    chunks: list[RetrievedChunk] = []
