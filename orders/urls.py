from django.urls import path
from .views import Order_upload_view


urlpatterns =[
    path ("orders/upload/", Order_upload_view, name = "Order_uploadview"),
   
    
]