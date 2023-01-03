from django.urls import path

from .views.delete_view import delete_view
from .views.login_view import login_view
from .views.logout_view import logout_view
from .views.user_details_view import user_details_view
from .views.signup_view import signup_view


urlpatterns = [
    path('delete', delete_view, name='delete'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('details/<str:pk>', user_details_view, name='details'),
    path('signup', signup_view, name='signup'),
]