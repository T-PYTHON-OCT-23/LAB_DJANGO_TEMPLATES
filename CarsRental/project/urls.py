from django.urls import path
from . import views

app_name = "project"


urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("random/password/", views.password_generator_view, name="password_generator_view"),
    path("fav/games/", views.fav_games_view, name="fav_games_view")
]