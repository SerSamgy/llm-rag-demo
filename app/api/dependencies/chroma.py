from typing import Annotated

from chromadb import HttpClient
from chromadb.api import ClientAPI
from fastapi import Depends

from app.api.dependencies.settings import SettingsDep


def get_chroma_client(settings: SettingsDep) -> ClientAPI:
    return HttpClient(host=settings.chroma_host, port=settings.chroma_port)


type ChromaClientDep = Annotated[ClientAPI, Depends(get_chroma_client)]
