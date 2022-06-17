from django.shortcuts import render
from Testapp.forms import studentform


def testappview(request):
    sf=studentform()

    if request.method=='POST':

        sf=studentform(request.POST)

        if sf.is_valid():
            print('form has been validated')

            print('Name ', sf.cleaned_data['name'])
            print('stdone', sf.cleaned_data['stdone'])
        else:
            sf=studentform()
                    

    return render(request, 'Testapp/StudentRegister.html', {'stdform':sf})


