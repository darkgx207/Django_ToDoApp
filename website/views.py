from django.shortcuts import render, HttpResponse
from .models import Tasks, OwnerTask
# Create your views here.

values = Tasks.objects.all()
test = [1,2,3,4,5,6,7,8,9,10,11,123,123,211]

def index(request):
    return render(request,'website/home.html',{
        'db':values,
        'test':test,
    })