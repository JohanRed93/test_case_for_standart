from django.urls import path

from . import views

app_name = 'reqtable'

urlpatterns = [
    path('cominfo/', views.cominfo, name='cominfo'),
    path('', views.index, name='index_page'),
]
