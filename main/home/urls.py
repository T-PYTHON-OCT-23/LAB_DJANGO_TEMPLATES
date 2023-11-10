from django.urls import path
from . import views

app_name = "home"

#path("main/home/", views.page_view, name="page_view")
urlpatterns = [ 
    path("", views.page_view, name="page_view"),
    path("today/", views.today_view, name="today_view"),
    path("fav_games/", views.games_view, name="games_view"),
    path("password/", views.password_view, name="password_view"),
]
