from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api_usican.misc.views import BaseModelViewSet
from .models import customer
from .serializers import customerSerializer


class customerView(BaseModelViewSet):
    queryset = customer.objects.all()
    serializer_class = customerSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "name"]
