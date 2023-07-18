from django.db import models



# Create your models here.
class Cart(models.Model):
    product_name = models.CharField(max_length=25)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    date_added = models.DateTimeField
    vendor_id = models.IntegerField()

def __str__(self):
        return self.product_name
