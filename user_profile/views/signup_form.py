from django.forms import CharField
from utils.validation.exact_form import ExactForm

username_constraints = {}
password_constraints = {}


class SignupForm(ExactForm):
    username = CharField(**username_constraints)
    password = CharField(**password_constraints)