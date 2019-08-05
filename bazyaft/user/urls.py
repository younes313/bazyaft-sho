from django.urls import path
from rest_framework.authtoken import views as views2

from . import views

app_name = 'user'

urlpatterns = [
    # path('GetOrder', views.GetOrder.as_view() , name='GetOrder'),

    
    path('GetOrder', views.GetOrder.as_view() , name='GetOrder'),
    path('UserLogout', views.UserLogout.as_view() , name='UserLogout'),
    path('GetMyCoins', views.GetMyCoins.as_view() , name='GetMyCoins'),
    path('GetTokenPhone', views.GetTokenPhone.as_view() , name='GetTokenPhone'),
    path('get-token' , views.GetTokenUsername.as_view() , name = "GetTokenUsername" ) ,
    path('get-token-email', views.GetTokenEmail.as_view() , name='GetTokenEmail'),
    path('TegariEmailRegister', views.TegariEmailRegister.as_view() , name='TegariEmailRegister'),
    path('EdariEmailRegister', views.EdariEmailRegister.as_view() , name='EdariEmailRegister'),
    path('KhanevarEmailRegister', views.KhanevarEmailRegister.as_view(), name='KhanevarEmailRegister'),
]
