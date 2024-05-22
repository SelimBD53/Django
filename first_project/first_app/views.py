from django.shortcuts import render
from django.http import HttpResponse

def  home(request):
    return HttpResponse("<h1>Hi This is a First Django Page.</h1>")

def  about(request):
    return HttpResponse("<h1>Hi This is a about Page.</h1>")
