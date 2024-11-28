from django.contrib import admin
from .models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'book']
    search_fields = ['name', 'phone_number', 'email']
    list_filter = ['book']