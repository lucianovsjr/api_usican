from django.db import models


class Client(models.Model):
    name = models.CharField("Nome", max_length=50, blank=False, null=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name
