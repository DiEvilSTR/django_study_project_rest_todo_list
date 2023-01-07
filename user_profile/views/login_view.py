from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from utils.http.responses.JSONResponse import JSONResponse
from utils.http.constants import HttpMethod, HttpStatus
from utils.http.decorators.views.view import view

from .user_manager import UserManager
from .login_form import LoginPostForm

@csrf_exempt
@view(login_required=False, post=LoginPostForm)
def login_view(request, data):
    if request.method == HttpMethod.POST:
        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return JSONResponse(error='', status=HttpStatus.BAD_REQUEST)
        
        login(request, user)
    
    manager = UserManager.get(username=request.user.username)
    
    response_data = manager.read()

    return JSONResponse(response_data)
