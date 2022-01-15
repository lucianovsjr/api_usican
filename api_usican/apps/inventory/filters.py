from django_filters import rest_framework as filters

from .models import ProductType, Product


class ProductTypeFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    description = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = ProductType
        fields = ["name", "description", "active"]


class ProductFilter(filters.FilterSet):
    description = filters.CharFilter(lookup_expr="icontains")
    full_description = filters.CharFilter(lookup_expr="icontains")
    product_type = filters.ModelMultipleChoiceFilter(queryset=ProductType.objects.all())

    class Meta:
        model = Product
        fields = ["description", "full_description", "product_type", "active"]
