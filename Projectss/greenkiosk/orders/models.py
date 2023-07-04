from django.db import models

# Create your models here.
class Orders(models.Model):
    order_id = models.IntegerField()
    order_date = models.DateTimeField()
    order_total = models.DecimalField(max_digits=10,decimal_places=2)
    order_status = models.CharField(max_length=36)