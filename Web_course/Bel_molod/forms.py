from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class RegistForm(forms.Form):
    name = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'class': 'reg__input-item',  'placeholder': 'Ваше имя'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'reg__input-item',  'placeholder': 'E-mail'}))
    password1 = forms.CharField(max_length=200, label='', widget=forms.PasswordInput (attrs={'class': 'reg__input-item',  'placeholder': 'Пароль'}))
    password2 = forms.CharField(max_length=200, label='', widget=forms.PasswordInput (attrs={'class': 'reg__input-item',  'placeholder': 'Подтверждение пароля'}))
 

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'class': 'auth__input-item', 'placeholder': 'Ваше имя'}))
    password = forms.CharField(max_length=200, label='', widget=forms.PasswordInput(attrs={'class': 'auth__input-item', 'placeholder': 'Пароль'}))
    class Meta:
        model = User
        fields = ('username', 'password')