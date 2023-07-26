from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generation/home.html')


def password(request):
    resultpassword = ""
    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get('uppercase'):
        characters.extend("ABCDEFGHIJKLMNOPQRSTUXWXYZ")

    if request.GET.get('special'):
        characters.extend("!@#$%^&*()_+=-.~,?/'")
    
    if request.GET.get('numbers'):
        characters.extend("0123456789")

    lenght = int(request.GET.get('lenght', 12))

    for x in range(lenght):
        resultpassword += random.choice(characters)

    return render(request, 'generation/new.html', {'password': resultpassword})

def about(request):
    return render(request, 'generation/about.html')
