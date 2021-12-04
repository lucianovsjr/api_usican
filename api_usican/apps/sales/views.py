from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api_usican.misc.views import BaseModelViewSet
from .models import Customer, Contact
from .serializers import CustomerSerializer, ContactSerializer
from .filters import CustomerFilter, ContactFilter


class CustomerView(BaseModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "name"]
    filterset_class = CustomerFilter


class ContactView(BaseModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "name"]
    filterset_class = ContactFilter
