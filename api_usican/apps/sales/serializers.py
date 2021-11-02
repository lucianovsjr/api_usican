from rest_framework.serializers import ModelSerializer

from .models import customer


class customerSerializer(ModelSerializer):
    class Meta:
        model = customer
        fields = "__all__"
