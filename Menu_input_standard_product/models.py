from django.db import models

# Create your models here.

class Standard_Product(models.Model):
    nama = models.CharField(max_length=255, primary_key=True)
    standard_sc = models.CharField(max_length=225)
    standard_ph = models.CharField(max_length=225)
    standard_appearance =models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nama)



