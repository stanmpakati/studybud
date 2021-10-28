from django.http import request
from django.shortcuts import redirect, render
from .models import Room, Topic
from .forms import RoomForm

def home(req):
    rooms = Room.objects.all()
    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}

    return render(req, 'base/home.html', context)

def room(req, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(req, 'base/room.html', context)

def createRoom(req):
    form = RoomForm()
    if req.method =='POST':
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form': form}
    return render(req, 'base/room_form.html', context)

def updateRoom(req, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)

    if req.method == 'POST':
        form = RoomForm(req.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render (req, 'base/room_form.html', context)

def deleteRoom(req, pk):
    room = Room.objects.get(id = pk)
    if req.method == 'POST':
        room.delete()
        return redirect('home')

    return render(req, 'base/delete.html', {'obj': room})