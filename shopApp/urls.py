from django.urls import path
from . import views
from .views import product_delete, product_detail, product_update, update_quantity
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shopApp'
urlpatterns = [
    path('', views.index, name='home'),
    path('products', views.product_page, name='productsPage'),
    path('product_upload', views.product_add, name = 'image_upload'), 
    path('<id>' , product_detail),
    path('<id>/update' , product_update),
    path('<id>/update_quantity' , update_quantity),
    path('<id>/delete', product_delete ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)