
    
from django.contrib import admin
from .models import Stock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')
    search_fields = ('name',) 