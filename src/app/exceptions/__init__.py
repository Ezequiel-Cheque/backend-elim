from fastapi import HTTPException

class Error(HTTPException):
    def __init__(self, code, message) -> HTTPException:
        response = {}
        response["success"] = False
        response["message"] = str(message)
        response["errors"] = []
        raise HTTPException(status_code=code, detail=response)