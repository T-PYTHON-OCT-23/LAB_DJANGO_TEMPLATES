from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import *
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.shortcuts import resolve_url


# Create your views here.


# Create your views here.
def page_view(request :HttpRequest):
      
      return render(request, "home/home.html" )


def today_view(request : HttpRequest):
   contaxt = { "today" : datetime.today()   
   }
   return render(request, "home/today.html" , contaxt )


def password_view(request :HttpRequest):
   
   dict= { "password" : get_random_string(8)}
   return render(request, "home/password.html" , dict )



def games_view(request :HttpRequest):
        return render(request, "home/fav_games.html"  ) 

'''   fav_games =["Tarazan" , "crach" , "driver" , "fefa" ]
   dict = {"games" : fav_games}'''
 

