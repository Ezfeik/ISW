from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "Horarios/index.html")

def profesor(request):
    return render(request, "Horarios/profesor.html")
