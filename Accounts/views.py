from django.shortcuts import render
from .models import UserProfile

# Create your views here.

def add_education(request):
    if request.method == "GET":
        return render(
            request,
            'add-education.html',
            context={})

def add_experience(request):
    if request.method == "GET":
        return render(
            request,
            'add-experience.html',
            context={})

def create_profile(request):
    if request.method == "GET":
        return render(
            request,
            'createprofile.html',
            context={})

def dashboard(request):
    if request.method == "GET":
        return render(
            request,
            'dashboard.html',
            context={})

def login(request):
    if request.method == "GET":
        return render(
            request,
            'login.html',
            context={})

def profile(request):
    if request.method == "GET":
        return render(
            request,
            'profile.html',
            context={})

def profiles(request):
    profiles = UserProfile.objects.all()
    if request.method == "GET":
        return render(
            request,
            'profiles.html',
            context={"profiles": profiles})

def register(request):
    if request.method == "GET":
        return render(
            request,
            'register.html',
            context={})
    
