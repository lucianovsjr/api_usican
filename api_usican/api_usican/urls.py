from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.sales.views import CustomerView, ContactView, BudgetRequestView
from apps.inventory.views import ProductTypeView, ProductView
from apps.configurator.views import CustomOptionView, CustomOptionItemView


router = DefaultRouter()
router.register("customer", CustomerView)
router.register("contact", ContactView)
router.register("budget_request", BudgetRequestView)
router.register("product_type", ProductTypeView)
router.register("product", ProductView)
router.register("custom_option", CustomOptionView)
router.register("custom_option_item", CustomOptionItemView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
