from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder

class receipt_create_schema(BaseModel):
    file_name: str = Field(description="")
    id_payment: str = Field(description="")

class receiptCreateSchemaRoot(BaseModel):
    __root__: receipt_create_schema

class receiptCreate:
    def create(receiptCreate: receipt_create_schema):
        return jsonable_encoder(receiptCreateSchemaRoot(__root__=receiptCreate))