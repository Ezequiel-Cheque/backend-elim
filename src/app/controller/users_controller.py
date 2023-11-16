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