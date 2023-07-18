from django.contrib import admin
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display=("contact_number","email_address","created_on","updated_on")
admin.site.register(Vendor,VendorAdmin)

 