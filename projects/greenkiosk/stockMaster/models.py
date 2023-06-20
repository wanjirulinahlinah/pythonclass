from django.db import models

# Create your models here.
from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    def purchase_order(self, quantity):
        self.quantity += quantity
        self.save()

    def remove_stock(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            self.save()
        else:
            raise ValueError("Insufficient stock")

    def check_stock_level(self):
        return self.quantity

    def check_availability(self, quantity):
        return self.quantity >= quantity