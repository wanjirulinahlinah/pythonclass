from django.db import models

# Create your models here.
from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
