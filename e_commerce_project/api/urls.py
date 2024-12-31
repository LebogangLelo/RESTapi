from django.urls import path
from .views import ProductListCreateView, ProductDetailView, UserListCreateView, UserDetailView, ProductSearchView, OrderListCreateView, CategoryListCreateView, CategoryDetailView 

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
]
