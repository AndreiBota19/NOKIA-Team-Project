from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm




def home(request):
    return render(request, 'WebApp/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'WebApp/about.html', {'title': 'About'})





