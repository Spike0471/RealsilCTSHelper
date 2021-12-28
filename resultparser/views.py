from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    #template = loader.get_template('resultparser/index.html')
    context = {}
    #return HttpResponse(template.render(context,request))
    return render(request,'resultparser/index.html',context)

def record(request):
    context = {}
    return render(request,'resultparser/record.html',context)

def search(request):
    context = {}
    return render(request,'resultparser/search.html',context)

def result(request):
    context = {}
    return render(request,'resultparser/result.html',context)
