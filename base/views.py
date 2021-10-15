from django.shortcuts import render

def home(req):
    return render(req, 'home.html')

def room(req):
    return render(req, 'room.html')
