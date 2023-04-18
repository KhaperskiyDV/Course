from django.shortcuts import render

menu_list = ["ГЛАВНАЯ", "СОБЫТИЯ", "ПРОЕКТЫ", "СООБЩЕСТВА", "ТРУДОУСТРОЙСТВО МОЛОДЫХ", "О НАС"]

def index(request):
    return render(request, 'Bel_molod/index.html', {'menu_list': menu_list, 'title': 'Молодежь Белово'})


def about(request):
    return render(request, 'Bel_molod/about.html', {'menu_list': menu_list, 'title': 'О нас'})

def send(request):
    return render(request, 'Bel_molod/send.html', {'menu_list': menu_list, 'title': 'Обратная связь'})

def regist(request):
    return render(request, 'Bel_molod/regist.html', {'menu_list': menu_list, 'title': 'Регистрация'})

def auth(request):
    return render(request, 'Bel_molod/auth.html', {'menu_list': menu_list, 'title': 'Авторизация'})

def events(request):
    return render(request, 'Bel_molod/events.html', {'menu_list': menu_list, 'title': 'События'})