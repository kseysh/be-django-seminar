from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from .forms import UserCreateForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
def signup(request):
    if request.method=='GET':
        #form = UserCreateForm
        form = UserCreationForm
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('accounts:login')
        else:
            messages.add_message(request, messages.WARNING, form.error_messages)
            return redirect('accounts:signup')
def user_login(request):
    form = AuthenticationForm(request, data = request.POST)
    if request.method =='GET':
        return render(request,'accounts/login.html',{'form':AuthenticationForm()})
    else:
        if form.is_valid():
            login(request,form.user_cache)
            if form.user_cache.mbti:
                return redirect('home')
            print(form.user_cache.mbti)
            return redirect('mbtitest')
            
        else:
            messages.add_message(request, messages.WARNING,form.error_messages)
            return render(request, 'accounts/login.html',{'form':form})
        

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')
       