from django.forms import BooleanField, CharField
from utils.validation.exact_form import ExactForm

from task.models import title_model_constraints, description_model_constraints


class TaskPostForm(ExactForm):
    title = CharField(max_length=title_model_constraints['max_length'])
    description = CharField(max_length=description_model_constraints['max_length'], required=False)