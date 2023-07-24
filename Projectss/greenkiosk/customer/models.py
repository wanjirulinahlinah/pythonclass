from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_Name = models.CharField(max_length=32)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
   
    
    def __str__(self) :
        return self.customer_Name
