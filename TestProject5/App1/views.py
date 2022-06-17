from django.shortcuts import render

# Create your views here.
def app1view(request):
    return render(request, 'tax/appone.html')