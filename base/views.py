from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Fine I\'ll learn Django'},
    {'id': 2, 'name': 'Yey Flutter'},
    {'id': 3, 'name': 'Yey Angular'},
]

def home(req):
    return render(req, 'base/home.html', {'rooms': rooms})

def room(req, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i

    context = {'room': room}

    return render(req, 'base/room.html', context)
