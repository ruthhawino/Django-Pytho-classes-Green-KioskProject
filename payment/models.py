from django.db import models

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    date = models.DateTimeField(auto_now=True)
    method = models.CharField(max_length=10)
    customer = models.ForeignKey('customer.customer', on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)

    def customer_name(self):
        return self.customer.name

    def is_valid(self):
        if self.amount > 0 and self.currency and self.method and self.customer and self.order:
            return True
        else:
            return False

from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'amount', 'payment_status', 'order_status', 'payment_method')
    list_filter = ('currency', 'method')  

    def customer_name(self, obj):
        return obj.customer_name()  

    def payment_status(self, obj):
        return obj.status  

    def order_status(self, obj):
        return obj.order.status  

    def payment_method(self, obj):
        return obj.method

admin.site.register(Payment, PaymentAdmin)