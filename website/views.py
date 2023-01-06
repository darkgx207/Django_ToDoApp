from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse

from .models import Tasks
# Create your views here.



def index(request):
    context = {
        'db':Tasks.objects.all(),
    }
    return render(request,'website/home.html',context)


def edit(request, int):
    # Context of variables
    context = {'id': Tasks.objects.get(id=int)}

    # POST METHODS
    if request.method == 'POST' and 'delete' in request.POST:
        Tasks.objects.filter(pk=int).delete()
        return redirect('/') 

    if request.method == 'POST' and 'mudar' in request.POST:
        return HttpResponse(Tasks.objects.filter(pk=int)) 
    # GET method
    return render(request ,'website/edit.html' , context)


def create(request):
    context = {'db':Tasks.objects}
    if request.method == 'POST':
        pass
        
    return render(request,'website/create.html', context)