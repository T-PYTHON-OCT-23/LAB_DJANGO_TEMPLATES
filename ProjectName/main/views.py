from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.utils.crypto import get_random_string
import datetime
# Create your views here.


def home_view(request : HttpRequest):

    return render(request, 'main/home.html')


def today_view(request : HttpRequest):
 context ={

    "date": datetime.date.today()
}
 return render(request,'main/today.html', context)



def random_pass_view(request : HttpRequest):
   
   password = get_random_string(8)
   context={
      
      "pass":password
   }
   return render(request,'main/random_pass.html', context)



def fava_games_view(request : HttpRequest):

   gemes =["GTA V ", "Project Makeover ","bowling"]

   context= {
   "gemes": gemes
   }

   return render(request,'main/favs_gemes.html', context)