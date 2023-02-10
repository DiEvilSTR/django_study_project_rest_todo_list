from django.contrib.auth import logout

from utils.http.constants import HttpStatus
from utils.http.constants import HttpMethod
from utils.http.decorators.views.view import view
from utils.http.responses.JSONResponse import JSONResponse
from utils.validation.no_data_form import NoDataForm

from .user_manager import UserManager


@view(delete=NoDataForm, get=NoDataForm)
def details_view(request, pk=None):
    pk = pk or request.user.username
    manager = UserManager.get(username=pk)
    
    if not manager:
        return JSONResponse(error='', status=HttpStatus.NOT_FOUND)

    match request.method:
        case HttpMethod.DELETE:
            if pk != request.user.username:
                return JSONResponse(error='', status=HttpStatus.FORBIDDEN)
            logout(request)
            manager.delete()
            
    response_data = manager.read()

    return JSONResponse(response_data)
