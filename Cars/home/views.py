from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from datetime import *
from django.utils.crypto import get_random_string

# Create your views here.
def home_view(request : HttpRequest):
    return render(request,"home/homepage.html")


def today_page_view(request :HttpRequest):
    context= {
        "today":  datetime.today()
    }
    return render(request,"home/today.html",context)


def random_password_view(request :HttpRequest):
   random_password={"password":get_random_string(8)}
   return render(request, 'home/passward.html',random_password)


def  favorite_games_view(request :HttpRequest):
    return render(request, 'home/games.html')