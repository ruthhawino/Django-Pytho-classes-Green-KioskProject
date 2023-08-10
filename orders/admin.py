from django.contrib import admin

from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display=("quantity","customer_email","order_date","price")
admin.site.register(Order,OrderAdmin)

