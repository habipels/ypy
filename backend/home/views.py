from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def ogr_home(request):
    return render(request,"ogrenci_anasayfa.html")