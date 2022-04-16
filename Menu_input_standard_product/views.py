from django.shortcuts import render
from . forms import Standard_ProductForm
from . models import Standard_Product
# Create your views here.

def index(request):
    Form = Standard_ProductForm()
    if request.method=="POST":
        Standard_Product.objects.create(
            nama = request.POST.get('nama'),
            standard_sc = request.POST.get('standard_sc'),
            standard_ph = request.POST.get('standard_ph'),
            standard_appearance = request.POST.get('standard_appearance'),
        )
        
    context ={
        'form':Form,
        'title':'standard product',
        'body':'standard product',
        'nav':[['/','Menu Utama'],
              ['/Menu_input_standard_product','Menu Standard Product'],
              ['/Menu_kedatangan_product','Menu Kedatangan Product'],
              ['/Menu_login','Menu Login'],
              ['/Menu_record_hasil_pengecekan','Menu Record Hasil Pengecekan'],
        
        ],
    }
    return render(request, 'index.html',context)