from django.contrib import admin

# Register your models here.

from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ("product_name","product_price","product_quantity","date_added","vendor_id")
admin.site.register(Cart,CartAdmin)