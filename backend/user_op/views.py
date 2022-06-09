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