from django.forms import BooleanField, CharField, DateTimeField, IntegerField
from utils.validation.exact_form import ExactForm


class TaskListGetForm(ExactForm):
    # Filters
    title = CharField(required=False)
    is_done = BooleanField(required=False)
    updated_at_gte = DateTimeField(required=False)
    updated_at_lte = DateTimeField(required=False)
    user = CharField(required=False)
    # Pagination
    count = IntegerField(min_value=0, required=False)
    page = IntegerField(min_value=1, required=False)
