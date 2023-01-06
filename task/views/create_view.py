from utils.http.constants import HttpStatus
from utils.http.constants import HttpMethod
from utils.http.decorators.views.view import view
from utils.http.responses.JSONResponse import JSONResponse
from utils.validation.no_data_form import NoDataForm

from .create_form import TaskPostForm
from .task_manager import TaskManager


@view(post=TaskPostForm)
def create_view(request, data: dict):
    manager = TaskManager.create(user=request.user, **data)
    
    response_data = manager.read()

    return JSONResponse(response_data)