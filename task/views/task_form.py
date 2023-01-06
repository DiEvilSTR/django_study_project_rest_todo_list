from django.forms import BooleanField, CharField
from utils.validation.exact_form import ExactForm

from task.models import title_model_constraints, description_model_constraints

title_form_constraints = {
    'max_length': title_model_constraints['max_length'],
    'required': False
}

description_form_constraints = { 
    'max_length': description_model_constraints['max_length'],
    'required': False
}

is_done_form_constraints = {
    'required': False
}


class TaskPatchForm(ExactForm):
    title = CharField(**title_form_constraints)
    description = CharField(**description_form_constraints)
    is_done = BooleanField(**is_done_form_constraints)