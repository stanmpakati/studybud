from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(req):
    return HttpResponse('Home')

def room(req):
    return HttpResponse('Room')
