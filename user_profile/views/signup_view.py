from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from utils.http.responses.JSONResponse import JSONResponse
from utils.http.constants import HttpStatus
from utils.http.decorators.views.view import view

from .signup_form import SignupPostForm
from .user_manager import UserManager


@csrf_exempt
@view(login_required=False, post=SignupPostForm)
def signup_view(request, data):
    username = data['username']
    password = data['password']

    if User.objects.filter(username=username).exists():
        return JSONResponse(error='', status=HttpStatus.BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password)
    user.save()

    # Log user in
    user_login = authenticate(username=username, password=password)
    login(request, user_login)

    manager = UserManager.get(username=request.user.username)

    response_data = manager.read()

    return JSONResponse(response_data)