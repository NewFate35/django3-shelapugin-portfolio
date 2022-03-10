from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name', 'order_phone', 'order_choice', 'order_dt')
    fields = ('order_name', 'order_phone', 'order_choice')
