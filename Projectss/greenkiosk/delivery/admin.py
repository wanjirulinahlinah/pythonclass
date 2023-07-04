from django.contrib import admin
from .models import Delivery
# Register your models here.
class deliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_number', 'delivery_date','delivery_time','delivery_address','status')
admin.site.register(Delivery,deliveryAdmin)
