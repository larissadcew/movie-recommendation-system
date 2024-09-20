from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Profile/', views.Profile, name='profile'),
    path('Watchlist/', views.watchilist, name='Watchlist'),
    path('Trending/', views.Trending, name='Trending'),

]  

