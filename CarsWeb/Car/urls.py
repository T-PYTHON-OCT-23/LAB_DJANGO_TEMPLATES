from django.urls import path
from . import views

app_name = "Car"


urlpatterns = [
    path('',views.home_views, name="home_views"),
    path('today/', views.Date_views, name="Date_views"),
    path('favs/games/',views.FavGame_views, name="FavGame_views") ,
    path('random/password/',views.generatedPassword, name="generatedPassword")
]