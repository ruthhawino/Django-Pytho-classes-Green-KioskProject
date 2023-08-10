from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "total_amount", "payment_status", "order_status", "payment_method")

if Payment not in admin.site._registry:
    admin.site.register(Payment, PaymentAdmin)
