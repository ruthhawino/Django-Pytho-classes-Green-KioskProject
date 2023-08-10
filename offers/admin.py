
from django.contrib import admin
from .models import Product, Offer

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')
    list_per_page = 20

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'discount_percentage', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'product__name')
    list_per_page = 20
