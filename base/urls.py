from django.urls import path
from . import views

urlPatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
]