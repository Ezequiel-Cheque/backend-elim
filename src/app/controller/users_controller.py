from fastapi import APIRouter
from fastapi.security import HTTPBearer
from ..dto import user_create_schema
from ..service.users_service import Users_service

users = APIRouter(prefix="/users", tags=["Users endpoints"])
security = HTTPBearer()

@users.post(
    "/create",
    description="Create an user",
    responses={}
)
def index(body: user_create_schema):
    return Users_service().create(body)

@users.get(
    "/get/all",
    description="Get all users",
    responses={}
)
def getall():
    return Users_service().get_all()

@users.get(
    "/get/id/{id}",
    description="Get by user_id",
    responses={}
)
def getall(id: str):
    return Users_service().get_by_id(id)

@users.get(
    "/get/email/{email}",
    description="Get by email",
    responses={}
)
def get_by_email(email: str):
    return Users_service().get_by_email(email)

@users.delete(
    "/delete/{id}",
    description="delete user",
    responses={}
)
def delete(id: str):
    return Users_service().delete(id)