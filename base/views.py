from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Fine Django'},
    {'id': 2, 'name': 'Yey Flutter'},
    {'id': 3, 'name': 'Yey Angular'},
]

def home(req):
    return render(req, 'base/home.html', {'rooms': rooms})

def room(req):
    return render(req, 'base/room.html')
