from fastapi import APIRouter, UploadFile, File
from fastapi.security import HTTPBearer
from fastapi.responses import FileResponse
from ..dto import payment_create_schema
from ..service.payments_service import Payments_service
from typing import Annotated
from os import getcwd

payments = APIRouter(prefix="/payments", tags=["Payments endpoints"])
security = HTTPBearer()

@payments.post(
    "/create",
    description="Create a payment",
    responses={}
)
def create(body: payment_create_schema):
    return Payments_service().create(body)

@payments.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    url = getcwd() + "/assets/receipts/" + file.filename
    with open(url, "wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    return file.filename

@payments.post("/file/{name}")
def get_file(name: str):
    return FileResponse(getcwd() + "/assets/receipts/" + name)

@payments.get(
    "/get/all",
    description="Get all payments",
    responses={}
)
def getall():
    return Payments_service().get_all()

@payments.get(
    "/get/{id}",
    description="Get by user_id",
    responses={}
)
def getall(id: str):
    return Payments_service().get_by_id(id)