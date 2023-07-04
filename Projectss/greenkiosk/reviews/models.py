from django.db import models

# Create your models here.

class Review (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    review_content = models.CharField(max_length=20)
    rating = models.IntegerField()
    author = models.CharField(max_length=25)
    created_date = models.DateTimeField(auto_now_add=True)


    