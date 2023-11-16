from . import Error

class CatalogsExceptions:

    def userNotExist():
        Error(400, "El usuario que buscas no existe, revisa tus datos")

    def paymentNotExist():
        Error(400, "Los pagos que buscan no se encuentran")