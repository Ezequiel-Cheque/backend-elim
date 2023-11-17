from . import Error

class CatalogsExceptions:

    def userNotExist():
        Error(400, "El usuario que buscas no existe, revisa tus datos")

    def paymentNotExist():
        Error(400, "Los pagos que buscan no se encuentran")
        
    def errorUploadFile():
        Error(400, "error, no se pudo subir el archivo")

    def receiptNotFound():
        Error(400, "Recibo no encontrado")