from django.urls import path


from . import views

app_name = 'adminn'

urlpatterns = [

    path('HasUpdate', views.HasUpdate.as_view() , name='HasUpdate'),
    path('GetImage', views.GetImage.as_view() , name='GetImage'),

    path('ItemCreate', views.ItemCreate.as_view() , name='ItemCreate'),

    path('ItemsList', views.ItemsList.as_view() , name='ItemsList'),


]
