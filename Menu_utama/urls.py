from django.urls import path
from .views import index as viewsMenuUtama


urlpatterns =[
    path('', viewsMenuUtama),

]