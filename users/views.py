from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request, 'users/login.html')

def registration_view(request):
    return render(request, 'users/registration.html')

def password_recovery_view(request):
    return render(request, 'users/password_recovery.html')