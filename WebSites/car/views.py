from django.shortcuts import render
from django.http import HttpRequest
import datetime
import secrets
import string
today_date = datetime.date.today()


# Create your views here.
def home_page_views(request:HttpRequest):
    rate = 5
    rate_of = 5
    title = "Car Rentals - Special Offers Online"
    image = "data:image/jpeg;base64,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"
    paragraph = "The 500 is small, but if you don’t need space it could be your only car. That’s because it’ll go far enough on a charge to make motorway trips tenable. Whereas the Honda e or Mini electric would have to be second cars to anyone who ever drives beyond conurbations rather than just within them. It’s not as fun to drive as those are, mind. It’s trying harder to feel normal. With a stylish, recognisable design and a quality feel."
    context = {
        "rate": rate,
        "rate_of": rate_of,
        "title": title,
        "image":image,
        "paragraph":paragraph
    }

    return render(request,"car/home_page.html",context)

def today_date_views(request:HttpRequest):
    
    today = today_date
    context = {
        "date":today
    }
    return render(request,"car/today_date.html",context)


def random_password_views(request:HttpRequest):
    def generated_password( length = 14):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password
    genetare_password = generated_password()

    context = {
        "password": genetare_password
    }
    return render(request,"car/random_password.html",context)

def favs_game_views(request:HttpRequest):
    games = [
        {
        "name":"League of leagend",
        "title":"League of Legends is a multiplayer online battle arena (MOBA) game in which the player controls a character ('champion') with a set of unique abilities from an isometric perspective. As of 2023, there are over 160",
        "image":"data:image/jpeg;base64,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"
        },{
        "name":"GTA5",
        "title":"Set within the fictional state of San Andreas, based on Southern California, the single-player story follows three protagonists—retired bank robber Michael De Santa, street gangster Franklin Clinton, and drug dealer and gunrunner Trevor Philips—and their attempts to commit heists while under pressure from a corrupt",
        "image":"https://cdn.cloudflare.steamstatic.com/steam/apps/271590/capsule_616x353.jpg?t=1695060909"
        },{
        "name":"Total War Rome II",
        "title":"Gameplay is split between real-time tactical battles and a turn-based strategic campaign. Within the campaign, players manage the economy, government, diplomacy, and military of their faction and attempt to accomplish a series of objectives on a map that encompasses most of Europe, North Africa, and the Near East",
        "image":"https://upload.wikimedia.org/wikipedia/en/d/da/Total_War_Rome_II_cover.jpg"
        }]
    
    return render(request,"car/favs_game.html",{'games': games})