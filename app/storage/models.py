from pydantic import BaseModel


class CollectionKey(BaseModel):
    tenant_id: str
    name: str

    @property
    def chroma_name(self) -> str:
        return f"t__{self.tenant_id}__c__{self.name}"
