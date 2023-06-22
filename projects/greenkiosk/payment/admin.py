from django.contrib import admin


from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display=("payment_date","payment_method")
admin.site.register(Payment,PaymentAdmin)

