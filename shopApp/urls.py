from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shopApp'
urlpatterns = [
    path('', views.index, name='home'),
    path('products', views.product_page, name='productsPage'),
    path('product_upload', views.product_add, name = 'image_upload'), 
    path('success', views.success, name = 'success'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)