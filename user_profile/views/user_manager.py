from django.contrib.auth.models import User

from utils.model.manager.model_manager import ModelManager


class UserManager(ModelManager):
    model = User
    
    fields = (
        'username',
    )