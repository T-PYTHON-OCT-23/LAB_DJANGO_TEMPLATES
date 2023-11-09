from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import *
from django.utils.crypto import get_random_string
import string
# Create your views here.


def home(request: HttpRequest):
    return render(request, 'cars/home.html')


def day(request: HttpRequest):
    context = {
        "today": datetime.today()
    }
    return render(request, 'cars/day.html', context)


def password(request: HttpRequest):
    password = get_random_string(10)
    password = get_random_string(
        10, string.ascii_letters+string.digits+string.punctuation)
    context = {
        "pass": password
    }
    return render(request, 'cars/password.html', context)


def favGame(request: HttpRequest):
    return render(request, 'cars/favGame.html')
