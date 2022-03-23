from django.contrib.auth.models import Permission

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


class PermissionSerializer(serializers.ModelSerializer):
    content_type__model = serializers.CharField(source="content_type.model")

    class Meta:
        model = Permission
        fields = ["id", "codename", "content_type__model"]
