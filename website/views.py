from django.shortcuts import render, HttpResponse, redirect


from .models import Tasks


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
        target = Tasks.objects.get(pk=int)
        target.done = not target.done
        target.save()
        return redirect(index)
    # GET method
    return render(request ,'website/edit.html' , context)


def create(request):
    context = {'db':Tasks.objects}
    if request.method == 'POST' and request.POST.get('task') != '':
        task = request.POST.get('task')
        description = request.POST.get('description')
        context['db'].create(task=task, description= description)
        return redirect(index)
        
    return render(request,'website/create.html', context)