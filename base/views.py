from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return HttpResponse('Home')

def room(req):
    return HttpResponse('Room')
