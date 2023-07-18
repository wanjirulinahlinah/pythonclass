from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    customer_Name = models.CharField(max_length=32)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
   
    
    def __str__(self) :
        return self.customer_Name
