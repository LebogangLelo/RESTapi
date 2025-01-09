from rest_framework import generics, permissions, filters, status
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, User, Order, Category, ProductImage
from django.contrib.auth import get_user_model
from .serializers import ProductSerializer, UserSerializer, OrderSerializer, CategorySerializer
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAdminUser, IsSelfOrAdmin

def home(request):
    return HttpResponse("Welcome to the E_Commerce platform API!")


User = get_user_model()


class CustomAuthToken(ObtainAuthToken):
     def post(self, request, *args, **kwargs):
         serializer = self.serializer_class(data=request.data, context={'request': request})
         serializer.is_valid(raise_exception=True)
         user = serializer.validated_data['user']
         token, created = Token.objects.get_or_create(user=user)
         return Response({ 
             'token': token.key, 
             'user_id': user.pk, 
             'email': user.email 
         })

# User Management Views
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': serializer.data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer
     
     def get_permissions(self):
         if self.request.method in ['GET', 'PUT', 'DELETE']:
             return [IsSelfOrAdmin()] 
         return [permissions.IsAuthenticated] 

# Category Management Views
class CategoryListCreateView(generics.ListCreateAPIView):
     queryset = Category.objects.all() 
     serializer_class = CategorySerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     search_fields = ['name'] 
     filterset_fields = ['name', 'created_date']
     
     def get_permissions(self):
         if self.request.method == 'POST': 
            return [IsAdminUser()] 
         return [IsAuthenticatedOrReadOnly()]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Product Management Views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'category']

                 # restrict product creation to admin users only while letting authenticated users view products
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]


    def create(self, request, *args, **kwargs):
         data = request.data
         product_serializer = self.get_serializer(data=data)
         product_serializer.is_valid(raise_exception=True)
         product = product_serializer.save()
         images_data = data.get('images')

         if images_data:
             for image_data in images_data:
                 ProductImage.objects.create(product=product, **image_data) 
                 
         headers = self.get_success_headers(product_serializer.data)
         return Response(product_serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
         if self.request.method == 'DELETE':
             return [IsAdminUser()]
         return [IsAuthenticated]

    def update(self, request, *args, **kwargs):
         partial = kwargs.pop('partial', False)
         instance = self.get_object()
         product_serializer = self.get_serializer(instance, data=request.data, partial=partial)
         product_serializer.is_valid(raise_exception=True)
         self.perform_update(product_serializer)
         images_data = request.data.get('images') 
         
         if images_data:
             ProductImage.objects.filter(product=instance).delete() 
             for image_data in images_data:
                 ProductImage.objects.create(product=instance, **image_data)
                 
         return Response(product_serializer.data)
    
    def delete(self, request, *args, **kwargs):
         instance = self.get_object()
         instance.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

# Product Search and Filtering
class ProductSearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'category']
    filterset_fields = ['category', 'price', 'stock_quantity']


# Order managent 
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


