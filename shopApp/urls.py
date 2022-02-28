from django.urls import path
from . import views

app_name = 'shopApp'
urlpatterns = [
    path('', views.index, name='accueil'),
]