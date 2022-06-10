from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class akademisyen(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    isim_soyisim = models.CharField(max_length=100)
    def __str__(self):
        return self.isim_soyisim

class ogrenci(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    isim_soyisim = models.CharField(max_length=100)
    def __str__(self):
        return self.isim_soyisim
class users_status(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status = models.BooleanField()
    