from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return #render(request,"dashboard.html",context)