from fastapi import APIRouter, UploadFile, File
from fastapi.security import HTTPBearer
from fastapi.responses import FileResponse
from ..dto import payment_create_schema
from ..service.payments_service import Payments_service
from os import getcwd
from ..exceptions.catalogue_exceptions import CatalogsExceptions

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
    
    upload_response = {}
    upload_response["success"] = True
    upload_response["data"] = {}
    
    try:
        url = getcwd() + "/assets/receipts/" + file.filename
        with open(url, "wb") as myfile:
            content = await file.read()
            myfile.write(content)
            myfile.close()
            
            file_name = file.filename
            
            response = {}
            response["file_name"] = file_name
            upload_response["data"] = response 
             
        return upload_response
    
    except Exception as err:
        print(str(err))
        CatalogsExceptions.errorUploadFile()
        

@payments.get("/file/{name}")
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