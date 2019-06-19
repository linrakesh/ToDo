from django.shortcuts import render,redirect
from django.utils.timezone   import datetime
from .models import List

# Create your views here.
def home(request):
    posts = List.objects.all().order_by('-update_on')
    return render(request,'todoList/home.html',{'posts':posts})

def detail(request,pk):
    posts= List.objects.get(id=pk)
    return render(request,'todoList/details.html',{'posts':posts})

def remove(request,pk):
    List.objects.get(id=pk).delete()
    return redirect('home')    # this is required


def add_new_todo(request):
    if request.method=='POST':
        post = List()
        post.title = request.POST['title']    
        post.desc = request.POST['desc']
        post.update_on = datetime.now()
        post.save()
        return redirect('home')
    else:
        return render(request,'todoList/create.html')


def edit_todo(request,pk):
    if request.method =='POST':
        post= List.objects.get(id=pk)
        post.title = request.POST['title']    
        post.desc = request.POST['desc']
        post.update_on = datetime.now()
        post.save()
        return redirect('home')
    else:
        post= List.objects.get(id=pk)
        return render(request,'todoList/update.html',{'post':post})