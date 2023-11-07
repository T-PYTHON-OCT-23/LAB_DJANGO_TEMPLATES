from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.home_view, name="home_views"),
    path("today/", views.today_view, name="today_views"),
    path("random/pass/", views.random_pass_view, name="random_pass_views"),
    path("favs/games/", views.fava_games_view, name="fava_games_views"),
]

