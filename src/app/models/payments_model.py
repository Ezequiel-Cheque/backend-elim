from pymongo import MongoClient
from os import getenv
from ..conection import db
from datetime import datetime
from bson.objectid import ObjectId

client = MongoClient(db)
database = client[getenv("DB_SCHEMA")]

collection = database["payments"]

class Payments:
    id_user: str
    amount: float
    date: str
    form_data: dict
    active: bool
    paid: bool

    def create(**request):
        date = datetime.now()
        formatDate = date.strftime("%d-%m-%Y %H:%M:%S")
        request["id_user"] = ObjectId(request["id_user"])
        request["active"] = True
        request["date"] = formatDate
        request["paid"] = False

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
            return list(collection.find({"id_user": id, "active": True}))
        except Exception as err:
            print(str(err))
            return None
    
    def get_payment_by_id(id):
        try:
            id = ObjectId(id)
            return collection.find_one({"_id": id, "active": True})
        except Exception as err:
            print(str(err))
            return None

    def delete_payment(id):
        try:
            id = ObjectId(id)
            return collection.update_one(
                {"_id": id},
                {"$set": {"active": False}},
                upsert=True,
            )
        except Exception:
            return None