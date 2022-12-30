from django.contrib.auth.models import User

from utils.http.constants import HttpStatus
from utils.http.decorators.views.view import view
from utils.http.responses.JSONResponse import JSONResponse
from utils.validation.no_data_form import NoDataForm


@view(get=NoDataForm)
def user_details_view(request, pk):
    try:
        user_details = User.objects.values('username').get(username=pk)
    except User.DoesNotExist:
        return JSONResponse(error='', status=HttpStatus.NOT_FOUND)

    return JSONResponse(user_details)
