from django.shortcuts import render
from .forms import VendorUploadForm
from vendor.models import Vendor

def vendor_upload_view(request):
    form = VendorUploadForm()
    return render(request,"vendor/vendor_upload.html", {"form":form})