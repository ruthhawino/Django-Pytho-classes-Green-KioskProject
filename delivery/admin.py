from django.contrib import admin



from .models import Delivery
class DeliveryAdmin(admin.ModelAdmin):
    list_display=("recipient_name","address","delivery_date","is_delivered")
admin.site.register(Delivery,DeliveryAdmin)

