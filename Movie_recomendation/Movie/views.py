from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def watchilist(request):
    return render(request , 'Watchlist.html')

def Profile(request):
    return render(request, 'Profile.html')

def Trending(request):
    return render(request, 'Trending.html')