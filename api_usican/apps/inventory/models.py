from django.db import models

from api_usican.misc.models import BaseModel


class ProductType(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    description = models.CharField(max_length=200, blank=False, null=False)
    full_description = models.TextField(blank=True, null=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return f"{self.code} - {self.description[:50]}"
