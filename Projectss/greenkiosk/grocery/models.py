from django.db import models

# Create your models here.


class Grocery(models.Model):
    product_id = models.AutoField(primary_key=True)
    grocery_name = models.CharField(max_length=100)
    description = models.TextField()
    expiry_date = models.DateTimeField()
    stocked_date = models.DateTimeField()
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.grocery_name