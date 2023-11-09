import secrets
import string
import random
import requests
from django.shortcuts import render
import datetime

def password(request):
    strong_password = generate_strong_password()
    context = {'password': strong_password}
    return render(request, 'main/password.html', context)

def generate_strong_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 2
            and any(c in string.punctuation for c in password)):
            return password

   
def myGame():
    games_list = {
        
        "The Elder Scrolls V: Skyrim":"TheElderScrollsVSkyrim.jpg",
        "God of War (2018)":"GodofWar.jpg",
        "Resident Evil Village":"ResidentEvilVillage.jpg"
    }
    # Randomly select a game from the list
    selected_game, image_path = random.choice(list(games_list.items()))

    return {'game': selected_game, 'image_path': image_path}
    
def games(request):
    context = myGame()
    return render(request,'main/games.html',context)



def ip():
    response = requests.get('https://api.ipify.org/')
    context = {'ip': response.text}
    return context


def today(request):
    context = { "iP":ip().get('ip'),
               "DATE":datetime.datetime.now()}
    return render(request,'main/today.html',context)



def home(request):
    return render(request,'main/home.html')