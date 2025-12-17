import json

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from enum import Enum

class Colors(Enum):
    Azul = "Azul"
    Amarillo = "Amarillo" 
    Rosa = "Rosa" 
    Morado = "Morado" 
    Rojo = "Rojo" 

class team_create_schema(BaseModel):
    name: str = Field(description="", example="")
    color: Colors = Field(description="", example="Azul,Amarillo,Rosa,Morado,Rojo")
    point: int = Field(description="", example=0)
    position: int = Field(description="", example=0)

class teamCreateSchemaRoot(BaseModel):
    __root__: team_create_schema

class teamCreate:
    def create(teamCreate: team_create_schema):
        return jsonable_encoder(teamCreateSchemaRoot(__root__=teamCreate))
    
class team_points(BaseModel):
    team: str = Field(description="", example="")
    point: int = Field(description="", example=0)

class pointsSchemaRoot(BaseModel):
    __root__: team_points

class teamPoints:
    def create(teamPoints: team_points):
        return jsonable_encoder(pointsSchemaRoot(__root__=teamPoints))