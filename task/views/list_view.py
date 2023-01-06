from utils.http.decorators.views.view import view
from utils.http.responses.JSONResponse import JSONResponse

from .list_form import TaskListGetForm
from .list_manager import TaskListManager


filters_name_map = {
    'title': 'title__icontains',
    'is_done': 'is_done',
    'updated_at_gte': 'updated_at__gte',
    'updated_at_lte': 'updated_at__lte',
    'user': 'user__username',
}

read_param_list = set(['count', 'page'])

@view(get=TaskListGetForm)
def list_view(request, data: dict):
    filters = { filters_name_map[key]: value for (key, value) in data.items() if key in filters_name_map }

    manager = TaskListManager.filter(**filters)

    read_params = { key: data[key] for key in read_param_list if key in data }

    response_data = manager.read(**read_params)

    return JSONResponse(response_data)