from django.shortcuts import render, redirect
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_view(request):

    page_name = 'Login'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            existing_user = User.objects.get(username=username)
        except:
            messages.error(request, f'User with username "{username}" does not exist.')
            return render(request, 'users/login.html', context={'page_name': page_name})
   
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Wrong password.')
        return render(request, 'users/login.html', context={'page_name': page_name})

    return render(request, 'users/login.html', context={'page_name': page_name})

def logout_view(request):
    logout(request)
    return redirect('login-page')

def registration_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return render(request, 'users/registration.html')
        user = User.objects.create(username=username, password=password2, email=email, first_name='', last_name='')
        login(request, user)
        messages.success(request, f'Welcome, {username}!')
        return redirect('home')
    return render(request, 'users/registration.html')

def password_recovery_view(request):
    return render(request, 'users/password_recovery.html')