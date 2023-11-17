from ..dto import receipt_create_schema, receiptCreate
from ..models import Receipts
from ..exceptions.catalogue_exceptions import CatalogsExceptions


class Receipts_service:

    def create(self, body: receipt_create_schema):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        body = receiptCreate.create(body)

        result = Receipts.create(**body)

        create_response["data"] = {
            "message": "receipt create successfully",
            "id": result
        }

        return create_response



    def get_by_filename(self, filename: str):
        response = {}
        response["success"] = True
        response["data"] = None

        result = Receipts.get_by_filename(filename)

        if not result:
            CatalogsExceptions.receiptNotFound()

        del result["_id"]
        del result["active"]
        result["id_payment"] = str(result["id_payment"])

        response["data"] = result

        return response