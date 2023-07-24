from django.db import models


# Create your models here.
class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    contact_number = models.CharField(max_length=20)
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    delivery_address = models.CharField(max_length=20)
    status = models.CharField(max_length=25)
    