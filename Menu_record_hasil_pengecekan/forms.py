from django import forms
from . models import Record_Hasil_Pengecekan

class Record_Hasil_PengecekanForm(forms.ModelForm):
    class Meta:
        model = Record_Hasil_Pengecekan
        fields =['nama',
             'nomor_batch',
             'quantity',
             'supplier',
             'standard_sc',
             'standard_ph',
             'standard_appearance',
             'actual_sc',
             'actual_ph',
             'actual_appearance',
             'status',
    ]