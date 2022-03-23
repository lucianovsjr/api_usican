from django.contrib.auth.models import Permission

from rest_framework.permissions import IsAuthenticated

from api_usican.misc.views import BaseModelViewSet

from .models import CustomOption, CustomOptionItem
from .serializers import (
    CsutomOptionSerializer,
    CsutomOptionItemSerializer,
    PermissionSerializer,
)

CONTENT_TYPE_LOG_ENTRY = 1
CONTENT_TYPE_PERMISSION = 2
CONTENT_TYPE_GROUP = 3
CONTENT_TYPE_USER = 4
CONTENT_TYPE_CONTENT_TYPE = 5
CONTENT_TYPE_SESSION = 6
CONTENT_TYPE_CUSTOM_OPTION = 12
CONTENT_TYPE_CUSTOM_OPTION_ITEM = 13


class CustomOptionView(BaseModelViewSet):
    queryset = CustomOption.objects.all()
    serializer_class = CsutomOptionSerializer
    permission_class = [IsAuthenticated]
    ordering_fields = ["id", "name"]
    filterset_fields = ["name"]


class CustomOptionItemView(BaseModelViewSet):
    queryset = CustomOptionItem.objects.all()
    serializer_class = CsutomOptionItemSerializer
    permission_class = [IsAuthenticated]
    ordering_fields = ["id", "name"]
    filterset_fields = ["custom_option__name"]


class PermissionView(BaseModelViewSet):
    queryset = Permission.objects.exclude(
        content_type__in=(
            CONTENT_TYPE_LOG_ENTRY,
            CONTENT_TYPE_PERMISSION,
            CONTENT_TYPE_GROUP,
            CONTENT_TYPE_USER,
            CONTENT_TYPE_CONTENT_TYPE,
            CONTENT_TYPE_SESSION,
            CONTENT_TYPE_CUSTOM_OPTION,
            CONTENT_TYPE_CUSTOM_OPTION_ITEM,
        )
    )
    serializer_class = PermissionSerializer
    permission_class = [IsAuthenticated]
    ordering_fields = ["id", "codename", "content_type__model"]
    filterset_fields = ["name", "codename", "content_type__model"]
