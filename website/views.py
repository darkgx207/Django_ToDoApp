from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse

from .models import Tasks
# Create your views here.



def index(request):
    return render(request,'website/home.html',{
        'db':Tasks.objects.all(),
    })

def edit(request, int):
    if request.method == 'POST' and 'delete' in request.POST:
        Tasks.objects.filter(pk=int).delete()
        return redirect('/') 

    return render(request ,'website/edit.html' , {
        'id': Tasks.objects.get(id=int)
    })
