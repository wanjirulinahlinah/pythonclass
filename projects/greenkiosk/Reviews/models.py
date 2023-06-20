from django.db import models

# Create your models here.



class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    comment = models.TextField()
    user_id = models.IntegerField()
    review_date = models.DateField(auto_now_add=True)