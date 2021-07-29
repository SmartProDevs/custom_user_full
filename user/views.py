from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *

def login_required(func):
    return login_required(function=func, url="login-page")

def login_page(request):
    if request.POST:
        email =request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(user)
            return redirect("home_page")
    return render(request, "login.html")

def register_page(request):
    if request.POST:
        email =request.POST.get('email')
        password=request.POST.get('password')
        user = User.objects.create_user(email=email, password=password, full_name=full_name)
        if user is not None:
            login(user)
            return redirect("home_page")
    return render(request, "login.html")

def home_page(request):
    return render(request, 'index.html')
