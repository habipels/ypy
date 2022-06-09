from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.utils.datastructures import MultiValueDictKeyError
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.
