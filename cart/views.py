from django.shortcuts import render ,redirect
from .forms import CartUploadForm
from .models import Cart

def cart_upload(request):
    form = CartUploadForm()
    return render(request,"cart/cart_upload.html", {"form":form})

def cart_list(request):
    products = Cart.objects.all()
    return render(request,"cart/cart_list.html",{"cart":Cart})


def cart_detail(request,id):
    product = Cart.objects.get(id=id)
    return render(request,"cart/cart_details.html", {"cart":Cart})

def cart_update(request, id):
    Cart = Cart.objects.get(id=id)
    if request.method == 'POST':
        form = CartUploadForm(request.POST, instance=Cart)
        if form.is_valid():
            form.save()
            return redirect("cart_detail", id=Cart.id)

    else:
        form =CartUploadForm(instance=Cart)
        return render(request, "cart/edit_cart.html", {'form': form})




