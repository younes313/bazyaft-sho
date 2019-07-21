from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [

    path('KhanevarEmailRegister', views.KhanevarEmailRegister.as_view(), name='KhanevarEmailRegister'),
]
