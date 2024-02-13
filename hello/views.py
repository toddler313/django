from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html") 
#The reason for naming the template is hello/index.html
# because we gonna have multiple other applications, each with another index.html
# => Django best practice is to prefix the app name before each index.html

def brian(request):
    return HttpResponse("Welcome, Brian")

# def greeting(request, name):
#     return HttpResponse(f"Welcome, {name.capitalize()}!")

def greeting(request, name):
    return render(request, "hello/greeting.html", {
        "name": name.capitalize()
    })