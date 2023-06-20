from django.contrib import admin

# Register your models here.


from .models import SalesRecord, Order

admin.site.register(SalesRecord)
admin.site.register(Order)
