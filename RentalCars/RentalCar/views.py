from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
from datetime import date

def homePage(request : HttpRequest):
    
    return render(request ,"RentalCar/homePage.html")

def passwordPage(request : HttpRequest):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRCTUVWXYZ"
    number = "1234567890"
    symbols = "!@#$%^&*()"
    string = lower + upper + number + symbols
    length = 8
    password = "".join(random.sample(string, length))
    context = {
       "password" : password ,
    }
    
    return render(request ,"RentalCar/password.html" , context)

def todayPage(request : HttpRequest):
    today = date.today()
    context = {
       "today" : today ,
    }
    
    
    return render(request ,"RentalCar/today.html", context)

def gamesPage(request : HttpRequest):
     games = ["pubg", "crash", "fortnite"]
     context = {
       "games" : games ,
    }
     return render(request ,"RentalCar/favoriteGames.html" , context)
