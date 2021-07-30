from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *

def login_page(request):
    if request.POST:
        email =request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect("home-page")
    return render(request, "login.html")

def login_required_decorator(funf):
    return login_required(function=funf, login_url="login-page")

def register_page(request):
    if request.POST:
        email =request.POST.get('email')
        password=request.POST.get('password')
        full_name=request.POST.get('full-name')
        user = User.objects.create_user(email=email, password=password, full_name=full_name)
        if user is not None:
            login(request, user)
            return redirect("home-page")
    return render(request, "register.html")

@login_required_decorator
def home_page(request):
    users =User.objects.all()
    print(users)
    ctx = {
        'users': users,
        'counts': {
            'user_count': len(User.objects.all())
        }
    }
    return render(request, 'cooladmin/index.html', ctx)

def create_user(request):
    if request.POST:
        email =request.POST.get('email')
        password=request.POST.get('password')
        full_name=request.POST.get('full-name')
        user_type=request.POST.get('user_type')
        user = User.objects.create_user(email=email, password=password, full_name=full_name, user_type=user_type)
        if user is not None:

            return redirect("home-page")
    return render(request, "create.html")

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login-page")
