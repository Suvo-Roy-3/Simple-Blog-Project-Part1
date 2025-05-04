from django.shortcuts import render,redirect
from .forms import authorForms

def home(request):
    if request.method == 'POST':
        form=authorForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form=authorForms()
    return render(request,'author.html',{'form':form})

