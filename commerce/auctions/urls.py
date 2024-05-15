from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing", views.create_list, name="create"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("removeWatchlist/<int:id>", views.removeWatchlist, name="removeWatchist"),
    path("addWatchlist/<int:id>", views.addWatchlist, name="addWatchist"),
    path("watchlist", views.watchlist, name="watchlist")
]
