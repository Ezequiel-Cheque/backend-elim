import json
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, EmailStr, Field
from fastapi import UploadFile

class payment_create_schema(BaseModel):
    id_user: str = Field(description="")
    amount: float = Field(description="")
    receipt: str = Field(description="")

class paymentCreateSchemaRoot(BaseModel):
    __root__: payment_create_schema

class paymentCreate:
    def create(paymentCreate: payment_create_schema):
        return jsonable_encoder(paymentCreateSchemaRoot(__root__=paymentCreate))