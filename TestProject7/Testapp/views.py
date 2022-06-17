from django.shortcuts import render

from Testapp.forms import StudentRegistrationForm

# Create your views here.


def RegistrationFormView(request):
    srf=StudentRegistrationForm()
    return render(request, 'Testapp/RegistrationForms.html', {'srfkey':srf})