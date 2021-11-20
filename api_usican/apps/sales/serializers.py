from rest_framework.serializers import ModelSerializer

from .models import Customer, Contact


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
