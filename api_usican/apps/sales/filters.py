import django_filters

from .models import Customer, Contact


class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = "__all__"


class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = "__all__"
