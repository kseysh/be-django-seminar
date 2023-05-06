from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    return render(request, 'create.html')

def login(request):
    return render(request,'login.html')

def community(request):
    return render(request,'community.html')

def newuser(request):
    return render(request,'newuser.html')

def mbtitest(request):
    return render(request,'mbtitest.html')

