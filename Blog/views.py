from django.shortcuts import render,redirect
from post.models import post
from post.forms import postForms
def home(request):
    data=post.objects.all()
    return render(request,'index.html',{'data':data})