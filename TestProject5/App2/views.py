from django.shortcuts import render

# Create your views here.

def app2views(request):
    return render(request, 'templates/apptwo.html')
