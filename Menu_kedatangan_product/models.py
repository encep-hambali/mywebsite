from django.db import models
from Menu_input_standard_product.models import Standard_Product
# Create your models here.
class Kedatangan_Product(models.Model):
    nama = models.ForeignKey(Standard_Product, on_delete=models.CASCADE)
    nomor_batch = models.CharField(max_length=225)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=225)

    def __str__(self):
        return '{}'.format(self.nama)