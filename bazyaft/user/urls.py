from django.urls import path
from rest_framework.authtoken import views as views2

from . import views

app_name = 'user'

urlpatterns = [
    # path('GetOrder', views.GetOrder.as_view() , name='GetOrder'),


    path('GetOrder', views.GetOrder.as_view() , name='GetOrder'),
    path('GetTokenPhone', views.GetTokenPhone.as_view() , name='GetTokenPhone'),
    path('UserLogout', views.UserLogout.as_view() , name='UserLogout'),
    path('TegariEmailRegister', views.TegariEmailRegister.as_view() , name='TegariEmailRegister'),
    path('EdariEmailRegister', views.EdariEmailRegister.as_view() , name='EdariEmailRegister'),
    path('GetMyCoins', views.GetMyCoins.as_view() , name='GetMyCoins'),
    path('get-token' , views2.obtain_auth_token ) ,
    path('get-token-email', views.GetTokenEmail.as_view() , name='GetTokenEmail'),
    path('KhanevarEmailRegister', views.KhanevarEmailRegister.as_view(), name='KhanevarEmailRegister'),
]
