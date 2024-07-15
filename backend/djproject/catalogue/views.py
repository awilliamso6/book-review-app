from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")


def detail(request, title):
    return HttpResponse("You're looking at book %s." % title)


def add(request, title):
    return HttpResponse("You're adding book %s." % title)