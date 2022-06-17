from django.shortcuts import render
from Testapp.forms import Registrationform

def testviewregister(request):
    rf=Registrationform()

    return render(request, 'Testapp/Register.html',{'rfkey':rf})
