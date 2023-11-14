from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    return render(request, 'main/home.html')

def today(request):
    today_date = date.today()
    return render(request, 'main/today.html', {'today_date': today_date})

def random_password(request):
    random_password = get_random_string(length=12)
    return render(request, 'main/random_password.html', {'random_password': random_password})

def favorite_games(request):
    favorite_games_list = [
        {
        'title': 'Overwatch 2', 
        'image': '/static/images/overwatch.png'
        },
        {'title': 'Fortnite',
        'image': '/static/images/fortnite.jpeg'
        },
    ]
    return render(request, 'main/favorite_games.html', {'favorite_games_list': favorite_games_list})


def about(request):
    return render(request,'main/about.html')

def big_view(request):

    response = redirect("/")
    response.set_cookie('size', 'biggest')
    return response

def small_view(request):

    response = redirect("home")
    response.set_cookie('size', 'smallest')
    return response

def big_about(request):

    response = redirect("about")
    response.set_cookie('size_about', 'biggest')
    return response

def small_about(request):

    response = redirect("about")
    response.set_cookie('size_about', 'smallest')
    return response

def reset(request):
    response= redirect("home")
    response.delete_cookie("size")
    response.delete_cookie("size_about")

    return response 