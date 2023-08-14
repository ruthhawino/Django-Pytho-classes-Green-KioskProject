from django.shortcuts import render 
from .forms import DeliveryUploadForm
from delivery.models import Delivery

def delivery_upload_view(request):
    form = DeliveryUploadForm()
    return render(request,"delivery/delivery_upload.html", {"form":form})

# def products_list_view(request):
#     products = Product.objects.all()
#     return render(request,"inventory/products_list.html",{"products":products})


# def product_detail(request,id):
#     product = Product.objects.get(id=id)
#     return render(request,"inventory/product_details.html", {"product":product})

# def product_update_view(request, id):
#     product = Product.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProductUploadForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect("product_detail_view", id=product.id)

#     else:
#         form =ProductUploadForm(instance=product)
#         return render(request, "inventory/edit_product.html", {'form': form})




