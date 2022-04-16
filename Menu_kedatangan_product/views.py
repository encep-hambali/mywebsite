from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from . forms import Kedatangan_ProductForm
from . models import Kedatangan_Product
from Menu_input_standard_product.models import Standard_Product

# Create your views here.

def index(request):
    
    Form = Kedatangan_ProductForm(request.POST or None)
    if request.method=="POST":
        if Form.is_valid():
            Form.save()
        return HttpResponseRedirect('/Menu_kedatangan_product')

    context ={
        'form':Form,
        'title':'kedatangan product',
        'body':'kedatangan product',
        'nav':[['/','Menu Utama'],
              ['/Menu_input_standard_product','Menu Standard Product'],
              ['/Menu_kedatangan_product','Menu Kedatangan Product'],
              ['/Menu_login','Menu Login'],
              ['/Menu_record_hasil_pengecekan','Menu Record Hasil Pengecekan'],
        
        ],
    }
    return render(request, 'index.html',context)