from django.contrib import admin

from .models import Receipt

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'amount', 'transaction_id', 'payment_method')
    search_fields = ('id', 'transaction_id')
    list_filter = ('created', 'payment_method')
    date_hierarchy = 'created'
    list_per_page = 20
