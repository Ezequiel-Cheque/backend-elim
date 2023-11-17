from fastapi import APIRouter, UploadFile, File
from fastapi.security import HTTPBearer
from fastapi.responses import FileResponse
from ..dto import receipt_create_schema
from ..service.receipts_service import Receipts_service
from os import getcwd
from ..exceptions.catalogue_exceptions import CatalogsExceptions

receipts = APIRouter(prefix="/receipts", tags=["Receipts endpoints"])

security = HTTPBearer()

@receipts.post(
    "/create",
    description="Create a receipt register",
    responses={}
)
def create(body: receipt_create_schema):
    return Receipts_service().create(body)

@receipts.get(
    "/get/{filename}",
    description="Get by filename",
    responses={}
)
def get_by_filename(filename: str):
    return Receipts_service().get_by_filename(filename)

@receipts.post("/uploadfile/")
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
        

@receipts.get("/file/{name}")
def get_file(name: str):
    return FileResponse(getcwd() + "/assets/receipts/" + name)