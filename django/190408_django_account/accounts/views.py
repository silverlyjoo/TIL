from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash as update_session
from .forms import UserCustomChangeForm, UserCustomCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from boards.models import Board, Comment



# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    
    if request.method == "POST":
        form = UserCustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    
    else:
        form = UserCustomCreationForm()
        
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)
    

def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.POST.get('next') or 'boards:index')
        
    else:
        form = AuthenticationForm()
    
    context = {
        'form':form,
        'next':request.GET.get('next', ''),
    }
    return render(request, 'accounts/login.html', context)
    

def logout(request):
    auth_logout(request)
    return redirect('boards:index')
    
    
def delete(request):
    user = request.user
    if request.method == "POST":
        user.delete()
    
    return redirect('boards:index')

def edit(request):
    if request.method == "POST":
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = UserCustomChangeForm(instance=request.user)
    
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session(request, user)
            
            return redirect('boards:index')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {'form':form,}
    return render(request, 'accounts/auth_form.html', context)

@login_required
def profile(request, user_pk):
    profile_user = get_object_or_404(get_user_model(), pk=user_pk)
    context = {
        'profile_user':profile_user,
    }
    return render(request, 'accounts/profile.html', context)