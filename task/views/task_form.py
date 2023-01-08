from django.forms import BooleanField, CharField
from utils.validation.exact_form import ExactForm

from task.models import title_model_constraints, description_model_constraints


class TaskPatchForm(ExactForm):
    title = CharField(max_length=title_model_constraints['max_length'], required=False)
    description = CharField(max_length=description_model_constraints['max_length'], required=False)
    is_done = BooleanField(required=False)