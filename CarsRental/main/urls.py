from django.urls import path

from .import views

app_name ='main'

urlpatterns = [
    path('',views.home,name='home'),
    path('today/',views.today,name='today'),
    path('random/password/',views.random_password,name='random_password'),
    path('favs/games/',views.favs_game,name='favs_game')
]

