from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.utils.datastructures import MultiValueDictKeyError
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from all_users.models import *
# Create your views here.
def giris(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            return render(request, "login.html",context)
        login(request,user)
        user_status_ = users_status.objects.filter(user= request.user)
        for i in user_status_:
            if i.status:
                return redirect("ogrenci")
            else:
                return redirect("akademisyen")
    return render(request, "login.html",context)

def kayit(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        newUser = User(username =username,email=email)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        return redirect("index")
    context = {
            "form" : form
        }
    return # render(request,"user_temp/register.html",context)

def cikis(request):
    logout(request)
    return redirect("index")