from pymongo import MongoClient
from os import getenv
from ..conection import db
from bson.objectid import ObjectId

client = MongoClient(db)
database = client[getenv("DB_SCHEMA")]

collection = database["team"]

class Teams:


    def save(**request):
        request["active"] = True
        result = collection.insert_one(request)
        return str(result.inserted_id)
    
    def updatePoints(id: str, points: int, position: int):
        try:
            id = ObjectId(id)
            updated = collection.update_one({'_id': id }, { '$set': { 'point': points, 'position': position } })
            return updated.modified_count
        except Exception as err:
            print(str(err))
            return None

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

    def delete(id):
        try:
            id = ObjectId(id)
            return collection.update_one(
                {"_id": id},
                {"$set": {"active": False}},
                upsert=True,
            )
        except Exception:
            return None    
