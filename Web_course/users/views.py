from django.shortcuts import render, redirect
from django.urls import reverse
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm
from Bel_molod.views import menu_list
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {'form': form, 'menu_list': menu_list, 'title': 'Авторизация'}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form, 'menu_list': menu_list, 'title': 'Авторизация'}
    return render(request, 'users/regist.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('home'))
