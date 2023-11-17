from pymongo import MongoClient
from os import getenv
from ..conection import db
from bson.objectid import ObjectId

client = MongoClient(db)
database = client[getenv("DB_SCHEMA")]

collection = database["receipts"]

class Receipts:
    id_payment: str
    date: str
    file_name: str

    def save(**request):
        request["active"] = True
        request["id_payment"] = ObjectId(request["id_payment"])
        result = collection.insert_one(request)
        return str(result.inserted_id)
    
    def get_by_filename(filename):
        try:
            return collection.find_one({ "active": True, "file_name": filename })
        except Exception as err:
            print(str(err))
            return None