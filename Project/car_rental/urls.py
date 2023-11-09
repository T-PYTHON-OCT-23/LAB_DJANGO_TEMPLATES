from django.urls import path
from . import views

app_name = "car_rental"

urlpatterns =[
    path("" , views.index_viwe , name="index_view"),
    path("today/" , views.today_viwe , name="today_viwe"),
    path("random/password/" , views.random_password, name="random_password"),
    path("favs/games/" , views.favs_games , name="favs_games"),
]
