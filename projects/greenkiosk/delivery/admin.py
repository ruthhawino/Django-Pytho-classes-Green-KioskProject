from django.contrib import admin



from .models import Deliver
class DeliverAdmin(admin.ModelAdmin):
    list_display=("recipient_name","address","delivery_date","is_delivered")
admin.site.register(Deliver,DeliverAdmin)

