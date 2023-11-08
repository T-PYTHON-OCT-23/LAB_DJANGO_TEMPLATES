from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.utils.crypto import get_random_string
import datetime


# Create your views here.

def home_page_views(request:HttpRequest):
    return render(request,'main/HomePage.html')


def today_view(request:HttpRequest):
    context={
        "date":datetime.date.today()
    }
    return render(request, 'main/Date.html',context)

def random_pass_view(request :HttpRequest):
    password=get_random_string(8)
    context={
        "pass":password
    }
    return render(request,'main/Password_Generator.html',context)

def fav_games_view(request:HttpRequest):
    games =['Crash' , 'Call of duty','Brawlhalla']
    context={
        'games':games
    }
    return render(request,'main/Favorite_Game.html',context)
