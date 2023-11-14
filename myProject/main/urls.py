from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('today/', views.today, name='today'),
    path('random/password/', views.random_password, name='random_password'),
    path('favs/games/', views.favorite_games, name='favorite_games'),
    path('about/',views.about, name='about'),
    path("big/view/", views.big_view, name="big_view"),
    path('small/view/', views.small_view, name="small_view"),
    path('big/about/', views.big_about, name="big_about"),
    path('small/about/', views.small_about, name="small_about"),
    path('reset/', views.reset, name="reset")
    ]