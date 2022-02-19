from rest_framework import serializers

from api_usican.misc.serializers import BaseRegisterSerializer
from apps.configurator.models import CustomOptionItem

from .models import Customer, Contact, BudgetRequest


class CustomerSerializer(BaseRegisterSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ContactSerializer(BaseRegisterSerializer):
    customer_name = serializers.CharField(source="customer.name", read_only=True)
    link_redirect = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = "__all__"

    def get_link_redirect(self, obj):
        return f"/customer/{obj.customer.id}/3"


class BudgetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetRequest
        fields = "__all__"

    def validate(self, attrs):
        data = super().validate(attrs)
        open_status = CustomOptionItem.objects.get(pk=4)

        is_status_bulk_update = len(data) <= 2 and bool(data.get("status"))

        if is_status_bulk_update and data.get("status") != self.instance.status:
            decline_status = CustomOptionItem.objects.get(pk=6)
            cancel_status = CustomOptionItem.objects.get(pk=7)

            if data.get("status") == cancel_status:
                if self.instance.status != open_status:
                    raise serializers.ValidationError(
                        {"message": "usican.error.budget_request.bulk_cancel_failure"}
                    )
            elif data.get("status") == open_status:
                if not self.instance.status in (decline_status, cancel_status):
                    raise serializers.ValidationError(
                        {"message": "usican.error.budget_request.bulk_reopen_failure"}
                    )
        else:
            if self.instance.status != open_status:
                raise serializers.ValidationError(
                    {"message": "usican.error.budget_request.edit_without_open_status"}
                )

        return data
