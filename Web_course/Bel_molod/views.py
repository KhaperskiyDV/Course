from django.shortcuts import render


def index(request):
    return render(request, 'Bel_molod/index.html', {'title': 'Молодежь Белово'})


def about(request):
    return render(request, 'Bel_molod/about.html', {'title': 'О нас'})
