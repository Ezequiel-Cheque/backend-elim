import json

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from enum import Enum

class SexClass(Enum):
    F = "F"
    M = "M"

class user_create_schema(BaseModel):
    name: str = Field(description="")
    last_name: str = Field(description="")
    # email: str = Field(description="", example='Default')
    # phone: str = Field(description="", min_length=10, example='0000000000')
    age: int = Field(description="")
    church: str = Field(description="")
    sex: SexClass = Field(description="", example="M")
    team: str = Field(description="", example="")
    cabin: str = Field(description="", example="")
    status: str = Field(description="")
    total_paid: int = Field(description="")
    isStaff: bool = Field(description="", example=False)

class userCreateSchemaRoot(BaseModel):
    __root__: user_create_schema

class userCreate:
    def create(userCreate: user_create_schema):
        return jsonable_encoder(userCreateSchemaRoot(__root__=userCreate))