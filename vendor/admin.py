from django.contrib import admin
from .models import Vendor



# Register your models here.
class Vendor_admin(admin.ModelAdmin):
  list_display=('first_name','last_name','email','Password','date_updated')
admin.site.register(Vendor ,Vendor_admin)