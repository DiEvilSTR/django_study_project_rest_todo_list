from django.contrib.auth.models import User
from django.db import models


title_model_constraints = {
    'max_length': 42,
}

description_model_constraints = {
    'max_length': 500,
    'blank': True,
}

is_done_model_constraints = {
    'default': False,
}

user_model_constraints = {
    'on_delete': models.CASCADE,
}

class Task(models.Model):
    title = models.CharField(**title_model_constraints)
    description = models.TextField(**description_model_constraints)
    is_done = models.BooleanField(**is_done_model_constraints)
    user = models.ForeignKey(User, **user_model_constraints)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title