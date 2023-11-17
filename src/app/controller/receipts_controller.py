from fastpi import Apirouter
from fastapi import APIRouter
from fastapi.security import HTTPBearer
from ..dto import receipt_create_schema
from ..service.receipts_service import Receipts_service

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
    "get/{filename}",
    desciption="Get by filename",
    responses={}
)
def get_by_filename(filename: str):
    return Receipts_service().get_by_filename(filename)