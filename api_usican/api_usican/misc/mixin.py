import re

from api_usican.misc.const_error import ERROR


def camel_to_snake(name):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def get_error_message(instance, code):
    return ERROR[instance.get_app()][instance.get_model()][code.upper()]
