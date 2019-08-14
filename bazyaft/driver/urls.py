from django.urls import path
from rest_framework.authtoken import views as views2

from . import views

app_name = 'driver'

urlpatterns = [
    # path('GetOrder', views.GetOrder.as_view() , name='GetOrder'),

    path('GetToken', views.GetToken.as_view() , name='GetToken'),
    path('user_login/', views.user_login , name='user_login'),
    path('register/', views.register , name='register'),
    path('GetMyAcceptedOrder', views.GetMyAcceptedOrder.as_view() , name='GetMyAcceptedOrder'),
    path('CancelOrder', views.CancelOrder.as_view() , name='CancelOrder'),
    path('AcceptOrder', views.AcceptOrder.as_view() , name='AcceptOrder'),
    path('GetAllOrders', views.GetAllOrders.as_view() , name='GetAllOrders'),
]
