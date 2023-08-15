
from django.urls import path
from .views import product_upload_view
from  .views import products_list_view
from .views import product_detail
from .views import product_update_view

urlpatterns =[
    path ("products/upload/", product_upload_view, name = "product_uploadview"),
    path("products/list",products_list_view,name ="products_list_view"),
    path("products/<int:id>/",product_detail, name="product_detail_view"),
    path("products/edit/<int:id>", product_update_view, name = "product_update_view"),

    
]




















# from django.urls import path
# from .views import product_upload
# from  .views import products_list
# from .views import product_detail
# from .views import product_update

# urlpatterns =[
#     path ("products/upload/", product_upload, name = "product_upload"),
#     path("products/list",products_list,name ="products_list"),
#     path("products/<int:id>/",product_detail, name="product_detail"),
#     path("products/edit/<int:id>", product_update, name = "product_update"),

    
# ]