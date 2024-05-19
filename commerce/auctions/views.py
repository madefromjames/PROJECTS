from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Bid

def index(request):
    activeListing = Listing.objects.filter(isActive=True)
    return render(request, "auctions/index.html", {
        "listing": activeListing
    })

def listing(request, id):
    listing = Listing.objects.get(pk=id)
    listingWatchlist = request.user in listing.watchlist.all()
    if request.method == "POST":
        newBid = request.POST["bid"]
    return render(request, "auctions/listing.html", {
        "listing": listing, "listingWatchlist": listingWatchlist
    })

def removeWatchlist(request, id):
    listing = Listing.objects.get(pk=id)
    currentUser = request.user
    listing.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def addWatchlist(request, id):
    listing = Listing.objects.get(pk=id)
    currentUser = request.user
    listing.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def watchlist(request):
    currentUser = request.user
    listing = currentUser.watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "listing": listing
    })

def create_list(request):
    if request.method == "GET":
        categorys = Category.objects.all() 
        return render(request, "auctions/create.html", {
            "category": categorys
        })
    else:
        # Get the form data
        title = request.POST['title']
        description = request.POST['description']
        image = request.POST['imageURL']
        price = request.POST['price']
        category = request.POST['category']

        # Current User
        currentUser = request.user

        # Get the particuar category
        categoryData = Category.objects.get(categoryName=category)

        # Bid
        bid = Bid(bid=float(price), user=currentUser)
        bid.save()

        # Create a new list object
        newList = Listing(title=title,
                          description=description,
                          imageUrl=image,
                          price=bid,
                          owner=currentUser,
                          category=categoryData)

        # Insert newList into databse
        newList.save()

        return HttpResponseRedirect(reverse(index))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
