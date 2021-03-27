from pydantic import BaseModel, AnyHttpUrl, ValidationError, validator
from uuid import UUID, uuid4


class Source(BaseModel):
    id: str
    title: str
    link: AnyHttpUrl
    publication: UUID

    @validator('id')
    def id_is_uuid(cls, v):
        UUID(v)
        return v

    @validator('publication')
    def publication_is_uuid(cls, v):
        UUID(v)
        return v


class SourceIN(BaseModel):
    title: str
    link: AnyHttpUrl
    publication: UUID

    @validator('publication')
    def publication_is_uuid(cls, v):
        UUID(v)
        return v

# Source.parse_obj({
#     "id": "9251dbb4-8f0a-11eb-8dcd-0242ac130003",
#     "title": "Spiegel Schlagzeilen",
#     "publication": "9251dbb4-8f0a-11eb-8dcd-0242ac130003",
#     "link": "http://spiegel.de",
# })
