from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api_usican.misc.views import BaseModelViewSet

from .models import ProductType, Product
from .serializers import ProductTypeSerializer, ProductSerializer
from .filters import ProductTypeFilter, ProductFilter


class ProductTypeView(BaseModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "name"]
    filterset_class = ProductTypeFilter


class ProductView(BaseModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "code"]
    filterset_class = ProductFilter
