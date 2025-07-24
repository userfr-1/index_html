from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

def index(request):
    count = Country.objects.all()
    reg = Region.objects.all()
    context = {
        'count': count,
        'reg': reg,
    }

    return render(request,'index.html',context=context)

def category(request,pk):
    count = Country.objects.all()
    reg = Region.objects.filter(country = pk)
    context = {
        'count': count,
        'reg': reg,
    }

    return render(request,'category.html',context=context)
