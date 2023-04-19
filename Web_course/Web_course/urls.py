
from django.contrib import admin
from django.urls import path

from Bel_molod.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('send/', send, name='send'),
    path('regist/', regist, name='regist'),
    path('auth/', auth, name='auth'),
    path('events/', events, name='events'),
    path('testform/', testform, name='testform')
   ]
