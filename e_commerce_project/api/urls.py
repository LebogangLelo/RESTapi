from django.urls import path
from .views import UserCreateView, ProductDetailView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
