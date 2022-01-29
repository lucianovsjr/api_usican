from rest_framework import serializers

from .models import CustomOption, CustomOptionItem


class CsutomOptionSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = CustomOption
        fields = ["name", "items"]


class CsutomOptionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomOptionItem
        fields = ["id", "name"]
