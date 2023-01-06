from django.urls import path

from .views.create_view import create_view
from .views.list_view import list_view
from .views.task_view import task_view


urlpatterns = [
    path('create', create_view, name='create_task'),
    path('list', list_view, name='task_list'),
    path('<int:pk>', task_view, name='task'),
]
