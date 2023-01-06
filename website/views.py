from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from .models import Tasks
# Create your views here.

values = Tasks.objects.all()
v2 = Tasks.objects

def index(request):
    return render(request,'website/home.html',{
        'db':values,
        'dd':v2,
    })

def api(request):
    return JsonResponse({'welcome':'merda'})