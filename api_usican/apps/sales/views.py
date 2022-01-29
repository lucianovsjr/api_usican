from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api_usican.misc.views import BaseModelViewSet
from .models import Customer, Contact, BudgetRequest
from .serializers import CustomerSerializer, ContactSerializer, BudgetRequestSerializer
from .filters import CustomerFilter, ContactFilter, BudgetRequestFilter


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


class BudgetRequestView(BaseModelViewSet):
    queryset = BudgetRequest.objects.all()
    serializer_class = BudgetRequestSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id"]
    filterset_class = BudgetRequestFilter
