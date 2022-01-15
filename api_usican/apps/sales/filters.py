from django_filters import rest_framework as filters

from .models import Customer


class CustomerFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    email = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Customer
        fields = ["name", "email", "active"]
