from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 
from django.db.models.signals import post_save, pre_save 
from django.dispatch import receiver

# Custom User Model
class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    

# Category Model 
class Category(models.Model):
     name = models.CharField(max_length=100)
     description = models.TextField(blank=True, null=True)
     created_date = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
         return self.name
    
# Product Model 
class Product(models.Model):
     name = models.CharField(max_length=200)
     description = models.TextField()
     price = models.DecimalField(max_digits=10, decimal_places=2)
     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
     stock_quantity = models.PositiveIntegerField()
     image_url = models.URLField(blank=False, null=False)
     created_date = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
         return self.name
     

     def is_in_stock(self):
        return self.stock_quantity > 0
     

# Product Image Model
class ProductImage(models.Model):
     product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
     image_url = models.URLField()
     
     def __str__(self):
         return f"Image for {self.product.name}"

# Order managemant Model
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.username} for {self.product.name} (Quantity: {self.quantity})"
    
# Pre-save signal to calculate total price 
@receiver(pre_save, sender=Order) 
def calculate_total_price(sender, instance, **kwargs):
    instance.total_price = instance.quantity * instance.product.price
    
 # Post-save signal to reduce stock quantity
@receiver(post_save, sender=Order)
def reduce_stock_quantity(sender, instance, created, **kwargs):
    if created:  # Ensure the logic runs only when a new order is created
        product = instance.product
    if product.stock_quantity >= instance.quantity:
        product.stock_quantity -= instance.quantity
        product.save()
    else:
        raise ValueError("Insufficient stock to complete the order.")
    

    
    


