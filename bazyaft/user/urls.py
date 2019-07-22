from django.urls import path
from rest_framework.authtoken import views as views2

from . import views

app_name = 'user'

urlpatterns = [
    path('GetMyCoins', views.GetMyCoins.as_view() , name='GetMyCoins'),
    path('get-token' , views2.obtain_auth_token ) ,
    path('KhanevarEmailRegister', views.KhanevarEmailRegister.as_view(), name='KhanevarEmailRegister'),
]
