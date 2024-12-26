from django.urls import path
from .views import UserViewSet, ProductViewSet

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]


# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Add routes for obtaining abd refreshing tokens
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


from django.urls import path
from .views import ProductSearchView

urlpatterns = [
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
]
