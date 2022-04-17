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
        'nav':[['/', 'fa fa-desktop','Dashbrod'],
              ['/Menu_input_standard_product','fa fa-cogs','Standard Product'],
              ['/Menu_kedatangan_product','fa fa-table','Kedatangan Product'],
              ['/Menu_login','fa fa-th','Login'],
              ['/Menu_record_hasil_pengecekan','fa fa-info-circle','Hasil Pengecekan'],

        ],
    }
    return render(request, 'side.html',context)