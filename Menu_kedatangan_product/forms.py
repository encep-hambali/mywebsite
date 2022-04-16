from django  import forms
from .models import Kedatangan_Product

class Kedatangan_ProductForm(forms.ModelForm):
    class Meta:
        model = Kedatangan_Product
        fields =['nama',
             'nomor_batch',
             'quantity',
             'supplier',
             ]