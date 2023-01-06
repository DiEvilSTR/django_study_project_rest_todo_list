from django.contrib.auth.models import User

from utils.model.manager.model_set_manager import ModelSetManager


class UserListManager(ModelSetManager):
    model = User
    
    fields = (
        'username',
    )