from django.shortcuts import render,redirect
from .forms import *

from .models import tasks
# Create your views here.
def home(request):

    task=tasks.objects.all()

    form=taskForm()

    context={'task':task,'form':form}

    if request.method=="POST":
        form=taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'task/home.html',context)


def update(request,pk):
    task=tasks.objects.get(id=pk)

    form=taskForm(instance=task)
    context={'form':form}
    if request.method=="POST":
        task1=taskForm(request.POST,instance=task)
        task1.save()
        return redirect('/')
    return render(request,'task/update.html',context)

def delete(request,pk):
    task=tasks.objects.get(id=pk)
    context={'task':task}
    if request.method=="POST":
        task.delete()
        return redirect('/')

    return render(request,'task/delete.html',context)
