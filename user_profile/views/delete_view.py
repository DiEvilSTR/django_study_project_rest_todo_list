from django.contrib.auth.models import User
from django.contrib.auth import logout

from utils.http.constants import HttpStatus
from utils.http.decorators.views.view import view
from utils.http.responses.JSONResponse import JSONResponse
from utils.validation.no_data_form import NoDataForm


@view(delete=NoDataForm)
def delete_view(request):
    try:
        user = User.objects.get(username=request.user.username)
        
        logout(request)
        user.delete()
    except User.DoesNotExist:
        return JSONResponse(error='', status=HttpStatus.NOT_FOUND)

    return JSONResponse(None)
