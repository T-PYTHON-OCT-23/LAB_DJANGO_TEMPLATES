from django.urls import path
from . import views

app_name = "project"


urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("today/", views.today_view, name="today_view"),
    path("password/", views.password_view, name="password_view"),
    path("favorite/game/", views.favorite_game_view, name="favorite_game_view"),
]