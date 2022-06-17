from django.shortcuts import render

# Create your views here.

def apponeview(request):
    return render(request, 'App1/appone.html')

