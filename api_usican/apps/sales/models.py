from django.db import models

from api_usican.misc.models import BaseModel
from .const import *


class customer(BaseModel):
    legal_entity = models.CharField(
        max_length=1, choices=LEGAL_ENTITY, default=JURIDICAL_PERSON
    )
    identity_number = models.CharField(max_length=14, blank=True, default="")
    name = models.CharField("Nome", max_length=40, blank=False, null=False)
    email = models.EmailField(max_length=30, default="", blank=True)
    phone_number = models.CharField(max_length=14, default="", blank=True)
    phone_number2 = models.CharField(max_length=14, default="", blank=True)

    # address
    cep = models.CharField(max_length=8, default="", blank=True)
    state = models.CharField(
        max_length=2, choices=STATE_CHOICES, default="", blank=True
    )
    city = models.CharField(max_length=40, default="", blank=True)
    public_place = models.CharField(max_length=40, default="", blank=True)
    address_number = models.CharField(max_length=5, default="", blank=True)
    address_complement = models.CharField(max_length=40, default="", blank=True)
    district = models.CharField(max_length=20, default="", blank=True)

    active = models.BooleanField(default=True, blank=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name
