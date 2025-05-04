from django.shortcuts import render,redirect
from .forms import profileForms
def home(request):
    if request.method == 'POST':
        form=profileForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form=profileForms()
    return render(request,'author.html',{'form':form})