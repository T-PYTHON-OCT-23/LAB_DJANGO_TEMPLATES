from django.urls import path
from . import views
app_name = "cars"
urlpatterns = [
    path("", views.home, name="home"),
    path("day/", views.day, name="day"),
    path("favGame/", views.favGame, name="favGame"),
    path("password/", views.password, name="password"),
]
