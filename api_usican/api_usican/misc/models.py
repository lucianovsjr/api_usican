from django.db import models

from api_usican.misc.mixin import camel_to_snake


class BaseModel(models.Model):
    def get_app(self):
        return self.__class__.__module__.split(".")[1].upper()

    def get_model(self):
        return camel_to_snake(self.__class__.__name__).upper()

    class Meta:
        abstract = True
