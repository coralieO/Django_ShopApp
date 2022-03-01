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

def product_detail(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Product.objects.get(id = id)
         
    return render(request, "shopApp/product_detail.html", context)

def product_update(request,id):

    context = {}
    obj = get_object_or_404(Product, id = id)
    form = ProductForm(request.POST, request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/shopApp/"+id)
    
    context["form"] = form
 
    return render(request, "shopApp/product_update.html", context)

def product_delete(request, id): 
    context ={}
    obj = get_object_or_404(Product, id = id)

    if request.method == "POST" :
        obj.delete()

        return HttpResponseRedirect("/shopApp/product_page")

    return render(request, "shopApp/product_delete.html",context)