from django.shortcuts import render

menu_list = [
    {'text': "ГЛАВНАЯ", 'url_name': 'home'},
    {'text': "СОБЫТИЯ", 'url_name': 'events'},
    {'text': "ПРОЕКТЫ", 'url_name': 'plug'},
    {'text': "СООБЩЕСТВА", 'url_name': 'plug'},
    {'text': "ТРУДОУСТРОЙСТВО МОЛОДЫХ", 'url_name': 'plug'},
    {'text': "О НАС", 'url_name': 'about'},
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


def plug(request):
    return render(request, 'Bel_molod/plug.html', {'menu_list': menu_list, 'title': 'Раздел в разработке'})
