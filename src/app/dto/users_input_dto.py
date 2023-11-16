import json

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, EmailStr, Field

class user_create_schema(BaseModel):
    name: str = Field(description="")
    last_name: str = Field(description="")
    email: str = Field(description="")
    phone: str = Field(description="")
    age: int = Field(description="")
    church: str = Field(description="")
    paid: bool = Field(description="")

class userCreateSchemaRoot(BaseModel):
    __root__: user_create_schema

class userCreate:
    def create(userCreate: user_create_schema):
        return jsonable_encoder(userCreateSchemaRoot(__root__=userCreate))