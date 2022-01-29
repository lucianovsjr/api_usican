from rest_framework.permissions import IsAuthenticated

from api_usican.misc.views import BaseModelViewSet

from .models import CustomOption, CustomOptionItem
from .serializers import CsutomOptionSerializer, CsutomOptionItemSerializer


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
    ordering_fields = ["id"]
    filterset_fields = ["custom_option__name"]
