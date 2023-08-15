from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("amount","currency","date")

if Payment not in admin.site._registry:
    admin.site.register(Payment, PaymentAdmin)
