from django.db import models

from api_usican.misc.models import BaseModel, BaseRegisterModel
from .const import *


class Customer(BaseModel):
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


class Contact(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    name = models.CharField("Nome completo", max_length=40, blank=False, null=False)
    position = models.CharField("Cargo", max_length=20, blank=False, null=False)

    email = models.EmailField(max_length=30, default="", blank=True)
    phone_number = models.CharField(max_length=14, default="", blank=True)
    phone_number2 = models.CharField(max_length=14, default="", blank=True)

    active = models.BooleanField(default=True, blank=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return "{0} - {1}".format(self.name, self.cargo)


class BudgetRequest(BaseRegisterModel):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    contact = models.ForeignKey(
        Contact, on_delete=models.PROTECT, blank=True, null=True
    )
    deadline = models.DateField(blank=True, null=True)
    observation = models.TextField(blank=True, default="")
    reason_decline = models.ForeignKey(
        "configurator.CustomOptionItem",
        on_delete=models.PROTECT,
        related_name="budget_request_reason_decline_set",
        blank=True,
        null=True,
    )
    observation_reason = models.TextField(blank=True)
    means_receipt = models.ForeignKey(
        "configurator.CustomOptionItem",
        on_delete=models.PROTECT,
        related_name="budget_request_means_receipt_set",
        blank=True,
        null=True,
    )
    informed_customer_decline = models.BooleanField(default=False)
    status = models.ForeignKey(
        "configurator.CustomOptionItem",
        on_delete=models.PROTECT,
        related_name="budget_request_status_set",
    )
