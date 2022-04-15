from django.shortcuts import render

# Create your views here.
def index(request):
    context ={
        'title':'Menu Login',
        'body':'Menu Login',
        'nav':[['/','Menu Utama'],
              ['/Menu_input_standard_product','Menu Standard Product'],
              ['/Menu_kedatangan_product','Menu Kedatangan Product'],
              ['/Menu_login','Menu Login'],
              ['/Menu_record_hasil_pengecekan','Menu Record Hasil Pengecekan'],
        
        ],
    }
    return render(request, 'index.html',context)