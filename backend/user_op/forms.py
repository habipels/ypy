from django import forms
from django.forms import widgets

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı" , widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı', 'class': 'form-control'}))
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput(attrs={'placeholder': 'Parola', 'class': 'form-control'}))
