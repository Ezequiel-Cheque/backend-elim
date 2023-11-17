from fastapi import APIRouter
from fastapi.security import HTTPBearer
from ..dto import payment_create_schema
from ..service.payments_service import Payments_service


payments = APIRouter(prefix="/payments", tags=["Payments endpoints"])
security = HTTPBearer()

@payments.post(
    "/create",
    description="Create a payment",
    responses={}
)
def create(body: payment_create_schema):
    return Payments_service().create(body)

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

@payments.delete(
    "/delete/{id}",
    description="delete user",
    responses={}
)
def delete(id: str):
    return Payments_service().delete(id)