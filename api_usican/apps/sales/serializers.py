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

        if self.instance.status != open_status:
            raise serializers.ValidationError(
                {"message": "usican.error.budget_request.edit_without_open_status"}
            )

        return data
