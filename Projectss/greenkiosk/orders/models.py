from django.db import models

from customer.models  import Customer
from cart.models import Cart
from delivery.models import Delivery

# Create your models here.
class Orders(models.Model):

    customer=models.OneToOneField(Customer , null=True, on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, null=True , on_delete=models.CASCADE)
    delivery=models.ManyToManyField(Delivery)

    order_id = models.IntegerField()
    order_date = models.DateTimeField()
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=36)