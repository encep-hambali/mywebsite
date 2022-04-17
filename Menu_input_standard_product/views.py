from django.shortcuts import render, HttpResponseRedirect
from . forms import Standard_ProductForm
from . models import Standard_Product
# Create your views here.

def index(request):
    tabel_standard = Standard_Product.objects.all()
    Form = Standard_ProductForm(request.POST or None)
    if request.method=="POST":
        if Form.is_valid():
            Form.save()
        return HttpResponseRedirect('/Menu_input_standard_product')
        
    context ={
        'tabel_standard':tabel_standard,
        'form':Form,
        'title':'standard product',
        'body':'standard product',
        'nav':[['/', 'fa fa-desktop','Dashbrod'],
              ['/Menu_input_standard_product','fa fa-cogs','Standard Product'],
              ['/Menu_kedatangan_product','fa fa-table','Kedatangan Product'],
              ['/Menu_login','fa fa-th','Login'],
              ['/Menu_record_hasil_pengecekan','fa fa-info-circle','Hasil Pengecekan'],

        ],
    }
    return render(request, 'side.html',context)