from utils.http.constants import HttpStatus
from utils.http.responses.JSONResponse import JSONResponse

def validate_login_required(request, login_required):
    if login_required and not request.user.is_authenticated:
        return JSONResponse(error='', status=HttpStatus.UNAUTHORIZED)
