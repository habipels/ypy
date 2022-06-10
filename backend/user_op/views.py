from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.utils.datastructures import MultiValueDictKeyError
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
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
            return #login front
        login(request,user)
        return redirect("index")
    return  #login front

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