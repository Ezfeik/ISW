from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "Horarios/index.html")

def profesor(request):
    return render(request, "Horarios/profesor.html")
