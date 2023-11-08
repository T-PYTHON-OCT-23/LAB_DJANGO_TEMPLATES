from django.urls import path
from . import views

app_name = "main"
urlpatterns =[
    path("", views.home_page_views, name="home_page_views"),
    path('random/password', views.random_pass_view, name="random_pass_view"),
    path("Today/", views.today_view, name="today_view"),
    path('favs/games/',views.fav_games_view, name='fav_games_view')
]