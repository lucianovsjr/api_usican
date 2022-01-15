from rest_framework.permissions import IsAuthenticated

from api_usican.misc.views import BaseModelViewSet

from .models import CustomOption
from .serializers import CsutomOptionSerializer


class CustomOptionView(BaseModelViewSet):
    queryset = CustomOption.objects.all()
    serializer_class = CsutomOptionSerializer
    permission_class = [IsAuthenticated]
    ordering_fields = ["id", "name"]
    filterset_fields = ["name"]
