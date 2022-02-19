from django.db.models.signals import pre_save

from .models import BudgetRequest

from apps.configurator.models import CustomOptionItem


def save_budget_request(sender, instance, **kwargs):
    decline_status = CustomOptionItem.objects.get(pk=6)

    if instance.informed_customer_decline:
        instance.status = decline_status


pre_save.connect(save_budget_request, sender=BudgetRequest)
