from fastapi import APIRouter
from fastapi.security import HTTPBearer
from ..dto import team_create_schema, team_points
from ..service.teams_service import Teams_service

teams = APIRouter(prefix="/teams", tags=["Teams endpoints"])
security = HTTPBearer()

@teams.post(
    "/create",
    description="Create an user",
    responses={}
)
def index(body: team_create_schema):
    return Teams_service().create(body)

@teams.post(
    "/add-points",
    description="Add points to the team",
    responses={}
)
def points(body: team_points):
    return Teams_service().addPoints(body)

@teams.get(
    "/get/all",
    description="Get all users",
    responses={}
)
def getall():
    return Teams_service().get_all()

@teams.get(
    "/get/id/{id}",
    description="Get by user_id",
    responses={}
)
def getall(id: str):
    return Teams_service().get_by_id(id)

@teams.delete(
    "/delete/{id}",
    description="delete user",
    responses={}
)
def delete(id: str):
    return Teams_service().delete(id)