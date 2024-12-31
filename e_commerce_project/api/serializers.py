from rest_framework import serializers
from .models import Product, User, Order, Category
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

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        if data.get('price') <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        if data.get('stock_quantity') < 0:
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
        if data['quantity'] > product.stock_quantity:
            raise serializers.ValidationError("Insufficient stock available.")
        return data


