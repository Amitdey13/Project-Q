from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def logIn(request):
    return render(request, 'app/login.html')

def register(request):
    return render(request, 'app/register.html')