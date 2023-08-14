from django.urls import path
from .views import payment_upload

urlpatterns =[
    path ("delivery/upload/", payment_upload, name = "payment_upload"),
    # path("products/list",products_list_view,name ="products_list_view"),
    # path("products/<int:id>/",product_detail, name="product_detail_view"),
    # path("products/edit/<int:id>", product_update_view, name = "product_update_view"),

    
]