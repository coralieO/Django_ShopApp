from django.contrib import admin

from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    fields = ['picture_link', 'price','quantity', 'name','description']

admin.site.register(Product)