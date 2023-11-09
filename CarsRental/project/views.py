

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.utils.crypto import get_random_string
import string
import random
# Create your views here.
#view in django




def password_generator_view(request: HttpRequest):

    password = get_random_string(15, string.ascii_letters+string.digits+string.punctuation)
    passsword2 = random.choices(string.ascii_letters+string.digits+string.punctuation, k=15)
    passsword2 = "".join(passsword2)
    return render(request, "project/password.html", {"password" : password, "password2" : passsword2})



def fav_games_view(request: HttpRequest):

    fav_games = [
        {
            "title" : "League of Legends",
            "image" : "/static/image/game1.jpg"
        },
        {
            "title" : "Overwatch",
            "image" : "/static/image/game2.png"
        },
        {
            "title" : "Crash Bandicoot",
            "image" : "/static/image/game3.jpg"
        },

        {
            "title" : "Overwatch",
            "image" : "/static/image/game2.png"
        },
        {
            "title" : "Crash Bandicoot",
            "image" : "/static/image/game3.jpg"
        },
    ]


    return render(request, "project/favorite.html", context = {"games" : fav_games})

def index_view (request:HttpRequest):
    return render(request,"project/home.html")