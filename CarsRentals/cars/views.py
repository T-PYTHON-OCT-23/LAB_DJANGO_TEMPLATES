from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import *
# Create your views here.


def home(request: HttpRequest):
    return render(request, 'cars/home.html')


def day(request: HttpRequest):
    context = {
        "today": datetime.today()
    }
    return render(request, 'cars/day.html', context)


def password(request: HttpRequest):
    return render(request, 'cars/password.html')


def favGame(request: HttpRequest):
    return render(request, 'cars/favGame.html')
