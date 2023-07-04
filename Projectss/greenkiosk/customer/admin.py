from django.contrib import admin
from .models import Customer
# Register your models here.# Regster your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_Name', 'email_address', 'phone_number',"address")
admin.site.register(Customer,CustomerAdmin)

