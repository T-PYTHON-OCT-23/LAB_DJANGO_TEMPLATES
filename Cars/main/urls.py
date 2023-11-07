from django.urls import path
from . import views

app_name= "main"

urlpatterns =[
    path('',views.home, name="home"),
    path('today/', views.today,name="today"),
    path('pass/', views.random_password, name="pass"),
    path('favorite/', views.favorite_games,name="favorite")

]
