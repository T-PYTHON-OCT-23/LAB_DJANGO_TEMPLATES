from django.urls import path
from . import views





app_name = "main"


urlpatterns = [

    path("today/" , views.today_view , name = "today_views"),
    path("random/pass/" , views.random_pass_view , name = "random_pass_views" ),
    path("favs/games/"  , views.favs_games_view , name = "favs_games_views"),
    path(""  , views.home_view , name = "home_views"),
]