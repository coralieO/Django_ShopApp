from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,response,Http404,HttpResponseRedirect


# Create your views here.

def index(request):
  return render(request, 'shopApp/index.html')
