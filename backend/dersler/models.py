import imp
from statistics import mode
from tkinter import CASCADE
from django.db import models
from all_users.models import *
# Create your models here.

class dersler(models.Model):
    sinif_adi = models.CharField(max_length=100)
    ders_sorumlusu = models.ForeignKey(akademisyen,on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.sinif_adi


class sorumlu_ogrenciler(models.Model):
    ders = models.ForeignKey(dersler,on_delete=models.CASCADE)
    ogr = models.ForeignKey(ogrenci,on_delete=models.CASCADE)