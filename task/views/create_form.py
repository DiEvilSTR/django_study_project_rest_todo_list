from django.forms import BooleanField, CharField
from utils.validation.exact_form import ExactForm

from task.models import title_model_constraints, description_model_constraints

title_form_constraints = {
    'max_length': title_model_constraints['max_length'],
}

description_form_constraints = {
    'max_length': description_model_constraints['max_length'],
    'required': False
}


class TaskPostForm(ExactForm):
    title = CharField(**title_form_constraints)
    description = CharField(**description_form_constraints)