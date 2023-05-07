from django.contrib import admin
from django.urls import path, include
from users.views import *

app_name = 'users'
urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout')
]
