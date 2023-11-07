from django.urls import path
from . import views

app_name = "main"
urlpatterns =[
  path("",views.home_page,name="home_page"),
  path("date/",views.date_today_view,name="date_today_view"),
  path("password/" , views.password_view , name="password_view"),
  path("games/" , views.list_games_view , name="list_games_view"),
]