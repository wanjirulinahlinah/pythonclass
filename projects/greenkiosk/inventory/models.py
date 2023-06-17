from django.db import models

class Product(models.Model):
    name = models.CharField (max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.TextField()
    image = models.ImageField()
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    

# Create your models here.
