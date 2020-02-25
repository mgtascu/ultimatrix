from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Lol this wtf 123!</h1>")

