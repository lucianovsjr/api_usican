from django.db import models


class CustomOption(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CustomOptionItem(models.Model):
    custom_option = models.ForeignKey(
        CustomOption, related_name="items", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
