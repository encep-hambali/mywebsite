from django.shortcuts import render

# Create your views here.

def index(request):
    context ={
        'title':'Menu Utama',
        'body':'Menu Utama',
        'nav':[['/', 'fa fa-desktop','Dashbrod'],
              ['/Menu_input_standard_product','fa fa-cogs','Standard Product'],
              ['/Menu_kedatangan_product','fa fa-table','Kedatangan Product'],
              ['/Menu_login','fa fa-th','Login'],
              ['/Menu_record_hasil_pengecekan','fa fa-info-circle','Hasil Pengecekan'],

        ],
    }
    return render(request, 'side.html',context)