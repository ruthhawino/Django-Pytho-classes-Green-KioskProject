from django.contrib import admin


from .models import Cart
class CartAdmin(admin.ModelAdmin):
    list_display=("item_id","item_name","price","quantity","total_price","date_added","product_image")
admin.site.register(Cart,CartAdmin)

