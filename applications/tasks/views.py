from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy

def index(request):
    sleepy(3)
    return HttpResponse('<h1>Tasks is done!</h1?')
