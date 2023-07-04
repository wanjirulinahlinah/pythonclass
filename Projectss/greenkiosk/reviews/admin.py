from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','title','review_content','rating','author','created_date')
admin.site.register(Review ,ReviewAdmin)