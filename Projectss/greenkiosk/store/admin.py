from django.contrib import admin

# Register your models here.
from .models import Store


class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_name','store_location','address','contact_information','email')
admin.site.register(Store ,StoreAdmin)