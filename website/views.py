from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from .models import Tasks
# Create your views here.



def index(request):
    return render(request,'website/home.html',{
        'db':Tasks.objects.all(),
    })

def create(request, int):
    return render(request ,'website/create.html' )