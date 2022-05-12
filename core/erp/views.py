from django.shortcuts import render
from django.http import JsonResponse
from core.erp.models import Category, Client

# Create your views here.



def firstview(request):
    data = {
    'name':'Cristian',
    'categories': Category.objects.all()
    }
    return render(request,'home.html', data)

def secondtview(request):
    data = {
    'name':'Cristian',
    'clients': Client.objects.all()
    }
    return render(request,'index.html', data)

