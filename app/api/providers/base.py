from typing import Protocol


class EmbeddingsProvider(Protocol):
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Return one embedding vector per input text."""
        ...


class LLMProvider(Protocol):
    def generate(self, prompt: str) -> str:
        """Return a single generated answer string."""
        ...
