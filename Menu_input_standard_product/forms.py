from django import forms
from . models import Standard_Product


class Standard_ProductForm(forms.ModelForm):
    class Meta:
        model = Standard_Product
        fields =['nama',
                'standard_sc',
                'standard_ph',
                'standard_appearance',]