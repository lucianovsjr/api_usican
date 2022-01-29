from django_filters import rest_framework as filters

from .models import Customer, Contact, BudgetRequest


class CustomerFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    email = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Customer
        fields = ["name", "email", "active"]


class ContactFilter(filters.FilterSet):
    class Meta:
        model = Contact
        fields = ["customer"]


class BudgetRequestFilter(filters.FilterSet):
    deadline__gt = filters.DateFilter(field_name="deadline", lookup_expr="gt")
    deadline__lt = filters.DateFilter(field_name="deadline", lookup_expr="lt")

    class Meta:
        model = BudgetRequest
        fields = [
            "customer",
            "status",
            "informed_customer_decline",
            "deadline__gt",
            "deadline__lt",
        ]
