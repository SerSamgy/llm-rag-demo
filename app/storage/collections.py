from chromadb import Collection
from chromadb.api import ClientAPI

from app.storage.models import CollectionKey


class CollectionsRepo:
    def __init__(self, client: ClientAPI) -> None:
        self._client = client

    def get(self, key: CollectionKey) -> Collection:
        return self._client.get_collection(name=key.chroma_name)

    def create(self, key: CollectionKey, metadata: dict | None = None) -> Collection:
        if metadata is None:
            metadata = {}

        return self._client.create_collection(
            name=key.chroma_name,
            metadata=metadata,
        )

    def get_or_create(
        self, key: CollectionKey, metadata: dict | None = None
    ) -> Collection:
        return self._client.get_or_create_collection(
            name=key.chroma_name,
            metadata=metadata or {},
        )
