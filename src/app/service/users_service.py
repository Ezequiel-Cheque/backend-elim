from ..dto import user_create_schema, userCreate
from ..models import Users, Teams
from ..exceptions.catalogue_exceptions import CatalogsExceptions
from typing import List

class Users_service:

    def create(self, body: user_create_schema):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        body = userCreate.create(body)

        result = Users.save(**body)

        create_response["data"] = result
        
        return create_response
    
    def createMany(self, bodyList: List[user_create_schema]):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = []

        for user in bodyList:
            body = userCreate.create(user)
            result = Users.save(**body)
            create_response["data"].append(result)
        
        return create_response

    def get_all(self):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        users = Users.get_all()

        for user in users:
            user["id"] = str(user["_id"])
            del user["_id"]

        create_response["data"] = users
        
        return create_response

    def get_by_id(self, id: str):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None
        
        user = Users.get_by_id(id)
        
        if not user:
            CatalogsExceptions.userNotExist()

        user["id"] = str(user["_id"])
        del user["_id"]
        create_response["data"] = user
        
        return create_response
    
    def getAll_by_team(self, teamId: str):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        team = Teams.get_by_id(teamId)
        
        if not team:
            CatalogsExceptions.userNotExist()

        userList = Users.get_by_team(teamId, team['color'])

        create_response["data"] = userList
        
        return create_response

    def get_by_email(self, email: str):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        user = Users.get_by_email(email)
        if not user:
            CatalogsExceptions.userNotExist()

        user["id"] = str(user["_id"])
        del user["_id"]
        create_response["data"] = user
        
        return create_response
    
    def delete(self, id: str):
        delete_response = {}
        delete_response["success"] = True
        delete_response["data"] = None
        
        user = Users.get_by_id(id)
        
        if not user:
            CatalogsExceptions.userNotExist()
        
        result = Users.delete_user(id)
        
        delete_response["data"] = {
            "message": "User delete successfully",
            "id": id
        }

        return delete_response
