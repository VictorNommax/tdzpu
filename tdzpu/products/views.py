from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def gethead(req):
    return HttpResponse("<h1>Our Products:</h1>")
