# RAGDock — Architecture

## Components

- API Layer (FastAPI)
- Core RAG Pipeline
- Provider Layer (LLM + Embeddings abstraction)
- Storage Layer (Chroma)
- Prompt Templates
- Evaluation Module

## Ingest Flow

Client -> API -> Chunker -> Embeddings Provider -> Vector Store

## Query Flow

Client -> API -> Retriever -> Prompt Builder -> LLM -> Answer + Citations