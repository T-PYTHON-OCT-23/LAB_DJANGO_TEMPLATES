from . import views
from django.urls import path

app_name = "car"


urlpatterns = [
    path("",views.home_page_views, name="home_page_views"),
    path("today/",views.today_date_views, name="today_date_views"),
    path("random/password/",views.random_password_views, name="random_password_views"),
    path("favs/games/",views.favs_game_views, name="favs_game_views")
]