from django.urls import path
from . import views


app_name = "RentalCar"

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("random/password/", views.passwordPage, name="password"),
    path("today/", views.todayPage, name="today"),
    path("favs/games/", views.gamesPage, name="games"),
]