from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,response,Http404,HttpResponseRedirect

from app1.models import Question
from .forms import QuestionForm


# Create your views here.

def index(request):
  return render(request, 'app1/index.html')

def create_view(request):

    context = {}

    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(request,'app1/add.html',context)

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    context["dataset"] = Question.objects.all()

    return render(request, "app1/list.html", context)

def detail(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Question.objects.get(id = id)
         
    return render(request, "app1/detail.html", context)

def update(request, id):

    context = {}
    obj = get_object_or_404(Question, id = id)
    form = QuestionForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app1/"+id)
    
    context["form"] = form
 
    return render(request, "app1/update.html", context)

def delete(request, id): 
    context ={}
    obj = get_object_or_404(Question, id = id)

    if request.method == "POST" :
        obj.delete()

        return HttpResponseRedirect("/app1/list")

    return render(request, "app1/delete.html",context)
