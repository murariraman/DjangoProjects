from django.shortcuts import render
from Testapp.forms import testadmissionform


def testadmissionformview(request):
    
    if request.method=='POST':
        taf=testadmissionform(request.POST)

        if taf.is_valid():
            print('successful')

            print('name', taf.cleaned_data['name'])
            print('age', taf.cleaned_data['age'])
            print('email', taf.cleaned_data['email'])

        else:
            taf=testadmissionform()

    return render(request, 'Testapp/admissionform.html', {'taf':taf})




# Create your views here.
