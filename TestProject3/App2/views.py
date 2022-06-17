from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def app2view(request):
    return render(request, 'App2/apptwo.html')


def app2views(request):
    return render(request, ' App2/appstwo.html')