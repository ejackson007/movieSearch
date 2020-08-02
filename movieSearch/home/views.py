from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Search Home</h1>')

def about(request):
    return HttpResponse('<h1>Created by Evan Jackson</h1>')