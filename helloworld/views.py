from django.shortcuts import render
from django.http import HttpResponse
import django
import sys

def index(request):
    return HttpResponse("Hellow World from Python version: " + sys.version.split(' ')[0] + "   and Django version: " + django.get_version() )
# Create your views here.
