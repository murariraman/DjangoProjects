from django.shortcuts import render

# Create your views here.
def app2views(request):

    name='ramam'
    age=26
    city='Bhagalpur'
    return render(request, 'App2/app2.html', {'namek': name, 'agek':age, 'cityk':city})