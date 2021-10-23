from rest_framework.serializers import ModelSerializer

from .models import customer


class customerSerializer(ModelSerializer):
    class Meta:
        model = customer
        fields = [
            "id",
            "legal_entity",
            "identity_number",
            "name",
            "email",
            "phone_number",
            "phone_number2",
            "state",
            "city",
            "cep",
            "public_place",
            "address_number",
            "address_complement",
            "district",
            "active",
        ]
