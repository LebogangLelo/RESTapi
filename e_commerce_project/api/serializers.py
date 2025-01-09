from rest_framework import serializers
from .models import Product, User, Order, Category, ProductImage
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProductImageSerializer(serializers.ModelSerializer):
     class Meta:
         model = ProductImage
         fields = ['image_url']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        price = data.get('price', 0)
        stock_quantity = data.get('stock_quantity', 0)
        if price <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        if stock_quantity < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'quantity', 'created_date']

    def validate(self, data):
        product = data['product']
        if data['quantity'] <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero")
        if data['quantity'] > product.stock_quantity:
            raise serializers.ValidationError("Insufficient stock available.")
        return data


