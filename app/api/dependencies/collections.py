from typing import Annotated

from fastapi import Depends

from app.api.dependencies.chroma import ChromaClientDep
from app.storage.collections import CollectionsRepo


def get_collections_repo(chroma_client: ChromaClientDep) -> CollectionsRepo:
    return CollectionsRepo(client=chroma_client)


type CollectionsRepoDep = Annotated[CollectionsRepo, Depends(get_collections_repo)]
