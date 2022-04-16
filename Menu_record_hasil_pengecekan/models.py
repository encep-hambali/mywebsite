from django.db import models
from Menu_kedatangan_product.models import Kedatangan_Product
# Create your models here.

class Record_Hasil_Pengecekan(models.Model):
    nama = models.OneToOneField(Kedatangan_Product, 
                                on_delete=models.CASCADE)
    nomor_batch = models.CharField(max_length=225)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=225)
    standard_sc = models.CharField(max_length=225)
    standard_ph = models.CharField(max_length=225)
    standard_appearance =models.CharField(max_length=255)
    actual_sc = models.CharField(max_length=225)
    actual_ph = models.CharField(max_length=225)
    actual_appearance =models.CharField(max_length=255)
    STATUS =( ('ok', 'OK'), ('ng', 'NG'))
    status = models.CharField(max_length=225, choices=STATUS, null=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)