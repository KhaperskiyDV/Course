from django.contrib import admin
from django.urls import path, include
from Bel_molod.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('send/', send, name='send'),
    path('users/', include('users.urls', namespace='users')),
    path('events/', events, name='events'),
    path('plug/', plug, name='plug'),
]
