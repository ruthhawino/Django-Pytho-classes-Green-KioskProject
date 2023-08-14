from django.urls import path;
from .views import customer_details
from .views import customer_upload
from  .views import customer_list


urlpatterns=[
path("customer/<int:id>/",customer_details, name="customer_detail"),
path ("customer/upload/", customer_upload, name = "customer_upload"),
    path("customer/list",customer_list,name ="customer_list"),
]

