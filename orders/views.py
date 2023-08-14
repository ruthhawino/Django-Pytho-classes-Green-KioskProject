from django.shortcuts import render ,redirect
from .forms import OrderUploadForm
from orders.models import Order

def Order_upload_view(request):
    form = OrderUploadForm()
    return render(request,"orders/Order_upload.html", {"form":form})
