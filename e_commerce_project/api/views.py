from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import User, Product
from .serializers import UserSerializer, ProductSerializer

def home(request):
    return HttpResponse("Welcome to the E_Commerce platform API!")

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




