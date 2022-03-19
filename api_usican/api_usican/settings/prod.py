from .base import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "usican",
        "USER": "sa_usican",
        "PASSWORD": "7X.+TXfvgz@K_",
        "HOST": "db",
        "PORT": "5432",
    }
}
