from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api_usican.misc.views import BaseModelViewSet
from .models import Customer
from .serializers import CustomerSerializer


class CustomerView(BaseModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "name"]
