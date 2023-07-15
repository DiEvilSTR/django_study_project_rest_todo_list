from django.http import QueryDict
from django.http.multipartparser import MultiPartParser

from utils.http.constants import HttpMethod, HttpStatus
from utils.http.responses.JSONResponse import JSONResponse


def validate_request_data(request, Form):
    if request.method == HttpMethod.GET:
        query_dict = request.GET
        multi_value_dict = QueryDict()
        form = Form(query_dict)

    elif request.method == HttpMethod.POST:
        query_dict = request.POST
        multi_value_dict = request.FILES
        form = Form(query_dict, multi_value_dict)

    elif request.method == HttpMethod.DELETE:
        query_dict = QueryDict(request.body)
        multi_value_dict = QueryDict()
        form = Form(query_dict, multi_value_dict)

    else:
        query_dict, multi_value_dict = MultiPartParser(request.META, request, request.upload_handlers).parse()
        form = Form(query_dict)

    if not form.is_valid():
        return JSONResponse(error=form.errors, status=HttpStatus.BAD_REQUEST)
    
    changed_data = None

    if len(form.fields):
        changed_data = { key: form.cleaned_data[key] for key in form.data.keys() }

    # TODO: Test file validation

    return changed_data