from django.shortcuts import render 
from django.http import HttpRequest, HttpResponse 
from django.utils.crypto import get_random_string
import datetime
import time

# Create your views here.

def home(request:HttpRequest):
    return render(request, 'main/home.html')




def today(request:HttpRequest):
    date=datetime.date.today
    t= time.strftime("%A")
    content={
        'date': date,
        'today' :t
    }
    return render(request,'main/today.html',content)


def random_password(request : HttpRequest):
    password = get_random_string(length=12)
    content= {
        'Password': password

    }
    return render(request, "main/pass.html",content)


pubg="https://www.pubgmobile.com/ar/home.shtml"
Call_of="https://www.callofduty.com/ar/modernwarfare"

def favorite_games(request:HttpRequest):
    content={
        "pubg_website": pubg,
        "call_website": Call_of,
    }
    return render(request, "main/favorite.html",content)