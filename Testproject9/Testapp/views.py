from django.shortcuts import render
from Testapp.forms import StudentRegister


# Create your views here.

def registerview(request):

    sr=StudentRegister(label_suffix=' ',initial={'name':'somename', 'age':'434'})

    return render(request, 'Testapp/Resgister.html', {'srkey':sr})

