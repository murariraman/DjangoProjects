from django.shortcuts import render

# Create your views here.


def app1views(request):
    name='kumar'
    roll_number=25
    age=26
    return render(request, 'App1/app1.html',{'namek':name, 'agek':age, 'roll_numberk':roll_number})