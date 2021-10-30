from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import ProductType, Product
from .serializers import ProductTypeSerializer, ProductSerializer

from api_usican.misc.views import BaseModelViewSet


class ProductTypeView(BaseModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "name"]


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["id", "code"]
