from django.forms import CharField, IntegerField

from utils.validation.exact_form import ExactForm


class UserListGetForm(ExactForm):
    # Filters
    username = CharField(required=False)
    # Pagination
    count = IntegerField(min_value=0, required=False)
    page = IntegerField(min_value=1, required=False)
