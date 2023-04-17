
from django.contrib import admin
from django.urls import path

from Bel_molod.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about)
]
