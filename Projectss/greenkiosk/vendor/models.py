from django.db import models

# Create your models here.

class Vendor(models.Model):
    contact_number = models.CharField(max_length=20)
    email_address=models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
