from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.sales.views import CustomerView, ContactView
from apps.inventory.views import ProductTypeView, ProductView
from apps.configurator.views import CustomOptionView


router = DefaultRouter()
router.register("customer", CustomerView)
router.register("contact", ContactView)
router.register("product_type", ProductTypeView)
router.register("product", ProductView)
router.register("custom_option", CustomOptionView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
