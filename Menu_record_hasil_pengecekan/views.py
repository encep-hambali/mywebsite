from django.shortcuts import render, HttpResponseRedirect
from . forms import Record_Hasil_PengecekanForm
from . models import Record_Hasil_Pengecekan
# Create your views here.

def index(request):
    Form = Record_Hasil_PengecekanForm(request.POST or None)
    if request.method=="POST":
        if Form.is_valid():
            Form.save()
            
        return HttpResponseRedirect('/Menu_record_hasil_pengecekan')


    context ={
        'form':Form,
        'title':'Menu Record Hasil Pengecekan',
        'body':'Menu Record Hasil Pengecekan',
        'nav':[['/','Menu Utama'],
              ['/Menu_input_standard_product','Menu Standard Product'],
              ['/Menu_kedatangan_product','Menu Kedatangan Product'],
              ['/Menu_login','Menu Login'],
              ['/Menu_record_hasil_pengecekan','Menu Record Hasil Pengecekan'],
        
        ],
    }
    return render(request, 'index.html',context)