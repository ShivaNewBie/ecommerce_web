from unicodedata import decimal
from django.db import models
from PIL import Image 
from ast import Bytes
from io import BytesIO
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True,null=True)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/{self.id}/'
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url