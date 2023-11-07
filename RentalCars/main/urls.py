from django.urls import path
from . import views
app_name = "main"

urlpatterns = [
    path("", views.basic, name="basic"),
    path("today/", views.today, name='today'),
    path("random/password/", views.random_password, name='password'),
    path("favs/games/",views.games , name='games')
]
