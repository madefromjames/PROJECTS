from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError


# Create your views here.
def index(request):
    return render(request, "note/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
    return render(request, "note/login.html")

def logout_view(request):
    logout(request)
    return redirect("index")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
             return render(request, "note/signup.html", {"message": "Password must match!"})

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError: 
            return render(request, "note/signup.html", {"message": "Username already taken!"})

        auth.login(request, user)
        return redirect("index")
    return render(request, "note/signup.html")