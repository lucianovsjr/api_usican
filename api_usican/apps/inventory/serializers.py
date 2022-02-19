from api_usican.misc.serializers import BaseRegisterSerializer

from .models import ProductType, Product


class ProductTypeSerializer(BaseRegisterSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"


class ProductSerializer(BaseRegisterSerializer):
    class Meta:
        model = Product
        fields = "__all__"
