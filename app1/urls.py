import imp
from django.urls import path
from . import views
from .views import delete, detail, update

app_name = 'app1'
urlpatterns = [
    path('', views.index, name='detail'),
    path('add', views.create_view, name='add'),
    path('list', views.list_view, name='list'),
    path('<id>' , detail),
    path('<id>/update' , update),
    path('<id>/delete', delete ),
]