from django.shortcuts import render
from Testapp.models import User
from Testapp.forms import StudentRegistration

# Create your views here.


def addandshowfuntion(request):

    if request.method== 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=User(name=nm, email=em, password=pwd)
            reg.save()
            fm=StudentRegistration()

    else:
        fm=StudentRegistration()
        
    return render(request, 'Testapp/addandshow.html', {'fmkey':fm})

def updatestudentfunction(request, id):

    if request.method=='POST':
        pi=User.object.get(pk=id)
        pi.delete()

    return render(request, 'Testapp/updatestudent.html',)

def basefunctiondisplay(request):

    fm=User.objects.all()
    return render(request, 'Testapp/base.html', {'fmkey':fm})