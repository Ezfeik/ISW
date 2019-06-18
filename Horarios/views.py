from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "Horarios/index.html")
    # return redirect('/accounts/login/')

def profesor(request):
    return render(request, "Horarios/profesor.html")
