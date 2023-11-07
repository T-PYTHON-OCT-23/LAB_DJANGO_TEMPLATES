from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from django.utils.crypto import get_random_string



# Create your views here.


def home(request:HttpRequest):
    return render(request,'main/home.html')

def today(request:HttpRequest):

    date_time = datetime.now().strftime("%Y-%m-%d || %I:%M:%S")

    context = {
        'datetime':date_time
    }

    return render(request,'main/today.html',context)

def random_password(request:HttpRequest):

    password = get_random_string(length=12, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

    context = {
        'password':password
    }
    return render(request,'main/random_password.html',context)

def favs_game(requeat:HttpRequest):
    return render(requeat,'main/favs_game.html')