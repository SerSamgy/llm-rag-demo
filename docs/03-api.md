# RAGDock — API

## POST /collections
Creates a tenant-scoped collection.

### Request
- tenant_id: string
- collection_name: string

### Response
- collection_id: string
- tenant_id: string
- collection_name: string

## POST /ingest
Ingests items into a collection.

### Request
- collection_id: string
- items: [{ text, source?, time?, tags[], extra{} }]

### Response
- collection_id: string
- documents_ingested: int
- chunks_created: int
- chunks: [{ chunk_id, document_id, text, metadata }]

## POST /query
Queries a collection.

### Request
- collection_id: string
- question: string
- top_k: int (default 5)

### Response
- collection_id: string
- answer: string
- citations: [{ chunk_id, document_id, source?, score? }]
- chunks: [{ chunk_id, document_id, text, score?, metadata }]