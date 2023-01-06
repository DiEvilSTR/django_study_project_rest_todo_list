from django.forms import CharField
from utils.validation.exact_form import ExactForm

username_constraints = {}
password_constraints = {}


class SignupPostForm(ExactForm):
    username = CharField(**username_constraints)
    password = CharField(**password_constraints)