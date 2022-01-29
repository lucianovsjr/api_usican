from rest_framework import serializers

from .models import Customer, Contact, BudgetRequest


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
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
