from django.contrib import admin
from .models import Product

# Register your models here.
class ProductsAdmin (admin.ModelAdmin):
    list_display=("name","stock","price","data_created")
admin.site.register(Product,ProductsAdmin)
