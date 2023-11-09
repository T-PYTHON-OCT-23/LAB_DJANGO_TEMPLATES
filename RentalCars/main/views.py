from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.utils.crypto import get_random_string
import datetime


# Create your views here.

def cars_rentals(request : HttpRequest):
    return render(request, "main/cars_rentals.html")

def today_date(request : HttpRequest):
    date = datetime.datetime.today().date()
    content = {
        'date':date
    }
    return render(request,"main/today_date.html" ,content)

def random_password(request : HttpRequest):
    password = get_random_string(length=12)
    content= {
        'Password': password

    }
    return render(request, "main/password.html",content)


def fav_games_list(request: HttpRequest):

    fav_games = [
        {
            "title" : "Overwatch",
            "image" : "/static/images/game1.jpg"
        },
        {
            "title" : "Subway surfers",
            "image" : "/static/images/game2.jpg"
        },
        {
            "title" : "SUDOKU",
            "image" : "/static/images/game3.jpg"
        },
        {
            "title" : "Cluedo",
            "image" : "/static/images/game4.jpg"
        },
    ]
    return render(request, "main/games.html", context = {"games" : fav_games})