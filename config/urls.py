
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Menu_utama.urls")),
    path('Menu_input_standard_product/', include("Menu_input_standard_product.urls")),
    path('Menu_kedatangan_product/', include("Menu_kedatangan_product.urls")),
    path('Menu_login/', include("Menu_login.urls")),
    path('Menu_record_hasil_pengecekan/', include("Menu_record_hasil_pengecekan.urls")),
]
