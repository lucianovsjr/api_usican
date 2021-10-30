from django.db import models

from api_usican.misc.models import BaseModel


class ProductType(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    code = models.CharField(max_length=11, blank=True, null=False)
    description = models.TextField(blank=False, null=False)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return f"{self.code} - {self.description[:50]}"
