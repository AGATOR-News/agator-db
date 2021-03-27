from pydantic import BaseModel, AnyHttpUrl, ValidationError, validator
from pydantic.color import Color
from uuid import UUID as UUID


class Publication(BaseModel):
    id: str
    title: str
    link: AnyHttpUrl
    description: str
    banner: AnyHttpUrl
    icon: AnyHttpUrl
    color: str

    @validator('id')
    def id_is_uuid(cls, v):
        UUID(v)
        return v

    @validator('color')
    def color_is_valid(cls, v):
        return Color(v).as_hex()


class PublicationIN(BaseModel):
    title: str
    link: AnyHttpUrl
    description: str
    banner: AnyHttpUrl
    icon: AnyHttpUrl
    color: str

    @validator('color')
    def color_is_valid(cls, v):
        return Color(v).as_hex()
