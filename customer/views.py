from django.shortcuts import render
from customer.models import Customer

from  .forms import CustomerUploadForm

def customer_upload(request):
    form = CustomerUploadForm()
    return render(request,"customer/customer_upload.html", {"form":form})

def customer_list(request):
    Customer = Customer.objects.all()
    return render(request,"customer/customer_list.html",{"customer":Customer})




def customer_details(request,id):
    product = customer_details.objects.get(id=id)
    return render(request,"customer/customer_details.html", {"customer":Customer})
