from django.contrib import admin

# Register your models here.
from .models import Orders
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("order_id","order_date","order_total","order_status")
admin.site.register(Orders,OrdersAdmin)