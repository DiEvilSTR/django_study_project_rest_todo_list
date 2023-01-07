from django.urls import path

from .views.list_view import list_view
from .views.login_view import login_view
from .views.logout_view import logout_view
from .views.details_view import details_view
from .views.signup_view import signup_view


urlpatterns = [
    path('list', list_view, name='user_list'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup_view, name='signup'),
    path('details/<str:pk>', details_view, name='user_details'),
]