from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
#view in django
def index_view(request:HttpRequest):

    return render(request, 'main/home.html')