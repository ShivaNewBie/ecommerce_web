from django.db import models
from django.contrib.auth.models import User 

from product.models import Product 


class Checkout(models.Model):
    created_by = models.ForeignKey(User,related_name='checkout', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    pay = models.DecimalField(max_digits=8, decimal_places=2, blank=True,null=True)
    stripe_token = models.CharField(max_length=100)

    class Meta: 
        ordering = ['-created_at']
    
    def __str__(self):
        return self.first_name 

class CheckoutItem(models.Model):
    order = models.ForeignKey(Checkout, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)