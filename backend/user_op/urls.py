from django.contrib import admin
from django.urls import path
from . import views

app_name = "user_op"

urlpatterns = [
    path('register/',views.kayit,name = "register"),
    path('login/',views.giris,name = "login"),
    path('logout/',views.cikis,name = "logout"),
    #path('reset/<int:idim>/<int:kod>',views.parola_sifirlama,name = "reset"),
    #path('passrest/',views.pass_reset,name="passreset"),
    #path('kod/',views.email_gonder,name = "email_gonder"),
]
