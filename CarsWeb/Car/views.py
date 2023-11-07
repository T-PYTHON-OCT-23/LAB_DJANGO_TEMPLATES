from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date 
from django.utils.crypto import get_random_string
  
# Create your views here.

def home_views(request:HttpRequest):
    image_url = "https://hips.hearstapps.com/hmg-prod/images/10best-cars-group-cropped-1542126037.jpg"
    context = {
        'image_url': image_url
    }
    return render(request, 'Car/home.html', context)

def Date_views(request:HttpRequest):
    today = date.today() 
    context={
        "Date":today
    }
    return render(request,'Car/date.html', context)


def FavGame_views(request:HttpRequest):
    game = ["Chess","Fortnite","SEQUENCE"]
    
    context={
        "games":game
    }
    return render(request,'Car/favsGames.html',context )

def generatedPassword(request:HttpRequest):
     password=get_random_string(length=13)
     
     context={
         "pas":password
     }
     return render(request,'Car/pas.html',context )