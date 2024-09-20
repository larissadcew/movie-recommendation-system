from django.shortcuts import render
from django.conf import settings
import requests
from .utils import get_api_movie
from django.contrib.auth.decorators import login_required




def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def watchilist(request):
    return render(request , 'Watchlist.html')

@login_required
def Profile(request):
    return render(request, 'Profile.html')

@login_required
def Trending(request):
    return render(request, 'Trending.html')

