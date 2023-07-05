from django.contrib import admin

from .models import Product, Review

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    # Customize other options or fields if needed

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'product', 'date_added')
    list_filter = ('product', 'date_added')
    search_fields = ('title', 'body', 'user__username', 'product__name')
    # Customize other options or fields if needed
