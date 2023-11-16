from ..dto import payment_create_schema, paymentCreate
from ..models import Payments
from ..exceptions.catalogue_exceptions import CatalogsExceptions


class Payments_service:

    def create(self, body: payment_create_schema):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        body = paymentCreate.create(body)

        result = Payments.create(**body)
        create_response["data"] = result
        
        return create_response
    
    def get_all(self):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        payments = Payments.get_all()
        
        for payment in payments:
            payment["id"] = str(payment["_id"])
            payment["id_user"] = str(payment["id_user"])
            del payment["_id"]

        create_response["data"] = payments
        
        return create_response

    def get_by_id(self, id):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        payments = Payments.get_by_id(id)

        if not payments:
            CatalogsExceptions.paymentNotExist()

        for payment in payments:
            payment["id"] = str(payment["_id"])
            payment["id_user"] = str(payment["id_user"])
            del payment["_id"]

        create_response["data"] = payments
        
        return create_response