from pymongo import MongoClient
from os import getenv
from ..conection import db
from bson.objectid import ObjectId

client = MongoClient(db)
database = client[getenv("DB_SCHEMA")]

collection = database["users"]

class Users:
    name: str
    last_name: str
    email: str
    phone: str
    age: int
    church: str
    paid: bool

    def save(**request):
        request["active"] = True
        result = collection.insert_one(request)
        return str(result.inserted_id)

    def get_all():
        try:
            return list(collection.find({"active": True}))
        except Exception as err:
            print(str(err))
            return None

    def get_by_id(id):
        try:
            id = ObjectId(id)
            return collection.find_one({"_id": id, "active": True})
        except Exception as err:
            print(str(err))
            return None
    
    def get_by_id(email):
        try:
            return collection.find_one({"email": email, "active": True})
        except Exception as err:
            print(str(err))
            return None


