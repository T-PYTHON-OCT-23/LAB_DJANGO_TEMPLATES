from django.shortcuts import render
from django.http import HttpResponse
import time
from django.utils.crypto import get_random_string

# Create your views here.

def index_viwe(request:HttpResponse):

    return render(request , 'car_rentall/index.html')

def today_viwe(request:HttpResponse):
    time_now = time.ctime(time.time())

    context ={
        "today" : time_now 
    }
    return render(request,'car_rentall/today.html',context)

def random_password(request:HttpResponse):
    password=get_random_string(12)
    context ={
        "random_password" : password
    }
    return render(request,'car_rentall/random_password.html',context)

def favs_games(request:HttpResponse):
    list_favs_games=["X & O","Pepsi man","Fifa EA"]
    context = {
        "games" : list_favs_games

    }

    return render(request,'car_rentall/favs_games.html',context)