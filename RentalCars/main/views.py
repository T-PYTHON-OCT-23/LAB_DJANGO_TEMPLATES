from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.utils.crypto import get_random_string
import datetime
# Create your views here.
def home_page(request : HttpRequest):
    return render(request,'main/home.html')

def password_generator(request : HttpRequest):
    password=get_random_string(length=12)
    content={
        'pass':password
    }
    return render(request,'main/pass.html',content)

def today_date(request : HttpRequest):
    date=datetime.datetime.today().date()
    content={
        'date':date
    }
    return render(request,'main/today.html',content)

def favs_games(request):
    games = [
        {
            'title': 'pubg',
            'image': '/static/images/pupg.jpeg',
        },
        {
            'title': 'ludo star',
            'image': '/static/images/ludo.jpeg',
        },
        {
            'title': 'ouno',
            'image': '/static/images/uno.jpeg',
        },
    ]

    return render(request, 'main/favs.html', {'games': games})

    


