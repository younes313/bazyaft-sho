from django.urls import path


from . import views

app_name = 'adminn'

urlpatterns = [

    path('getfirstimage', views.getfirstimage.as_view() , name='getfirstimage'),

    path('ImageCreate', views.ImageCreate.as_view() , name='ImageCreate'),

    path('ImageList', views.ImageList.as_view() , name='ImageList'),


]
