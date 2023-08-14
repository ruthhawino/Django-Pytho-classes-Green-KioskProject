from django.urls import path
from .views import delivery_upload_view

urlpatterns =[
    path ("delivery/upload/", delivery_upload_view, name = "delivery_upload_view"),
    # path("products/list",products_list_view,name ="products_list_view"),
    # path("products/<int:id>/",product_detail, name="product_detail_view"),
    # path("products/edit/<int:id>", product_update_view, name = "product_update_view"),

    
]