from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse

from .forms import *

# menu_list = ["ГЛАВНАЯ", "СОБЫТИЯ", "ПРОЕКТЫ", "СООБЩЕСТВА", "ТРУДОУСТРОЙСТВО МОЛОДЫХ", "О НАС"]
menu_list = [
{'text': "ГЛАВНАЯ",'url_name': 'home'},
{'text': "СОБЫТИЯ",'url_name': 'events'},
{'text': "ПРОЕКТЫ",'url_name': 'home'},
{'text': "СООБЩЕСТВА",'url_name': 'home'},
{'text': "ТРУДОУСТРОЙСТВО МОЛОДЫХ",'url_name': 'home'},
{'text': "О НАС",'url_name': 'about'},
]

def index(request):
    return render(request, 'Bel_molod/index.html', {'menu_list': menu_list, 'title': 'Молодежь Белово'})


def about(request):
    return render(request, 'Bel_molod/about.html', {'menu_list': menu_list, 'title': 'О нас'})

def send(request):
    return render(request, 'Bel_molod/send.html', {'menu_list': menu_list, 'title': 'Обратная связь'})

def regist(request):
    return render(request, 'Bel_molod/regist.html', {'menu_list': menu_list, 'title': 'Регистрация'})


def events(request):
    return render(request, 'Bel_molod/events.html', {'menu_list': menu_list, 'title': 'События'})


def userauth(request):
    if request.method == 'POST':
        f = UserLoginForm(data=request.POST)
        if f.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                print('OK')
                return redirect(reverse('home'))
    else:
        f = UserLoginForm()
    context = {'form': f, 'menu_list': menu_list, 'title': 'Авторизация'}
    return render(request, 'Bel_molod/auth.html', context)


def testform(request):
    if request.method == 'POST':
        f = RegistForm(request.POST)
        if f.is_valid():
            return redirect('auth')
    else:
        f = RegistForm()
    context = {'form': f, 'menu_list': menu_list, 'title': 'testform'}
    return render(request, 'Bel_molod/testform.html', context )
