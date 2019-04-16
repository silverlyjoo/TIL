from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm



def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
        
    else:
        form = SignupForm()
    
    context = {
        'form':form
    }

    return render(request, 'accounts/signup.html', context)
    

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            
            return redirect(request.GET.get('next') or 'posts:list')
        
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)
    

def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    
    
def people(request, username):
    people = get_object_or_404(get_user_model(), username=username)
    context = {
        'people':people,
    }
    
    return render(request, 'accounts/people.html', context)