from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [

    path('UserSignupEmail', views.UserSignupEmail.as_view(), name='UserSignupEmail'),
]
