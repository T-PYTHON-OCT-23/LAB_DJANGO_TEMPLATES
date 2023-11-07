from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.utils.crypto import get_random_string


# Create your views here.

def basic(request : HttpRequest):
    return render(request, "main/basic.html")

def today(request : HttpRequest):
    return render(request,"main/today.html" )

def random_password(request : HttpRequest):
    password = get_random_string(length=12)
    content= {
        'Password': password

    }
    return render(request, "main/password.html",content)

def games(request : HttpRequest):
    return render(request, "main/games.html")
