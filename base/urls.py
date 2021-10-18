from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='rooms'),
    path('room/<str:pk>', views.room, name='room'),
]