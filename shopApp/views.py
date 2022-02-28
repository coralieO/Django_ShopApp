from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,response,Http404,HttpResponseRedirect
from .models import Product
from .forms import *
# Create your views here.

def index(request):
  return render(request, 'shopApp/index.html')

def product_page(request):
   # dictionary for initial data with
    # field names as keys
    context ={}

    context["dataset"] = Product.objects.all()

    return render(request, "shopApp/product_page.html", context)

def product_add(request):

    context = {}

    form = ProductForm(request.POST,request.FILES or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(request,'shopApp/product_add.html',context)

def success(request): 
    return HttpResponse(request,'successfully uploaded') 