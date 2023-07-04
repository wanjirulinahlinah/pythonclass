from django.db import models

# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
   
    
