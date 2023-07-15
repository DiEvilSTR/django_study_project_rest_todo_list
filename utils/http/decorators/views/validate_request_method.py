from django.forms import Form

from utils.http.constants import HttpStatus
from utils.http.responses.JSONResponse import JSONResponse

def validate_request_method(FormClass):
    if not FormClass or not issubclass(FormClass, Form):
        return JSONResponse(error='', status=HttpStatus.METHOD_NOT_ALLOWED)
