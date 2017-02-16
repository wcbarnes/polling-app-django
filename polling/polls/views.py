from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import mongoengine
from polls.models import Poll, Choice


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


