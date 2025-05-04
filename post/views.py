from django.shortcuts import render,redirect
from .forms import postForms
from . import models
def home(request):
    if request.method == 'POST':
        form=postForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form=postForms()
    return render(request,'post.html',{'form':form})

def edit_post(request,id):
    post=models.post.objects.get(pk=id)
    form=postForms(instance=post)
    if request.method == 'POST':
        form=postForms(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(request,'post.html',{'form':form})

def delete_post(request,id):
    post=models.post.objects.get(pk=id)
    post.delete()
    return redirect('home')