from django import forms
from vendor.models import Vendor

class VendorUploadForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'