from django.shortcuts import render
from .forms import VendorUploadForm
from.models import Vendor

def vendor_upload_view(request):
    # vendors=Vendor.objects.all()
    form = VendorUploadForm()
    return render(request,"vendor/vendor_upload.html", {"form":form})