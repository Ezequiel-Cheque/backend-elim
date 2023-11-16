from pymongo import MongoClient
from os import getenv
from ..conection import db

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



