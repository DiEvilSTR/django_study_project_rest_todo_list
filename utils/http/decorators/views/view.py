from django.forms import Form

import functools

from utils.http.constants import HttpMethod
from utils.http.responses.JSONResponse import JSONResponse

from .validate_login_required import validate_login_required
from .validate_request_data import validate_request_data
from .validate_request_method import validate_request_method

def view(*, login_required=True, delete:Form=None, get:Form=None, patch:Form=None, post:Form=None, put:Form=None):
    methods_forms = {
        HttpMethod.DELETE: delete,
        HttpMethod.GET: get,
        HttpMethod.PATCH: patch,
        HttpMethod.POST: post,
        HttpMethod.PUT: put,
    }

    def view_decorator(func):
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            ValidationForm = methods_forms.get(request.method)

            method_validation_result = validate_request_method(ValidationForm)
            if isinstance(method_validation_result, JSONResponse):
                return method_validation_result

            login_validation_result = validate_login_required(request, login_required)
            if isinstance(login_validation_result, JSONResponse):
                return login_validation_result

            data_validation_result = validate_request_data(request, ValidationForm)
            if isinstance(data_validation_result, JSONResponse):
                return data_validation_result

            mixed_kwargs = { **kwargs }
            if not (data_validation_result is None):
                mixed_kwargs['data'] = data_validation_result

            return func(request, *args, **mixed_kwargs)
        return wrapper
    return view_decorator