from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from company.views import CompanyViewSet
from product.views import ProductViewSet


router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'product', ProductViewSet, basename='product')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/company/
    path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/product/
]
