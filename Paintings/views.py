from django.shortcuts import render
from django.http import HttpResponse
from .models import Painting


def index(request):
    return HttpResponse('Hello World')
def new(request):
    return HttpResponse('New Products')


