from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app1view(request):
    return render(request, 'App1/appone.html')



def apps1view(request):
    return render(request, 'App1/appsone.html')
