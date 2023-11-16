from ..dto import payment_create_schema, paymentCreate
from ..models import Payments


class Payments_service:

    def create(self, body: payment_create_schema):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        body = paymentCreate.create(body)

        result = Payments.create(**body)
        create_response["data"] = result
        
        return create_response