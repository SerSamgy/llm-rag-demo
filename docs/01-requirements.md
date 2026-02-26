# RAGDock — Requirements

## Functional Requirements

- Create collections (multi-tenant)
- Ingest documents into a collection
- Chunk + embed documents
- Store embeddings in vector DB
- Query collection
- Return answer with citations

## Non-Functional Requirements

- LLM-agnostic architecture
- Config via environment variables
- Structured logging
- Local Docker deployment
- Deterministic evaluation capability

## Constraints

- Python 3.13
- FastAPI
- Chroma vector DB
- LangChain
- OpenAI provider (initial)