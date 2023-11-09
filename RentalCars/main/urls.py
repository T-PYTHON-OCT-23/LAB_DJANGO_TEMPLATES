from django.urls import path
from . import views
app_name = "main"

urlpatterns = [
    path("", views.cars_rentals, name="cars_rentals"),
    path("today_date/", views.today_date, name='today_date'),
    path("random/password/", views.random_password, name='random_password'),
    path("favs/games/",views.fav_games_list , name='fav_games_list')
]
