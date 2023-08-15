from django import forms
from .models import Product

class ProductUploadForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = "__all__"






















# from django import forms
# from inventory.models import Product

# class ProductUploadForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'