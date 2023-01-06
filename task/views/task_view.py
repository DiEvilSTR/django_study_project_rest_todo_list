from utils.http.constants import HttpStatus
from utils.http.constants import HttpMethod
from utils.http.decorators.views.view import view
from utils.http.responses.JSONResponse import JSONResponse
from utils.validation.no_data_form import NoDataForm

from .task_form import TaskPatchForm
from .task_manager import TaskManager


@view(delete=NoDataForm, get=NoDataForm, patch=TaskPatchForm)
def task_view(request, pk, data=None):
    manager = TaskManager.get(id=pk)
    
    if not manager:
        return JSONResponse(error='', status=HttpStatus.NOT_FOUND)

    match request.method:
        case HttpMethod.PATCH:
            manager.update(data)
        case HttpMethod.DELETE:
            manager.delete()
    
    response_data = manager.read()

    return JSONResponse(response_data)