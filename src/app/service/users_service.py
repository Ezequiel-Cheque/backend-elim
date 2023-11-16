from ..dto import user_create_schema, userCreate
from ..models import Users

class Users_service:

    def create(self, body: user_create_schema):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        body = userCreate.create(body)

        result = Users.save(**body)

        create_response["data"] = result
        
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

    def get_by_id(self, id):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        user = Users.get_by_id(id)
        user["id"] = str(user["_id"])
        del user["_id"]
        create_response["data"] = user
        
        return create_response

    def get_by_email(self, email):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        user = Users.get_by_email(email)
        user["id"] = str(user["_id"])
        del user["_id"]
        create_response["data"] = user
        
        return create_response
        