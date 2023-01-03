from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from utils.http.responses.JSONResponse import JSONResponse
from utils.http.constants import HttpMethod, HttpStatus
from utils.http.decorators.views.view import view

from .login_form import LoginForm

@csrf_exempt
@view(login_required=False, post=LoginForm)
def login_view(request, data):
    if request.method == HttpMethod.POST:
        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return JSONResponse(error='', status=HttpStatus.BAD_REQUEST)
        
        login(request, user)
    
    user_details = User.objects.values('username').get(username=request.user.username)

    return JSONResponse(user_details)
