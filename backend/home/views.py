from django.shortcuts import render ,redirect
from all_users.models import *
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user_status_ = users_status.objects.filter(user= request.user)
        for i in user_status_:
            if i.status:
                pass
                #return redirect("ogrenci")
            else:
                return redirect("akademisyen")
    return render(request,"index.html")

def ogr_home(request):
    return render(request,"ogrenci_anasayfa.html")
def akademisyen_home(request):
    return render(request,"akademisyen_anasayfa.html")