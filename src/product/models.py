from unicodedata import decimal
from django.db import models
from PIL import Image 
from ast import Bytes
from io import BytesIO
from django.contrib.auth.models import User 
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/{self.slug}/'
class Product(models.Model):

    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE) 
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    modified_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.id}/'
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url