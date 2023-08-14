from django.urls import path
from .views import cart_upload
from  .views import cart_list
from .views import cart_detail
from .views import cart_update

urlpatterns =[
    path ("cart/upload/", cart_upload, name = "cart_upload"),
    path("cart/list",cart_list,name ="cart_list"),
    path("cart/<int:id>/",cart_detail, name="cart_detail"),
    path("cart/edit/<int:id>",cart_update, name = "cart_update"),

    
]