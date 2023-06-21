from django.db import models

# Create your models here.


class Order(models.Model):
    sales_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

