from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path("", views.home_page, name="home_page"),
    path('random/password/',views.password_generator,name='password_generator'),
    path('today/',views.today_date,name='today_date'),
    path('favs/games/',views.favs_games,name='favs_games')
]