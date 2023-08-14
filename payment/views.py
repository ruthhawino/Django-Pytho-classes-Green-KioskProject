from django.shortcuts import render

from .forms import PaymentUploadForm
from payment.models import Payment

def payment_upload(request):
    form = PaymentUploadForm()
    return render(request,"payment/payment_upload.html", {"form":form})

