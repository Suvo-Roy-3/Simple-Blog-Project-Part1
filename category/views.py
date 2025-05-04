from django.shortcuts import render,redirect
from .forms import categoryForms
def home(request):
    if request.method == 'POST':
        form=categoryForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form=categoryForms()
    return render(request,'category.html',{'form':form})