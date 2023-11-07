

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
#view in django
def index_view(request:HttpRequest):

    return render(request, 'project/home.html')

def today_view(request:HttpRequest):#تاريخ اليوم


    return render(request, 'project/today.html')


def favorite_game_view(request : HttpRequest):#الالعاب المفضلة


   

           
   return render(request, 'project/favorite.html' , )



# Create your views here.
def password_view(request : HttpRequest):

    

    #pass context to template
    return render(request, 'project/password.html')


