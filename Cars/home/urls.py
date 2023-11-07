from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("today/", views.today_page_view,name="today_page_view"),
    path("random/password/",views.random_password_view,name="random_password_view"),
    path("favs/games/",views.favorite_games_view,name="favorite_games_view"),
]