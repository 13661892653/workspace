from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html')

def login(request):
    pass