
from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('sales_date', 'amount')
    list_filter = ('sales_date',)
    search_fields = ('sales_date',)

    fieldsets = (
        ('Order Information', {
            'fields': ('sales_date', 'amount'),
        }),
    )

