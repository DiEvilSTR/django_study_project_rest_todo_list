from utils.http.decorators.views.view import view
from utils.http.responses.JSONResponse import JSONResponse

from .list_form import UserListGetForm
from .list_manager import UserListManager


filters_name_map = {
    'username': 'username__icontains',
}

read_param_list = set(['count', 'page'])

@view(get=UserListGetForm)
def list_view(request, data: dict):
    filters = { filters_name_map[key]: value for (key, value) in data.items() if key in filters_name_map }

    manager = UserListManager.filter(**filters)

    read_params = { key: data[key] for key in read_param_list if key in data }

    response_data = manager.read(**read_params)

    return JSONResponse(response_data)